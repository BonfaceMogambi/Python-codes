import imaplib
import email
from email.header import decode_header
import re
from datetime import datetime, timedelta
def process_emails(email_address, password, days_back=1):
    """
    Automatically sort and categorize emails
    NOTE: Use an app-specific password, never your main password
    """
    
    # Connect to email server (Gmail example)
    mail = imaplib.IMAP4_SSL("bonfacemogambi96.gmail.com")
    mail.login(email_address, password)
    mail.select("inbox")
    
    # Search for recent emails
    date = (datetime.now() - timedelta(days=days_back)).strftime("%d-%b-%Y")
    status, messages = mail.search(None, f'(SINCE {date})')
    
    email_ids = messages[0].split()
    
    # Categories for sorting
    categories = {
        'Urgent': ['urgent', 'asap', 'immediately', 'critical'],
        'Meetings': ['meeting', 'schedule', 'calendar', 'zoom', 'call'],
        'Invoices': ['invoice', 'payment', 'receipt', 'billing'],
        'Reports': ['report', 'weekly', 'monthly', 'summary'],
        'Questions': ['?', 'how to', 'can you', 'could you', 'help']
    }
    
    sorted_emails = {cat: [] for cat in categories}
    sorted_emails['Other'] = []
    
    print(f"\n📧 Processing {len(email_ids)} emails...\n")
    
    for email_id in email_ids[-20:]:  # Process last 20 emails
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                
                # Get subject
                subject = decode_header(msg["Subject"])[0][0]
                if isinstance(subject, bytes):
                    subject = subject.decode()
                
                # Get sender
                from_ = msg.get("From")
                
                # Get email body
                body = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True).decode()
                            break
                else:
                    body = msg.get_payload(decode=True).decode()
                
                # Categorize
                categorized = False
                search_text = f"{subject} {body}".lower()
                
                for category, keywords in categories.items():
                    if any(keyword in search_text for keyword in keywords):
                        sorted_emails[category].append({
                            'from': from_,
                            'subject': subject,
                            'preview': body[:100]
                        })
                        categorized = True
                        break
                
                if not categorized:
                    sorted_emails['Other'].append({
                        'from': from_,
                        'subject': subject,
                        'preview': body[:100]
                    })
    
    # Print results
    for category, emails in sorted_emails.items():
        if emails:
            print(f"\n📁 {category} ({len(emails)} emails):")
            for e in emails[:3]:  # Show first 3
                print(f"  • From: {e['from']}")
                print(f"    Subject: {e['subject']}")
                print()
    
    mail.close()
    mail.logout()
    
    print("✓ Email processing complete!")
    return sorted_emails
# HOW TO USE:
# IMPORTANT: Never use your main password. Create an "App Password" in your email settings
# process_emails("your.email@gmail.com", "your-app-password", days_back=7)