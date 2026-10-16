#Temparature- It controls randomness in token selection:
#0.0-Always picks most likely token; Use for-Math,Code,Facts.
#0.7-Balanced; Use for-Chat
#1.5-Wildly creative; Use for-Brainstorming

client.chat.completion.creative(...,temparature=0.0) #same answer everytime
client.chat.completion.creative(...,temparature=1.5) #different answer each time