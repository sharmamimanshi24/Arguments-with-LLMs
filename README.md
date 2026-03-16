# ⚔️ AI vs AI Debate System

> Two LLMs enter. One defends. One attacks. Neither backs down.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat&logo=python)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLMs-black?style=flat)
![Gemma](https://img.shields.io/badge/Gemma-Proponent-green?style=flat)
![Mistral](https://img.shields.io/badge/Mistral-Opponent-red?style=flat)
![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=flat)

---

## 📋 Table of Contents
- [About](#about)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 📖 About

This project simulates a structured debate between two Large Language Models running locally via Ollama.

One model takes the **Proponent** role — defending a given topic. The other takes the **Opponent** role — challenging every argument made. They go back and forth for multiple rounds, each responding directly to the other's previous point — just like a real debate.

The goal was to explore how LLMs handle adversarial reasoning, argumentation structure, and multi-turn context when forced to argue opposing sides of a topic.

---

## ⚙️ How It Works

```
Define a debate topic
        ↓
Gemma (Proponent) — opening statement
        ↓
Mistral (Opponent) — counterargument
        ↓
Gemma — rebuttal
        ↓
Mistral — counter-rebuttal
        ↓
  [repeats for N rounds]
        ↓
Full debate saved to debate.txt
```

**Example topic:**
```
"Artificial Intelligence will do more good than harm to society."
Gemma defends it. Mistral tears it apart.
```

---

## 🛠️ Installation

### Prerequisites
- Python 3.11+
- [Ollama](https://ollama.ai) installed locally
- Gemma and Mistral models pulled

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/sharmamimanshi24/Conversational-arguments-with-LLMs.git
cd Conversational-arguments-with-LLMs
```

**2. Install dependencies**
```bash
pip install ollama
```

**3. Pull the models**
```bash
ollama pull gemma
ollama pull mistral
```

**4. Make sure Ollama is running**
```bash
ollama serve
```

---

## 🚀 Usage

**1. Set your debate topic in `convo.py`:**
```python
topic = "AI will do more good than harm to society"
rounds = 3
```

**2. Run the debate:**
```bash
python convo.py
```

**3. Read the full debate in `debate.txt`:**
```
TOPIC: AI will do more good than harm to society

[ROUND 1]
Proponent (Gemma): AI has already revolutionized healthcare...
Opponent (Mistral): That argument ignores the mass job displacement...

[ROUND 2]
...
```

---

## 📁 Project Structure

```
argue_llm/
│
├── convo.py        # Main script — runs the full debate loop
├── debate.txt      # Output — the full saved debate transcript
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Please follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/).

---

## 📄 License

This project is licensed under the Apache 2.0 License. See [LICENSE](LICENSE) for details.

---

## 🆘 Support

- **Issues:** [GitHub Issues](https://github.com/sharmamimanshi24/Conversational-arguments-with-LLMs/issues)
- **Email:** sharma.mimanshi24@gmail.com

---

## 👩‍💻 Authors & Acknowledgments

**Mimanshi Sharma**

[![GitHub](https://img.shields.io/badge/GitHub-sharmamimanshi24-181717?style=flat&logo=github)](https://github.com/sharmamimanshi24)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-mimanshi--sharma-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/mimanshi-sharma/)

**Acknowledgments:**
- [Ollama](https://ollama.ai) — for local LLM inference
- [Gemma](https://ai.google.dev/gemma) — Google's open model
- [Mistral AI](https://mistral.ai) — for the Mistral model

---

*Built with Ollama · Gemma · Mistral · 2025*
