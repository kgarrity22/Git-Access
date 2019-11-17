from github import Github

from ratelimiter import RateLimiter
import time

def limited(until):
    duration = int(round(until - time.time()))
    print("Rate limited, sleeping for {:d} seconds".format(duration))

rate_limiter = RateLimiter(max_calls=2, period=3, callback=limited)

g = Github("3e0d6fcd7bfcd3420bc62d9b5f717e99ddd820e8")

def collect_python_repos():
    repositories = list(g.search_repositories(query='language: python', sort='stars'))
    return repositories[0]


print(collect_python_repos())
