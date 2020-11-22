import flask
import base64
from flask import request, redirect

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def main():
    print('Request Arguments')
    print(request.args)
    state = request.args.get("state")
    code = request.args.get("code")
    error = request.args.get("error")
    error_code = request.args.get("error_code")
    error_description = request.args.get("error_description")
    error_reason = request.args.get("error_reason")
    data = decode(state).split('##')
    if code != None :
        redirectURL = data[1] + '?state=' + state + '&code=' + code
    else :
        redirectURL = data[1] + '?state=' + state + '&error=' + error + '&error_code=' + error_code + '&error_description=' + '&error_reason=' + error_reason
    print('Redirect URL')
    print(redirectURL)
    return redirect(redirectURL)

def decode(message):
    base64_message = message
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode('ascii')

def encode(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode('ascii')

if __name__ == "__main__":
    app.run(debug=True)