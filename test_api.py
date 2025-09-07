import requests
import json

# Define the URL of your FastAPI endpoint
URL = "http://localhost:8000/predict"

# The text you want to summarize. You can change this to any text you like.
text_to_summarize = """
The human brain is an incredibly complex organ, serving as the central nervous system's control center. It allows us to think, feel, move, and remember. Scientists have long studied the brain to understand how it functions, but many mysteries remain. Recent advancements in neuroscience and technology, such as fMRI and EEG, are helping researchers map the brain's intricate networks and uncover the secrets of consciousness and cognition.
"""

# Create the JSON payload. FastAPI expects the data in this format.
payload = {
    "text": text_to_summarize
}

print("Sending a POST request to the API...")

try:
    # Send the POST request
    response = requests.post(URL, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        summary_data = response.json()
        summary = summary_data.get("summary")
        print("\nAPI Response:")
        print("---")
        print(f"Original Text:\n{text_to_summarize}")
        print("---")
        print(f"Summary:\n{summary}")
        print("---")
    else:
        print(f"Error: Received status code {response.status_code}")
        print(response.json())

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
