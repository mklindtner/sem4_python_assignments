from flask import Flask, request, jsonify, make_response

app = Flask(__name__)
SERVER_PASSWORD = "a9"

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    json_obj = request.get_json()
    secret = json_obj['password']
    mr = make_response()
    if secret == SERVER_PASSWORD:
        mr.status_code = 200
        return mr
    mr.status_code = 403
    return mr

if __name__ == '__main__':
    app.run()
