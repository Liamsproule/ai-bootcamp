import requests, sys; print("Status:", requests.get("https://httpbin.org/status/200").status_code)
