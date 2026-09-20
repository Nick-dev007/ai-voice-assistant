# 🎙️ Anaya — AI Voice Assistant

Anaya is a beginner-friendly **AI-powered voice assistant built with Python**. The project uses speech recognition to listen for a wake word, processes voice commands, performs predefined actions, retrieves news, plays music, and can use an AI model to answer general questions.

This project was built as my **first Python project using external modules, APIs, and Python packages**, helping me understand how different technologies can work together to create a real-world application.

---

## ✨ Features

* 🎤 **Voice Recognition** — Understands commands through the microphone.
* 🔊 **Text-to-Speech** — Responds using generated speech.
* 🗣️ **Wake Word Detection** — Activates when the user says **"Anaya"**.
* 🌐 **Website Automation** — Opens websites using voice commands.
* 🎵 **Music Player** — Plays songs from a custom music library.
* 📰 **News Updates** — Fetches the latest Indian headlines using NewsAPI.
* 🤖 **AI Responses** — Uses OpenAI to handle general questions and commands.
* 💻 **Python-Based** — Built using Python libraries and APIs.

---

## 🛠️ Technologies Used

| Technology        | Purpose                        |
| ----------------- | ------------------------------ |
| Python            | Core programming language      |
| SpeechRecognition | Converts voice input into text |
| gTTS              | Converts text into speech      |
| Pygame            | Plays generated audio          |
| OpenAI API        | Handles AI-based responses     |
| NewsAPI           | Retrieves news headlines       |
| Requests          | Makes HTTP/API requests        |
| PyAudio           | Microphone/audio input         |
| Webbrowser        | Opens websites from commands   |

---

## 📂 Project Structure

```text
ai-voice-assistant/
│
├── Anaya.py
├── musicLibrary.py
├── client.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

### File Description

* **`Anaya.py`** — Main voice assistant program.
* **`musicLibrary.py`** — Contains the custom music library and links.
* **`client.py`** — Supporting client/API code.
* **`requirements.txt`** — Python dependencies required by the project.
* **`.env.example`** — Example environment variables for API configuration.
* **`.gitignore`** — Prevents sensitive and unnecessary files from being uploaded.
* **`README.md`** — Project documentation.

---

## ⚙️ How It Works

The basic workflow of Anaya is:

```text
User
  ↓
Microphone
  ↓
Speech Recognition
  ↓
Wake Word: "Anaya"
  ↓
Voice Command
  ↓
Command Processing
  ↓
┌─────────────────────────┐
│                         │
▼                         ▼
Predefined Commands     AI Processing
│                         │
├── Open Websites         └── OpenAI API
├── Play Music
└── Get News
          │
          ▼
    Voice Response
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Nick-dev007/ai-voice-assistant.git
```

Go into the project:

```bash
cd ai-voice-assistant
```

---

### 2. Create a virtual environment

Using Python 3.11:

```bash
py -3.11 -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If PyAudio causes an installation error, make sure you are using the Python version supported by your installed audio dependencies.

---

## 🔑 API Configuration

Anaya uses APIs for AI responses and news.

Create a `.env` file in the project directory:

```text
OPENAI_API_KEY=your_openai_api_key
NEWS_API_KEY=your_newsapi_key
```

The application loads these values using environment variables.

### ⚠️ Security

**Never upload your real API keys to GitHub.**

Your `.gitignore` should contain:

```text
.env
__pycache__/
*.pyc
.venv/
venv/
.vscode/
```

Use `.env.example` to show other developers which variables are required:

```text
OPENAI_API_KEY=your_openai_api_key_here
NEWS_API_KEY=your_newsapi_key_here
```

---

## ▶️ Run the Assistant

Run:

```bash
python Anaya.py
```

You should hear the initialization message.

Then say:

```text
Anaya
```

The assistant will activate and wait for your command.

---

## 🗣️ Example Commands

### Open Websites

```text
Anaya
Open Google
```

```text
Anaya
Open YouTube
```

```text
Anaya
Open Facebook
```

```text
Anaya
Open LinkedIn
```

### 🎵 Play Music

If a song is available in `musicLibrary.py`:

```text
Anaya
Play Believer
```

### 📰 Get News

```text
Anaya
News
```

The assistant retrieves the latest available headlines and reads them aloud.

### 🤖 AI Questions

For commands that aren't handled by predefined functions, Anaya can send the request to the configured AI service.

Example:

```text
Anaya
What is machine learning?
```

---

## 🧠 What I Learned

This project helped me understand several important concepts:

* Python modules and packages
* Installing and managing dependencies with `pip`
* Working with APIs
* Speech recognition
* Text-to-speech systems
* HTTP requests
* JSON/API responses
* Environment variables
* Basic command processing
* Python functions
* Working with external libraries
* Git and GitHub
* Debugging Python projects

---

## 🔮 Future Improvements

Some improvements planned for future versions include:

* 🔐 Better API and credential management
* 🧠 Improved natural-language command processing
* 🎯 More reliable wake-word detection
* 🖥️ Graphical user interface
* 📱 Better cross-platform support
* 🌍 Support for multiple languages
* 🎵 Improved music search and playback
* 🧩 More automation commands
* 💬 Conversation history
* 🤖 More advanced AI-agent capabilities

---

## 📌 Project Status

**Current Status:** Working Prototype

The current version demonstrates the core functionality of a Python-based voice assistant and serves as a foundation for future improvements.

---

## ⚠️ Disclaimer

This project is created for **learning and educational purposes**.

The project uses third-party APIs and services. Their availability and functionality may change independently of this project.

---


---

## ⭐ Acknowledgements

This project was created as part of my journey learning Python, APIs, Git, and real-world software development.

If you find the project interesting, consider giving the repository a ⭐.

