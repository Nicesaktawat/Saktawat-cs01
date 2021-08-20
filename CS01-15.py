def my_list(list):
    for x in range (len(list)):
        if (list[x] == 20):
            list[x] = 200
        print(list)

list = [5, 10, 15, 25, 50, 20]
my_list(list)