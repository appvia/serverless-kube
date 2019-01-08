from flask import request, jsonify

def main():
    print('Invoking function')
    if request.args.get('name'):
        name = request.args.get('name')
    else:
        name = 'anon'
    return jsonify('Hello {}'.format(name))
