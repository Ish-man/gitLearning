def toh(n, A, B, C):
	if n == 0:
		return
	
	toh(n-1, A, C, B)
	print(n, '[', A, '->', B,']')
	toh(n-1, C, B, A)
	
if __name__ == '__main__':
	n = int(input())
	tower1 = str(input())
	tower2 = str(input())
	tower3 = str(input())
	toh(n, tower1, tower2, tower3)