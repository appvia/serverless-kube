# Template for deploying an app to openfaas

## Pre-reqs
* Kube cluster with openfaas installed
* Python 3, kubectl and faas-cli installed
* faas-cli configured to point to the gateway using `export OPENFAAS_URL=...`

## Initialise a function using the CLI and build into an image
```
$ faas-cli new --lang python hello-you
```

## Update the handler.py
```
$ cp handler.py ./hello-world/handler.py
$ faas-cli build -f ./hello-you.yml
```

## If you are using a remote kube cluster, tag and push the image to a remote registry so it can be pulled on deploy (will require image pull secrets if authentication required)
```
$ docker tag hello-you yourregistry/hello-you
$ docker push yourregistry/hello-you
# Now update `image:` in `hello-you.yml` to match this
```

## Deploy the function, check it is in ready state and then send a request
```
$ faas-cli deploy -f ./hello-you.yml
$ faas-cli describe hello-you
$ curl $OPENFAAS_URL/function/hello-you -d "yourname"
```
