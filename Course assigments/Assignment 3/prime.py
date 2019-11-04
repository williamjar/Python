def main(): 

	amount = 0
	number = 0
	while amount < 1000:
		if checkPrime(number):
			amount += 1
			print(number)
		number += 1




def checkPrime(number):

	result = True
	for i in range(2, number):
		if number % i == 0:
			
			result = False
			break

	if number <= 1:
		result = False
	return result
main()