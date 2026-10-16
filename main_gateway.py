"""
Root Master Gateway & Orchestrator - Iraqi AI Project
ملف التوزيع والربط المركزي في الجذر الرئيسي للمشروع
يتولى ربط وتوزيع البيانات بين قاعدة البيانات الكبرى، محرك الذكاء الاصطناعي، والسيرفرات المستقلة.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import os
import google.generativeai as genai

# استيراد قاعدة البيانات الكبرى من مجلد core
from core.curriculum_db import IraqiCurriculumDatabaseMaster

app = FastAPI(
    title="Iraqi AI Project - Root Master Gateway",
    version="1.0.0",
    description="البوابة المركزية في الجذر لتوزيع البيانات وربط المناهج بالذكاء الاصطناعي"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# تهيئة مفتاح جيميناي المركزي في الجذر
API_KEY = os.environ.get("GEMINI_API_KEY", "")
if API_KEY:
    genai.configure(api_key=API_KEY)

class MasterRequestPayload(BaseModel):
    stage: str = Field(default="السادس الإعدادي", description="المرحلة الدراسية")
    branch: str = Field(default="الفرع العلمي", description="الفرع أو التخصص")
    subject: str = Field(default="رياضيات", description="المادة الدراسية")
    query: str = Field(..., description="سؤال الطالب أو الاستعلام التعليمي")

@app.get("/")
def root_gateway_status():
    database_payload = IraqiCurriculumDatabaseMaster.get_full_database()
    return {
        "status": "ROOT_GATEWAY_ACTIVE",
        "message": "أهلاً بك في البوابة المركزية لمشروع الذكاء الاصطناعي التعليمي العراقي",
        "total_official_sources": len(database_payload.get("sources", [])),
        "supported_stages": list(database_payload.get("curriculum_data", {}).keys())
    }

@app.get("/api/sources")
def get_official_sources():
    """توزيع واسترجاع الـ 30 مصدر وموقع رسمي معتمد للمناهج"""
    return {
        "status": "success",
        "sources": IraqiCurriculumDatabaseMaster.get_all_official_sources()
    }

@app.post("/api/master/orchestrate")
def orchestrate_learning_process(payload: MasterRequestPayload):
    """
    النواة المركزية للتوزيع:
    1. جلب محتوى المنهج الدقيق والسياق من قاعدة البيانات الكبرى في core.
-    2. حقن السياق مع استعلام الطالب وتوجيهه لمحرك الذكاء الاصطناعي.
    """
    # 1. استخراج السياق من قاعدة البيانات الكبرى
    subject_context = IraqiCurriculumDatabaseMaster.get_subject_content(
        payload.stage, payload.branch, payload.subject
    )
    
    # 2. بناء التوجيه الشامل للذكاء الاصطناعي
    master_system_instruction = (
        f"أنت المعلم الأكاديمي المركزي للمناهج العراقية الرسمية.\n"
        f"المرحلة: {payload.stage} | الفرع: {payload.branch} | المادة: {payload.subject}\n"
        f"سياق المنهج والمقرر الوزاري المعتمد: {subject_context}\n"
        f"قم بتقديم شرح تفصيلي دقيق وعلمي يدعم الطالب العراقي."
    )
    
    if not API_KEY:
        return {
            "mode": "Root-Gateway-Local-Fallback",
            "stage": payload.stage,
            "subject": payload.subject,
            "injected_context": subject_context,
            "query": payload.query,
            "status": "Warning: GEMINI_API_KEY is missing in root environment."
        }
    
    try:
        model = genai.GenerativeModel(
            model_name='gemini-2.0-flash',
            system_instruction=master_system_instruction
        )
        response = model.generate_content(payload.query)
        
        if response and response.text:
            return {
                "status": "SUCCESS",
                "orchestrator": "Root Main Gateway",
                "stage": payload.stage,
                "subject": payload.subject,
                "curriculum_context_used": subject_context,
                "ai_response": response.text
            }
        else:
            raise HTTPException(status_code=500, detail="فشل المحرك المركزي في توليد الرد")
            
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"خطأ في البوابة المركزية: {str(err)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main_gateway:app", host="127.0.0.1", port=8000, reload=True)
  
