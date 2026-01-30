import telebot
import requests

# 1. Telegram Bot kaliti
TOKEN = "8259571397:AAFG8Dixr2SJSECV9aTorspOnMd1zTb8vFc" 

# 2. Groq AI kaliti
GROQ_KEY = "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" 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Yangi botingiz muvaffaqiyatli ishga tushdi. Savol bering!")

@bot.message_handler(func=lambda m: True)
def chat_ai(message):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_KEY}"}
    payload = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": message.text}]
    }
    
    try:
        res = requests.post(url, json=payload, headers=headers)
        if res.status_code == 200:
            bot.reply_to(message, res.json()['choices'][0]['message']['content'])
        else:
            bot.reply_to(message, "Xatolik: Groq API javob bermadi.")
    except Exception as e:
        bot.reply_to(message, "Ulanishda xatolik yuz berdi.")

if __name__ == "__main__":
    bot.infinity_polling()
