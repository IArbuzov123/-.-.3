# Задание №3
# Два инвестора - Майкл и Иван хотят вложиться в стартап. Фаундеры сказали, что минимальная сумма инвестиций - X долларов,
# больше инвестировать можно сколько угодно. У Майкла A долларов, у Ивана B долларов. Если оба могут вложиться - выведите 2, 
# если только Майкл - Mike, если только Иван - Ivan, если не могут по отдельности, но вместе им хватает - 1, если никто - 0.


инвестиция = int(input())
Майкл = int(input())
Иван = int(input())

if (Майкл >= инвестиция) and (Иван >= инвестиция):
    print(2)
elif (Майкл >= инвестиция): 
    print("Mike")
elif (Иван >= инвестиция): 
    print("Ivan")
elif (Майкл + Иван) == (инвестиция):
    print(1) 
else:
    print(0)
 
