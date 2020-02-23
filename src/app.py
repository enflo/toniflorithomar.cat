import os
import sentry_sdk
from flask import Flask, render_template, jsonify, request
from sentry_sdk.integrations.flask import FlaskIntegration

app = Flask(__name__)

sentry_sdk.init(
    dsn="https://add5490ec85c4c228c63e480f8e95293@sentry.io/2793838",
    integrations=[FlaskIntegration()]
)

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@app.errorhandler(404)
def resource_not_found(e):
    return ('', 404)


@app.errorhandler(405)
def method_not_allowed(e):
    return ('', 405)

@app.errorhandler(500)
def unexpected_server_error(e):
    return render_template('500_response.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=int(os.environ.get('PORT', 8080)))