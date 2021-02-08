# imageai-server
A simple HTTP server to automate detection of objects over a network

## Dependencies:
- https://github.com/OlafenwaMoses/ImageAI
- https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo-tiny.h5/

## Installation
- Install ImageAI
- Copy yolo-tiny.h5 to project folder

## Usage
curl -F 'file=@/path/to/file/image.jpg' http://localhost:8080/upload

OR

Open http://localhost:8080 in web browser
