// حفظ مفتاح الـ API في الذاكرة المحلية للمتصفح تلقائياً
document.getElementById('api-key-input').addEventListener('input', function(e) {
    localStorage.setItem('gemini_api_key', e.target.value);
});

window.addEventListener('DOMContentLoaded', () => {
    const savedKey = localStorage.getItem('gemini_api_key');
    if (savedKey) {
        document.getElementById('api-key-input').value = savedKey;
    }
});

async function sendMessage() {
    const input = document.getElementById('user-input');
    const text = input.value.trim();
    const grade = document.getElementById('grade-select').value;
    const apiKey = document.getElementById('api-key-input').value.trim();
    
    if (!text) return;

    const container = document.getElementById('chat-container');
    
    // إظهار رسالة المستخدم
    const userDiv = document.createElement('div');
    userDiv.className = 'message user-msg';
    userDiv.textContent = text;
    container.appendChild(userDiv);
    
    input.value = '';
    container.scrollTop = container.scrollHeight;

    // مؤشر التحميل ريثما يجيب الذكاء الاصطناعي
    const loadingId = 'loading-' + Date.now();
    const aiDiv = document.createElement('div');
    aiDiv.className = 'message ai-msg';
    aiDiv.id = loadingId;
    aiDiv.textContent = "جاري تحليل المنهج العراقي وإعداد الشرح المفصل...";
    container.appendChild(aiDiv);
    container.scrollTop = container.scrollHeight;

    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text, grade: grade, apiKey: apiKey })
        });
        
        const data = await response.json();
        const loadingElement = document.getElementById(loadingId);
        
        if (response.ok) {
            loadingElement.textContent = data.response;
        } else {
            loadingElement.textContent = "خطأ: " + (data.error || "تعذر الاتصال بالخادم");
        }
    } catch (error) {
        const loadingElement = document.getElementById(loadingId);
        if (loadingElement) {
            loadingElement.textContent = "عذراً، حدث خطأ في الاتصال بالشبكة.";
        }
    }
    container.scrollTop = container.scrollHeight;
}

function handleKeyPress(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
}

function clearChat() {
    const container = document.getElementById('chat-container');
    container.innerHTML = `<div class="message ai-msg">تم مسح المحادثة. كيف يمكنني مساعدتك في شرح دروس المنهج العراقي اليوم؟</div>`;
}
