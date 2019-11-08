from github import Github

g = Github("3e0d6fcd7bfcd3420bc62d9b5f717e99ddd820e8")

for repo in g.get_user().get_repos():
  print(repo.name)
  
