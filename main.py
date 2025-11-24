from fastapi import FastAPI, Depends, UploadFile, File, HTTPException
from models import CompareRequest, CompareResponse
from dependencies import get_similarity_service
from services.similarity_service import SimilarityService

app = FastAPI(
    title="Document Semantic Similarity API",
    description="API для сравнения текстовых документов по смыслу с использованием LLM + RAG.",
    version="1.0.0"
)


@app.post("/compare", response_model=CompareResponse)
async def compare_documents(
        request: CompareRequest,
        service: SimilarityService = Depends(get_similarity_service)
):
    return await service.compare_texts(request.document_a, request.document_b)


@app.post("/compare_files", response_model=CompareResponse)
async def compare_files(
        file_a: UploadFile = File(...),
        file_b: UploadFile = File(...),
        service: SimilarityService = Depends(get_similarity_service)
):
    if not (file_a.filename.endswith(".txt") and file_b.filename.endswith(".txt")):
        raise HTTPException(status_code=400, detail="Поддерживаются только файлы .txt")

    content_a = (await file_a.read()).decode("utf-8", errors="ignore")
    content_b = (await file_b.read()).decode("utf-8", errors="ignore")

    return await service.compare_texts(content_a, content_b)
