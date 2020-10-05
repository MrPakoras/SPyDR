# Super Python Drag Racer
# Lets you custom create a car
# Selects random car and random specs from file for opponent
# Generates random times based on specs
# Earn money to buy more components


import time, random

def prog():

    def opp():
        co = random.choice(cl)
        eo = random.choice(el)
        nit = random.choice(['y','n'])
        global avgo
        avgo = round(random.uniform(0,0.8),3)

        if nit == 'y':
            fail = random.randint(1,3)
            if fail == 1:
                avgo += random.uniform(0.2,0.5)
                avgo = round(avgo,3)

        print('\nYour opponent has a:\n'+co+'\n'+'with a '+eo)

    print('Welcome to the SPyDR drag strip. Here you will build a car ready to be raced... choose your parts wisely...\n\n')

    print('________________________________________________________________________________\n')

    c = open('Chassis.txt','r').read()
    cl = c.split('\n')
    num = 1
    for x in cl:
        print(str(num)+'> '+x)
        num += 1

    cs = int(input('\nPlease choose a chassis number: '))
    print('You have selected the '+cl[(cs-1)]+' chassis')

    print('________________________________________________________________________________\n')

    e = open('Engines.txt','r').read()
    el = e.split('\n')
    num = 1
    for x in el:
        print(str(num)+'> '+x)
        num +=1

    es = int(input('\nPlease choose an engine number: '))
    print('You have selected the '+el[(es-1)]+' engine\n')

    print('________________________________________________________________________________\n')

    nit = input('Would you like Nitrous Oxide to be fitted to your vehicle (Warning, using Nitrous may cause engine failiures) "y"es or "n"o:   ')
    if nit == 'y':
        print('Nitrous Oxide Systems installed in your '+cl[cs-1])
        

    def shift():
        global times
        global avg
        times = 0

        def s():
            s = input('Shift Now!   ')

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
        elif 0.3<avg<0.4:
            print('good')
        elif 0.4<avg<0.7:
            print('poor')
        elif avg>0.7:
            print('not worth waiting for')

        if nit == 'y':
            fail = random.randint(1,3)
            if fail == 1:
                times += random.uniform(0.2,0.5)
                avg = round(times/5,3)
                print('Oh dear. You have blown a head gasket. Therefore your actual time was: '+str(avg))
                    


    print('________________________________________________________________________________\n')

    print('Okay, your car has been built. Here are your specs:')
    print(cl[(cs-1)]+' with a '+el[(es-1)],end='')
    if nit == 'y':
        print(' and with nitrous installed.')
    print('\n________________________________________________________________________________\n')
    print('Get ready to drag race. Wait for the "Shift Now!" signal and press the "Enter" key to shift up a gear.\n')
    print('Finding opponent, please wait...')
    time.sleep(2)

    print('________________________________________________________________________________\n')

    print('Opponent found. Commencing in 5 seconds...')
    opp()
    time.sleep(5)
    print('Drag race starts NOW!\n\n')

    shift()

    print('________________________________________________________________________________\n')


    print('Your opponent clocked in at '+str(avgo)+' seconds.')

    print('________________________________________________________________________________\n')

    if avg < avgo:
        cash = random.randint(100,1000)
        print('You won by '+str(round(avgo-avg, 3))+' seconds')
        print('Congratulations on the win. Here is £'+str(cash)+' as a reward.')
    else:
        print('You lost by '+str(round(avg-avgo, 3))+' seconds unfortunately.')
        print('Better luck next time.')


    p = input('Race again? y or n:   ')
    if p == 'y':
        print('\n\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\n')
        prog()
    else:
        quit()



prog()





























