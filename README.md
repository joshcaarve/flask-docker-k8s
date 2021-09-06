# flask-docker-k8s

###

# run locally
python3 app.py
./test.py localhost 5000 /

############################################



# Installing Docker Desktop
https://www.docker.com/products/docker-desktop
or
brew cask install docker


# Docker First
############################################
docker build -t josh-flask:0.0.1 . --no-cache
docker run -p 8000:5000 josh-flask:0.0.1
./test.py 127.0.0.1 8000 /

############################################

# Installing minikube
https://minikube.sigs.k8s.io/docs/start/

brew install minikube

# Test with minikube
############################################

source alias.sh

minikube start  # start minikube

# connect to docker desktop
eval $(minikube docker-env)

# build image
docker build -t josh-flask:0.0.1 . --no-cache

# Kustomzize build and apply
cd k8s/dev && kustomize edit set image josh-flask:0.0.1
kustomize build k8s/dev/ | k apply -f -

kubectl port-forward svc/josh-flask 8000
k logs <pod-name> josh-flask
kgs 
# hit server
./test.py 127.0.0.1 8000 /



# cleanup
kgd
k delete deployment josh-flask
k delete service josh-flask

minikube delete
