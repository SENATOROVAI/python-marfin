#  вставь ссылку на задачу и перепиши этот файл на юпитер
num = int(input())
for i in range(num):
    word = input()
    if len(word) > 10:
        print(word[0] + str(len(word) - 2) + word[-1])
    else:
        print(word)