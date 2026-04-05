from pydantic import BaseModel

class UnderwritingRequest(BaseModel):
    document_text: str