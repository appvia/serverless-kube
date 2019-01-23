# Example app for deployment to Fn
[Fn](http://fnproject.io)

## Pre-reqs
* Kube cluster with Fn installed (requires ingress-nginx and cert-manager)
* Python 3, kubectl and [fn](https://github.com/fnproject/cli) CLI installed locally
* fn CLI context created for calling the fn API `fn create context --api-url ... --registry docker.io/yourusername... fn`
* A Docker registry with permissions/credentials to push images

## Deploy an action and inspect what has been created
```
$ fn deploy --app hello-you
$ fn list apps
$ fn inspect app hello-you
$ fn list functions hello-you
$ fn inspect function hello-you hello-you
$ fn list triggers hello-you
```

## Get the trigger URL and send a request
```
$ ENDPOINT=$(fn list triggers hello-you | grep -v ENDPOINT | awk '{print $6}')
$ curl -i http://$ENDPOINT -d '{"name": "yourname"}'
```

## Get a call ID from the response header and then view the call info
```
$ curl -s -i http://lb.example.com/t/hello-you/hello | grep Fn-Call-Id
$ fn get calls hello-you hello-you <your Call ID from above>
```

## View all calls
```
$ fn list calls hello-you hello-you
```

## After 30s send another request and time the cold start
```
$ time curl -i http://$ENDPOINT -d '{"name": "yourname"}'
```

## Cold start example timings
```
0m1.232s
0m1.101s
0m1.375s
```

## Hot function example timings
```
0m0.067s
0m0.071s
0m0.074s
```

### Debugging
* Add `DEBUG=1` before any fn command to see more detailed information
* Use `fn -v` to increase verbosity
* Use a syslog server to send logs from functions https://github.com/fnproject/tutorials/blob/master/Troubleshooting/README.md
