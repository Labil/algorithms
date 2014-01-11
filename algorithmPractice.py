#Factorial exercise iterative & recursive
#To get the factorial of a number, you multiply every number from 1 and 
#up to that number with the number. Ex: f(5) = 1*5 + 2*5 + 3*5 + 4*5 + 5*5
def factorial(number):
	if number <= 1:
		return 1
	else:
		return number * factorial(number -1)

	#product = 1
	#for i in range(number):
	#	product = product * (i + 1)
	#return product

inputNum = input("Input a non-negative integer: ")
factorialResult = factorial(inputNum)
print(factorialResult)

#The Fibonacci sequence increases by adding together the last two numbers in 
#succession. Ex: fib(5): 0, (0+1=) 1, (1+1=) 2, (1+2 =) 3, (2+3=) 5   ---> fib(5) = 5
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 etc 

#Iterative
def fibonacci(numbr):
	if numbr == 0:
		return 0
	else:
		inc = 1
		cur = 0
		last = 0
		for i in range(numbr):
			cur = last + inc
			inc = last
			last = cur
			print(cur)
		return cur

fibInput = input("Input a non-negative integer: ")
fibResult = fibonnaci(fibInput)
print(fibResult)

#Better version
def fib(n):
	sequence = [0, 1] #Start of every fibonacci
	i = 2
	while i <= n:
		sequence.append(sequence[i-2] + sequence[i-1])
		i = i + 1

	return sequence[n]

fibInput = 12
fibResult = fib(fibInput)
print(fibResult)

#recursive try
def recFib(n, seq):
	if(len(seq) > n):
		return seq[n]
	else:
		seq.append(seq[len(seq) - 2] + seq[len(seq) - 1])
		return recFib(n, seq) #Remember to return the recursion, and not just call it
							  #if not the calling step won't have access to the previous results

fibResult = recFib(4, [0,1])
print(fibResult)
 
#recursive Better
#But this is not very effective, even tho it looks sweet. It has to make a lot of recursive calls to get the result
def recursiveFib(n):
	if n == 0 or n == 1:
		return n
	else:
		return recursiveFib(n-1) + recursiveFib(n-2)

fibResult = recursiveFib(10)
print(fibResult)



