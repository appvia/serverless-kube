import os

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
    if request.args.get('name'):
        name = request.args.get('name')
    else:
        name = 'anon'
    return jsonify('Hello {}!'.format(name))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
