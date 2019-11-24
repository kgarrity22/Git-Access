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
    return repositories[:10]

# print(collect_python_repos())

import geopy.geocoders
from geopy.geocoders import Nominatim

####geopy.geocoders.options.defult_user_agent = 'my_app/1'
##geopy.geocoders.options.default_timeout = 7
##geolocator = Nominatim(user_agent="https://github.com/kgarrity22")
##location = geolocator.geocode("Boston, MA")
##print((location.latitude, location.longitude))
import ssl
import geopy.geocoders
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
geopy.geocoders.options.default_ssl_context = ctx


geolocator = Nominatim()
location = geolocator.geocode("175 5th Avenue NYC")
print(location.address)

# code to get a user's location 
commit = commits[0]

user = commit.committer
print(user.location)
