import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Acknowledge the use of a GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device for inference: {device}")

# --- 1. Load the tokenizer and fine-tuned model ---
# The model and tokenizer were saved to this directory after training.
model_path = "./fine-tuned-flan-t5-samsum"

try:
    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    # Load the fine-tuned model and move it to the appropriate device (CPU or GPU)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path).to(device)
    print(f"Successfully loaded fine-tuned model and tokenizer from '{model_path}'")
except Exception as e:
    print(f"Error loading model from {model_path}: {e}")
    print("Please ensure the directory exists and contains all model files.")
    # Exit if the model cannot be loaded
    exit()

# Set the model to evaluation mode
# This is important for inference, as it disables training-specific layers like dropout.
model.eval()

# --- 2. Define a function to generate a summary ---
def generate_summary(dialogue, max_length=150):
    """
    Generates a summary for a given dialogue using the fine-tuned model.

    Args:
        dialogue (str): The dialogue text to summarize.
        max_length (int): The maximum length of the generated summary.

    Returns:
        str: The generated summary.
    """
    # The FLAN-T5 model requires a specific prefix for the summarization task
    input_text = f"summarize: {dialogue}"
    
    # Tokenize the input text
    inputs = tokenizer(
        input_text,
        max_length=1024,
        truncation=True,
        return_tensors="pt"
    ).to(device)

    # Generate the summary using the model
    # We use 'no_grad' to ensure no gradients are calculated during inference, saving memory and time
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=max_length,
            num_beams=4,
            early_stopping=True
        )

    # Decode the generated token IDs back into a human-readable string
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary

# --- 3. Example Usage ---
if __name__ == "__main__":
    # Sample dialogue to summarize
    sample_dialogue = """
    # Person1: What do you think about the new project?
    # Person2: It's going well. I've finished the core backend logic.
    # Person1: That's great! When will the frontend be ready?
    # Person2: The frontend team is working on it. They said it'll be done by the end of the week.
    # Person1: Awesome. We can start testing next week then.
    """
    
    print("--- Dialogue for Summarization ---")
    print(sample_dialogue)
    
    # Generate the summary
    generated_summary = generate_summary(sample_dialogue)
    
    print("\n--- Generated Summary ---")
    print(generated_summary)
