# Check local PostgreSQL data
$env:PGPASSWORD = "Gun@123!"

Write-Host "`n=== Checking Local PostgreSQL ===" -ForegroundColor Cyan
Write-Host "Files count:"
psql -h localhost -U postgres -d agentic_kb -c "SELECT COUNT(*) FROM files;"

Write-Host "`nEmbeddings count:"
psql -h localhost -U postgres -d agentic_kb -c "SELECT COUNT(*) FROM embeddings;"

Write-Host "`nSample files:"
psql -h localhost -U postgres -d agentic_kb -c "SELECT filename, uploaded_at FROM files LIMIT 5;"
