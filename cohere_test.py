import cohere

co = cohere.Client("YOUR_API_KEY")

response = co.chat(
    model="command-a-03-2025",
    message="Explain artificial intelligence in one sentence"
)

print(response.text)






