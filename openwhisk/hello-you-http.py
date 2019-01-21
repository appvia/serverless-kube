def main(args):
    try:
        name = args.name
    except:
        name = 'anon'
    return {'body': 'Hello {}'.format(name)}
