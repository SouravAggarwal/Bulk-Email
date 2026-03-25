import time
from config import INPUT_EXCEL_PATH, OUTPUT_EXCEL_PATH, DELAY_BETWEEN_EMAILS_SECONDS, SENDER_EMAIL
from excel_handler import read_emails_from_excel, log_email_status
from email_templates import get_email_content
from email_sender import send_email

def main():
    print(f"--- Starting Bulk Email Application System ---")
    if not SENDER_EMAIL:
        print("WARNING: Sender credentials not found. This will be a dry run where logs are marked as FAILED if sending is attempted, or you might see missing credentials errors.")
    
    print(f"Reading emails from: {INPUT_EXCEL_PATH}")
    email_list = read_emails_from_excel(INPUT_EXCEL_PATH)
    
    if not email_list:
        print("No valid emails found to process. Exiting.")
        return
        
    print(f"Found {len(email_list)} valid emails. Processing...")
    
    subject, plain_body, html_body = get_email_content()
    
    for i, target_email in enumerate(email_list):
        print(f"[{i+1}/{len(email_list)}] Processing: {target_email}...")
        
        # In a real scenario, you could extract the name from the email or another column
        # Here we use a generic string as requested in the template.
        success = send_email(target_email, subject, plain_body, html_body)
        
        if success:
            log_email_status(OUTPUT_EXCEL_PATH, target_email, "SUCCESS")
            print(f"Successfully sent and logged for {target_email}")
        else:
            log_email_status(OUTPUT_EXCEL_PATH, target_email, "FAILED")
            print(f"Failed to send for {target_email}. Logged as FAILED.")
            
        # Rate Limiting
        if i < len(email_list) - 1:
            print(f"Waiting for {DELAY_BETWEEN_EMAILS_SECONDS} seconds before next email to avoid rate limits...")
            time.sleep(DELAY_BETWEEN_EMAILS_SECONDS)
            
    print("--- Bulk Email Process Completed ---")
    print(f"Please check {OUTPUT_EXCEL_PATH} for the full log.")

if __name__ == "__main__":
    main()
