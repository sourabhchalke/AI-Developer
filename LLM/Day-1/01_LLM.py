# LLM-Large Language Model
# It's core job is to predict the next token given on previous tokens.

#LLM call
r=client.chat.completion.create(
    model="gpt-40-mini",
    messages=[{"role":"user","content":"The capital of France is"}]
)
print(r.choices[0].message.content)