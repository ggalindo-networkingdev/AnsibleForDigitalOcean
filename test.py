import os
import time

os.system("mkdir testing")
time.sleep(1)
os.system("nohup minikube tunnel &")
print("--------------")
print("Make Minikube end")
time.sleep(25)
os.system("nohup kubectl port-forward svc/awx-demo-service --address 0.0.0.0 30886:80 &")
print("--------------")
print("Make kubectl end")
