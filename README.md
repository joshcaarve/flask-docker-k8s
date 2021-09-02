# flask-docker-k8s

###

# run locally
############################################
# Docker First
############################################
docker build -t josh-flask:0.1.1 . --no-cache
docker run -p 8000:5000 josh-flask:0.1.1
./test.py 127.0.0.1 8000 /

############################################
# Test with minikube
############################################
minikube start  # start minikube

# shellcheck disable=SC2046
# connect to docker desktop
eval $(minikube docker-env)

# build image
docker build -t josh-flask:0.1.2 . --no-cache

# deploy
k apply -f k8s/deployment.yaml

# service
k apply -f k8s/service.yaml


minikube tunnel
kgp --watch
#k logs <pod-name> josh-flask
k logs josh-flask-5445f6bbdb-rfk67 josh-flask
kgs # look for external ip

# hit server
./test.py 127.0.0.1 8000 /


kgd
k delete deployment josh-flask
k delete service josh-flask

minikube delete


######




############################################
# Test with kind (DNF)
############################################
docker build -t josh-flask:0.1.2 . --no-cache
kind create cluster
kind load docker-image josh-flask:0.1.2
# deploy
k apply -f k8s/deployment.yaml
# service
k apply -f k8s/service.yaml

# load balancer sucks to implement
