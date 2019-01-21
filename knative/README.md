# Template for autoscaling flask app using knative
[Knative](https://github.com/knative/)

## Pre-reqs
* Kube cluster with knative installed
* Python 3, kubectl and flask installed locally

## Run the app locally
```
$ flask run
$ open http://localhost:5000?name=yourname
```

## Deploy to kube
```
$ kubectl apply -f service.yaml
```

## Watch things happen
```
$ kubectl get events --sort-by=.metadata.creationTimestamp
```

## Check there are some pods (they will only live for 5 mins with no requests)
```
$ kubectl get pods
```

## Get the ingress and send a request once no pods are alive
```
$ export IP_ADDRESS=`kubectl get svc knative-ingressgateway --namespace istio-system --output jsonpath="{.status.loadBalancer.ingress[*].ip}"`
$ time curl --header "Host: hello-you.default.example.com" "http://${IP_ADDRESS?}?name=yourname"
```

## Cold start samples (images already pulled, no pods running)
```
0m7.365s
0m6.100s
0m7.926s
```

## Warm start samples (pods running)
```
0m0.353s
0m0.628s
0m0.355s
```
