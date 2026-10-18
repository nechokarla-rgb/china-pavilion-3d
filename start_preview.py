from pathlib import Path
import socket, subprocess, sys, webbrowser
root = Path(__file__).resolve().parent
with socket.socket() as sock:
    running = sock.connect_ex(('127.0.0.1', 8767)) == 0
if not running:
    subprocess.Popen([sys.executable, '-m', 'http.server', '8767', '--bind', '127.0.0.1', '--directory', str(root)], creationflags=subprocess.CREATE_NO_WINDOW)
webbrowser.open('http://127.0.0.1:8767/')
