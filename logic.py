import math, random

from datetime import datetime
    
def mathExercise(iterations, coinTrue, coinFalse, coinSkip, numbers, exercise):

	question = int(input(str("==== Cколько вы хотите выполнить заданий: ")))
	print("==============================================")
	start_time = datetime.now().replace(microsecond=0)

	while iterations < question:

		if exercise == 0:
			mathSign = 0
		elif exercise == 1:
			mathSign = 1
		elif exercise == 2:
			mathSign = 2
		elif exercise == 4:
			mathSign = 4
		else:
			mathSign = random.randint(0, 2)

		a = math.floor((random.random()) * 10)
		b = math.floor((random.random()) * 10)

		numbers += 1

		if mathSign == 0:
			answer = input("= "+ str(numbers) + ": " + str(a) + "+" + str(b) + "= ")
			c = a + b
		elif mathSign == 1:
			answer = input("= "+ str(numbers) + ": " + str(a) + "-" + str(b) + "= ")
			c = a - b
		elif mathSign == 2:
			answer = input("= "+ str(numbers) + ": " + str(a) + "*" + str(b) + "= ")
			c = a * b
		# elif mathSign == 3:
		# 	break
		elif mathSign == 4:
			chooseBetween = random.randint ( 1,2  )
			a = random.randint ( 1, 10 )
			b = random.randint ( 1, 10 )
			c = random.randint ( 1, 10 )
			d = random.randint ( 1, 10 )

			if chooseBetween == 1 :
				z1 = random.randint( 1,4 )
				if z1 == 1 :
					answer = input("= "+ str(numbers) + ": " + str(a) + "+" + str(b) +  "-" + str(c) + "= ")
					e = a + b - c
				elif z1 == 2 :
					answer = input("= "+ str(numbers) + ": " + str(a) + "-" + str(b) +  "+" + str(c) + "= ")
					e = a - b + c
				elif z1 == 3 :
					answer = input("= "+ str(numbers) + ": " + str(a) + "-" + str(b) +  "-" + str(c) + "= ")
					e = a - b - c
				elif z1 == 4 :
					answer = input("= "+ str(numbers) + ": " + str(a) + "+" + str(b) +  "+" + str(c) + "= ")
					e = a + b + c
			else :
				z2 = random.randint(1,6)
				if z2 == 1 :
					answer = input("= "+ str(numbers) + ": " + str(a) + "+" + str(b) +  "-" + str(c) + "+" + str(d) + "= ")
					e = a + b - c + d
				elif z2 == 2 :
					answer = input("= "+ str(numbers) + ": " + str(a) + "-" + str(b) +  "+" + str(c) + "-" + str(d) + "= ")
					e = a - b + c - d
				elif z2 == 3 :
					answer = input("= "+ str(numbers) + ": " + str(a) + "+" + str(b) +  "+" + str(c) + "-" + str(d) + "= ")
					e = a + b + c - d
				elif z2 == 4 :
					answer = input("= "+ str(numbers) + ": " + str(a) + "-" + str(b) +  "-" + str(c) + "+" + str(d) + "= ")
					e = a - b - c + d
				elif z2 == 5 :
					answer = input("= "+ str(numbers) + ": " + str(a) + "-" + str(b) +  "-" + str(c) + "-" + str(d) + "= ")
					e = a - b - c - d
				elif z2 == 6 :
					answer = input("= "+ str(numbers) + ": " + str(a) + "+" + str(b) +  "+" + str(c) + "+" + str(d) + "= ")
					e = a + b + c + d

		if not answer:
			coinSkip += 1
			iterations += 1
			continue
		else:
			if math.fabs(int(answer)) == math.fabs(c) or math.fabs(int(answer)) == math.fabs(e):
				coinTrue += 1
			else:
				coinFalse += 1
				print("ОШИБКА")

		iterations += 1

	totalTime = ((datetime.now().replace(microsecond=0) - start_time))
	
	print("==============================================")
	print("================== РЕЗУЛЬТАТ =================")
	print("======== Количество верных упражнений: " + str(coinTrue))
	print("===== Количество НЕ верных упражнений: " + str(coinFalse))
	print("=== Количество пропущенных упражнений: " + str(coinSkip))
	print("====== Время на выполнение упражнений: " + str(totalTime))
