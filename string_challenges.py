# Вывести последнюю букву в слове
word = "Архангельск"
print(word[-1])


# Вывести количество букв "а" в слове
word = "Архангельск"
print(len(word))


# Вывести количество гласных букв в слове
word = "Архангельск"
vowels = "аеёиоуэюя"
print(len([letter for letter in word.lower() if letter in vowels]))


# Вывести количество слов в предложении
sentence = "Мы приехали в гости"
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = "Мы приехали в гости"
print("\n".join(word[0] for word in sentence.split()))


# Вывести усреднённую длину слова в предложении
sentence = "Мы приехали в гости"
words = sentence.split()
print(sum(map(len, words)) / len(words))
