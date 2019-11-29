from github import Github
from ratelimiter import RateLimiter
import time
import geopy.geocoders
from geopy.geocoders import Nominatim
import operator
import ssl

# collect the number of commits each user has made to a repo and return data as a dictionary
def get_commit_info(dictionary, repo):
    # get all the commits made to that repo
    commits = repo.get_commits()

    # for each commit, find the user
    # update the count of a user's commit number if they are already in the dictionary
    # otherwise, add the user to the dictionary (with a commit count of 1)
    for commit in commits:
        user=commit.committer
        if str(type(user)) == "<class 'NoneType'>":
            dictionary[user]=0
        elif user in d:
            dictionary[user]+=1
        else:
            dictionary[user]=1

    return dictionary

# combine two dictionaries (used to add a user's total commits across repos)
# returns a single dictionary with updated user commit #'s
def combine_dicts(d1, d2):
    for item in d2:
        if item in d1:
            d1[item]= d1[item] + d2[item]
        else:
            d1[item]=1

    return d1

def main():

    username = raw_input("Enter your Github username: ")
    password = raw_input("Enter your Github password: ")

    g = Github(username, password)

    # get the top 10 most starred python repos
    repositories = g.search_repositories(query='language: python', sort='stars', order='desc')
    top_10 = list(repositories[:10])

    # create a dictionary for the commits of each repo
    d = dict()

    # sleep in between to prevent rate limiting
    d1 = get_commit_info(d, top_10[0])
    time.sleep(1800)

    newdict2 = dict()
    d2 = get_commit_info(newdict2, top_10[1])
    time.sleep(1800)

    newdict3 = dict()
    d3 = get_commit_info(newdict3, top_10[2])
    time.sleep(1800)

    newdict4 = dict()
    d4 = get_commit_info(newdict4, top_10[3])
    time.sleep(1800)

    newdict5 = dict()
    d5 = get_commit_info(newdict5, top_10[4])
    time.sleep(1800)

    newdict6 = dict()
    d6 = get_commit_info(newdict6, top_10[5])
    time.sleep(1800)

    newdict7 = dict()
    d7 = get_commit_info(newdict7, top_10[6])
    time.sleep(1800)

    newdict8 = dict()
    d8 = get_commit_info(newdict8, top_10[7])
    time.sleep(1800)

    newdict9 = dict()
    d2 = get_commit_info(newdict9, top_10[8])
    time.sleep(1800)

    newdict10 = dict()
    d10 = get_commit_info(newdict10, top_10[9])
    time.sleep(1800)

    d12 = combine_dicts(d1, d2)
    d34 = combine_dicts(d3, d4)
    d56 = combine_dicts(d5, d6)
    d78 = combine_dicts(d7, d8)
    d910 = combine_dicts(d9, d10)
    d14 = combine_dicts(d12, d34)
    d58 = combine_dicts(d56, d78)
    most = combine_dicts(d14, d58)
    total = combine_dicts(most, d910)

    # create a list of tuples (user, commit_num) ordered by commit number in descending order
    sorted_by_commit = sorted(total.items(), key=operator.itemgetter(1), reverse=True)

    # list of tuples containing the usernames and number of commits of the top 150 contributors
    top_50_committers = sorted_by_commit[:150]


    # # testing writing to a csv file to make sure data collection is working
    # for item in top_150_committers:
    #     row = [item[0], item[1]]
    #     with open('name.csv', 'a', encoding='utf8') as csvFile:
    #         writer = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
    #         writer.writerow(row)


    # handling SSL Certificate error
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    geopy.geocoders.options.default_ssl_context = ctx

    geolocator = Nominatim()

    # write the location data to a csv
    for person in top_150_committers:
        user = person[0]
        if user.location == None:
            print('x')
        elif str(type(user.location)) == "<class 'NoneType'>":
            print('x')
        else:
            location = geolocator.geocode(user.location)
            if location==None:
                print('x')
            else:
                info = [location.longitude, location.latitude, user.location, user.name, person[1], user]
                with open('locationdata.csv', 'a', encoding='utf8') as csvFile:
                    writer = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
                    writer.writerow(info)


if __name__ == '__main__':
    main()
