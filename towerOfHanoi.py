#A python program which gives steps to move 3 discs from one tower to another
def toh(n, A, B, C):
	if n == 0:
		return
	
	toh(n-1, A, C, B)
	print(n, '[', A, '->', B,']')
	toh(n-1, C, B, A)
	
if __name__ == '__main__':
	n = int(input())
	t1 = str(input())
	t2 = str(input())
	t3 = str(input())
	toh(n, t1, t2, t3)
