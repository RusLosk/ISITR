from pydantic import BaseModel, Field


class CompareRequest(BaseModel):
    document_a: str = Field(..., description="Первый текстовый документ")
    document_b: str = Field(..., description="Второй текстовый документ")


class CompareResponse(BaseModel):
    similarity_score: float = Field(..., ge=0.0, le=1.0, description="Сходство документов по смыслу (0-1)")
    summary: str = Field(..., description="Краткое объяснение результата сравнения")
