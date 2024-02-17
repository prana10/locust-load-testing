from locust import HttpUser, task, between

class ServerLoadTesting(HttpUser):
    # wait_time is used to define the time between the tasks
    wait_time = between(1, 2.5)

    # Test to check the server status
    # @task decorator is used to define the task
    @task
    def index(self):
        self.client.get("/catalogue-customer")
    
    @task
    def index(self):
        self.client.get("/featured-category")
    
    @task
    def index(self):
        self.client.get("/product-customer?search=&page=1&limit=10")