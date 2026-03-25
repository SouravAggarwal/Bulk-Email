import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import time
from config import SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD, MAX_RETRIES, DATA_DIR

def send_email(to_email, subject, plain_body, html_body, max_retries=MAX_RETRIES):
    """
    Sends an email using standard SMTP. Implements retries on failure.
    Includes both plain text and HTML versions, and attaches a resume PDF if found.
    Returns True if sent successfully, False otherwise.
    """
    if not SENDER_EMAIL or not SENDER_PASSWORD:
        print("Cannot send email: Credentials missing.")
        return False
        
    msg = MIMEMultipart('mixed')
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Create the alternative part for plain text and HTML
    alt_part = MIMEMultipart('alternative')
    alt_part.attach(MIMEText(plain_body, 'plain'))
    alt_part.attach(MIMEText(html_body, 'html'))
    msg.attach(alt_part)
    
    # Attach the PDF resume
    resume_path = os.path.join(DATA_DIR, "Sourav Aggarwal's Resume.pdf")
    if os.path.exists(resume_path):
        try:
            with open(resume_path, "rb") as f:
                pdf_part = MIMEApplication(f.read(), Name=os.path.basename(resume_path))
            pdf_part['Content-Disposition'] = f'attachment; filename="{os.path.basename(resume_path)}"'
            msg.attach(pdf_part)
        except Exception as e:
            print(f"Warning: Failed to attach resume from {resume_path}. Error: {e}")
    else:
        print(f"Warning: Resume not found at {resume_path}. Sending without attachment.")
    
    retries = 0
    while retries < max_retries:
        try:
            # Set up the server
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls() # Secure the connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            
            # Send email
            text = msg.as_string()
            server.sendmail(SENDER_EMAIL, to_email, text)
            server.quit()
            
            return True
            
        except smtplib.SMTPAuthenticationError:
            print("Authentication failed. Check your SENDER_EMAIL and SENDER_PASSWORD.")
            return False # No point retrying this
        except Exception as e:
            retries += 1
            print(f"Attempt {retries} failed for {to_email}. Error: {e}")
            if retries < max_retries:
                time.sleep(2) # wait a bit before retrying
                
    return False
