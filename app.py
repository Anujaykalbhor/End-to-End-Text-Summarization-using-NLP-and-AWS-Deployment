from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline, AutoTokenizer
import uvicorn

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a Pydantic model for the request body
class TextRequest(BaseModel):
    text: str

# Use a global variable to load the model and tokenizer once
summarizer = None
tokenizer = None

# A function to load the model on application startup
@app.on_event("startup")
async def load_model():
    global summarizer, tokenizer
    try:
        # Load the tokenizer from your specified path
        tokenizer = AutoTokenizer.from_pretrained("./fine-tuned-flan-t5-samsum/")
        
        # Load the model with the pipeline
        summarizer = pipeline(
            "summarization",
            model="./fine-tuned-flan-t5-samsum/",
            tokenizer=tokenizer
        )
        print("Model and tokenizer loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")
        # Exit or handle the error gracefully

@app.get("/")
def home():
    return {"message": "Summarization API is ready. Use the /predict endpoint to get a summary."}

@app.post("/predict")
async def predict_route(request: TextRequest):
    """
    Summarizes the given text.
    """
    if not summarizer:
        return {"error": "Model not loaded. Please check server logs."}

    try:
        gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}
        summary = summarizer(request.text, **gen_kwargs)[0]["summary_text"]
        return {"summary": summary}
    except Exception as e:
        return {"error": f"An error occurred during prediction: {e}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
