from http.server import BaseHTTPRequestHandler
from routes import GetRoutesHandler, PostRoutesHandler, PutRoutesHandler, DeleteRoutesHandler
import json


data = {'text': 'text_path',
        '': 'main_path'}


class ServiceHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        length = int(self.headers['Content-Length'])
        content = self.rfile.read(length)
        temp = str(content).strip('b\'')
        self.end_headers()
        return temp

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        path = self.path
        s_path = path.replace('/', '')
        r_data = data.get(s_path, "invalid_route")
        p_data = getattr(GetRoutesHandler, r_data)(self)
        self.wfile.write(json.dumps(p_data).encode())

    def do_POST(self):
        temp = self._set_headers()
        path = self.path
        s_path = path.replace('/', '')
        r_data = data.get(s_path, "invalid_route")
        p_data = getattr(PostRoutesHandler, r_data)(self)
        print(temp)
        self.wfile.write(json.dumps(p_data).encode())

    def do_PUT(self):
        temp = self._set_headers()
        path = self.path
        s_path = path.replace('/', '')
        r_data = data.get(s_path, "invalid_route")
        p_data = getattr(PutRoutesHandler, r_data)(self)
        print(temp)
        self.wfile.write(json.dumps(p_data).encode())

    def do_DELETE(self):
        temp = self._set_headers()
        path = self.path
        s_path = path.replace('/', '')
        r_data = data.get(s_path, "invalid_route")
        p_data = getattr(DeleteRoutesHandler, r_data)(self)
        print(temp)
        self.wfile.write(json.dumps(p_data).encode())
