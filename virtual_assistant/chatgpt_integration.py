import openai
class ChatGPTClient:
    def __init__(self, api_key=None, model="gpt-4o-mini"):
        """
        Initializes the ChatGPT client with an API key and model.

        :param api_key: The OpenAI API key.
        :param model: The ChatGPT model to use.
        """
        self.model = model
        openai.api_key = self.api_key

    def create_chat(self, prompt, system_message="You are a helpful assistant."):
        """
        Sends a prompt to ChatGPT and retrieves the response.

        :param prompt: The input text to send to ChatGPT.
        :param system_message: The system message for ChatGPT's role.
        :return: The response from ChatGPT.
        """
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt}
                ]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"An error occurred: {str(e)}"
