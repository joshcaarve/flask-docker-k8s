# flask-docker-k8s


# Running locally

## Start flask app
```sh
$ cd flask_and_docker
$ python3 app.py
```

## Test a request to API
```sh
$ ./test_request test.py localhost 5000 /
```

# Running flask app with Docker

## Set image name:
```sh
export IMAGE_NAME='josh-flask:0.0.1'
```

## Installing Docker Desktop

```sh
$ brew cask install docker
```

## Build the Image
```sh
$ cd flask_and_docker
$ docker build -t $IMAGE_NAME . --no-cache
$ docker run -p 8000:5000 $IMAGE_NAME
```

## Test a request to API
```sh
$ ./test_request/test.py 127.0.0.1 8000 /
```


# Running with Kubernetes
## Intall minikube

```sh
$ brew install minikube
```

## Start minikube and use aliases

```sh
$ source k8s/alias.sh
$ minikube start
```

## Link to Docker to minikube and build image
```sh
eval $(minikube docker-env)
cd flask_and_docker
docker build -t $IMAGE_NAME . --no-cache
```

## Using script to kustomize and deploy dev
```sh
$ cd k8s/dev && kustomize edit set image $IMAGE_NAME
$ kustomize build k8s/dev | kubectl apply -f - 
$ k port-forward svc/josh-flask 8000
```

## Test a request to API
```sh
$ ./test_request/test.py 127.0.0.1 8000 /
```

## Using script to kustomize and deploy prod
```sh
$ cd k8s/prod && kustomize edit set image $IMAGE_NAME
$ kustomize build k8s/prod | kubectl apply -f - 
$ k port-forward svc/josh-flask 8000
```

## Test a request to API
```sh
$ ./test_request/test.py 127.0.0.1 8000 /
```

# Cleanup
```sh
$ minikube delete
```
