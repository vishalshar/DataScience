import json
import csv

csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)


outputFile = "./categoriesCount.json"
businessReviews = json.loads(open(outputFile, "r").read())

with open('mydata.csv', 'w') as mycsvfile:
    thedatawriter = csv.writer(mycsvfile, dialect='mydialect')
    for k,v in businessReviews.items():
        if v > 70000:
            thedatawriter.writerow([k, v])
            # print k,'\t',v