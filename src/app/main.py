"""Main FastAPI application module."""

from fastapi import FastAPI
from app.routers import items, auth

app = FastAPI(title="Item Management API")

app.include_router(auth.router, prefix="/auth", tags=["authentication"])

@app.get("/")
async def root():
    return {"message": "Welcome to the LLMOps Issue Resolver test Application!"}
