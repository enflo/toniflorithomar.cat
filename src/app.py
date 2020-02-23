import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

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