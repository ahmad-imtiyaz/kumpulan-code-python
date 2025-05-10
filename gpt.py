import openai

def generate_response(prompt):
    """
    Function to generate a response using OpenAI's GPT model.
    :param prompt: The input prompt for the GPT model.
    :return: The generated response.
    """
    try:
        openai.api_key = "your-api-key-here"  # Replace with your OpenAI API key
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    user_prompt = input("Masukkan prompt Anda: ")
    result = generate_response(user_prompt)
    print("Response dari GPT:", result)

print("selesai")
