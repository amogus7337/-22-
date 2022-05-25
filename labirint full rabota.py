import random
         
spisok =[['#', 'o', '#', '*', '*', '*', '#', '#', '#', '#'],
         ['#', '*', '#', '*', '#', '*', '#', '*', '*', '*'],
         ['#', '*', '*', '*', '#', '*', '#', '*', '#', '*'],
         ['#', '#', '#', '#', '#', '*', '#', '*', '#', '*'],
         ['#', '*', '*', '*', '*', '*', '#', '*', '#', '*'],
         ['#', '*', '#', '#', '#', '#', '#', '*', '#', '*'],
         ['#', '*', '*', '*', '*', '*', '*', '*', '#', '*'],
         ['#', '#', '#', '#', '#', '#', '#', '#', '#', '*'],
         ['#', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
         ['#', '*', '#', '#', '#', '#', '#', '#', '#', '#']]
print('список каманд : печаить-Распечатать Список, d-Право, a-Лево, w-Верх, s-Вниз,Телепорт на X и Y Лабиринта телепорт только на *')  
print('другие команды не работают только эти !!!!!! ☝☝☝☝')
k= input('Введите команду')
while True:
    a = 0
    g = 0
    if k == 'd':
        for stroka in range(len(spisok)):
            for stolb in range(len(spisok)):
                if spisok[stroka][stolb] == "o":     
                    a = stroka
                    g = stolb
        
        if spisok[a][g+1]=='#':
            print('там стена')
        else:
            spisok[a][g+1]= 'o'
            spisok[a][g]='*'
            
    elif k=='a':
        for stroka in range(len(spisok)):
            for stolb in range(len(spisok)):
                if spisok[stroka][stolb] == "o":
                    a = stroka
                    g = stolb
                    
        if spisok[a][g-1]=='#':
            print('там стена')
        else:    
            spisok[a][g-1]= 'o'
            spisok[a][g]='*'
        
    elif k=='s':
        for stroka in range(len(spisok)):
            for stolb in range(len(spisok)):
                if spisok[stroka][stolb] == "o":
                    a = stroka
                    g = stolb
                    
        if spisok[a+1][g]=='#':
            print('там стена')
        else:
            spisok[a+1][g]= 'o'
            spisok[a][g]='*'
        
    elif k=='w':
        for stroka in range(len(spisok)):
             for stolb in range(len(spisok)):
                 if spisok[stroka][stolb] == "o":
                     a = stroka
                     g = stolb
                     
        if spisok[a-1][g]=='#':
            print('там стена')
        else:
            spisok[a-1][g]= 'o'
            spisok[a][g]='*'           
        
        
            
    elif k=="печать":
        for stroka in spisok:
            for stolb in stroka:
                print(stolb, end="")
            print()
    
    elif k == "телепорт":
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
                if spisok[stroka][stolb] == "o":
                    a = stroka
                    g = stolb
        spisok[a][g]='*'
        spisok[r-1][s-1]='o'

    else:
        print('нет таких команд')
        k = input('введите  команду')
    
    k = input('введите  команду')
