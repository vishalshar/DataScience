import json
import operator

outputFile = "/home/vishal/Downloads/yelp_dataset_challenge_academic_dataset/"+"businessCheckIn.json"

listCity = ['edinburgh', 'karlsruhe', 'montreal', 'waterloo', 'pittsburgh', 'phoenix', 'las vegas']
city = {}
categorySet = set(['Nightlife','Food','Bars','American (New)','American (Traditional)','Breakfast & Brunch','Mexican',
                   'Arts & Entertainment','Shopping','Hotels & Travel','Event Planning & Services','Pizza','Beauty & Spas',
                   'Italian','Sandwiches','Burgers','Japanese','Seafood','Chinese','Casinos','Automotive','Hotels'])
edinburghCategory={}
karlsruheCategory={}
montrealCategory={}
waterlooCategory={}
pittsburghCategory={}
phoenixCategory={}
las_VegasCategory={}

def updateCategory(categoryDict, categories):
    for category in categories:
        if category in categoryDict:
            categoryDict[category] += 1
        else:
            categoryDict[category] = 1
    return categoryDict


def sortCategory(category):
    category = dict((k,v) for k,v in category.iteritems() if k in categorySet)
    category = sorted(category.items(), key=operator.itemgetter(0))
    printCategory(category)



def printCategory(category):
    for cat in category:
        print cat[0],',', cat[1]

with open(outputFile) as f:
    for line in f:
        line_json = json.loads(line)
        data_city = line_json['city']
        data_city = data_city.lower().strip()
        data_city = data_city.encode('ascii', 'ignore')
        # print data_city
        if data_city in listCity:
            if data_city == 'edinburgh':
                edinburghCategory = updateCategory(edinburghCategory, line_json['categories'])
            if data_city == 'karlsruhe':
                karlsruheCategory = updateCategory(karlsruheCategory, line_json['categories'])
            if data_city == 'montreal':
                montrealCategory = updateCategory(montrealCategory, line_json['categories'])
            if data_city == 'waterloo':
                waterlooCategory = updateCategory(waterlooCategory, line_json['categories'])
            if data_city == 'pittsburgh':
                pittsburghCategory = updateCategory(pittsburghCategory, line_json['categories'])
            if data_city == 'phoenix':
                phoenixCategory = updateCategory(phoenixCategory, line_json['categories'])
            if data_city == 'las vegas':
                las_VegasCategory = updateCategory(las_VegasCategory, line_json['categories'])

# edinburghCategory = dict((k, v) for k, v in edinburghCategory.iteritems() if k in categorySet)
# waterlooCategory = sorted(waterlooCategory.items(), key=operator.itemgetter(1))
# print waterlooCategory

print "edinburgh"
sortCategory(edinburghCategory)

print "\n\n"
print "karlsruhe"
sortCategory(karlsruheCategory)

print "\n\n"
print "montreal"
sortCategory(montrealCategory)

print "\n\n"
print "waterloo"
sortCategory(waterlooCategory)

print "\n\n"
print "pittsburgh"
sortCategory(pittsburghCategory)

print "\n\n"
print "phoenix"
sortCategory(phoenixCategory)

print "\n\n"
print "las Vegas"
sortCategory(las_VegasCategory)