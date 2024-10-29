import ast
import os
from dotenv import load_dotenv
from mitmproxy import http

load_dotenv()

SUBSTRINGS_TO_BLOCK = os.getenv("SUBSTRINGS_TO_BLOCK", "")
SUBSTRINGS_TO_BLOCK = ast.literal_eval(SUBSTRINGS_TO_BLOCK) if SUBSTRINGS_TO_BLOCK else []

def request(flow: http.HTTPFlow) -> None:
    if any(substring in flow.request.pretty_url for substring in SUBSTRINGS_TO_BLOCK):
        flow.response = http.Response.make(
            403,
            "Blocked by custom filter",
            {"Content-Type": "text/html"}
        )
    
    referer = flow.request.headers.get("Referer", "")
    if any(substring in referer for substring in SUBSTRINGS_TO_BLOCK):
        flow.response = http.Response.make(
            403,
            "Blocked by custom filter",
            {"Content-Type": "text/html"}
        )
