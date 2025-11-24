from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import FAISS

from services.similarity_service import LLMSimilarityService


# similarity_service: LLMSimilarityService
#
#
# @app.on_event("startup")
# async def startup_event():
#     global similarity_service
#     similarity_service = init_similarity_service()


def init_similarity_service():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    vector_store = FAISS()  # позже будет реальный объект

    return LLMSimilarityService(llm_client=llm, embedding_model=embeddings, vector_store=vector_store)


def get_similarity_service() -> LLMSimilarityService:
    return init_similarity_service()
