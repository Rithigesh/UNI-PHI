from csv_analyzer import load_and_analyze_csv
from claude_api import send_message_to_claude

if __name__ == "__main__":
    
    csv_path = "r15_3651e0f3_20250422_143733.csv" 
    df = load_and_analyze_csv(csv_path)
    
    # Create a string summary from your DataFrame
    # Make sure csv_summary is a string, not a list
    csv_summary = df.head().to_string()
  
    message = f"Analyze this CSV data: How is the coolant temperature? {csv_summary}"
    word_count = len(message.split())
    if word_count > 50:
        words = message.split()
        message = ' '.join(words[:50])
    response = send_message_to_claude(message)
    print(response)
