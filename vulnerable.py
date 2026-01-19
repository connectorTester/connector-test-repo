
import os
import flask

app = flask.Flask(__name__)

@app.route("/rce")
def rce():
    # Vulnerable to command injection and SQL injection
    cmd = flask.request.args.get("cmd")
    os.system(cmd)
    return "Executed"
