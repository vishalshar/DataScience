from __future__ import division
import json
import operator

outputFile = "/home/vishal/Downloads/yelp_dataset_challenge_academic_dataset/"+"yelp_academic_dataset_user.json"
# outputFile = "/home/vishal/Downloads/yelp_dataset_challenge_academic_dataset/sampleData/"+"sampleUser.json"


topProfile = {}
with open(outputFile) as f:
    for line in f:
        # print line
        j_content = json.loads(line)
        eliteCount = len(j_content['elite'])
        name = j_content['name']
        # print name, useful, fans, complimentCount, friendsCount, reviewCount, score
        topProfile[name] = eliteCount

topProfile = sorted(topProfile.items(), key=operator.itemgetter(1),reverse=True)
print topProfile[:500]