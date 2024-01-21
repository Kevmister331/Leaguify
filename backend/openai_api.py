from openai import OpenAI

client = OpenAI(
    api_key = "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"
)

prompt = "Whats the biggest country in the world?"
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role":"user",
            "content":prompt
        }
    ],
    model="gpt-3.5-turbo"
)

print(chat_completion.choices[0].message.content)