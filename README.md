# Github Social Graph Vizualization Project

## Github Access (see APIaccess.py)
Part 1 of this project simply involved accessing the Github API. I did this in the file APIaccess.py where I simply printed out the names of my repositories. The code was originally run with IDLE and then pushed to github through atom.

## Project Overview
The purpose of this project was to find out where in the world the most productive python developers are located. To do this, I considered the top 10 most saved python repositories and collected data on which developers were contributing to those repositories the most. I then gathered data from developers’ bios to see where they were located.

To run the data collection, the libraries PyGithub and GeoPy are required.

## The Vizualization
Originally, I was just using basic HTML and JavaScript with d3 to create my visualization. The code for this work can be found in index.html. However, I was unable to pull the data in from the csv file where it was stored without causing issues with the map projection. As a result, I created a new map using the Mapbox API which is built on top of Leaflet. The code for this can be found in working_map.html

An image of my original map can be found in the file originald3-map.17.43 PM.png and images of my final mapbox powered map can be found in the files leaflet-close-view.14.46 PM.png and leaflet-zoomed-out.17.26 PM.png.

## Potential Issues
Clearly an analysis of this sort could lead to problems. First, only developers who contributed to the 10 most starred repositories were considered. There may be python developers who are contributing much more python code to Github, but these developers were not considered here. Also, developer contributions were measured in number of commits which may not accurately depict how much work a developer is really doing. A third problem was that some developers do not put their location in their bio, and therefore were not able to be considered in this study. 

