def activity_selector(activites):

    results = [activites[0]]
    activityList = [1]

    for x in range(1, len(activites)):
        if activites[x][0] >= results[-1][1]:
            results.append(activites[x])
            activityList.append(x+1)

    return activityList


act = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
print(activity_selector(act))