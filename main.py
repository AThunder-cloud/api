# main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.database import engine, Base
from app.controllers.user_controller import user_controller

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield  # Allows FastAPI to continue execution

# ✅ Correctly initialize FastAPI with lifespan
app = FastAPI(title="🔥FastAPI", lifespan=lifespan)

# ✅ Register routes AFTER defining the FastAPI app
app.include_router(user_controller.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "FastAPI Backend Running 🚀"}
