from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import google.generativeai as genai
import uvicorn

app = FastAPI(title="Iraqi AI Engine Server", version="1.0")

# تهيئة مفتاح جيميناي
api_key = os.environ.get("GEMINI_API_KEY", "")
if api_key:
    genai.configure(api_key=api_key)

class ChatRequest(BaseModel):
    message: str
    grade_level: str = "السادس الإعدادي"

@app.post("/generate")
def generate_ai_response(data: ChatRequest):
    if not api_key:
        raise HTTPException(status_code=500, detail="مفتاح السيرفر غير معرّف في بيئة النظام")
    
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        prompt = f"المرحلة الدراسية: {data.grade_level}\nالسؤال: {data.message}"
        response = model.generate_content(prompt)
        
        if response and response.text:
            return {"response": response.text}
        else:
            raise HTTPException(status_code=500, detail="لم يتمكن النموذج من توليد إجابة")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("server_ai:app", host="127.0.0.1", port=8001, reload=True)
  
