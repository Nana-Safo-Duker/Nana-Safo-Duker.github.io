@echo off
echo Starting local server...
start http://localhost:8080
npx http-server . -p 8080 -o

