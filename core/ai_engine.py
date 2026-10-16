import os
import google.generativeai as genai
from core.curriculum_db import IraqiCurriculumDB

class AIEngine:
    def __init__(self):
        # تهيئة قاعدة بيانات المناهج العراقية
        self.curriculum_db = IraqiCurriculumDB()
        
        # استدعاء مفتاح الـ API من بيئة الخادم بشكل آمن
        api_key = os.environ.get("GEMINI_API_KEY", "")
        if api_key:
            genai.configure(api_key=api_key)
            
        # استخدام أحدث نموذج Gemini مخصص للمهام التعليمية والتحليلية
        self.model_name = 'gemini-2.0-flash'
        
        

    def generate_response(self, user_text: str, grade_level: str) -> str:
        """
        توليد استجابة ذكية موجهة حصرياً للطالب العراقي، تدمج بيانات المنهج وتلتزم بقواعد الشرح أولاً.
        """
        try:
            api_key = os.environ.get("GEMINI_API_KEY", "")
            if not api_key:
                return "عذراً، مفتاح السيرفر (GEMINI_API_KEY) غير مُعرّف في إعدادات البيئة."

            genai.configure(api_key=api_key)
            
            # جلب سياق المنهج العراقي والقواعد الصارمة الخاصة بالمرحلة
            system_instruction = self.curriculum_db.get_structured_prompt_context(grade_level, user_text)
            
            # تهيئة النموذج مع التوجيهات التعليمية الصارمة
            generation_config = {
                "temperature": 0.3,
                "max_output_tokens": 1500,
            }
            
            model = genai.GenerativeModel(
                model_name=self.model_name,
                system_instruction=system_instruction,
                generation_config=generation_config
            )

            # إرسال السؤال للنموذج
            response = model.generate_content(user_text)
            
            if response and response.text:
                return response.text
            else:
                return "عذراً، لم يتمكن النموذج من توليد إجابة واضحة. حاول مرة أخرى."

        except Exception as e:
            return f"حدث خطأ أثناء معالجة الطلب عبر خوارزميات الذكاء الاصطناعي: {str(e)}"
            
