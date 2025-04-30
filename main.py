import pandas as pd
import anthropic
import json
from config import ANTHROPIC_API_KEY

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

csv_path = 'r15_3651e0f3_20250422_143733.csv' 

df = pd.read_csv(csv_path)

csv_data_str = df.to_string(index=False)

message_content = f"Give me the coolant performance within 100 words.\n\n{csv_data_str}"
response = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=200,
    messages=[{"role": "user", "content": message_content}]
)
print(response.content)
#message = response.content

