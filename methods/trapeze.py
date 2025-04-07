def calculate(function, a, b, n):
	h = (b - a) / n
	return h / 2 * (function(a) + function(b) + 2 * sum(function(a + i * h) for i in range(1, n)))
