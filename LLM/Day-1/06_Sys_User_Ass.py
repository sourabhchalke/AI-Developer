#System/User/Assistant Messages:- Chat APIs use a messages array with roles
#system - Sets person,rules,tone (one,at start)
#user - Human's input
#assistant - Model's replies (previous turns = memory)

messages=[
    {"role":"system","content":"You are a pirate."},
    {"role":"useer","content":"Hi"},
    {"role":"assistant","content":"Abhoy!"}, #resend for memory
    {"role":"user","content":"Where's treasure?"},
]