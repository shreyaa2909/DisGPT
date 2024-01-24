import openai

OPENAI_API_KEY = "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"

# Initialize OpenAI
openai.api_key = OPENAI_API_KEY

def openai_handler(prompt):
    response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct", 
    prompt=prompt, 
    max_tokens=150
    )
    return response
