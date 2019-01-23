import fdk
import json


def handler(ctx, data=None, loop=None):
    name = 'anon'
    if data and len(data) > 0:
        body = json.loads(data)
        try:
            name = body.get('name')
        except:
            print('Name not found')
    return name


if __name__ == '__main__':
    fdk.handle(handler)

