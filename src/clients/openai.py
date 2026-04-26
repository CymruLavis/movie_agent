from openai import AsyncOpenAI
from pydantic_ai.models.openai import OpenAIResponsesModel
from pydantic_ai.providers.openai import OpenAIProvider

from src.config import OpenAIConfig


class OpenAIClient:
    def __init__(self, config: OpenAIConfig):

        self._model_name: str = config.MODEL
        self._open_ai_client: AsyncOpenAI = AsyncOpenAI(api_key=config.API_KEY)
        self._provider: OpenAIProvider = OpenAIProvider(
            openai_client=self._open_ai_client
        )

        self._model: OpenAIResponsesModel = OpenAIResponsesModel(
            model_name=self._model_name, provider=self._provider
        )

    def get_model(self) -> OpenAIResponsesModel:
        return self._model
