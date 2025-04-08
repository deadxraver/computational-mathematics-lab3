import math

global function, preferred_method, a, b, eps

from methods import trapeze, simpson, rectangles

functions = [
	("x^3", lambda x: x ** 3),
	("sin x", lambda x: math.sin(x)),
	("3x^3 − 4x^2 + 5x − 16", lambda x: 3 * x ** 3 - 4 * x ** 2 + 5 * x - 16)
]

methods_names = [
	"Метод левых прямоугольников",
	"Метод правых прямоугольников",
	"Метод средних прямоугольников",
	"Метод трапеций",
	"Метод Симпсона"
]

methods_list = [
	rectangles.calculate_left,
	rectangles.calculate_right,
	rectangles.calculate_middle,
	trapeze.calculate,
	simpson.calculate,
]


def invoke(method):
	k = 4 if method == simpson.calculate else 2
	n = 4
	I_prev = method(function, a, b, n)
	n *= 2
	I_current = method(function, a, b, n)

	while abs((I_current - I_prev) / (2 ** k - 1)) > eps:
		n *= 2
		I_prev = I_current
		I_current = method(function, a, b, n)

	print(f'Значение интеграла: {I_current}\nЧисло разбиения интервала: {n}')


for i in range(len(functions)):
	print(f'{i + 1}: {functions[i][0]}')

while 1:
	try:
		index = int(input("Выберите функцию: ")) - 1
		if index < 0 or index >= len(functions):
			raise ValueError
		function = functions[index][1]
		break
	except ValueError:
		print(f"Введите число от {1} до {len(functions)}")

[print(f'{i + 1}. {methods_names[i]}') for i in range(len(methods_names))]

while 1:
	try:
		input_str = input("Выберите метод или введите 'все', чтобы запустить все и сразу: ")
		if input_str.strip().lower() == 'все':
			preferred_method = None
			break
		else:
			index = int(input_str) - 1
		if index < 0 or index >= len(methods_names):
			raise ValueError
		preferred_method = methods_list[index]
		break
	except ValueError:
		print(f"Введите число от {1} до {len(methods_names)} или 'все'")

while 1:
	try:
		a = float(input("Введите a: "))
		break
	except ValueError:
		print("Введите действительное число")

while 1:
	try:
		b = float(input("Введите b: "))
		break
	except ValueError:
		print("Введите действительное число")

while 1:
	try:
		eps = float(input("Введите точность: "))
		break
	except ValueError:
		print("Введите действительное число")

if preferred_method is None:
	for i in range(len(methods_names)):
		print()
		print(methods_names[i], ':')
		invoke(methods_list[i])
else:
	print()
	invoke(preferred_method)
