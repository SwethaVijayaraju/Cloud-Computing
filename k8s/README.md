## Deploy:
```
kubectl apply -f deploy.yaml
```
## Verify:
```
kubectl get deploy
kubectl get service
```

## Meals Recommendation API access:
```
localhost:5000/api/v1/recommend_meal
```
- The page will return a json of food recommendation, it's price and the respective pod's hostname which served the request

## Meals Recommendation Webpage access:
```
localhost:80
```
- The page will give recommendation from a default meal set
- Keep refreshing the page to get new recommendations!
- Add new meal options to the meals database using PGAdmin

## Scale Deployment:
```
kubectl edit deploy meals-api
```
- Replace spec.replicas to 4
```
spec:
  replicas: 4
```

## Verify Deployment Creation:
```
kubectl get deploy meals-api
kubectl get pods 
```

## Meals Recommendation Endpoint: 
```
localhost:5000/api/v1/recommend_meal
```
- Everytime you refresh the page, you should see the api_hostname changing.

## Teardown:
```
kubectl delete -f deploy.yaml
```

## Verify Deployment/Pod Deletion:
```
kubectl get pods 
kubectl get service
```

