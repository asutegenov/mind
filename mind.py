import math, random, time
from datetime import datetime
from logic import mathExercise

coinTrue = 0
coinFalse = 0
coinSkip = 0
iterations = 0
numbers = 0

print("==============================================")
print("================== MIND v0.1 =================")
print("==============================================")
while True:
  try:

    print("==== 1. Основное задание =====================")
    print("==== 2. Таблица умножения  ===================")
    print("==== 3. Упражнения на сложение  ==============")
    print("==== 4. Упражнения на вычитание  =============")
    print("==== 5. Упражнения на деление  ===============")
    print("==== 6. Упражнение 'Цепочка чисел' ===========")
    print("==== 7. Выход ================================")
    print("==============================================")

    num_question = int(input("==== Выберите номер задания: "))
    print("==============================================")

    if num_question == 1:
      mathExercise(iterations, coinTrue, coinFalse, coinSkip, numbers)
    elif num_question == 2:
      print("**** Задание пока не готово. \n Позанимайтесь пока по Основному заданию ****")
      print("==============================================")
      mathExercise(iterations, coinTrue, coinFalse, coinSkip, numbers)
    elif num_question == 3:
      print("**** Задание пока не готово. \n Позанимайтесь пока по Основному заданию ****")
      print("==============================================")
      mathExercise(iterations, coinTrue, coinFalse, coinSkip, numbers)
    elif num_question == 4:
      print("**** Задание пока не готово. \n Позанимайтесь пока по Основному заданию ****")
      print("==============================================")
      mathExercise(iterations, coinTrue, coinFalse, coinSkip, numbers)
    elif num_question == 5:
      print("**** Задание пока не готово. \n Позанимайтесь пока по Основному заданию ****")
      print("==============================================")
      mathExercise(iterations, coinTrue, coinFalse, coinSkip, numbers)
    elif num_question == 6:
      print("**** Задание пока не готово. \n Позанимайтесь пока по Основному заданию ****")
      print("==============================================")
      mathExercise(iterations, coinTrue, coinFalse, coinSkip, numbers)
    elif num_question == 7:
      print("================ See you later ===============")
      print("==============================================")
      break
    else:
      print("====== ВЫ ВВЕЛИ НЕВЕРНЫЙ НОМЕР ЗАДАНИЯ! ======")

    print("==============================================")
  except ValueError:
    print("==============================================")
    print("========= ВВЕДИТЕ, ПОЖАЛУЙСТА, ЦИФРЫ =========")
    print("==============================================")

