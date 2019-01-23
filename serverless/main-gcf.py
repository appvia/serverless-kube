def hello_you(request):
    data = event['data']
    name = data.decode('utf-8')
    if not name:
        name = 'anon'
    return 'Hello {}'.format(name)

