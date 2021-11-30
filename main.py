import flask
import os

app = flask.Flask(__name__)
port = os.environ.get("PORT")
flagfile = "/tmp/NG"

@app.route("/")
def _check():
    if os.path.isfile(flagfile):
        return "NG", 503
    return "ok", 200

if __name__ == '__main__':
    app.run(port=port)
