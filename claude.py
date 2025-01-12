#!/usr/bin/env python
import anthropic as claude
import os
from dotenv import load_dotenv
load_dotenv()

client = claude.Anthropic(
    api_key= os.getenv('claude_api_key'),
)

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=8192,
    temperature=0,
    messages=[]
)
print(message.content)