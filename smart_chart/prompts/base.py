class BasePrompt:
    """
    Base class for creating and formatting prompts.
    """

    prompt_context = None
    key_words = {}

    def __init__(self, **kwargs) -> None:
        """
        Initialize prompt.

        Args:
            **kwargs: Keyword arguments.
        """
        if kwargs:
            self.key_words = kwargs

    def __str__(self) -> str:
        """
        String representation of prompt.

        Returns:
            str: String representation of prompt.
        """
        if self.prompt_context is None:
            print("Prompt Context is not set.")
        return self.prompt_context.format(**self.key_words)
