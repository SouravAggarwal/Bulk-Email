EMAIL_SUBJECT_TEMPLATE = "[Your Job Title] | [Key Skill 1], [Key Skill 2], [Key Skill 3]"

EMAIL_BODY_TEMPLATE = """\
Hello Hiring Manager/Team,

I hope you're having a great week!

I'm reaching out to express my strong interest in [Target Role] opportunities within your team.

I am a [Current Job Title] with [X]+ years of experience building [Skill Area 1], [Skill Area 2], and [Skill Area 3]. I have worked extensively on [Domain/System Type], including leading [Key Achievement 1] and building [Key Achievement 2].

My career highlights include:
- [Area 1]: [Achievement/Metric 1]
- [Area 2]: [Achievement/Metric 2]
- [Area 3]: [Achievement/Metric 3]
- Tech Stack Expertise: [Language 1], [Language 2], [Framework 1], [Cloud Platform].

For more details about my professional journey, please find my links below, and my detailed resume attached.

LinkedIn: [Your LinkedIn Profile URL]
GitHub: [Your GitHub Profile URL]
Resume (External Link): [Your External Link, e.g., Google Drive]

Looking forward to the possibility of collaborating.

Best regards,
[Your First Name] [Your Last Name]
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
            <h1>[Your First Name] [Your Last Name]</h1>
            <p>[Your Title] | [Key Skill 1] & [Key Skill 2]</p>
        </div>
        
        <div class="content">
            <p class="greeting">Hello {recipient_name},</p>
            
            <p>I hope you're having a great week!</p>
            
            <p>I'm reaching out to express my strong interest in [Target Role] opportunities within your team.</p>
            
            <p>I am a [Current Job Title] with <strong>[X]+ years of experience</strong> building [Skill Area 1], [Skill Area 2], and [Skill Area 3]. I have worked extensively on [Domain/System Type], including leading [Key Achievement 1] and building [Key Achievement 2].</p>
            
            <p><strong>Key Career Highlights:</strong></p>
            <ul class="skills-list">
                <li><strong>[Area 1]:</strong> [Achievement/Metric 1]</li>
                <li><strong>[Area 2]:</strong> [Achievement/Metric 2]</li>
                <li><strong>[Area 3]:</strong> [Achievement/Metric 3]</li>
                <li><strong>Technology Stack:</strong> Fluent in [Language 1], [Language 2], [Framework 1], combined with [Cloud Platform].</li>
            </ul>
            
            <div class="cta-container">
                <a href="[Your External Link, e.g., Google Drive]" class="button">View Online Resume</a>
                <a href="[Your LinkedIn Profile URL]" class="button-outline">LinkedIn Profile</a>
                <a href="[Your GitHub Profile URL]" class="button-outline">GitHub Portfolio</a>
            </div>
            
            <p>I have also attached a PDF copy of my resume for your convenience.</p>
            
            <div class="footer">
                <p>Looking forward to hearing from you.</p>
                <div class="signature">
                    <p style="margin-bottom: 2px;">Best regards,</p>
                    <p class="signature-name">[Your First Name] [Your Last Name]</p>
                    <p style="margin-top: 0; color: #2a5298;">[Your Phone] | [Your Email]</p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

def get_email_content(recipient_name="Hiring Manager/Team"):
    """
    Generates the subject, plain text body, and html body for the email.
    """
    subject = EMAIL_SUBJECT_TEMPLATE
    plain_text_body = EMAIL_BODY_TEMPLATE.format(recipient_name=recipient_name)
    html_body = EMAIL_HTML_TEMPLATE.format(recipient_name=recipient_name)
    return subject, plain_text_body, html_body
