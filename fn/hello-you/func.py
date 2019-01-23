import fdk
import json


def handler(ctx, data=None, loop=None):
    print('Function invoked')
    name = 'anon'
    if data and len(data) > 0:
        print(data)
        body = json.loads(data)
        try:
            name = body.get('name')
        except:
            print('Name not found')
    return json.dumps(data)


if __name__ == '__main__':
    fdk.handle(handler)

