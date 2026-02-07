
import streamlit as st
import requests
from datetime import datetime
import os


st.markdown("""<style>
            .stDeployButton {
                visibility: hidden;
                }
            </style>""", unsafe_allow_html=True)


# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="FuteeAI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ---------------- API ----------------
# Get API key from secrets or environment variable
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except (FileNotFoundError, KeyError):
    # Try environment variable
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
    if not GROQ_API_KEY:
        st.error("❌ API Key not found! Please add GROQ_API_KEY to secrets or environment variables.")
        st.info("👉 Get free key from: https://console.groq.com/keys")
        st.stop()

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# ---------------- FUNCTIONS ----------------
def get_ai_response(messages, model):
    """Send messages to Groq and get response"""
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 1024
    }
    
    try:
        response = requests.post(
            GROQ_API_URL,
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
        elif response.status_code == 401:
            return "❌ Invalid API Key!"
        else:
            return f"❌ Error {response.status_code}"
            
    except Exception as e:
        return f"❌ Error: {str(e)}"

def save_current_chat():
    """Save current chat to history"""
    if len(st.session_state.messages) > 0:
        # Get first user message as title
        title = "New Chat"
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                title = msg["content"][:50] + ("..." if len(msg["content"]) > 50 else "")
                break
        
        chat_entry = {
            "id": datetime.now().strftime("%Y%m%d_%H%M%S"),
            "title": title,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "messages": st.session_state.messages.copy(),
            "model": st.session_state.model
        }
        
        st.session_state.chat_history.insert(0, chat_entry)
        
        # Keep only last 20 chats
        if len(st.session_state.chat_history) > 20:
            st.session_state.chat_history = st.session_state.chat_history[:20]

def load_chat(chat_id):
    """Load a specific chat from history"""
    for chat in st.session_state.chat_history:
        if chat["id"] == chat_id:
            st.session_state.messages = chat["messages"].copy()
            st.session_state.model = chat.get("model", "llama-3.1-8b-instant")
            st.rerun()

def delete_chat(chat_id):
    """Delete a specific chat from history"""
    st.session_state.chat_history = [
        chat for chat in st.session_state.chat_history 
        if chat["id"] != chat_id
    ]
    st.rerun()

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "model" not in st.session_state:
    st.session_state.model = "llama-3.1-8b-instant"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = None

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("💬 Chats")
    
    # New Chat Button
    if st.button("➕ New Chat", use_container_width=True, type="primary"):
        if len(st.session_state.messages) > 0:
            save_current_chat()
        st.session_state.messages = []
        st.session_state.current_chat_id = None
        st.rerun()
    
    st.divider()
    
    # Model Selection
    st.subheader("🤖 Ai Model")
    
    models = {
        "Llama 3.1 8B": "llama-3.1-8b-instant"
    }
    
    selected = st.selectbox(
        "Choose:",
        options=list(models.keys()),
        index=0,
        label_visibility="collapsed"
    )
    
    st.session_state.model = models[selected]
    
    st.divider()
    
    # Chat History
    st.subheader("📚 History")
    
    if len(st.session_state.chat_history) == 0:
        st.caption("No saved chats yet")
    else:
        for chat in st.session_state.chat_history:
            col1, col2 = st.columns([4, 1])
            
            with col1:
                if st.button(
                    f"💬 {chat['title']}", 
                    key=f"load_{chat['id']}",
                    use_container_width=True
                ):
                    load_chat(chat['id'])
            
            with col2:
                if st.button("🗑️", key=f"del_{chat['id']}"):
                    delete_chat(chat['id'])
            
            st.caption(chat['timestamp'])
            st.divider()
    
    # Clear All History
    if len(st.session_state.chat_history) > 0:
        if st.button("🗑️ Clear All History", use_container_width=True):
            st.session_state.chat_history = []
            st.success("✅ History cleared!")
            st.rerun()
    
    st.divider()
    st.caption("🆓 Free AI Chatbot")

# ---------------- MAIN CHAT UI ----------------
st.title("🤖 FuteeAI Chatbot")
st.caption("Fast & Free AI Assistant")

st.divider()

# Welcome message
if len(st.session_state.messages) == 0:
    st.info("👋 **Hi! I'm your AI assistant!**\n , How can I assist you today?")
# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("⚡Generating..."):
            
            # Prepare messages
            api_messages = [
                {"role": m["role"], "content": m["content"]} 
                for m in st.session_state.messages
            ]
            
            # Get response
            response = get_ai_response(
                api_messages,
                st.session_state.model
            )
            
            # Display response
            st.markdown(response)
    
    # Add AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })
    
    # Auto-save chat after every response
    save_current_chat()



