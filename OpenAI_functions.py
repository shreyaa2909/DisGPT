import openai

def chat_with_openai(prompt, model="gpt-3.5-turbo-instruct", max_tokens=150):
    """
    Function to chat with OpenAI's GPT model.

    :param prompt: The input prompt or question for the model.
    :param model: The model to be used. Default is 'text-davinci-003'.
    :param max_tokens: Maximum number of tokens to generate in the output.
    :return: The model's response as a string.
    """
    try:
        openai.api_key = "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"  # Replace with your OpenAI API key

        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens
        )

        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)


def continuous_conversation():
    """
    Continuously converses with the user by taking user input and providing chatbot responses.
    """
    print("OpenAI Chatbot: Hello! I'm an AI chatbot. How can I assist you today?\n(Type 'quit' to exit)")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            print("OpenAI Chatbot: Goodbye!")
            break
        
        response = chat_with_openai(user_input)
        print(f"OpenAI Chatbot: {response}")
