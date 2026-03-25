import requests

url = "http://localhost:11434/api/generate"

data = {
    "model": "llama3",
    "prompt": "Explain Newton's laws of motion in simple words",
    "stream": False
}

response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    print("Response:\n", result["response"])
else:
    print("Error:", response.status_code)
    
