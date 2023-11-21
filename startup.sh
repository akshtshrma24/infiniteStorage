USERNAME=""
PASSWORD=""
REPO=""

pip install fastapi uvicorn python-multipart 

uvicorn api:app --host 0.0.0.0 --port 8000 

docker build . 

docker tag "$(docker images | awk '{print $3}' | awk 'NR==2')" $REPO:savefiles

docker login --username $USERNAME --password $PASSWORD

docker push $REPO:savefiles