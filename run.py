import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

# from app.services.ingestion import load_file, chunk_documents
# from app.rag.vectorstore import ensure_index, get_embeddings, get_embedding_dimension

# docs = load_file(PROJECT_ROOT / "data/sample_kb/company_it_handbook.md")
# docs = chunk_documents(docs)

# print (len(docs))

import uvicorn
# from app.core.config import get_settings
# settings = get_settings()
# print(f"App Name: {settings.app_name}")
# print(f"Open AI API Key: {settings.openai_api_key}")

if __name__ == "__main__":
	uvicorn.run(
		"app.main:app",
		host="127.0.0.1",
		port=8080,
		reload=True,
		app_dir=str(PROJECT_ROOT),
	)
    
