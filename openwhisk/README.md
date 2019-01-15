# Example app for deployment to Openwhisk

## Pre-reqs
* Kube cluster with openwhisk installed and configured
* Python 3, kubectl and [wsk](https://github.com/apache/incubator-openwhisk-cli/releases) CLI installed locally
* wsk configured for accessing the openwhisk API

## GKE Gotchas
* You need to disable the default ingress and install the ingress-nginx before installing the openwhisk helm package
```
$ gcloud container clusters update yourcluster --update-addons HttpLoadBalancing=DISABLED
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/mandatory.yaml
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/provider/cloud-generic.yaml
```
* If you do not have a publicly resolvable domain name, use a hosts entry with the public ingress IP and the name used when generating certificates.
* `apiHostName` in `cluster.yaml` must be resolvable within the cluster else the `install-packages-*` pod will fail



## Deploy an action and invoke it
```
$ wsk -i action create hello-you hello-you.py --kind python:3
$ wsk -i action invoke --result hello-you --param name yourname
$ wsk -i action list
```


## Related links
* https://github.com/apache/incubator-openwhisk-workshop
