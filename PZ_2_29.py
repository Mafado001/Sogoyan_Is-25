# Варинат 29
# Дни недели пронумерованы следующим образом: 1 понедельник, 2 - вторник, 6 - суббота, 7 воскресенье.
# Дано целое число К, лежащее в диапазоне 1-365.
# Определить номер дня недели для К-го дня года, если известно, что в этом году 1 января было субботой.

K = (input("Введите число K (от 1 до 365): "))
try:
    K = int(K)
    if 0 < K < 366:
        a = K % 7
        if a == 0:
            print(K,"-й день года - воскресенье")
        elif a == 1:
            print(K,"-й день года - понедельник")
        elif a == 2:
            print(K,"-й день года - вторник")
        elif a == 3:
            print(K,"-й день года - среда")
        elif a == 4:
            print(K,"-й день года - четверг")
        elif a == 5:
            print(K,"-й день года - пятница")
        elif a == 6:
            print(K, "-й день года - суббота")

    else:
        print('Введите верное значение')
except ValueError:
    print('Введите верное значение')