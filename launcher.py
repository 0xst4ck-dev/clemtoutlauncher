# Made by the ClemtoutLauncher Team.
# You are allowed to use, modify, and redistribute this software for non-commercial purposes only.
# Sources:
# - Unpacker/Steamless: https://github.com/atom0s/Steamless
# - Steamtool : https://github.com/OpenSteam001/OpenSteamTool

import sys
import os
import threading
import time
import webview
import io
if getattr(sys, 'frozen', False):
    meipass = sys._MEIPASS
    dlls_to_remove = [
        'MSVCP140.dll',
        'VCRUNTIME140.dll',
        'VCRUNTIME140_1.dll',
        'ucrtbase.dll',
        'DWMAPI.dll',
    ]
    for dll in dlls_to_remove:
        dll_path = os.path.join(meipass, dll)
        try:
            if os.path.exists(dll_path):
                os.remove(dll_path)
                print(f"Delete : {dll}")
        except Exception as e:
            print(f"Unable to delete {dll}: {e}")

os.environ['_ORIGINAL_PATH'] = os.environ.get('PATH', '')
os.environ['_PYINSTALLER_FROZEN'] = '1'

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
if getattr(sys, 'frozen', False):
    project_root = sys._MEIPASS
else:
    current_file_path = os.path.abspath(__file__)
    project_root = os.path.dirname(current_file_path)

sys.path.insert(0, project_root)

try:
    from backend.app import app
except ImportError:
    from app import app

def start_backend():
    from werkzeug.serving import run_simple
    run_simple('127.0.0.1', 8000, app, use_reloader=False, threaded=True)

def main():
    backend_thread = threading.Thread(target=start_backend, daemon=True)
    backend_thread.start()

    time.sleep(1)

    webview.create_window(
        'Clemtout Launcher',
        'http://127.0.0.1:8000',
        width=1230,
        height=800,
        background_color='#171a21',
        text_select=True

    )
    webview.start()

if __name__ == '__main__':
    main()
