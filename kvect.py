print('ты проснулся в понедельник 5 утра, надо идти в школу...')
ans = int(input("1. спать 2. пойти в школу"))
if ans == 1:
    print("ты проспал и математичка поставила тебе 2")
    ans1 = int(input("1.стать гулём 1000-7 2.бросить петарду в математичку и убежать"))
    if ans1 == 1:
        print("ты сал гулем, и убежал из школы")
        ans2 = int(input("1. стать нормальным человеком 2. утонуть в туалете"))
        if ans2 == 1:
            print("Ура, за точто ты стал нормальным человеком математичка убрала двойку!")
        else:
            print("всё...")
else:
    if ans == 2:
        print("ты пошел в школу, но гопник стырил у тебя телефон")
        ans3 = int(input("1. догнять его 2. купить нокиа 3310"))
        if ans3 == 1:
            print("ты догнал его, ты вернул свой телефон")
            ans4 = int(input("1. убежать 2. сесть и разговаривать с ним о жизни"))
            if ans4 == 1:
                print("ты пытался убежать но он схватил тебя за ногу и уташил тебя в свою машину")
                ans5 = int(input("1. ударить его и убежать 2.орать"))
            if ans5 == 1:
                print("ты убежал, ура")

        else:
            if ans3 == 2:
                print("ура, новая покупка!")
                ans6 = int(input("1. прыгать от счастья 2. пойти дамой"))
            if ans6 == 1:
                print("ты настолько радовался что упал и сломал ногу")
            ans7 = int(input("1. радоваться что ты не пойдешь в школу 2. звать на помщь"))
            if ans7 == 1:
                print("ты радовался,но тебе пришли на помощь и начали распрашивать что произошло")
                ans8 = int(input("1. сказать что ты упал с дерева 2. сказать правду "))
                if ans8 == 1:
                    print("тебе не поверили и бросили тебя в дет.доме")
            else:
                 print("ты пошел домой")
            ans9 = int(input("1. не делать д/з 2. делать д/з"))
            if ans9 == 1:
                print("ты не сделал д/з и тебя отчислили")
                ans10 = int(input("1.работать уборщиком школы 2. попросить вернуться в школу"))
            if ans10 == 1:
                print("ты начал работать ")
