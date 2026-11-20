import json
import urllib.request


#open the website; read it; convert to python dictionary
handle = urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson")
data = handle.read()
eData = json.loads(data)

#go through the data and create a list of sig values
def makeSigList(earthquakeData):
    sigList = []
    earthquakes = earthquakeData.get('features')
    for i in range(len(earthquakes)):
        earthquake = earthquakes[i]
        properties = earthquake.get('properties')
        sig = properties.get('sig')
        sigList.append(sig)
    return sigList

sigList = makeSigList(eData)


#statistics
import statistics

#get the minimum sig
print("The minimum sig is", format(min(sigList), '.3f') + ".")

#get the maximum sig
print("The maximum sig is", format(max(sigList), '.3f') + ".")

#Mean
print("The mean sig is", format(statistics.mean(sigList), '.3f') + ".")

#median
print("The median sig is", format(statistics.median(sigList), '.3f') + ".")

#standard deviation
print("The standard deviation sig is", format(statistics.stdev(sigList), '.3f') + ".")

#mode
print("The mode sig is", format(statistics.mode(sigList), '.3f') + ".")
