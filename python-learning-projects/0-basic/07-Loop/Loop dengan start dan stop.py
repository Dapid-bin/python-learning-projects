#Loop dengan start dan stop basic
for basic in range(1, 6):# (1 start, stop 6)
	print(basic)#variabel output
'''
1 start = (0 1) -> 2 in machine
6 start = (0 1 2 3 4 5) -> 5 in machine
'''


Start = int(input("Start: "))
Stop = int(input("Stop: "))
start = 1
stop = 6

for b in range(Start, Stop):
	print(f"Angka: {b}")# Output f'-string {}'


for a in range(5, 9):# (5 start stop 9)
	print("Ke-{}".format(a))# Output .format()

'''
5 start = (0 1 2 3 4) -> 4 in machine
9 stop = (0 1 2 3 4 5 6 7 8) -> in machine
'''