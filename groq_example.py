from groq import Groq

# Configure API
client = Groq(api_key=YOUR_API_KEY")

def query_api(prompt):
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant"
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"

# Main execution
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying Groq API...")

    result = query_api(user_prompt)

    print("Response:")
    print(result)

