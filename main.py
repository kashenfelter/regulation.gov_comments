from settings import SECRET_KEY


import json
import requests


def getLastComments(SECRET_KEY):
    # Call the URL and get the number of comments based on the following
    # criteria: results per page = 100, sort order = DESCending,
    # sort by = Posted Date and keyword = florida
    commentsURL = "https://api.data.gov/regulations/v3/documents.json?api_key="+SECRET_KEY+"&rpp=100&so=DESC&sb=postedDate&s=florida&sp=O"
    response = requests.get(commentsURL)
    response.raise_for_status()
    commentData = json.loads(response.text)
    print(commentData)


getLastComments(SECRET_KEY)
