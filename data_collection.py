from github import Github

g = Github("3e0d6fcd7bfcd3420bc62d9b5f717e99ddd820e8")

repositories = g.search_repositories(query='language: python')

for repo in repositories:
    print(repo)
