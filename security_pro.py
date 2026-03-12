import datetime

def neutralize_link(link):
    # قائمة الكلمات التي يصطادها البوت
    words = ["win", "free", "gift", "login", "update", "result", "leak", "prize", "giftcard", "نتائج", "تسريب"]
    link = link.lower()
    
    for w in words:
        if w in link:
            # عزل الرابط برمجياً
            safe = link.replace(".", "[DOT]").replace("http", "hXXp")
            print(f"⚠️ تهديد أمني! تم عزل الرابط: {safe}")
            return
            
    print("✅ الرابط يبدو آمناً للفحص الأولي")

# واجهة التشغيل
print("--- 🛡️ نظام حماية ندى الذكي ---")
url = input("أدخل الرابط لفحصه: ")
neutralize_link(url)
