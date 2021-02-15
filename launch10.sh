trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT
python3 server.py localhost 8080 &
python3 server.py localhost 8081 &
python3 server.py localhost 8082 &
python3 server.py localhost 8083 &
python3 server.py localhost 8084 &
python3 server.py localhost 8085 &
python3 server.py localhost 8086 &
python3 server.py localhost 8087 &
python3 server.py localhost 8088 &
python3 server.py localhost 8089
