# Вычислить число Пи c заданной точностью d
# 3.141592653589793
# Пример:
#     - при d = 0.0001,  π = 3.1415    10^-1 ≤ d ≤10^-10


pi = 3.141592653589793   # или импортиуем метод пи
d = float(input('d = ')) # задаем точность
pi, d = str(pi), str(d)  # конвертируем в строку
print(float(pi[:len(d)]))# выводим флоат с нужной точностью