from github import Github
from ratelimiter import RateLimiter
import time
import geopy.geocoders
from geopy.geocoders import Nominatim
import operator


# def limited(until):
#     duration = int(round(until - time.time()))
#     print("Rate limited, sleeping for {:d} seconds".format(duration))
#
# rate_limiter = RateLimiter(max_calls=2, period=3, callback=limited)

g = Github("3e0d6fcd7bfcd3420bc62d9b5f717e99ddd820e8")

# create a dictionary to collect the users and count their number of commits
d = dict()

def collect_python_repos():

    # collect all the python repos in order of highest number of stars
    repositories = g.search_repositories(query='language: python', sort='stars', order='desc')

    # looking at the 10 most starred python repositories
    for repo in repositories[:10]:
        # sleep for 15 minutes before each iteration to avoid RateLimit error
        time.sleep(900)
        # get all the commits made to that repo
        commits = repo.get_commits()
        # for each commit, find the user
        # update the count of a user's commit number if they are already in the dictionary
        # otherwise, add the user to the dictionary (with a commit count of 1)
        for commit in commits:
            user=commit.committer
            if user in d:
                d[user]+=1
            else:
                d[user]=1

    # create a list of tuples (user, commit_num) that ordered by commit number in descending order
    sorted_by_commit = sorted(d.items(), key=operator.itemgetter(1), reverse=True)

    # list of tuples containing the usernames and number of commits of the top 150 contributors











####geopy.geocoders.options.defult_user_agent = 'my_app/1'
##geopy.geocoders.options.default_timeout = 7
##geolocator = Nominatim(user_agent="https://github.com/kgarrity22")
##location = geolocator.geocode("Boston, MA")
##print((location.latitude, location.longitude))
# import ssl
# import geopy.geocoders
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# geopy.geocoders.options.default_ssl_context = ctx


geolocator = Nominatim()
location = geolocator.geocode("175 5th Avenue NYC")
print(location.address)

# code to get a user's location
commit = commits[0]

user = commit.committer
print(user.location)

# convert a python dictionary into a json
import json
d = dict()
j = json.dumps(d)
