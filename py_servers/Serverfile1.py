from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import uvicorn
import google.generativeai as genai

# 1. تهيئة السيرفر الشامل والمتكامل
app = FastAPI(
    title="Iraqi AI Comprehensive Server - File 1",
    version="1.0.0",
    description="سيرفر مستقل ومتكامل يضم معالجة الذكاء الاصطناعي، المناهج العراقية، والبوابة في ملف واحد"
)

# تفعيل الـ CORS للاتصال الحر
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. إعداد قاعدة بيانات المناهج العراقية الشاملة داخل السيرفر
CURRICULUM_DATA = {
    "السادس الإعدادي": {
        "الرياضيات": "الفصل الأول: الاعداد المركبة، الفصل الثاني: القعور المخروطية.",
        "الفيزياء": "الفصل الأول: المتسعات، الفصل الثاني: الحث الكهرومغناطيسي.",
        "الكيمياء": "الفصل الأول: علم التبريد، الفصل الثاني: الاتزان الكيميائي."
    },
    "الخامس الإعدادي": {
        "الرياضيات": "المناهج العامة والأساسية للمرحلة الخامسة.",
        "الفيزياء": "الميكانิก والحرارة."
    }
}

# 3. إعداد نموذج الذكاء الاصطناعي (Gemini)
API_KEY = os.environ.get("GEMINI_API_KEY", "")
if API_KEY:
    genai.configure(api_key=API_KEY)

class FullAIRequest(BaseModel):
    message: str
    grade_level: str = "السادس الإعدادي"
    subject: str = "الرياضيات"

@app.get("/")
def home():
    return {
        "status": "Online",
        "server": "Serverfile1 - Independent & Comprehensive",
        "message": "أهلاً بك في السيرفر الشامل للمناهج العراقية والذكاء الاصطناعي"
    }

@app.post("/api/chat/comprehensive")
def comprehensive_chat(data: FullAIRequest):
    # جلب سياق المنهج العراقي محلياً من السيرفر الشامل
    grade_info = CURRICULUM_DATA.get(data.grade_level, {})
    subject_context = grade_info.get(data.subject, "مناهج الدراسات العراقية العامة")
    
    system_prompt = (
        f"أنت مساعد ذكاء اصطناعي تعليمي خاص بالمنهج العراقي حصراً.\n"
        f"المرحلة: {data.grade_level}\n"
        f"المادة: {data.subject}\n"
        f"سياق المنهج: {subject_context}\n"
        f"أجب بدقة وبشكل تعليمي منظم."
    )
    
    if not API_KEY:
        # نظام احتياطي في حال لم يُضاف مفتاح البيئة مؤقتاً
        return {
            "response": f"[وضع محلي متكامل]: استلمت سؤالك عن ({data.message}) في مرحلة {data.grade_level} لمادة {data.subject}.",
            "context_used": subject_context
        }
    
    try:
        model = genai.GenerativeModel(
            model_name='gemini-2.0-flash',
            system_instruction=system_prompt
        )
        response = model.generate_content(data.message)
        
        if response and response.text:
            return {
                "response": response.text,
                "grade_level": data.grade_level,
                "subject": data.subject
            }
        else:
            raise HTTPException(status_code=500, detail="فشل توليد الرد من النموذج")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("Serverfile1:app", host="127.0.0.1", port=8000, reload=True)
    
