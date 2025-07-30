from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the K8s Ollama FastAPI Demo!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Additional API endpoints can be defined here as needed.