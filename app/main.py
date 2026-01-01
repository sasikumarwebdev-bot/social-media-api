from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, get_db
from app import models
from app.routers import posts, users, auth, votes

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Social Media API", 
              description="A complete social media API built with FastAPI",
              version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)

@app.get("/")
def root():
    return {
        "message": "Welcome to Social Media API",
        "docs": "/docs",
        "redoc": "/redoc"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
