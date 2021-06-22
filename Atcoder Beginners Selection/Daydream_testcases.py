import random
import Daydream

counter = 0
for n in range(100):
    S = ''
    for i in range(5):
        r = random.choice(['dream', 'dreamer', 'erase', 'eraser'])
        S += r
    print(S)
    res = Daydream.execute(S)
    if res == 'YES':
        counter += 1
    else:
        print('NG:', S)
print(str(counter))



