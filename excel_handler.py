import pandas as pd
from datetime import datetime
import os
import re

def validate_email(email):
    """
    Basic email format validation.
    """
    if not isinstance(email, str):
        return False
    regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(regex, email) is not None

def read_emails_from_excel(file_path):
    """
    Reads an Excel file, extracts valid email IDs from the 'email' column,
    removes duplicates and invalid formats.
    """
    try:
        df = pd.read_excel(file_path)
        if 'email' not in df.columns:
            print(f"Error: 'email' column not found in {file_path}")
            return []
        
        # Drop NaN
        df = df.dropna(subset=['email'])
        
        # Clean email text
        df['email'] = df['email'].astype(str).str.strip().str.lower()
        
        # Drop duplicates
        initial_count = len(df)
        df = df.drop_duplicates(subset=['email'])
        if len(df) < initial_count:
            print(f"Removed {initial_count - len(df)} duplicate emails.")
            
        # Filter valid emails
        df['is_valid'] = df['email'].apply(validate_email)
        invalid_emails = df[~df['is_valid']]['email'].tolist()
        if invalid_emails:
            print(f"Filtered out {len(invalid_emails)} invalid emails: {invalid_emails}")
            
        valid_emails = df[df['is_valid']]['email'].tolist()
        return valid_emails
        
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []

def log_email_status(log_file_path, email_id, status):
    """
    Appends a new log entry to the Excel log file.
    Creates a new file if it doesn't exist.
    """
    new_entry = pd.DataFrame([{
        'email_id': email_id,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'status': status
    }])
    
    try:
        if os.path.exists(log_file_path):
            existing_df = pd.read_excel(log_file_path)
            # Use pd.concat instead of append
            updated_df = pd.concat([existing_df, new_entry], ignore_index=True)
            updated_df.to_excel(log_file_path, index=False)
        else:
            new_entry.to_excel(log_file_path, index=False)
    except Exception as e:
        print(f"Failed to log status for {email_id}: {e}")
