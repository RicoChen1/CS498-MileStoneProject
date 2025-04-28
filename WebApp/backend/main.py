# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# --- 配置 CORS ---
# 允许来自 Vue 开发服务器 (假设是 http://localhost:5173 或其他 Vite/Vue CLI 默认端口) 的请求
# 在生产环境中应配置更严格的来源
origins = [
    "http://localhost:5173", # Vite 默认端口
    "http://localhost:8080", # Vue CLI 默认端口 (以防万一)
    "http://127.0.0.1:5173",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # 允许访问的源
    allow_credentials=True, # 支持 cookie
    allow_methods=["*"], # 允许所有方法
    allow_headers=["*"], # 允许所有请求头
)
# --- CORS 配置结束 ---

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI Backend"}

@app.get("/api/test") # 示例 API 端点
async def get_test_data():
    return {"data": "Some data from backend API"}

# --- 后续在这里添加模型加载、推理等功能的 API 端点 ---