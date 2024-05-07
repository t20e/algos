# 0(nlogn) time | 0(1) space
def minimumWaitingTime(queries):
    queries.sort()
    waitingTime = 0
    for idx, duration in enumerate(queries):
        queriesLeft = len(queries) - (idx + 1)
        # givers u the one index to the left of the current query index
        waitingTime += duration * queriesLeft
        print('duration = ', duration, 'queries to the left =',
              queriesLeft, 'waiting time=', queriesLeft*duration)
        # then we multiply all the queries to the left by
    return waitingTime


queries = [3, 2, 1, 2, 6]
# 0 => 3 => 5 => 6 => 8
# 17
print(minimumWaitingTime(queries))
