import os
import sys
import json
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email_templates import generate_html_email, generate_text_email, BOOKS

SUBSCRIBERS_FILE = os.path.join(os.path.dirname(__file__), 'subscribers.json')

SUBJECTS = [
    "Caribbean Scribbles: This Week's Book Picks for Young Readers",
    "Recommended Reads: Caribbean Children's Books Your Family Will Love",
    "Island Stories for Little Minds: Weekly Book Recommendations",
    "Discover Caribbean Children's Books - Curated Just for You",
    "This Week's Featured Books from Caribbean Scribbles Publishing",
    "Bold Island Stories: Weekly Picks for Parents, Teachers & Families",
    "Caribbean Reads for Kids: Fresh Recommendations This Week",
]

def load_subscribers():
    if os.path.exists(SUBSCRIBERS_FILE):
        with open(SUBSCRIBERS_FILE, 'r') as f:
            return json.load(f)
    return []

def get_featured_books(audience):
    if audience == 'teacher':
        priority = [b for b in BOOKS if 'Science' in b['title'] or 'Kindergarten' in b['title'] or 'Rules' in b['title']]
        others = [b for b in BOOKS if b not in priority]
    elif audience == 'diaspora':
        priority = [b for b in BOOKS if 'Sugar Mas' in b['title'] or 'Harmony' in b['title'] or 'Saint Kitts' in b['title']]
        others = [b for b in BOOKS if b not in priority]
    elif audience == 'parent':
        priority = [b for b in BOOKS if 'Kindergarten' in b['title'] or 'Sketchbook' in b['title'] or 'Sweets' in b['title']]
        others = [b for b in BOOKS if b not in priority]
    else:
        return random.sample(BOOKS, min(3, len(BOOKS)))
    return (priority + others)[:3]

def send_email():
    sender_email = os.environ.get('GMAIL_USER')
    sender_password = os.environ.get('GMAIL_APP_PASSWORD')

    if not sender_email or not sender_password:
        print("ERROR: GMAIL_USER or GMAIL_APP_PASSWORD not set.")
        sys.exit(1)

    # Load from subscribers.json
    all_subs = load_subscribers()
    active_subs = [s for s in all_subs if s.get('active', True)]

    # Also include comma-separated emails from env var
    extra_str = os.environ.get('SUBSCRIBER_EMAILS', '')
    extra_emails = [e.strip() for e in extra_str.split(',') if e.strip()]

    # Merge unique recipients
    sub_map = {s['email']: s for s in active_subs}
    for e in extra_emails:
        if e not in sub_map:
            sub_map[e] = {'email': e, 'name': '', 'audience': 'general', 'active': True}

    recipients = list(sub_map.values())

    if not recipients:
        test = os.environ.get('TEST_EMAIL')
        if test:
            recipients = [{'email': test, 'name': '', 'audience': 'general'}]
        else:
            print("No recipients found. Exiting.")
            sys.exit(0)

    print(f"Sending campaign to {len(recipients)} recipients...")

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
    except Exception as e:
        print(f"SMTP Error: {e}")
        sys.exit(1)

    success = 0
    failed = 0

    for sub in recipients:
        email = sub.get('email', '')
        name = sub.get('name', '')
        audience = sub.get('audience', 'general')
        featured = get_featured_books(audience)

        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = random.choice(SUBJECTS)
            msg['From'] = f"Caribbean Scribbles Publishing <{sender_email}>"
            msg['To'] = email

            msg.attach(MIMEText(generate_text_email(featured, recipient_name=name), 'plain'))
            msg.attach(MIMEText(generate_html_email(featured, recipient_name=name), 'html'))

            server.sendmail(sender_email, email, msg.as_string())
            print(f"  Sent -> {email} ({audience})")
            success += 1
        except Exception as e:
            print(f"  Failed -> {email}: {e}")
            failed += 1

    server.quit()
    print(f"\nDone: {success} sent, {failed} failed out of {len(recipients)} total.")

if __name__ == "__main__":
    send_email()
