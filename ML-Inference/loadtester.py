from locust import HttpUser, TaskSet, task, between
class UserBehavior(TaskSet):
    @task(1)
    def classify_get(self):
        self.client.get("/")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 2) 