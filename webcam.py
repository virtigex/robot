import sys
import os
import subprocess
import SimpleHTTPServer

def get_image():
    file = 'image.png'
    ret = subprocess.call(['/usr/bin/fswebcam', 'image.png'])
    with open('image.png') as file:
        return file.read()
    #imgsrc = subprocess.Popen(['/usr/bin/fswebcam', '-'], shell=True, stdout=subprocess.PIPE)
    #imgdata = imgsrc.stdout.read()
    #return imgdata

class WebCamServer(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        print('do_GET', self.path)
        if self.path == '/image.png':
            print('process file', self.path)
            imagedata = get_image()
            self.send_response(200)
            self.send_header("Content-type", "octet/stream")
            self.send_header("Content-length", len(imagedata))
            self.end_headers()
            self.wfile.write(imagedata)
            #return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        else:
            self.send_response(404)

global httpd

httpd = None

def handler(signum, frame):
    global httpd
    print('got interrupted')
    httpd.shutdown()

if __name__ == '__main__':
    global httpd
    import SocketServer

    PORT = int(sys.argv[1])

    httpd = SocketServer.TCPServer(("", PORT), WebCamServer)

    pid = os.getpid()
    print("serving at port", PORT, 'with pid', pid)
    with open('webcam.id', 'w') as f:
        f.write(str(pid))
    httpd.serve_forever()

