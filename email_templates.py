EMAIL_SUBJECT_TEMPLATE = "[Subject of Your Email]"

EMAIL_BODY_TEMPLATE = """\
Hello {recipient_name},

I hope this email finds you well!

[Your Main Message / Value Proposition / Introduction goes here]. I am reaching out to share [Purpose of Email].

[Additional details, updates, or context regarding why you are reaching out].

Key Highlights:
- [Highlight 1]: [Metric / Detail 1]
- [Highlight 2]: [Metric / Detail 2]
- [Highlight 3]: [Metric / Detail 3]

For more details, please visit our links below, and find the relevant document attached.

Main Website: [Your Primary Link]
Secondary Resource: [Your Secondary Link]

Looking forward to connecting with you.

Best regards,
[Your Name / Company Name]
"""

EMAIL_HTML_TEMPLATE = """\
<!DOCTYPE html>
<html>
<head>
<style>
    body {{
        font-family: 'Inter', 'Segoe UI', Arial, sans-serif;
        line-height: 1.6;
        color: #333333;
        margin: 0;
        padding: 0;
    }}
    .container {{
        max-width: 1000px;
        margin: 0 auto;
        padding: 20px;
        background-color: #ffffff;
    }}
    .header {{
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: #ffffff;
        padding: 30px 20px;
        text-align: center;
        border-radius: 8px 8px 0 0;
    }}
    .header h1 {{
        margin: 0;
        font-size: 24px;
        font-weight: 600;
        letter-spacing: 0.5px;
    }}
    .header p {{
        margin: 5px 0 0;
        font-size: 16px;
        opacity: 0.9;
    }}
    .content {{
        padding: 30px;
        border: 1px solid #e0e0e0;
        border-top: none;
        border-radius: 0 0 8px 8px;
    }}
    .greeting {{
        font-size: 18px;
        font-weight: 600;
        color: #2c3e50;
    }}
    .skills-list {{
        padding-left: 20px;
        margin: 15px 0;
    }}
    .skills-list li {{
        margin-bottom: 10px;
    }}
    .skills-list strong {{
        color: #2a5298;
    }}
    .cta-container {{
        text-align: center;
        margin: 35px 0 20px;
    }}
    .button {{
        display: inline-block;
        padding: 12px 24px;
        background-color: #2a5298;
        color: #ffffff !important;
        text-decoration: none;
        border-radius: 5px;
        font-weight: 600;
        margin: 5px;
        transition: background-color 0.3s;
    }}
    .button-outline {{
        display: inline-block;
        padding: 12px 24px;
        background-color: transparent;
        color: #2a5298 !important;
        text-decoration: none;
        border: 2px solid #2a5298;
        border-radius: 5px;
        font-weight: 600;
        margin: 5px;
    }}
    .footer {{
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid #eeeeee;
        text-align: center;
        color: #7f8c8d;
        font-size: 14px;
    }}
    .signature-name {{
        font-size: 18px;
        font-weight: bold;
        color: #2c3e50;
        margin: 5px 0;
    }}
</style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>[Your Name / Company Name]</h1>
            <p>[Your Slogan / Title]</p>
        </div>
        
        <div class="content">
            <p class="greeting">Hello {recipient_name},</p>
            
            <p>I hope this email finds you well!</p>
            
            <p>[Your Main Message / Value Proposition / Introduction goes here]. I am reaching out to share [Purpose of Email].</p>
            
            <p>[Additional details, updates, or context regarding why you are reaching out].</p>
            
            <p><strong>Key Highlights:</strong></p>
            <ul class="skills-list">
                <li><strong>[Highlight 1]:</strong> [Metric / Detail 1]</li>
                <li><strong>[Highlight 2]:</strong> [Metric / Detail 2]</li>
                <li><strong>[Highlight 3]:</strong> [Metric / Detail 3]</li>
            </ul>
            
            <div class="cta-container">
                <a href="[Your Primary Link]" class="button">Visit Our Website</a>
                <a href="[Your Secondary Link]" class="button-outline">View Resources</a>
            </div>
            
            <p>I have also attached a relevant PDF document for your convenience.</p>
            
            <div class="footer">
                <p>Looking forward to connecting with you.</p>
                <div class="signature">
                    <p style="margin-bottom: 2px;">Best regards,</p>
                    <p class="signature-name">[Your Name / Company Name]</p>
                    <p style="margin-top: 0; color: #2a5298;">[Your Contact Info]</p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

def get_email_content(recipient_name="Recipient"):
    """
    Generates the subject, plain text body, and html body for the email.
    """
    subject = EMAIL_SUBJECT_TEMPLATE
    plain_text_body = EMAIL_BODY_TEMPLATE.format(recipient_name=recipient_name)
    html_body = EMAIL_HTML_TEMPLATE.format(recipient_name=recipient_name)
    return subject, plain_text_body, html_body
