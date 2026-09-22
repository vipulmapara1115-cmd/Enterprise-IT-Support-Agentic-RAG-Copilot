import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from app.services.ingestion import load_file, chunk_documents
from app.rag.vectorstore import add_documents


docs = load_file(PROJECT_ROOT /"data/sample_kb/company_it_handbook.md")
chunks = chunk_documents(docs)

print (len(chunks))
add_documents(chunks)





