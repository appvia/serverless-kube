def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    if req:
        name = req
    else:
        name = 'anon'

    return 'Hello {}'.format(name)
