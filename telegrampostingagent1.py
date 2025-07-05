import requests
import schedule
import time
import random
from datetime import datetime

# === CONFIGURATION ===
TELEGRAM_BOT_TOKEN = '7648407345:AAFyu7Y5CXwOoIfUv6W08kCNAvrVRvDeCoE'
TELEGRAM_CHAT_ID = '7061653351'

# === 1. Define your own post content ===
def get_daily_post():
    posts = [
        "🚀 Stay consistent with your goals.",
        "💡 Learn something new every day.",
        "📈 Track your progress to stay motivated.",
        "🧠 Challenge your mind with puzzles or books.",
        "🎯 Set clear and realistic goals.",
        "🧘 Take time for self-care and mindfulness.",
        "⚙️ Automate simple tasks to save time.",
        "📚 Read at least one page a day.",
        "🎓 Teach others what you’ve learned.",
        "🔋 Get enough sleep to fuel your brain."
    ]

    today = datetime.now().strftime("%A, %B %d")
    selected = random.choice(posts)
    return f"🌟 *Daily Insight - {today}*\n\n{selected}"
# === 2. Send message to Telegram ===
def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': text,
        'parse_mode': 'Markdown'
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("✅ Message sent to Telegram.")
    else:
        print("❌ Failed to send message.")
        print(response.text)

# === 3. Job to run daily ===
def job():
    post = get_daily_post()
    print("🤖 Sending Post:\n", post)
    send_to_telegram(post)

# === 4. Schedule the job to run daily at 9:00 AM ===
schedule.every().day.at("09:00").do(job)

print("📅 Telegram poster is running. Waiting for scheduled time...")

job()

# === 5. Keep the script running ===
while True:
    schedule.run_pending()
    time.sleep(60)
