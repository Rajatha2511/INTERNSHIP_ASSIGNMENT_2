from huggingface_hub import InferenceClient

# Configure API
client = InferenceClient(
    model="tiiuae/falcon-rw-1b",
    token="hf_your_token_here"
)

def query_api(prompt):
    try:
        response = client.text_generation(
            prompt,
            max_new_tokens=100
        )
        return response

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying Hugging Face API...")

    result = query_api(user_prompt)

    print("Final Output:")
    print(result)
    


