# Standarisasi Load Testing
# Test akan dilakukan dengan Total User 100 + spawn rate 1
# Run time akan berjalan selama 5 menit (hanya berguna untuk user total yang kecil, jika user total besar, maka run time tidak akan dibatasi sampai user mencapai max user)
# pengetesan akan terus berlanjut dengan total user yang bertambah sampai 1000 user
from locust import HttpUser, task, between, TaskSet, SequentialTaskSet
# List Task untuk Server Load Testing
class FeaturesTaskSet(TaskSet):
    @task
    def index(self):
        self.client.get("/")

    # # task untuk mengambil data product customer dan detail product customer
    @task
    def product_customer(self):
        self.client.get("/search")
        self.client.get("/product/126")
    
# Main Class untuk Proses Load Testing Server
class ClientLoadTesting(HttpUser):
    # wait_time is used to define the time between the tasks
    wait_time = between(1, 2)
    tasks = [FeaturesTaskSet]
