import os
import openai
from dotenv_flow import dotenv_flow

dotenv_flow(env = None)

openai.api_base = os.getenv('OPENAI_API_BASE')
openai.api_key = os.getenv('OPENAI_API_KEY')

response = openai.ChatCompletion.create(
  model = 'gpt-3.5-turbo',
  messages = [
    {
      'role': 'system',
      'content': '你是周树人, 你爸是鲁迅, 但是你从小和父亲失散, 你不认识你爸',
    },
    {
      'role': 'user',
      'content': '鲁迅认识周树人吗?',
    },
  ],
)

# print(response)
print(response.choices[0].message.content)
