# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""The EmbeddingsLLM class."""
import logging
from typing import Unpack
from graphrag.llm.base import BaseLLM
from graphrag.llm.types import (
    EmbeddingInput,
    EmbeddingOutput,
    LLMInput,
)

from http import HTTPStatus
import dashscope
import logging

log = logging.getLogger(__name__)


class QwenEmbeddingsLLM(BaseLLM[EmbeddingInput, EmbeddingOutput]):
    """A text-embedding generator LLM using Dashscope's API."""

    def __init__(self, llm_config: dict = None): # type: ignore
        log.info(f"llm_config: {llm_config}")
        self.llm_config = llm_config or {}
        self.api_key = self.llm_config.get("api_key", "")
        self.model = self.llm_config.get("model", dashscope.TextEmbedding.Models.text_embedding_v2)

    async def _execute_llm(
            self, input: EmbeddingInput, **kwargs: Unpack[LLMInput]
    ) -> EmbeddingOutput:
        log.info(f"input: {input}")

        response = dashscope.TextEmbedding.call(
            model=self.model,
            input=input,
            api_key=self.api_key
        )

        if response.status_code == HTTPStatus.OK:
            print("qwen TextEmbedding res")
            res = [embedding["embedding"] for embedding in response.output["embeddings"]]
            return res
        else:
            raise Exception(f"Error {response.code}: {response.message}")

