import csv

file = '/home/vishal/Desktop/usersData.csv'
fileW = './usersDataNAN.csv'


usefulMax = 75529
fansMax = 3549
complimentMax = 228054
numFriendsMax = 3795
reviewCountMax = 10897


def convertList(list):
    newList = []
    rowNew = []
    for item in list[0].split(','):
        if item:
            newList.append(item)
        else:
            newList.append('0')
    # print newList
    if newList[-1] != 'numberofElite':
        if int(newList[-1]) > 0:
            newList[-1] = 'true'
            comp = newList[5:15]
            sum = 0
            for compliment in comp:
                sum += int(compliment)
            rowNew.append(newList[1]) # useful
            rowNew.append(newList[4]) # fans
            rowNew.append(newList[3]) # review count
            rowNew.append(sum) # compliment
            rowNew.append(newList[16]) # num of friends
            rowNew.append(newList[-1]) # class
            # useful = float(float(newList[1]) / usefulMax)
            # fans = float(float(newList[4]) / fansMax)
            # numFriends = float(float(newList[16]) / numFriendsMax)
            # review = float(float(newList[3]) / reviewCountMax)
            # # print useful, fans, numFriends, review
            # rowNew.append(str(useful))
            # rowNew.append(str(fans))
            # rowNew.append(str(numFriends))
            # rowNew.append(str(review))
            # rowNew.append(str(newList[-1]))
        else:
            newList[-1] = 'false'
            comp = newList[5:15]
            sum = 0
            for compliment in comp:
                sum += int(compliment)
            rowNew.append(newList[1])  # useful
            rowNew.append(newList[4])  # fans
            rowNew.append(newList[3])  # review count
            rowNew.append(sum)  # compliment
            rowNew.append(newList[16])  # num of friends
            rowNew.append(newList[-1])  # class
            # useful = float(float(newList[1]) / usefulMax)
            # fans = float(float(newList[4]) / fansMax)
            # numFriends = float(float(newList[16]) / numFriendsMax)
            # review = float(float(newList[3]) / reviewCountMax)
            # # print useful, fans, numFriends, review
            # rowNew.append(str(useful))
            # rowNew.append(str(fans))
            # rowNew.append(str(numFriends))
            # rowNew.append(str(review))
            # rowNew.append(str(newList[-1]))
    # print rowNew
    return rowNew


with open(fileW, 'w') as f:
    writer = csv.writer(f)
    with open(file, 'rb') as csvfile:
        userData = csv.reader(csvfile, delimiter=' ',)
        for row in userData:
            newRow = convertList(row)
            print newRow
            writer.writerow(newRow)





