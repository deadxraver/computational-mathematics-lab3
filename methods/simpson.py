def calculate(function, a, b, n):
	h = (b - a) / n
	return h / 3 * (function(a) + function(b) + sum((2 + 2 * (i % 2)) * function(a + i * h) for i in range(1, n)))
