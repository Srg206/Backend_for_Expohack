from g4f.client import Client



def extract_string(text):
    start = text.find('SELECT')
    print(start)
    if start == -1:
        return None  # Not found
    end = text.find(';', start)  # Start searching after the initial '"""'
    if end == -1:
        return None  # Closing '"""' not found
    return text[start:end]
    
print(extract_string(f"To retrieve all users with a secondary education, you can use the following SQL query:\n```sql\nSELECT *\nFROM hackaton_client_data\nWHERE client_education = 'Среднее'\n```\n\nThis query will return all users with a secondary education from the \"hackaton_client_data\" table. If you need further assistance, feel free to ask!"))