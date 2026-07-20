import random
from datetime import datetime

# ─────────────────────────────────────────────
# BOOKS CATALOGUE
# ─────────────────────────────────────────────
BOOKS = [
    {
        "title": "Island Lab: 15 Caribbean Science Experiments for Young Explorers",
        "age": "6-12",
        "desc": "Bring the wonders of science to life with 15 fun, hands-on experiments inspired by the Caribbean environment. A fantastic way to encourage STEM learning at home!",
        "url": "https://www.amazon.com/author/vjsmithen",
        "price": "$7.99",
        "tag": "STEM & Science"
    },
    {
        "title": "Sweets, Treats, Toys and Me!",
        "age": "5-10",
        "desc": "A delightful story that captures the pure joy of childhood, perfect for cozy reading sessions together. Rated 5 stars by readers.",
        "url": "https://www.amazon.com/author/vjsmithen",
        "price": "$8.99",
        "tag": "Picture Book"
    },
    {
        "title": "Akejah and the Rules of Harmony Island",
        "age": "5-10",
        "desc": "A heartwarming Caribbean story about kindness, courage, and the power of rules. Wonderful lessons on social-emotional learning wrapped in an engaging island adventure.",
        "url": "https://www.amazon.com/author/vjsmithen",
        "price": "$8.40",
        "tag": "Character & Values"
    },
    {
        "title": "The Girls Of My Sketchbook: Hairstyles, Habitats & Hobbies Coloring Book",
        "age": "All Ages",
        "desc": "Let your child's creativity shine with this engaging coloring book featuring 24 pages of diverse characters celebrating natural hairstyles, hobbies, and habitats.",
        "url": "https://www.amazon.com/author/vjsmithen",
        "price": "$6.99",
        "tag": "Activity & Coloring"
    },
    {
        "title": "The Jingle of the Sugar Mas Bells",
        "age": "5-10",
        "desc": "Immerse your child in the vibrant culture and festive spirit of the Caribbean! A Saint Kitts Christmas story filled with carnival spirit and the magic of Sugar Mas.",
        "url": "https://www.amazon.com/author/vjsmithen",
        "price": "$8.40",
        "tag": "Holiday & Culture"
    },
    {
        "title": "My Kindergarten Handbook: Little Kinder Kids",
        "age": "4-6",
        "desc": "An excellent resource to help your little one navigate their early school years with confidence. Covers handwriting, counting, and confidence-building activities.",
        "url": "https://www.amazon.com/author/vjsmithen",
        "price": "$10.00",
        "tag": "Early Learning"
    },
    {
        "title": "Saint Kitts Pride: Exercise Book",
        "age": "All Ages",
        "desc": "A lined, island-themed exercise book that turns everyday writing practice into a quiet celebration of home. Perfect for schools and as a cultural gift.",
        "url": "https://www.amazon.com/author/vjsmithen",
        "price": "$13.00",
        "tag": "School & Practice"
    }
]

# ─────────────────────────────────────────────
# SAINT KITTS NEWS ITEMS
# ─────────────────────────────────────────────
NEWS_ITEMS = [
    "Saint Kitts and Nevis continues to celebrate its rich cultural heritage through community storytelling events and island festivals.",
    "Local schools in Saint Kitts report increased engagement with culturally relevant reading materials in classrooms.",
    "The Caribbean literacy initiative highlights the importance of island-themed stories for young readers across the region.",
    "Saint Kitts celebrates its vibrant heritage through storytelling, arts, and creative writing in local communities.",
    "Caribbean educators are championing diverse, locally authored children's books as essential tools for cultural identity and literacy.",
    "New reading programmes in Saint Kitts schools are incorporating Caribbean-authored books to boost engagement and pride.",
    "The Caribbean diaspora community continues to champion culturally representative children's literature for young readers abroad."
]

# ─────────────────────────────────────────────
# HTML EMAIL GENERATOR
# ─────────────────────────────────────────────
def generate_html_email(featured_books=None, news_item=None, recipient_name=''):
    if featured_books is None:
        featured_books = random.sample(BOOKS, 3)
    if news_item is None:
        news_item = random.choice(NEWS_ITEMS)

    date_str = datetime.now().strftime("%B %d, %Y")
    greeting = f"Hello {recipient_name}," if recipient_name else "Hello,"

    book_cards_html = ""
    for book in featured_books:
        book_cards_html += f"""
        <table width="100%" cellpadding="0" cellspacing="0" style="border:1px solid #e5e7eb; border-radius:10px; margin-bottom:18px; overflow:hidden;">
          <tr>
            <td style="padding:18px;">
              <span style="display:inline-block; background:#ffc857; color:#333; font-size:11px; font-weight:700; padding:3px 10px; border-radius:20px; margin-bottom:8px;">{book['tag']}</span>
              <h3 style="color:#007b83; margin:0 0 6px 0; font-size:17px;">{book['title']}</h3>
              <p style="font-size:12px; color:#6b7280; margin:0 0 8px 0;">Ages: {book['age']} &nbsp;|&nbsp; From {book['price']}</p>
              <p style="font-size:14px; color:#333; margin:0 0 14px 0;">{book['desc']}</p>
              <a href="{book['url']}" style="display:inline-block; background:#007b83; color:#ffffff; text-decoration:none; padding:9px 18px; border-radius:999px; font-weight:700; font-size:13px;">View on Amazon &rarr;</a>
            </td>
          </tr>
        </table>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Caribbean Scribbles Publishing - Weekly Book Recommendations</title>
</head>
<body style="margin:0; padding:0; background-color:#f5f7fb; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color:#333;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#f5f7fb; padding:30px 0;">
    <tr>
      <td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="background:#ffffff; border-radius:12px; overflow:hidden; box-shadow:0 4px 20px rgba(0,0,0,0.08); max-width:600px; width:100%;">
          <tr>
            <td style="background:linear-gradient(135deg, #007b83 0%, #005962 100%); padding:30px 35px; text-align:center;">
              <h1 style="color:#ffffff; margin:0; font-size:24px; letter-spacing:-0.5px;">Caribbean Scribbles Publishing</h1>
              <p style="color:#b2e0e3; margin:6px 0 0 0; font-size:13px;">Bold Island Stories for Children &nbsp;&bull;&nbsp; {date_str}</p>
            </td>
          </tr>
          <tr>
            <td style="padding:28px 35px 10px 35px;">
              <p style="font-size:15px; margin:0 0 10px 0;">{greeting}</p>
              <p style="font-size:15px; margin:0 0 18px 0;">We're delighted to bring you this week's curated Caribbean children's book recommendations. Each title celebrates island heritage, inspires young minds, and makes a wonderful addition to any home or classroom library.</p>
            </td>
          </tr>
          <tr>
            <td style="padding:0 35px 20px 35px;">
              <table width="100%" cellpadding="0" cellspacing="0" style="background:#e6f2f3; border-left:4px solid #007b83; border-radius:6px;">
                <tr>
                  <td style="padding:14px 16px;">
                    <p style="font-size:12px; font-weight:700; color:#005962; text-transform:uppercase; letter-spacing:0.5px; margin:0 0 4px 0;">&#127796; From Saint Kitts</p>
                    <p style="font-size:14px; color:#333; margin:0;">{news_item}</p>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
          <tr>
            <td style="padding:0 35px 16px 35px;">
              <h2 style="font-size:18px; color:#007b83; margin:0; border-bottom:2px solid #e5e7eb; padding-bottom:8px;">&#128218; Featured Books This Week</h2>
            </td>
          </tr>
          <tr>
            <td style="padding:0 35px 10px 35px;">
              {book_cards_html}
            </td>
          </tr>
          <tr>
            <td style="padding:0 35px 28px 35px;">
              <table width="100%" cellpadding="0" cellspacing="0" style="background:#ffc857; border-radius:10px;">
                <tr>
                  <td style="padding:18px 20px; text-align:center;">
                    <p style="font-size:15px; font-weight:700; color:#222; margin:0 0 10px 0;">Explore the full collection on Amazon</p>
                    <a href="https://www.amazon.com/author/vjsmithen" style="display:inline-block; background:#007b83; color:#ffffff; text-decoration:none; padding:10px 22px; border-radius:999px; font-weight:700; font-size:14px;">Browse All Books &rarr;</a>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
          <tr>
            <td style="background:#f5f7fb; padding:20px 35px; text-align:center; border-top:1px solid #e5e7eb;">
              <p style="font-size:13px; color:#6b7280; margin:0 0 6px 0;"><strong>Caribbean Scribbles Publishing</strong></p>
              <p style="font-size:12px; color:#9ca3af; margin:0 0 6px 0;">Based in Saint Kitts &amp; Nevis, Caribbean</p>
              <p style="font-size:12px; color:#9ca3af; margin:0 0 10px 0;">
                <a href="https://caribbeanscribblespublishing.com" style="color:#007b83;">Website</a>
                &nbsp;|&nbsp;
                <a href="https://www.amazon.com/author/vjsmithen" style="color:#007b83;">Amazon Author Page</a>
                &nbsp;|&nbsp;
                <a href="https://www.instagram.com/caribbeanscribblesPublishing" style="color:#007b83;">Instagram</a>
              </p>
              <p style="font-size:11px; color:#d1d5db; margin:0;">
                You are receiving this email because you subscribed to the Caribbean Scribbles newsletter.<br/>
                Emails are sent every Monday, Wednesday &amp; Friday.
              </p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>"""

    return html

# ─────────────────────────────────────────────
# PLAIN TEXT EMAIL GENERATOR
# ─────────────────────────────────────────────
def generate_text_email(featured_books=None, news_item=None, recipient_name=''):
    if featured_books is None:
        featured_books = random.sample(BOOKS, 3)
    if news_item is None:
        news_item = random.choice(NEWS_ITEMS)

    date_str = datetime.now().strftime("%B %d, %Y")
    greeting = f"Hello {recipient_name}," if recipient_name else "Hello,"

    text  = "CARIBBEAN SCRIBBLES PUBLISHING\n"
    text += f"Bold Island Stories for Children | {date_str}\n\n"
    text += f"{greeting}\n\n"
    text += "We're delighted to bring you this week's curated Caribbean children's book recommendations.\n\n"
    text += "FROM SAINT KITTS\n"
    text += f"{news_item}\n\n"
    text += "FEATURED BOOKS THIS WEEK\n"
    text += "-----------------------------------\n\n"

    for book in featured_books:
        text += f"[{book['tag'].upper()}]\n"
        text += f"{book['title']}\n"
        text += f"Ages: {book['age']}  |  From {book['price']}\n"
        text += f"{book['desc']}\n"
        text += f"View on Amazon: {book['url']}\n\n"

    text += "-----------------------------------\n"
    text += "Browse all books: https://www.amazon.com/author/vjsmithen\n\n"
    text += "Caribbean Scribbles Publishing\n"
    text += "Based in Saint Kitts & Nevis, Caribbean\n"
    text += "Website: https://caribbeanscribblespublishing.com\n"

    return text
