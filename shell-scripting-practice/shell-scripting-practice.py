import os
import random
problems = []
for path, d, *files, _ in os.fwalk():
    for file in files[0]:
        if file[-3:] == ".sh":
            problems.append( os.path.join(path, file))

random.shuffle(problems)
print('\n'.join(problems[0:10]))