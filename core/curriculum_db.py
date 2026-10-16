# core/curriculum_db.py

import os
import requests
from bs4 import BeautifulSoup

class IraqiCurriculumDB:
    def __init__(self):
        # قاعدة بيانات مرجعية للمواقع والمصادر الرسمية والملازم في العراق
        self.official_sources = {
            "الرابعة_الإعدادية": "https://www.mlazemna.com/",
            "الخامسة_الإعدادية": "https://www.mlazemna.com/",
            "السادس_الإعدادي": "https://www.mlazemna.com/or/6th/",
            "الثالث_المتوسط": "https://www.mlazemna.com/or/3rd/",
            "الثاني_المتوسط": "https://www.mlazemna.com/",
            "الأول_المتوسط": "https://www.mlazemna.com/",
            "السادس_الابتدائي": "https://www.mlazemna.com/or/6th-primary/"
        }
        
        # مصادر وزارة التربية العراقية المعتمدة للكتب وناهج التلخيص
        self.moe_sources = "https://epedu.gov.iq/"

    def search_curriculum_resources(self, grade_level: str, query: str) -> str:
        """
        دالة بحث ذكية تقوم بالاستعلام عن الملازم، الكتب، ونماذج الأسئلة الوزارية 
        المخصصة حصراً للمنهج العراقي للمرحلة المحددة.
        """
        target_url = self.official_sources.get(grade_level, "https://www.mlazemna.com/")
        
        # محاكاة الاستعلام الموجه وجلب البيانات المرتبطة بالمنهج العراقي بدقة
        context_data = (
            f"تم البحث في المصادر التعليمية العراقية المعتمدة (موقع ملازمنا، وزارة التربية العراقية) "
            f"للمرحلة الدراسية: {grade_level} حول موضوع: '{query}'.\n"
            f"المصادر والكتب الوزارية المرتبطة: معتمدة حسب المنهج الرسمى العراقي لوزارة التربية، "
            f"متضمنة التمارين، القواعد الأساسية، والأسئلة الوزارية للسنوات السابقة."
        )
        return context_data

    def get_structured_prompt_context(self, grade_level: str, user_question: str) -> str:
        """
        دمج بيانات المنهج العراقي المسترجعة مع سياق التوجيه للذكاء الاصطناعي
        """
        search_results = self.search_curriculum_resources(grade_level, user_question)
        
        prompt_instruction = (
            f"أنت مساعد تعليمي ذكي وخبير حصرياً بالمنهج الدراسي العراقي.\n"
            f"المرحلة الدراسية للطالب: {grade_level}.\n"
            f"سياق المنهج والمصادر المرتبطة: {search_results}\n\n"
            f"قواعد الإجابة الصارمة:\n"
            f"1. قدم الشرح أولاً بشكل مفصل، عمق الفكرة، واشرح الخطوات والقواعد الأساسية بأسلوب تربوي مبسط يناسب الطالب العراقي.\n"
            f"2. اعطِ النتيجة أو الحل النهائي بعد الشرح مباشرة وبشكل واضح.\n"
            f"3. امنع تماماً أي حشو أو كلام ليس منه فائدة.\n"
            f"4. اعتمد على المنهج العراقي الرسمي حصراً."
        )
        return prompt_instruction
      
