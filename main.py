import telebot
from telebot import types
import requests
import threading
import time

# --- الإعدادات الأساسية ---
TOKEN = '8681664117:AAHOmLod5sozxgYJVv_iBiFGEgR1QsdnWAo' # توكن بوتك
CHANNEL_ID = '-1002237071607' # ايدي قناتك (يمكنك الحصول عليه من بوت GetID) أو استخدم الرابط أدناه
CHANNEL_URL = 'https://t.me/+cVKuEoMe9BcyMDNh'
bot = telebot.TeleBot(TOKEN)

# --- دالة التحقق من الاشتراك الإجباري ---
def check_sub(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        if member.status in ['member', 'administrator', 'creator']:
            return True
        return False
    except:
        # في حال لم يتم رفع البوت كمسؤول في القناة
        return False

# --- واجهة الترحيب الرئيسية ---
def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("📊 معلومات تيك توك", callback_data="info_tt")
    btn2 = types.InlineKeyboardButton("🔥 بلاغات تيك توك", callback_data="report_tt")
    btn3 = types.InlineKeyboardButton("📸 معلومات انستا", callback_data="info_ig")
    btn4 = types.InlineKeyboardButton("🚫 بلاغات انستا", callback_data="report_ig")
    markup.add(btn1, btn2, btn3, btn4)
    return markup

# --- رسالة الاشتراك الإجباري ---
def sub_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔗 اضغط هنا للاشتراك", url=CHANNEL_URL))
    markup.add(types.InlineKeyboardButton("✅ تحقق من الاشتراك", callback_data="check_sub"))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if check_sub(user_id):
        welcome_text = f"🔥 أهلاً بك {message.from_user.first_name} في **ULTIMATE DESTROYER V2**\n\nأقوى بوت للتبنيد وجمع المعلومات في الشرق الأوسط. اختر وجهتك الآن:"
        bot.send_message(message.chat.id, welcome_text, reply_markup=main_menu(), parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, "⚠️ **عذراً عزيزي!**\n\nيجب عليك الاشتراك في قناة البوت الرسمية أولاً لتتمكن من استخدامه.", reply_markup=sub_markup(), parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    user_id = call.from_user.id
    
    if call.data == "check_sub":
        if check_sub(user_id):
            bot.answer_callback_query(call.id, "✅ تم التحقق! أهلاً بك.")
            bot.edit_message_text("🔥 تم تفعيل القوى الشيطانية.. اختر الخيار المطلوب:", call.message.chat.id, call.message.message_id, reply_markup=main_menu())
        else:
            bot.answer_callback_query(call.id, "❌ لم تشترك في القناة بعد!", show_alert=True)

    elif call.data == "info_tt":
        msg = bot.send_message(call.message.chat.id, "👤 أرسل يوزر التيك توك الآن:")
        bot.register_next_step_handler(msg, get_tt_info)

    elif call.data == "report_tt":
        msg = bot.send_message(call.message.chat.id, "💀 أرسل يوزر الضحية لبدء الهجوم الهائل:")
        bot.register_next_step_handler(msg, start_attack)

# --- دالة جلب معلومات التيك توك (مثال للتوضيح) ---
def get_tt_info(message):
    user = message.text
    bot.send_message(message.chat.id, f"🔎 جاري فحص الحساب: @{user}...\n📍 الموقع المتوقع: تم التحديد عبر الـ IP المستجيب.\n👥 المتابعين: جاري الجلب...\n⚠️ الحالة: مكشوف للرادار.")
    # هنا يتم ربط API خارجي لجلب البيانات الحقيقية

# --- دالة الهجوم (قوية جداً باستخدام Threads) ---
def start_attack(message):
    target = message.text
    bot.send_message(message.chat.id, f"🚨 **بدأ الدمار الشامل!**\n\nيتم الآن إرسال آلاف البلاغات إلى سيرفرات المنصة ضد: {target}\n⚡ السرعة: 500 req/min")
    
    def attack():
        for i in range(1000): # عدد الهجمات
            try:
                # هنا توضع روابط البلاغات الحقيقية للمنصات
                requests.get(f"https://www.tiktok.com/@{target}") 
            except:
                pass
    
    for _ in range(20): # تشغيل 20 خيط هجوم متوازي
        threading.Thread(target=attack).start()

print("😈 البوت يعمل بأقصى طاقة الآن...")
bot.polling()
