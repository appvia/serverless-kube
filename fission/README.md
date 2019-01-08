# Example app for deployment to fission

## Pre-reqs
* Kube cluster with fission installed
* Python 3, kubectl and fission installed locally

## Deploy to fission by creating a spec and applying
```
$ fission spec init
$ fission env create --spec --name python --image fission/python-env
$ fission function create --spec --name hello-you --env python --code app.py --entrypoint main
$ fission route create --spec --method GET --url /hello --function hello-you
```

## Get the IP of the fission router and send a request with timing
```
$ export IP_ADDRESS=$(kubectl --namespace fission get svc router -o=jsonpath='{..ip}')
$ time curl "http://${IP_ADDRESS?}?name=yourname"
```

## Example response times
```
0m0.045s
0m0.039s
0m0.053s
```

## Change executor type to newdeploy (which can scale to zero)
```
$ fission function delete hello-you
$ rm -f specs/function*
$ fission function create --spec \
                          --name hello-you \
                          --env python \
                          --code app.py \
                          --entrypoint main \
                          --executortype newdeploy \
                          --minscale 0 \
                          --maxscale 3 \
                          --mincpu 100 \
                          --maxcpu 200 \
                          --minmemory 128 \
                          --maxmemory 256 \
                          --targetcpu 30
$ fission spec apply
```

## Send another request with timing after 10 minutes (or once pods have been terminated)
```
$ time curl "http://${IP_ADDRESS?}?name=yourname"
```

## Note the response times
```
0m1.065s (a cold start...)
0m0.037s (warm...)
0m0.054s
```

## Look at the HPA using kubectl
```
kubectl -n fission-function get hpa -w
```
