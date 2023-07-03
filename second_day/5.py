name = input("Enter student name: ")
li = []
for i in range(3):

    ele = int(input("Enter the marks: "))
    li.append(ele)
dic = {"name": li}
print(dic["name"][0])

sumof = 0
for k, v in dic.items():
    sumof += sum(v)
perc_a = li[0]/sumof * 100
print(perc_a)
perc_b = li[1]/sumof * 100
perc_c = li[2]/sumof * 100
