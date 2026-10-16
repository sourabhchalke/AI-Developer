#API Concept = Application Programming Interface-> how your code sends requests to the model server.
#Flow :- Your python code
#            |  -HTTP POST with JSON
#        OpenAI Server
#            |
#           LLM
#            |  -JSON response
#        Your Python code

r=client.chat.completion.create(
    model="gpt-4o-mini",
    messages=[{"role":"user","content":"Hi"}],
    temparature=0.7,
)

print(r.choices[0].message.content) #reply
print(r.usage.total_tokens) #cost