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
		else:
			mathSign = random.randint(0, 2)

		a = math.floor((random.random()) * 10)
		b = math.floor((random.random()) * 10)

		numbers += 1

		if mathSign == 0:
			answer = input("= "+ str(numbers) + ": " + str(a) + "*" + str(b) + "= ")
			c = a * b
		elif mathSign == 1:
			answer = input("= "+ str(numbers) + ": " + str(a) + "+" + str(b) + "= ")
			c = a + b
		elif mathSign == 2:
			answer = input("= "+ str(numbers) + ": " + str(a) + "-" + str(b) + "= ")
			c = a - b

		if not answer:
			coinSkip += 1
			iterations += 1
			continue
		else:
			if math.fabs(int(answer)) == math.fabs(c) :
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
