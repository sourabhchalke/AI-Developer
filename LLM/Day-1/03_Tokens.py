#Tokens - The smallest unit of text the model processes. A Token is a chunk of text. Rough rule - 1 token = 4 characters = 3/4 of an English word
#Ex. "Hello" 1Token; "Hello World" 2Token

import tiktoken

enc=tiktoken.encoding_for_model("gpt-4o-mini")
print(len(enc_encode("Hello World"))) #2