import openai


# Initialize OpenAI
openai.api_key = OPENAI_API_KEY

def openai_handler(prompt):
            response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct", 
            prompt=prompt, 
            max_tokens=150

            )
