@echo off
set USERNAME=""
set PASSWORD=""
set REPO=""

pip install fastapi uvicorn python-multipart 

uvicorn api:app --host 0.0.0.0 --port 8000

docker build .

for /f "tokens=*" %%i in ('docker images ^| findstr /r /c:"[0-9]"') do set IMAGE_ID=%%i

docker tag %IMAGE_ID% %REPO:savefiles%

docker login --username %USERNAME% --password %PASSWORD%

docker push %REPO:savefiles%

rmdir uploads