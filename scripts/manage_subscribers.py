import json
import os
from datetime import datetime

SUBSCRIBERS_FILE = os.path.join(os.path.dirname(__file__), 'subscribers.json')

def load_subscribers():
    if os.path.exists(SUBSCRIBERS_FILE):
        with open(SUBSCRIBERS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_subscribers(subscribers):
    with open(SUBSCRIBERS_FILE, 'w') as f:
        json.dump(subscribers, f, indent=2)

def add_subscriber(email, name='', audience='general'):
    subscribers = load_subscribers()
    for sub in subscribers:
        if sub['email'].lower() == email.lower():
            sub['name'] = name or sub.get('name', '')
            sub['audience'] = audience
            sub['updated_at'] = datetime.now().isoformat()
            save_subscribers(subscribers)
            print(f"Updated: {email}")
            return True
    subscribers.append({
        'email': email.lower(),
        'name': name,
        'audience': audience,
        'subscribed_at': datetime.now().isoformat(),
        'active': True
    })
    save_subscribers(subscribers)
    print(f"Added: {email} ({audience})")
    return True

def remove_subscriber(email):
    subscribers = load_subscribers()
    for sub in subscribers:
        if sub['email'].lower() == email.lower():
            sub['active'] = False
            sub['unsubscribed_at'] = datetime.now().isoformat()
            save_subscribers(subscribers)
            print(f"Unsubscribed: {email}")
            return True
    print(f"Not found: {email}")
    return False

def list_subscribers(audience=None):
    subscribers = load_subscribers()
    active = [s for s in subscribers if s.get('active', True)]
    if audience:
        active = [s for s in active if s.get('audience') == audience]
    print(f"Active subscribers: {len(active)}")
    for s in active:
        print(f"  {s['email']} ({s.get('audience','general')}) - {s.get('name','')}")
    return active

if __name__ == "__main__":
    action = os.environ.get('ACTION', 'list')
    email = os.environ.get('EMAIL', '')
    name = os.environ.get('NAME', '')
    audience = os.environ.get('AUDIENCE', 'general')

    if action == 'add' and email:
        add_subscriber(email, name, audience)
    elif action == 'remove' and email:
        remove_subscriber(email)
    else:
        list_subscribers()
