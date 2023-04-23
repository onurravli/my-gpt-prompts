import requests

OPENAI_API_KEY: str = ""


def get_credit(model: str, content: str, temp: float = 0.5) -> str:
    return requests.post(
        url="https://api.openai.com/v1/chat/completions",
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": "I will give you some texts which are "
                                              "written by you. And I want you to give their resource texts as "
                                              "a JSON. The JSON should be like this: "
                                              "[{'resource': 'resource1'}. "
                                              "If you can't write any info about text, just return an empty JSON"},
                {"role": "user", "content": content}
            ],
            "temperature": temp
        },
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }).json()['choices'][0]['message']['content']


res = get_credit(
    "gpt-3.5-turbo",
    "McDonald's is a fast food restaurant chain that was "
    "founded in 1940 by brothers Richard and Maurice McDonald "
    "in San Bernardino, California. The first McDonald's "
    "franchise was sold in 1953, and by the 1960s, the company "
    "had expanded to thousands of locations worldwide. Today, "
    "McDonald's is one of the most recognizable brands in the world.",
    0.5
)

print(res)
