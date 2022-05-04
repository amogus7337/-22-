import random
         
spisok =[['о', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]

k= input('Введите команду')
while True:
    a = 0
    g = 0
    if k == 'd':
        for stroka in range(len(spisok)):
            for stolb in range(len(spisok)):
                if spisok[stroka][stolb] == "o" :
                    a = stroka
                    g = stolb
        spisok[a][g]='*'
        spisok[a][g+1]= 'o'
        
    if k=='a':
        for stroka in range(len(spisok)):
            for stolb in range(len(spisok)):
                if spisok[stroka][stolb] == "o" :
                    a = stroka
                    g = stolb
        spisok[a][g]='*'
        spisok[a][g-1]= 'o'
        
        
    if k=='s':
        for stroka in range(len(spisok)):
            for stolb in range(len(spisok)):
                if spisok[stroka][stolb] == "o" :
                    a = stroka
                    g = stolb
        spisok[a][g]='*'
        spisok[a+1][g]= 'o'
        
    if k=='w':
       for stroka in range(len(spisok)):
           for stolb in range(len(spisok)):
               if spisok[stroka][stolb] == "o" :
                   a = stroka
                   g = stolb
       spisok[a][g]='*'
       spisok[a-1][g]= 'o'
       
    if k=="печать":
        for stroka in spisok:
            for stolb in stroka:
                print(stolb, end="")
            print()
    
    if k == "телепорт":

       
        
        r = int (input('какой номер строки ?'))
        s = int (input('какая цифра столбца ?'))
        while (r>10 or r<0) and (s>10 or s<0):
            print('не верно надо 10 на 10!!!')
            r = int (input('какой номер строки ?'))
            s = int (input('какая цифра столбца ?'))
            
        while r>10 or r<0:
            r = int (input('какой номер строки ?'))
            print('неверное значения строки ')
        while s>10 or s<0:
            s = int (input('какая цифра столбца ?'))
            print('неверное значения столбца')
        a = 0
        g = 0
        for stroka in range(len(spisok)):
            for stolb in range(len(spisok)):
                if spisok[stroka][stolb] == "o" :
                    a = stroka
                    g = stolb
        spisok[a][g]='*'
        spisok[r-1][s-1]='o'
            

        
    k = input('введите  команду')
    