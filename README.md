# Mental Stress Detection Chatbot
<img src="" alt="screenshot">
This project is a Django-based web application that uses sentiment analysis (powered by `vaderSentiment`) to detect a user's emotional state and suggest supportive actions. It functions like a chatbot and is designed to help individuals monitor their mental well-being in a simple, accessible way.

## 🌍 SDG Alignment

### 🧠 SDG 3: Good Health and Well-being

> Ensure healthy lives and promote well-being for all at all ages.

This project addresses **Target 3.4** of SDG 3:
> *"By 2030, reduce by one third premature mortality from non-communicable diseases through prevention and treatment and promote mental health and well-being."*

Mental health is a growing concern globally, especially among youth and working populations. By providing a lightweight, AI-supported tool for stress detection, this app promotes **early self-awareness** and can serve as a stepping stone for seeking professional help.

---

## 📚 Table of Contents

- [🌍 SDG Alignment](#-sdg-alignment)
- [💡 Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [🚀 Getting Started](#-getting-started)
- [📁 Project Structure](#-project-structure)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [👥 Author](#-author)

---

## 💡 Features

- 🔍 Sentiment analysis using VADER (Valence Aware Dictionary for sEntiment Reasoning)
- 💬 Chat-like interface where users input messages
- 🧠 Real-time stress/mood evaluation (positive, neutral, negative)
- 🩺 Suggested actions based on mood
- 🕊️ Promotes self-awareness and emotional support

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Bootstrap)
- **AI/ML**: VADER Sentiment from `vaderSentiment` Python library

---

## 🚀 Getting Started

# 1. Clone the repository:
   ```bash
   git clone https://github.com/charlesricha/mood-tracker.git
   cd mood-tracker
   ```
# 2. Create and activate a virtual environment:
   
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
```
# 3. Install dependencies:
```bash
pip install -r requirements.txt

Run the app:

    python manage.py migrate
    python manage.py runserver
```
- Visit http://127.0.0.1:8000/ in your browser to start chatting!
  
## 📁 Project Structure
```bash
mood-tracker/
│
├── analyzer/
│   ├── templates/
│   │   └── analyzer/
│   │       └── chat.html
│   ├── views.py
│   ├── urls.py
│   └── ...
├── mentalhealth_ai/
│   ├── settings.py
│   └── urls.py
├── manage.py
└── requirements.txt
```
## 🤝 Contributing

We welcome contributions to improve this tool. Feel free to fork the repository, submit pull requests, or raise issues.
## 📜 License

This project is open-source and available under the MIT License.

## 👥 Author

Charles Richa
GitHub: charlesricha



