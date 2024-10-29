@echo off
set SCRIPT_PATH=%~dp0interceptor.py
mitmproxy -s "%SCRIPT_PATH%" --listen-port 8888
