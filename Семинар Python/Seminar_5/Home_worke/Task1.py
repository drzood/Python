# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

txt = 'Бывал я как то в Зимбабве'.split()
txt = list(filter(lambda x: 'абв' not in x, txt))
print(' '.join(txt))
