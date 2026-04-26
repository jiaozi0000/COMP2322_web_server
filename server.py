import socket
import threading
import os
import time
from datetime import datetime
#------------Configuration----------
HOST ='127.0.0.1'
PORT = 8080
WWW_DIR = 'www'
LOG_FILE = 'log.txt'

#------------MIME Types----------------
MIME_Types = {
    '.html': 'text/html', '.htm': 'text/html',
    '.txt': 'text/plain',
    '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
    '.png': 'image/png', '.gif': 'image/gif'
}


def get_mime_type(path):
    """Get MIME type from file extension."""
    ext = os.path.splitext(path)[1].lower()
    return MIME_Types.get(ext, 'application/octet-stream')


def write_log(ip, request_line, status):
    """Log one request to log.txt."""
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{now}] {ip} | {request_line} | {status}\n")


def parse_request(data):
    """Parse HTTP request into (method, path, headers, request_line)."""
    lines = data.split('\r\n')
    request_line = lines[0]
    parts = request_line.split(' ')
    
    if len(parts) < 3:
        return None, None, None, None
    
    method, path = parts[0], parts[1]
    headers = {}
    for line in lines[1:]:
        if ':' in line:
            k, v = line.split(':', 1)
            headers[k.strip()] = v.strip()
    
    return method, path, headers, request_line


def build_response(code, content_type, body, extra=None):
    """Build an HTTP response."""
    msgs = {200: 'OK', 304: 'Not Modified', 400: 'Bad Request',
            403: 'Forbidden', 404: 'Not Found'}
    
    resp = f'HTTP/1.1 {code} {msgs.get(code, "Unknown")}\r\n'
    resp += f'Content-Type: {content_type}\r\n'
    resp += f'Content-Length: {len(body)}\r\n'
    resp += f'Connection: close\r\n'
    resp += f'Server: Comp2322\r\n'
    
    if extra:
        for k, v in extra.items():
            resp += f'{k}: {v}\r\n'
    
    resp += '\r\n'
    return resp.encode() + body

#-----------------Error Response------------
def error_400():
    body = b'<h1>400 Bad Request</h1>'
    return build_response(400, 'text/html',body)

def error_403():
    body = b'<h1>403 Forbidden</h1>'
    return build_response(403, 'text/html',body)

def error_404():
    body = b'<h1>404 File Not Found</h1>'
    return build_response(404, 'text/html',body)

def error_304():
    return build_response(304, 'text/html', b'')

#-------------------Handle GET and HEAD---------------
def handle_get(path, headers):
    """Handle Get request."""
    if path == '/':
        path = '/index.html'
    
    safe = os.path.normpath(path.lstrip('/'))
    full = os.path.join(WWW_DIR, safe)
    
    if not os.path.exists(full):
        return error_404(), 404
    
    if not os.access(full, os.R_OK):
        return error_403(), 403
    
    mtime = os.path.getmtime(full)
    last_mod = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime(mtime))
    
    if headers.get('If-Modified-Since') == last_mod:
        return error_304(), 304
    
    mime = get_mime_type(full)
    is_img = mime.startswith('image/')
    
    with open(full, 'rb' if is_img else 'r', encoding=None if is_img else 'utf-8') as f:
        body = f.read()
    
    if not is_img:
        body = body.encode()
    
    return build_response(200, mime, body, {'Last-Modified': last_mod}), 200


def handle_head(path, headers):
    """Handle HEAD request."""
    resp, status = handle_get(path, headers)
    idx = resp.find(b'\r\n\r\n')
    return resp[:idx+4] if idx != -1 else resp, status











def start():
    """Start the server (placeholder)."""
    print(f"Server starting at http://{HOST}:{PORT}")
    print("Press Ctrl+C to stop")

 
if __name__ == '__main__':
    if not os.path.exists(WWW_DIR):
        os.makedirs(WWW_DIR)
    start()
