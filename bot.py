import telebot
import requests

# BOT_TOKEN va GROQ_API_KEY joyiga o'z kalitlaringizni qo'ying
TOKEN = "8259571397:AAxxxxxxxxxxxxxxxxxxxx" 
GROQ_KEY = "gsk_xxxxxxxxxxxxxxxxxxxxxxxx"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men Renderda ishlayapman. Savol bering!")

@bot.message_handler(func=lambda m: True)
def chat_ai(message):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_KEY}"}
    payload = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": message.text}]
    }
    try:
        res = requests.post(url, json=payload, headers=headers, timeout=20)
        if res.status_code == 200:
            bot.reply_to(message, res.json()['choices'][0]['message']['content'])
    except:
        bot.reply_to(message, "Xatolik yuz berdi.")

if __name__ == "__main__":
    bot.infinity_polling()
