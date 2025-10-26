# Export data from local PostgreSQL
Write-Host "Exporting data from local PostgreSQL..."
$env:PGPASSWORD = "Gun@123!"
pg_dump -h localhost -U postgres -d agentic_kb --data-only --inserts -f local_data.sql

# Import to Docker PostgreSQL
Write-Host "Importing data to Docker PostgreSQL..."
Get-Content local_data.sql | docker exec -i agentic-kb-platform-db-1 psql -U postgres -d agentic_kb

Write-Host "Data copied successfully!"
