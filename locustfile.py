from locust import HttpUser, task, between, events
import logging

class CounterUser(HttpUser):
    wait_time = between(0.5, 2)
    
    def on_start(self):
        logging.info("Starting new user")
    
    @task(3)
    def get_counter(self):
        with self.client.get("/api/counter", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Got status code {response.status_code}")
    
    @task(2)
    def increment_counter(self):
        with self.client.post("/api/counter/increment", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Got status code {response.status_code}")
    
    @task(1)
    def decrement_counter(self):
        with self.client.post("/api/counter/decrement", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Got status code {response.status_code}")
    
    @task(1)
    def reset_counter(self):
        with self.client.post("/api/counter/reset", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Got status code {response.status_code}")




@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    logging.info("Load test starting...")


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    logging.info("Load test completed")
    
    stats = environment.stats
    logging.info(f"Total requests: {stats.total.num_requests}")
    logging.info(f"Total failures: {stats.total.num_failures}")
    logging.info(f"Average response time: {stats.total.avg_response_time:.2f}ms")
    logging.info(f"RPS: {stats.total.total_rps:.2f}")
