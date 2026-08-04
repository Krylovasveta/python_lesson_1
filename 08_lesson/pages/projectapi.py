import requests


class ProjctApi:
    def __init__(self, url):
        self.url = url
        self.token = None

    def get_token(
        self,
        user="мойлогин",
        password="мойпароль",
        companyId="моякомпания",
    ):
        auth = {"login": user, "password": password, "companyId": companyId}

        resp = requests.post(f"{self.url}/auth/keys", json=auth)

        data = resp.json()
        self.token = data["key"]
        return self.token

    def create_project(self, title):
        my_token = self.get_token()
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + my_token,
        }
        project = {"title": title}
        resp = requests.post(f"{self.url}/projects", json=project, headers=my_headers)

        data = resp.json()
        l = [data["id"], resp.status_code]
        return l

    def update_project(self, id, new_title):
        my_token = self.get_token()
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + my_token,
        }
        project = {"title": new_title}
        resp = requests.put(
            f"{self.url}/projects/{id}", json=project, headers=my_headers
        )

        data = resp.json()
        l = [data["id"], resp.status_code]
        return l

    def get_project(self, id):
        my_token = self.get_token()
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + my_token,
        }
        resp = requests.get(f"{self.url}/projects/{id}", headers=my_headers)

        data = resp.json()
        l = [data["id"], resp.status_code]
        return l
