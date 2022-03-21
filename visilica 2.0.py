import random

words = ["ученый", "пк", "дом", "мод", "игра", "одежда","жажда","навыки","собака","бункер", ]

word=words[random.randint(0, 9)]#индекс слова 
len_word=len(word)#количество букв, которые осталось угадать
health = 10
test=False
used_word= " "
win_word=[]
used_letters= []
# заполнение массива для слова в игре
for s in range(len_word):
    win_word+="_"

while len_word != 0 and health != 0:
    test = False
    #ввод буквы и проверка на повтор
    
    letter = input("\nвведите букву ")
    if (letter in used_letters) or (len(letter)>1):
        print ("\nНе больше одного символа, попробуйте снова!")
    else:
        used_letters.append(letter)
        
    count=0
    for s in word:
        if letter == s :
            len_word -= 1
            test=True
            win_word[count]=letter
        count+=1
                    
    if test == False:
        health -= 1
        print ("НЕВЕРНО")
    else:
        print("ВЕРНО")
        print(win_word)
                        
        print("ваше здоровье = " + str(health))
                    
if(len_word == 0):
    print("\nПОБЕДИТЕЛЬ!!! Слово было " +  word)
else:
    print("\nВЫ ПРОИГРАЛИ! ПОПРОБУЙТЕ СНОВА!")
