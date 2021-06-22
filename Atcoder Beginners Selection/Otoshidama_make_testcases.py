import random
import Otoshidama

def make_testcases(num):
    with open('Otoshidama_testcases', 'w') as f:
        for i in range(num):
            N = random.randint(1, 2000)
            Y = random.randint(100,200000)*1000
            f.write('{0} {1}\n'.format(N, Y))
            try:
                Otoshidama.execute(N, Y)
            except:
                print('Exception')
                print(N, Y)

make_testcases(100)



