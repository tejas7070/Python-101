#Insert and Merge the intervals such that the intervals are non-overlapping


def insert(intervals,newintervals):
    res = []
    n = len(intervals)
    i = 0

    while (i<n and intervals[i][1] < newintervals[0]):
        res.append(intervals[i])    
        i +=1

    while(i<n and intervals[i][0]<= newintervals[1]):
        newintervals[0] = min(newintervals[0],intervals[i][0])    
        newintervals[1] = max(newintervals[1],intervals[i][1])
        i +=1   
    
    res.append(newintervals)    

    while(i<n):
        res.append(intervals[i])
        i += 1
    return res

intervals = [[1, 3], [4, 5], [6, 7], [8, 10]]
newintervals = [5,6]

print(insert(intervals,newintervals))
    