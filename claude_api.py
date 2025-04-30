import anthropic
from config import ANTHROPIC_API_KEY

client = anthropic.Anthropic(
    api_key=ANTHROPIC_API_KEY
)

def send_message_to_claude(message_content):
    message = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=1024,
        messages=[{"role": "user", "content": message_content}]
    )
    return message.content
