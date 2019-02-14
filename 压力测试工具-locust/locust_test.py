import subprocess

from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):

    @task(1)
    def baidu(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000


if __name__ == '__main__':
    subprocess.Popen('locust -f ./locust_test.py --host=http://127.0.0.1:5000', shell=True)