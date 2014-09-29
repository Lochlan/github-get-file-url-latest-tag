# get_file_url_github_latest_tag.py

This script outputs URLs of files from github repositories using the latest [tag](http://git-scm.com/book/en/Git-Basics-Tagging), which is often a way to find the latest stable versions of projects.

Usage:
```Shell
$ python3 get_file_url_github_latest_tag.py [github-user] [github-repo] [file-path]
```

For example, to get the latest tagged version of [Backbone.js](http://backbonejs.org/):
```Shell
$ python3 get_file_url_github_latest_tag.py jashkenas backbone backbone.js
```
