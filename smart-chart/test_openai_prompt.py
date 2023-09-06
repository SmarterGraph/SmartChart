from llms.gpt_all import OpenAI
from prompts.generate_code import GetCode
import unittest


class TestPrompt(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestPrompt, self).__init__(*args, **kwargs)
        self.openai = OpenAI()
        self.prompt = GetCode(
            df_columns="['a', 'b', 'c']",
            user_input="plot a chart",
            python_package="matplotlib",
        )

    def test_prompt(self):
        value = str(self.prompt)
        print(value)
        message = self.openai.query_chat_completion(value)
        print(message)


if __name__ == "__main__":
    unittest.main()
