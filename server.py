import json
from imageai.Detection import ObjectDetection
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
import cv2
import numpy as np
import base64
import time

hostName = ""
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if (self.path.endswith('/favicon.ico')):
            with open("./favicon.ico", "rb") as f:
                bytes_read = f.read()
                self.send_response(200)
                self.send_header("Content-type", "image/x-icon")
                self.end_headers()
                self.wfile.write(bytes_read)
        else:
            with open("./img.html", "rb") as f:
                bytes_read = f.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes_read)

    def do_POST(self):
        r, info = self.deal_post_data()
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(info), "utf-8"))

    def deal_post_data(self):
        ctype, pdict = cgi.parse_header(self.headers['Content-Type'])
        pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
        pdict['CONTENT-LENGTH'] = int(self.headers['Content-Length'])
        val = "error"
        if ctype == 'multipart/form-data':
            form = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD':'POST', 'CONTENT_TYPE':self.headers['Content-Type'], })
            try:
                if isinstance(form["file"], list):
                    for record in form["file"]:
                        val = self.process(record.filename, record.file)
                else:
                    val = self.process(form["file"].filename, form["file"].file)
            except IOError:
                    return (False, "Something went horribly wrong.")
        return (True, val)

    def process(self, outfile, infile):
        now = time.time()
        cv2_img_flag=cv2.IMREAD_COLOR
        img_array = np.asarray(bytearray(infile.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, cv2_img_flag)
        detection = detector.detectObjectsFromImage(input_type="stream", input_image=img, output_type="array")
        val, en = cv2.imencode('.jpg', detection[0])
        info = { "img": base64.b64encode(en.tobytes()).decode("utf-8"), "objects": detection[1], "millis": round((time.time()-now)*1000), "name": outfile }
        return info

# curl -F 'file=@/home/mraiser/Desktop/22.jpg' http://localhost:8080/upload
if __name__ == "__main__":
    detector = ObjectDetection()

    model_path = "./yolo-tiny.h5"

    detector.setModelTypeAsTinyYOLOv3()
    detector.setModelPath(model_path)
    detector.loadModel(detection_speed="fastest")

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

