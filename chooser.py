import random

topics = []
problems = []


with open("problems.txt") as problemFile:
    for line in problemFile:
        topics.append(line.split(':')[0])
        problems.append(line.split(':')[1].split(','))

    problems[len(problems)-1][len(problems[len(problems)-1])-1] = problems[len(problems)-1][len(problems[len(problems)-1])-1][:-1]


topicChoice = random.choice(topics)
topicNum = topics.index(topicChoice)

problemChoice = random.choice(problems[topicNum])
print(topicChoice)
print(problemChoice[1:])


