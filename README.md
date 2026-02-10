# AI vs AI Debate System

This project simulates a structured debate between two Large Language Models (LLMs) using predefined roles.

One model defends a topic (Proponent) and the other challenges it (Opponent).  
The models argue over multiple rounds, responding to each other’s points, just like a real debate.

The entire conversation is saved as a text file for review.

---

## How It Works

1. A debate topic is defined in the code  
2. Model A gives an opening statement  
3. Model B responds with a counterargument  
4. Model A replies with a rebuttal  
5. Steps 3 and 4 repeat for a fixed number of rounds  
6. The full debate is saved to a text file  

---

## Models Used

- **Model A (Proponent):** Gemma  
- **Model B (Opponent):** Mistral  

(Models are run locally using Ollama.)

---

## Project Structure

```text
argue_llm
│
├── convo.py
├── debate.txt
├── README.md
├── requirements.txt
└── LICENSE



