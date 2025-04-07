def calculate_left(function, a, b, n):
	h = (b - a) / n
	return h * sum(function(a + i * h) for i in range(n))


def calculate_right(function, a, b, n):
	h = (b - a) / n
	return h * sum(function(a + i * h) for i in range(1, n + 1))


def calculate_middle(function, a, b, n):
	h = (b - a) / n
	return h * sum(function(a + i * h + h / 2) for i in range(n))
