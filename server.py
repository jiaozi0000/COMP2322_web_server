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

def start():
    """Start the server (placeholder)."""
    print(f"Server starting at http://{HOST}:{PORT}")
    print("Press Ctrl+C to stop")

 
 if __name__ == '__main__':
    if not os.path.exists(WWW_DIR):
        os.makedirs(WWW_DIR)
    start()