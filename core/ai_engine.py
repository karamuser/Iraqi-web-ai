import os
import google.generativeai as genai

class AIEngine:
    def __init__(self, api_key=None):
        # استخدام مفتاح الـ API المرسل أو من متغيرات البيئة
        self.api_key = api_key or os.getenv("GEMINI_API_KEY", "")
        if self.api_key:
            genai.configure(api_key=self.api_key)
        # استخدام نموذج جميناي الحديث والأسرع
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
    def generate_response(self, user_text, grade_level="السادس الإعدادي", custom_api_key=None):
        try:
            # استخدام مفتاح مؤقت إذا أدخله المستخدم من واجهة الإعدادات
            key_to_use = custom_api_key or self.api_key
            if not key_to_use:
                return "⚠️ تنبيه: يرجى إدخال مفتاح Google Gemini API الخاص بك في قائمة الإعدادات الجانبية لكي يتم تفعيل الذكاء الاصطناعي."
            
            genai.configure(api_key=key_to_use)

            # توجيه صارم للذكاء الاصطناعي للاهتمام بالشرح أولاً ثم الناتج للمناهج العراقية
            system_instruction = (
                f"أنت خبير ومدرس استثنائي للمناهج الدراسية الرسمية لوزارة التربية في العراق. "
                f"المرحلة الدراسية للطالب حالياً هي: {grade_level}. "
                f"قواعد الإجابة الصارمة التي يجب أن تلتزم بها:\n"
                f"1. ابدأ دائماً بـ **الشرح المفصل والخطوات المبسطة** لفهم الفكرة العلمية أو المسألة قبل إعطاء الإجابة النهائية.\n"
                f"2. اجعل أسلوبك تربوي، محفز، ومطابق للمقررات المدرسية العراقية.\n"
                f"3. في النهاية ضع الناتج النهائي أو الخلاصة بشكل واضح."
            )
            
            chat = self.model.start_chat(history=[])
            prompt = f"{system_instruction}\n\nسؤال الطالب: {user_text}"
            
            response = chat.send_message(prompt)
            return response.text
        except Exception as e:
            return f"عذراً، حدث خطأ أثناء الاتصال بخوادم Google Gemini الذكية: {str(e)}"
          
