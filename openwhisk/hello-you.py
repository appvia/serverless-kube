def main(args):
    name = args.get('name', 'anon')
    greeting = {'Hello': name}
    print(greeting)
    return greeting
