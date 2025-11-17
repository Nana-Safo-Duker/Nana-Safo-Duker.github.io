Write-Host "Starting local server..." -ForegroundColor Green
Start-Process "http://localhost:8080"
npx http-server . -p 8080 -o

