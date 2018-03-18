from __future__ import division
import json
import operator
from compiler.ast import flatten

outputFile = "/home/vishal/Downloads/yelp_dataset_challenge_academic_dataset/"+"yelp_academic_dataset_user.json"
# outputFile = "/home/vishal/Downloads/yelp_dataset_challenge_academic_dataset/sampleData/"+"sampleUser.json"


usefulMax = 0
fansMax = 0
complimentMax = 0
numFriendsMax = 0
reviewCountMax = 0


def getCompliemntCount(complimentCount):
    sum = 0
    for k, v in complimentCount.iteritems():
        sum += int(v)
    return sum

with open(outputFile) as f:
    for line in f:
        j_content = json.loads(line)
        # Useful
        useful = int(j_content['votes']['useful'])
        if usefulMax < useful:
            usefulMax = useful
        # Fans
        fans = int(j_content['fans'])
        if fansMax < fans:
            fansMax = fans
        # Compliment Count
        complimentCount = getCompliemntCount(j_content['compliments'])
        if complimentMax < complimentCount:
            complimentMax = complimentCount
        # Num of friends
        friendsCount = len(j_content['friends'])
        if numFriendsMax < friendsCount:
            numFriendsMax = friendsCount
        # Review Count
        reviewCount = j_content['review_count']
        if reviewCountMax < reviewCount:
            reviewCountMax = reviewCount
f.close()
print usefulMax, fansMax, complimentMax, numFriendsMax, reviewCountMax
# 75529 3549 228054 3795 10897

topProfile = {}
eliteScore = {}
with open(outputFile) as f:
    for line in f:
        # print line
        j_content = json.loads(line)
        useful = int(j_content['votes']['useful'])
        fans = int(j_content['fans'])
        complimentCount = getCompliemntCount(j_content['compliments'])
        friendsCount = len(j_content['compliments'])
        reviewCount = j_content['review_count']
        name = j_content['name']
        score = float(fans/fansMax) + float(complimentCount/complimentMax) + float(friendsCount/numFriendsMax) + float(reviewCount/reviewCountMax)
        # print name, useful, fans, complimentCount, friendsCount, reviewCount, score
        topProfile[name] = score
        eliteScore[name] = len(j_content['elite'])

topProfile = sorted(topProfile.items(), key=operator.itemgetter(1),reverse=True)
topProfile = topProfile[:5000]

eliteScore = sorted(eliteScore.items(), key=operator.itemgetter(1),reverse=True)
eliteScore = eliteScore[:5000]


gt = set()
det = set()

for row in topProfile:
    det.add(row[0])

for row in eliteScore:
    gt.add(row[0])
#
# groundtruth = eliteScore[:500]
# detected = topProfile[:500]
#
#
# dec_keys = detected.keys()
# gt_keys =  eliteScore.keys()
#
# dec_keys = flatten(dec_keys)
# gt_keys = flatten(gt_keys)
#
print det
print gt
print len(list(det.intersection(gt)))

# 10 : 1
# 100 : 25
# 500 : 240
# 1000 : 585
# 5000 : 2469