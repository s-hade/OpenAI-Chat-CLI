# ==========================================
# Developer: Shade
# GitHub:   https://github.com/s-hade
# Telegram: https://t.me/shadee666
# X (Twitter):  https://x.com/shadeless_dev
# ==========================================

# pip install openai
from openai import OpenAI

# Enter your API key here
API_KEY = "sk-proj-YOUR_KEY_HERE"

# Select a model (you can choose gpt-4o, gpt-4o-mini, gpt-4-turbo, etc)
MODEL = "gpt-4o"

client = OpenAI(api_key=API_KEY)

print("=== OpenAI Chat ===")
print("Type your message below (type 'exit' to quit)\n")

messages = [
    {"role": "system", "content": "You are a helpful AI assistant who speaks clearly and naturally."}
]

while True:
    try:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit", "выйти"]:
            print("Exiting...")
            break

        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages
        )

        reply = response.choices[0].message.content.strip()
        print(f"AI: {reply}\n")

        messages.append({"role": "assistant", "content": reply})

    except KeyboardInterrupt:
        print("\nInterrupted. Exiting...")
        break
    except Exception as e:
        print(f"[Error] {e}\n")
