from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import sys

data = sys.argv[1]
host = ('localhost', 8080)


class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        datas = self.rfile.read(int(self.headers['content-length']))

        print('headers', self.headers)
        print("do post:", self.path, self.client_address, datas)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()