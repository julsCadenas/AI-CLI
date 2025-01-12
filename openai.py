#!/usr/bin/env python
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
  api_key=os.getenv('openai_api_key')
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
