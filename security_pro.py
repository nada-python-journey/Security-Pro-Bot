
import datetime

def neutralize_link(link):
    # 1. القائمة البيضاء: روابط رسمية نثق بها (مثل موقع الوزارة)
    whitelist = ["moedu.gov.iq", "results.mlazemna.com"]
    
    # 2. قائمة الكلمات المشبوهة
    suspicious = ["win", "free", "gift", "login", "update", "result", "leak", "نتائج", "تسريب"]
    
    link_lower = link.lower()

    # أولاً: فحص إذا كان الرابط رسمياً
    for trust in whitelist:
        if trust in link_lower:
            print(f"✅ هذا الرابط موثوق ورسمي: {link}")
            return

    # ثانياً: فحص الكلمات المشبوهة في الروابط الأخرى
    for word in suspicious:
        if word in link_lower:
            # عزل الرابط
            safe = link.replace(".", "[DOT]").replace("http", "hXXp")
            print(f"⚠️ تهديد! تم عزل الرابط المشبوه: {safe}")
            return
            
    print("✅ الرابط يبدو آمناً للفحص الأولي")

# واجهة التشغيل
print("--- 🛡️ نظام حماية ندى المطور ---")
url = input("أدخل الرابط لفحصه: ")
neutralize_link(url)
