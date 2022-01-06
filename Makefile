minikube:
		nohup minikube tunnel &

enter:
		echo -e -n "\r"

kubectl:
		nohup kubectl port-forward svc/awx-demo-service --address 0.0.0.0 30886:80 &

enter2:
		echo -e -n "\r"

        