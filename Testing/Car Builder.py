chas = open('chassis.txt','r').read()
chaslist = chas.split('\n')
eng = open('engines.txt','r').read()
englist = eng.split('\n')

print('Chassis:')
[print(str(chaslist.index(x)+1)+'>> '+x) for x in chaslist]
print('\nEngines:')
[print(str(englist.index(y)+1)+'>> '+y) for y in englist]


class car:
	def __init__(self, chassis, engine):
		self.chassis  = chaslist[int(chassis)-1]
		self.engine = englist[int(engine)-1]