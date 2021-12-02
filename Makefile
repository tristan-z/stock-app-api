all:
	docker build --tag stock-app-api .
	docker tag stock-app-api:latest clakeyman/stock-app-api:v1.0.0
	docker push clakeyman/stock-app-api:v1.0.0