from pydantic import BaseModel

# Model for receiving a request
class SummarizeRequest(BaseModel):
    text: str

# Answer model
class SummarizeOutput(BaseModel):
    summary: str