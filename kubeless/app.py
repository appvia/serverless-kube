def main(event, context):
    raw_request = event['extensions']['request']
    name = raw_request.query.name
    print(name)
    if not name:
        name = 'anon'
    return 'Hello {}'.format(name)
