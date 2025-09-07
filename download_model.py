from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Define the model name from Hugging Face
MODEL_NAME = "google/flan-t5-base"
SAVE_PATH = "./fine-tuned-flan-t5-samsum/"

def download_and_save_model():
    """Downloads the model and tokenizer from Hugging Face and saves them locally."""
    print(f"Downloading model '{MODEL_NAME}' and tokenizer...")
    try:
        # Load and save tokenizer
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        tokenizer.save_pretrained(SAVE_PATH)
        print("Tokenizer downloaded and saved successfully.")

        # Load and save model
        model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
        model.save_pretrained(SAVE_PATH)
        print("Model downloaded and saved successfully.")

    except Exception as e:
        print(f"An error occurred during download: {e}")
        print("Please check your internet connection and try again.")

if __name__ == "__main__":
    download_and_save_model()
