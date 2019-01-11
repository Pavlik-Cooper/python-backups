with open('multiplication_t.txt','a') as table:
    for i in range(2, 13):
        for j in range(1, 13):
            print(f"{str(j)} times {i} is {j*i}",file=table)
        print("==================",file=table)