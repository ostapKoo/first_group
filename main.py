q = str("Python is a powerful interpreted programming language created by Guido van Rossum in 1991. Its simple syntax and large number of libraries make it an excellent choice for various tasks: from web development to artificial intelligence. Python is used in companies such as Google, Facebook, Instagram, where it has found application in large projects. With its help, you can develop web applications on Django, perform data analysis using the Pandas library, or create machine learning using TensorFlow. Python is a language that combines simplicity for beginners and power for programming professionals.")
words = q.split()
# заміна першого й останнього символа
word1 = words[0]
wordl = words[-1]
print("Перше слово:", word1)
print("Друге слово:", wordl)
print("Після заміни першого й останнього слова:", wordl + " " + ' '.join(words[1:-1]) + " " + word1)
#перші 100 символів
print("Перші 100 символів:", q[:100])
#весь рядок
print("Перші 100 символів:", q[:])
#заміна всіх o на а
print("Заміна всіх О на А:", q.replace("o","a"))
#рядок навпаки
print("Рядок навпаки:", q[::-1])
#вивід з 36 символу по 346
print("Вивід з 36 по 346 символ:", q[36:346])
#вивід капсом
print("Вивід капсом:", q.upper())
#Кількість літер О в тексті
print("Кількість літер О в тексті:", q.count("o"))
#Кожне слово з великої літери
print("Кожне слово з великої літери:", q.title())