#Context Window - (Max tokens per call [input+output]. Model's short-term memory)
#GPT-3.5 - CW 4k-16k; GPT-4o - CW 128k; Claude 3.5 -CW 200k; Gemini 1.5Pro -CW 1M-2M
#If you exceed it-> older content gets truncated or the API errors.

CONTEXT_MAX = 128.000
tokens_in = len(enc.encode(system+user))
if tokens_in>CONTEXT_MAX:raise ValueError("Too Long")