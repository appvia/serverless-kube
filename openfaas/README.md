# Template for deploying an app to openfaas
[OpenFaas](https://www.openfaas.com/)

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

## Deploy the faas-idler to scale down to zero after 5 mins
```
$ git clone git@github.com:openfaas-incubator/faas-idler.git
$ cd faas-idler
# Remove the mounted secret from the Deployment YAML first if you are not using API authentication for gateway component
$ kubectl create -f faas-idler-dep.yml
```

## Enable zero scale for the faas gateway
```
# Change zero_scale from "false" to "true" in the gateway deployment
$ kubectl edit deploy gateway --namespace=openfaas
```

## Label the hello-you function so it uses zero scale
```
$ faas-cli deploy -f ./hello-you.yml  --label "com.openfaas.scale.zero=true"
# After 5 mins of no requests the idler will terminate the running pod
$ kubectl logs -f <faas-idler pod ID> --namespace=openfaas -w
```
## Once no pods are running send a request and time the response
```
$ time curl $OPENFAAS_URL/function/hello-you -d "yourname"
```
## Example warm start times
```
0.904s
0.972s
0.989s
```
## Example cold start times
```
9.665s
10.112s
11.315s
```
