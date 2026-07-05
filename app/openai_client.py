from openai import OpenAI

from app.config import OPENAI_API_KEY, OPENAI_MODEL


class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def generate(self, prompt: str) -> str:
        """
        Generate a response from the OpenAI model.

        Args:
            prompt (str): Prompt to send to the model.

        Returns:
            str: Model response.
        """
        response = self.client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert Business Proposal Generator."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
        )

        return response.choices[0].message.content.strip()


# Singleton instance
llm = OpenAIClient()