from flask import Flask, request, Response
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Replace with the URL of the server you want to forward requests to
TARGET_URL = "http://167.172.123.14:8081"

@app.route('/proxytest', methods=['GET'])
def proxy_test():
    return "Proxy server seems to be working"

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
    # Construct the target URL
    url = f"{TARGET_URL}/{path}"
    
    # Forward the request to the target server
    if request.method == 'GET':
        response = requests.get(url, headers=request.headers, params=request.args)
    elif request.method == 'POST':
        response = requests.post(url, headers=request.headers, json=request.json)
    elif request.method == 'PUT':
        response = requests.put(url, headers=request.headers, json=request.json)
    elif request.method == 'DELETE':
        response = requests.delete(url, headers=request.headers)

    # Return the response from the target server back to the client
    return Response(response.content, status=response.status_code, headers=dict(response.headers))

if __name__ == "__main__":

    app.run()
