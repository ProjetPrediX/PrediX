from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)  # Temps d'attente entre les requêtes

    @task
    def my_task(self):
        self.client.get("http://192.168.1.106:8501")  # Remplacez l'URL par l'endpoint de votre application
