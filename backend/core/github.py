import requests
from django.conf import settings


class GitHubAPI:
    BASE_URL = "https://api.github.com"

    def __init__(self):
        pass

    def search_repositories(self, query, token, sort="stars", order="desc"):
        url = f"{self.BASE_URL}/search/repositories"
        params = {"q": query, "sort": sort, "order": order}

        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None


if __name__ == "__main__":
    token = settings.GITHUB_TOKEN
    github_api = GitHubAPI()

    search_query = "online marketplace"

    repositories = github_api.search_repositories(search_query, token)

    if repositories:
        for repo in repositories.get("items", []):
            print(
                f"Name: {repo['name']}, Stars: {repo['stargazers_count']}, URL: {repo['html_url']}"
            )
