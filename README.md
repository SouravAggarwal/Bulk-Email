# Automated Job Application Email System

A robust, production-ready backend system built in Python to read candidate/recruiter email addresses from an Excel file, iteratively send a customized job application email, and log the delivery status (Success/Failed) to an output Excel file.

## Features
- **Batch Email Sending**: Parse an Excel file and cleanly iterate over it to send emails.
- **Config-Driven**: Environment variables control sensitive credentials and operational parameters.
- **Data Validation**: Automatically ignores duplicates and invalid email formats.
- **Self-Healing Retries**: Retries up to a configured threshold if sending fails before logging as FAILED.
- **Rate-Limiting Built In**: Respects strict rate limits using artificial delays to reduce the chance of spam blocking.
- **Audit Logging**: Keeps an exact timestamped record of every email attempted and its outcome.

## Setup Requirements

1. **Python version**: Python 3.8+ recommended.
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Copy the example config and edit it with your credentials.
   ```bash
   cp .env.example .env
   ```
   *Edit `.env` to include your actual `SENDER_EMAIL` and `SENDER_PASSWORD`.*

### Gmail App Password Setup (Important)
If you are using a standard Gmail account to send these emails, you cannot use your standard login password due to security restrictions. You must use an App Password:

1. Enable **2-Step Verification** for your Google Account.
2. Go to your Google Account -> **Security**.
3. Under "Signing in to Google", select **2-Step Verification**.
4. Scroll to the bottom and click on **App passwords**.
5. Select "Mail" for the app and "Other (Custom name)" for the device (e.g. "Python Script").
6. Click **Generate** and copy the 16-character password.
7. Paste this password generated into your `.env` file under `SENDER_PASSWORD`.

## How to use

1. Place your list of target emails in Excel form at `data/input_emails.xlsx` with at least one column titled `email`. (You can run `python generate_sample.py` to create a mock file automatically).
2. Tweak your email subject and body in `email_templates.py` if necessary.
3. Run the orchestration script:
   ```bash
   python main.py
   ```
4. Examine the `data/log.xlsx` file after completion to view success and failures.

## Adding Resume Attachments
To attach a resume:
1. Update `email_sender.py`.
2. Import `from email.mime.application import MIMEApplication` and `import os`.
3. Add logic to read the file and attach it to the `msg` object before sending:
```python
with open("resume.pdf", "rb") as f:
    part = MIMEApplication(f.read(), Name=os.path.basename("resume.pdf"))
part['Content-Disposition'] = f'attachment; filename="resume.pdf"'
msg.attach(part)
```
