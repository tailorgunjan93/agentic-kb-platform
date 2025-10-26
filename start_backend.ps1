$env:PYTHONPATH = "d:\Learning\KnowledgeBasePlatform\agentic-kb-platform"
Set-Location "d:\Learning\KnowledgeBasePlatform\agentic-kb-platform\backend"
uv run uvicorn main:app --reload --port 8000
