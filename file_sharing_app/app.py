import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
from pyqrcode import QRCode
import png
import os

PORT = 8010

os.environ['USERPROFILE']
desktop = os.path.join(os.environ['USERPROFILE'],
                       'Desktop')
os.chdir(desktop)

Handler = http.server.SimpleHTTPRequestHandler
hostname = socket.gethostname()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
s.close()

url = pyqrcode.create(IP)
qr_filename = "myqr.svg"
url.svg(qr_filename, scale=8)
webbrowser.open(qr_filename)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    print("Type this in your browser", IP)
    print("or use the QR code")
    httpd.serve_forever()