import time, random

def shift():
    times = 0

    def s():
        s = input('Shift now!   ')

    for loop in range(5):
        time.sleep(random.randint(1,5))
        t1 = time.perf_counter()
        s()
        t = round(time.perf_counter()-t1,3)
        times += t
        print('Gear Shift took '+str(t)+' seconds\n')

    avg = round(times/5,3)
    print('\n\nYour Average shift time was: '+str(avg))
    print('Your shifting speed was ',end='')
    if 0<avg<0.2:
        print('awesome')
    elif 0.2<avg<0.4:
        print('good')
    elif 0.4<avg<0.7:
        print('poor')
    elif avg>0.7:
        print('not worth waiting for')


shift()
