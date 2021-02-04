import sys
import json
import requests



if __name__ == "__main__":
    """ Input username, Output time of last event.

    Use like:  python githubber.py mattcasari
    """
    username = sys.argv[1]
    response = requests.get("https://api.github.com/users/{}/events".format(username))
    events = json.loads(response.content)

    print(events[0]['created_at'])


