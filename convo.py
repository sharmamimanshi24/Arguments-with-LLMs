import ollama
from datetime import datetime

# -----------------------------
# Configuration
# -----------------------------
MODEL_A = "gemma3:12b"   # Proponent
MODEL_B = "mistral-nemo:latest"          # Opponent

ROUNDS = 5
OUTPUT_FILE = "debate.txt"

TOPIC = "Do online courses actually teach skills, or just teach people how to feel productive?"

ROLE_A_PROMPT = (
    "You are Model A (gemma3). Your role is to DEFEND the position. "
    "Present structured arguments, clarify assumptions, and respond to criticism."
    "Give your answer in only 2 sentences; dont break rule"
)

ROLE_B_PROMPT = (
    "You are Model B (Mistral). Your role is to CHALLENGE the position. "
    "Identify weaknesses, counter arguments, and highlight risks or gaps."
    "Give your answer in only 2 sentences; dont break this rule"
)

# -----------------------------
# Initialize conversation
# -----------------------------
conversation = []
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

header = f"""
====================================================
SEQUENTIAL AI DEBATE (ON-PREM)
Time: {timestamp}
Model A (Proponent): {MODEL_A}
Model B (Opponent): {MODEL_B}
Topic: {TOPIC}
====================================================
"""

conversation.append(header)

print(header)

# -----------------------------
# Opening statement (Model A)
# -----------------------------
print("MODEL A — OPENING STATEMENT\n")

response_a = ollama.chat(
    model=MODEL_A,
    messages=[
        {"role": "system", "content": ROLE_A_PROMPT},
        {"role": "user", "content": TOPIC}
    ]
)

msg_a = response_a["message"]["content"]

print(msg_a + "\n")
conversation.append("MODEL A:\n" + msg_a + "\n")

# -----------------------------
# Debate rounds
# -----------------------------
for r in range(1, ROUNDS + 1):
    print(f"\n========== ROUND {r} ==========\n")

    # ----- Model B: Counter -----
    print("MODEL B — COUNTERARGUMENT\n")

    response_b = ollama.chat(
        model=MODEL_B,
        messages=[
            {"role": "system", "content": ROLE_B_PROMPT},
            {"role": "user", "content": "\n".join(conversation)}
        ]
    )

    msg_b = response_b["message"]["content"]

    print(msg_b + "\n")
    conversation.append("MODEL B:\n" + msg_b + "\n")

    # ----- Model A: Rebuttal -----
    print("MODEL A — REBUTTAL\n")

    response_a = ollama.chat(
        model=MODEL_A,
        messages=[
            {"role": "system", "content": ROLE_A_PROMPT},
            {"role": "user", "content": "\n".join(conversation)}
        ]
    )

    msg_a = response_a["message"]["content"]

    print(msg_a + "\n")
    conversation.append("MODEL A:\n" + msg_a + "\n")

# -----------------------------
# Save conversation
# -----------------------------
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(conversation))

print(f"\nDebate finished successfully.")
print(f"Conversation saved to: {OUTPUT_FILE}")
