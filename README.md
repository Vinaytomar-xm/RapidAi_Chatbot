# 🤖 AI Chatbot - Free & Fast

A powerful AI chatbot built with Streamlit and powered by Groq's lightning-fast LLM API. Chat with state-of-the-art language models completely free!

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](YOUR_LIVE_DEMO_LINK_HERE)

## ✨ Features

- 🚀 **Lightning Fast** - Powered by Groq's ultra-fast inference
- 💬 **Chat History** - Automatic conversation saving (ChatGPT-style sidebar)
- 🧠 **Smart AI Models** - Multiple Llama models to choose from
- 🆓 **100% Free** - No cost, no limits (14,400 requests/day)
- 💾 **Persistent Memory** - Your chats are saved automatically
- 🎨 **Clean UI** - Beautiful and intuitive interface
- ⚡ **Real-time Responses** - Get answers in seconds

## 🎥 Demo

**[🔗 Try Live Demo Here](YOUR_LIVE_DEMO_LINK_HERE)**

![Chatbot Screenshot](https://via.placeholder.com/800x400.png?text=AI+Chatbot+Screenshot)

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Groq API Key (free from [console.groq.com](https://console.groq.com))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/ai-chatbot.git
cd ai-chatbot
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up your API key**

Create `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "your-groq-api-key-here"
```

Or use environment variable:
```bash
export GROQ_API_KEY="your-groq-api-key-here"
```

4. **Run the app**
```bash
streamlit run app.py
```

5. **Open your browser**
```
http://localhost:8501
```

## 🔑 Get Free API Key

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up (free)
3. Navigate to "API Keys"
4. Create new key
5. Copy and use in the app

**Free Tier Limits:**
- ✅ 14,400 requests per day
- ✅ 30 requests per minute
- ✅ No credit card required

## 📦 Tech Stack

- **Frontend/Backend**: Streamlit
- **AI Model**: Llama 3.1 (via Groq API)
- **Language**: Python 3.8+
- **Libraries**: 
  - `streamlit` - Web interface
  - `requests` - API calls
  - `json` - Data handling

## 🎯 Usage

### Start a New Chat
Click "➕ New Chat" in the sidebar to begin a fresh conversation.

### Chat History
- All your conversations are auto-saved
- Click on any previous chat to reload it
- Delete individual chats or clear all history

### Switch Models
Choose different AI models from the sidebar dropdown for varying performance and capabilities.

## 🌐 Deployment

### Deploy on Streamlit Cloud (Recommended)

1. **Push to GitHub**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Deploy**
- Go to [share.streamlit.io](https://share.streamlit.io)
- Sign in with GitHub
- Click "New app"
- Select your repository
- Add your `GROQ_API_KEY` in Secrets
- Deploy!

## 📁 Project Structure
```
ai-chatbot/
├── Ai_chatbot.py          # Main application file
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── .gitignore             # Git ignore rules
└── .streamlit/
    ├── config.toml        # Streamlit configuration
    └── secrets.toml       # API keys (not in git)
```

## 🛠️ Configuration

### Customize Theme

Edit `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#0E1117"
secondaryBackgroundColor = "#262730"
textColor = "#FAFAFA"
font = "sans serif"
```

### Adjust AI Parameters

In `app.py`, modify:
```python
payload = {
    "model": model,
    "messages": messages,
    "temperature": 0.7,      # Creativity (0-1)
    "max_tokens": 1024       # Response length
}
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Groq](https://groq.com) - For providing ultra-fast LLM inference
- [Streamlit](https://streamlit.io) - For the amazing web framework
- [Meta](https://www.meta.com) - For the Llama models

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/YOUR_USERNAME/ai-chatbot](https://github.com/YOUR_USERNAME/ai-chatbot)

## 🐛 Known Issues

- Chat history is stored in session state (clears on page refresh in local dev)
- Large conversations may take longer to load

## 🔮 Future Enhancements

- [ ] Database integration for persistent storage
- [ ] User authentication
- [ ] File upload support
- [ ] Code syntax highlighting
- [ ] Voice input/output
- [ ] Multi-language support
- [ ] Export chat as PDF/TXT

## ⭐ Star History

If you find this project useful, please consider giving it a star!

[![Star History Chart](https://api.star-history.com/svg?repos=YOUR_USERNAME/ai-chatbot&type=Date)](https://star-history.com/#YOUR_USERNAME/ai-chatbot&Date)

---

Made with ❤️ by [Your Name](https://github.com/YOUR_USERNAME)
