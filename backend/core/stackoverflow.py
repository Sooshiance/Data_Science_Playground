import requests
from datetime import datetime
import logging

logger = logging.basicConfig()


def get_todays_questions():
    today_start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    today_end = datetime.now().replace(
        hour=23, minute=59, second=59, microsecond=999999
    )

    from_timestamp = int(today_start.timestamp())
    to_timestamp = int(today_end.timestamp())

    url = "https://api.stackexchange.com/2.3/questions"

    params = {
        "order": "desc",
        "sort": "creation",
        "fromdate": from_timestamp,
        "todate": to_timestamp,
        "site": "stackoverflow",
        "pagesize": 50,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get("items", [])
    else:
        print(f"Error: {response.status_code}")
        return []


def main():
    todays_questions = get_todays_questions()
    results = []

    if todays_questions:
        print(f"Today's Questions ({len(todays_questions)}):")
        for question in todays_questions:
            title = question["title"]
            link = question["link"]
            results = [(ti,li) for ti in title for li in link]
        return results
    else:
        print("No questions found for today.")
