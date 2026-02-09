from pydantic.v1 import BaseModel


class PromptQuestion(BaseModel):
    question: str