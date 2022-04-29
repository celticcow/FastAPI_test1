setup init libs

python3 -m pip install fastapi uvicorn[standard]

basic get / function in async mode

run command 

$ uvicorn fastapi_1:app --host 0.0.0.0 --port 9000 --reload

uvicorn fastapi_1:app --host 0.0.0.0 --port 9443 --ssl-keyfile='./key.pem' --ssl-certfile='./cert.pem' --reload

$ curl https://localhost:9443 -k
{"msg":"root"}

curl -k localhost:9443/info -X POST --data '{"info" : "hola"}'
