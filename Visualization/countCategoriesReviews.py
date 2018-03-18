import json
import csv

outputFile = "/home/vishal/Downloads/yelp_dataset_challenge_academic_dataset/"+"businessCategories.json"
# businessReviews = json.load(open(outputFile, "r").read())
#
# print businessReviews[0]

csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)

categories = {}
data = []
count = 0
with open(outputFile) as f:
    for line in f:
        line_json = json.loads(line)
        data.append(line_json)
        # print line_json['text']
        count += 1
        print count
        for category in line_json['business'][0]['categories']:
            if category in categories:
                categories[category] += 1
            else:
                categories[category] = 1


outputFile = "./categoriesCount.json"
with open(outputFile, 'w') as fp:
    json.dump(categories, fp)

print categories


with open('mydata.csv', 'w') as mycsvfile:
    thedatawriter = csv.writer(mycsvfile, dialect='mydialect')
    for k,v in categories:
        if v > 100:
            thedatawriter.writerow([k, v])

total = 0
for count in categories.values():
    total += count
print total