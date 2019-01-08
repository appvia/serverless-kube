# Template for deploying an app to kubeless

## Pre-reqs
* Kube cluster with kubeless installed
* Python 3, kubectl and kubeless CLI
* If you are using GKE you will need to disable the default ingress controller and use another [see this](https://kubeless.io/docs/http-triggers/)

## Deploy to kubeless and expose using ingress
```
$ kubeless function deploy hello-you --runtime python3.7 --handler app.main -f app.py
```

## Check the function is in READY state
```
$ kubeless function ls
```
Note - Troubleshooting logs are found on the kubeless-function-controller container of the kubeless-controller-manager pod.

## Call the function from the CLI
```
$ kubeless function call hello-you --data 'Hello world!'
```

## Check the function logs
```
$ kubeless function logs hello-you
```

## Expose using http via nginx ingress and send a test request
```
$ kubeless trigger http create hello-you --function-name hello-you --path hello --hostname example.com --gateway nginx
```
