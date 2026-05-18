from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.emails import router
from api.routes.auth import router as auth_router
from config import GEMINI_API_KEY
from database import init_db
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="supersecretkey")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://*.vercel.app"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()

app.include_router(router)
app.include_router(auth_router, prefix="/auth")