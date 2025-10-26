# Test the search API
$query = "What is Gunjan experience"
$encodedQuery = [System.Web.HttpUtility]::UrlEncode($query)
$url = "http://localhost:8000/search/?query=$encodedQuery"

Write-Host "Testing search with query: $query" -ForegroundColor Cyan
Write-Host "URL: $url`n" -ForegroundColor Gray

try {
    $response = Invoke-RestMethod -Uri $url -Method Get
    Write-Host "Success! Found files:" -ForegroundColor Green
    $response.files | ForEach-Object {
        Write-Host "  - $($_.filename)" -ForegroundColor Yellow
    }
    Write-Host "`nTotal results: $($response.files.Count)" -ForegroundColor Green
} catch {
    Write-Host "Error: $_" -ForegroundColor Red
}
