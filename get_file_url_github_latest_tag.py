import sys
import json
from urllib.error import HTTPError
from urllib.request import urlopen

def get_sha_latest_tag(user, repo):
    response = urlopen("https://api.github.com/repos/" + user + "/" + repo + "/tags")
    json_string = response.read().decode('utf-8')
    json_obj = json.loads(json_string)

    try:
        sha_latest_tag = json_obj[0]["commit"]["sha"]
    except IndexError:
        sys.exit("No tags for " + user + "/" + repo)

    return sha_latest_tag

def get_file_url_latest_tag(user, repo, filepath):
    sha_latest_tag = get_sha_latest_tag(user, repo)
    file_url = "https://raw.githubusercontent.com/" + user + "/" + repo + "/" + sha_latest_tag + "/" + filepath

    # check if file is available
    try:
        urlopen(file_url)
    except HTTPError as e:
        sys.exit(file_url + " " + str(e.code) + " " + e.reason)

    return file_url

def main():
    if len(sys.argv) < 4:
        sys.exit("Not enough arguments")

    user = sys.argv[1]
    repo = sys.argv[2]
    filepath = sys.argv[3]

    file_url_latest_tag = get_file_url_latest_tag(user, repo, filepath)
    print(file_url_latest_tag)

if __name__ == "__main__":
    main()
