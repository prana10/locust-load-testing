# Standarisasi Load Testing
# Test akan dilakukan dengan Total User 100 + spawn rate 1
# Run time akan berjalan selama 5 menit (hanya berguna untuk user total yang kecil, jika user total besar, maka run time tidak akan dibatasi sampai user mencapai max user)
# pengetesan akan terus berlanjut dengan total user yang bertambah sampai 1000 user / sampai server down

from locust import HttpUser, task, between, TaskSet, SequentialTaskSet
from dotenv import load_dotenv
from pathlib import Path
import os

# Confuguration for .env file
dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

USERNAME = os.getenv("username")
PASSWORD = os.getenv("password")
# token = os.getenv("access_token")
token = os.getenv("sampletoken")

# List Task untuk Server Load Testing
class AuthAndUserTaskSets(TaskSet):
    # task untuk fetch me (mengambil data user akun melalui token)
    @task
    def fetch_me(self):
        headers = {"Authorization": f"Bearer {token}"}
        self.client.get("/auth/me", headers=headers)
    
    # task untuk mengambil data user address
    @task
    def users_address(self):
        headers = {"Authorization": f"Bearer {token}"}
        self.client.get("/user/address", headers=headers)

    # task untuk mengambil data user merchant
    @task
    def users_merchant(self):
        headers = {"Authorization": f"Bearer {token}"}
        self.client.get("/merchant/user", headers=headers)

class ProductAndCatalogueTaskSets(TaskSet):
    # task untuk mengambil data product dan detail product
    @task
    def product(self):
        headers = {"Authorization": f"Bearer {token}"}
        self.client.get("/product", headers=headers)
        # hit detail product by id
        # id = 126
        self.client.get("/product/126", headers=headers)

    # task untuk mengambil data product customer dan detail product customer
    @task
    def product_customer(self):
        self.client.get("/product-customer")
        # hit detail product customer by id
        # id = 126
        self.client.get("/product-customer/126")
    
    # task untuk mengambil data featured category
    @task
    def featured_category(self):
        self.client.get("/featured-category")
    
    # task untuk mengambil data catalogue
    @task
    def catalogue_customer(self):
        self.client.get("/catalogue-customer")

    # task untuk mengambil data catalogue membership
    @task
    def membership_catalogue(self):
        headers = {"Authorization": f"Bearer {token}"}
        self.client.get("/membership-catalogue", headers=headers)


# Main Class untuk Proses Load Testing Server
class ServerLoadTesting(HttpUser):
    # wait_time is used to define the time between the tasks
    wait_time = between(1, 2)
    tasks = [AuthAndUserTaskSets, ProductAndCatalogueTaskSets]
