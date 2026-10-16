from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI(title="Iraqi AI Gateway Server", version="1.0")

@app.get("/")
def gateway_root():
    return {"status": "Gateway Server is running successfully", "service": "gateway"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("server_gateway:app", host="127.0.0.1", port=8000, reload=True)
  
