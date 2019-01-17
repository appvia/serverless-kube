# Template for deploying an app using serverless

## Pre-reqs
* Kube cluster with kubeless installed
* Python 3, kubectl, kubeless CLI and serverless CLI installed
* Google cloud credentials configured [see link](https://serverless.com/framework/docs/providers/google/guide/credentials/)

## Install serverless plugin (within project dir)
```
$ sls plugin install --name serverless-kubeless
$ sls plugin install --name serverless-google-cloudfunctions
```

## Deploy to kubeless
```
$ sls deploy -f hello-you
$ sls invoke --function hello-you --log --data 'yourname'
```

