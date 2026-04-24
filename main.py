# main.py
from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "status": "Online",
        "app": "Lab-Kubernetes-Argo",
        "version": "1.0.0",
        "container_id": os.uname().nodename
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}