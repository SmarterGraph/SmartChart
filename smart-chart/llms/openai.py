import openai
import os


class OpenAI:
    """OpenAI large language model class.

    Args:
        api_key (str, optional): OpenAI API key. Defaults to None.
        model_name (str, optional): OpenAI model name. Defaults to "gpt-4".
        temperature (float, optional): OpenAI temperature. Defaults to 0.1.
        max_tokens (int, optional): OpenAI max tokens. Defaults to 1000.
        top_p (float, optional): OpenAI top p. Defaults to 1.
        frequency_penalty (float, optional): OpenAI frequency penalty. Defaults to 0.
        presence_penalty (float, optional): OpenAI presence penalty. Defaults to 0.

    Raises:
        ValueError: If API key is not set.

    Returns:
        OpenAI: OpenAI large language model.
    """

    def __init__(
        self,
        api_key: str = None,
        model_name: str = "gpt-4",
        temperature: float = 0.1,
        max_tokens: int = 1000,
        top_p: float = 1,
        frequency_penalty: float = 0,
        presence_penalty: float = 0,
    ):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if api_key is None:
            raise ValueError("API key is not set.")
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty

        self.messages = []

    def query_chat_completion(self, value: str) -> str:
        """Query chat completion.

        Args:
            value (str): Value to query.

        Returns:
            str: Query result.
        """
        params = {
            "model": self.model_name,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "top_p": self.top_p,
            "frequency_penalty": self.frequency_penalty,
            "presence_penalty": self.presence_penalty,
            "messages": [
                {
                    "role": "system",
                    "content": value,
                }
            ],
        }
        response = openai.chatCompletion.create(**params)
        message = response["choices"][0]["message"]["content"]

        self.add_history(value, message)
        return message

    def add_history(self, user_message, bot_message):
        """add a user and bot message to the conversation history.

        Args:
            user_message (str): User message.
            bot_message (str): Bot response message.
        """
        self.messages.extend(
            [
                {"role": "system", "content": bot_message},
                {"role": "human", "content": user_message},
            ]
        )
