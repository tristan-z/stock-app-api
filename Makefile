all:
	eval $(minikube docker-env)
	docker build --tag stock-app-api .
	docker tag stock-app-api:latest stock-app-api:v1.0.0