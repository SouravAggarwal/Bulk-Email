import pandas as pd
from pathlib import Path
from config import INPUT_EXCEL_PATH

def generate():
    # Ensure data directory exists
    Path(INPUT_EXCEL_PATH).parent.mkdir(parents=True, exist_ok=True)
    
    # Create some dummy emails + one invalid one to show filtering
    data = {
        'email': [
            'test1@example.com',
            'test2@example.com',
            'test1@example.com', # Duplicate
            'invalid-email-format',
            'test3_mock@example.com'
        ]
    }
    
    df = pd.DataFrame(data)
    df.to_excel(INPUT_EXCEL_PATH, index=False)
    print(f"Sample input Excel file created at: {INPUT_EXCEL_PATH}")

if __name__ == "__main__":
    generate()
