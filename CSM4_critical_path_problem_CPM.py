import numpy as np

class Activity:
    def __init__(self, idx, name, duration) -> None:
        self.idx = idx
        self.name = name
        self.duration = duration
        self.predecessor = []
        self.successor = []
        self.early_start = 0
        self.early_finish = 0
        self.late_start = 0
        self.late_finish = 0

def main():
    file_path = './input2.txt'
    activities = {}
    index = []

    for line in open(file_path):
        words = line.strip('\n').split(',')
        # print(words)
        idx = int(words[0])
        name = words[1]
        duration = int(words[2])
        predecessors = words[3]
        index.append(idx)
        activities[idx] = Activity(idx, name, duration)
        if (predecessors != ''):
            predecessors = predecessors.split(';')
            for item in predecessors:
                activities[idx].predecessor.append(int(item))
                activities[int(item)].successor.append(idx)
    
    # for idx in index:
    #     print(activities[idx])
    
    maxEF = 0

    for idx in index:
        if (len(activities[idx].predecessor) == 0):
            activities[idx].early_finish = activities[idx].duration
        else:
            maxTime = 0
            for item in activities[idx].predecessor:
                maxTime = max(maxTime, activities[item].early_finish)
            
            activities[idx].early_start = maxTime
            activities[idx].early_finish = maxTime + activities[idx].duration

        maxEF = max(maxEF, activities[idx].early_finish)

    for i in range(len(index)):
        idx = index[-1-i]
        if (len(activities[idx].successor) == 0):
            activities[idx].late_finish = maxEF
            activities[idx].late_start = maxEF - activities[idx].duration
        else:
            minTime = 9999999
            for item in activities[idx].successor:
                minTime = min(minTime, activities[item].late_start)

            activities[idx].late_finish = minTime
            activities[idx].late_start = minTime - activities[idx].duration

    # for idx in index:
    #     print(activities[idx].idx, ' ', activities[idx].name, ' ', activities[idx].duration, ' ', activities[idx].predecessor, ' ', activities[idx].successor, ' ', activities[idx].early_start, ' ', activities[idx].early_finish, ' ', activities[idx].late_start, ' ', activities[idx].late_finish)

    result = []
    for idx in index:
        if (activities[idx].early_finish == activities[idx].late_finish):
            result.append(activities[idx].name)

    # print(result)
    for i in range(len(result)-1):
        print(result[i], end=' -> ')
    print(result[len(result)-1])

if __name__ == '__main__':
    main()