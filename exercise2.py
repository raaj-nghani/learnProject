choice = int(input("Enter Choice 1 (Exercise) or 2 (Food) : "))
name = int(input("Enter choose name 1(Kiran) 2(Mohan) 3(Kamlesh) "))
if choice==1 and name ==1:
    kiran_ex = open("d:/prj_exerc/kiran_exer.txt", "a")
    text = input("Enter exercise")
    kiran_ex.write(text)
    kiran_ex.close()
elif choice ==2 and name ==1:
    kiran_fo = open("d:/prj_exerc/kiran_food.txt", "a")
    food = input("Enter Food : ")
    kiran_fo.write(food)
    kiran_fo.close()
elif choice==1 and name ==2:
    mohan_ex = open("d:/prj_exerc/mohan_exer.txt","a")
    text = input("Enter exercise")
    mohan_ex.write(text)
    mohan_ex.close()
elif choice ==2 and name ==2:
    mohan_fo = open("d:/prj_exerc/mohan_food.txt","a")
    food = input("Enter Food : ")
    mohan_fo.write(food)
    mohan_fo.close()
elif choice==1 and name ==3:
    kamesh_ex = open("d:/prj_exerc/kamesh_exer.txt","a")
    text = input("Enter exercise")
    kamesh_ex.write(text)
    kamesh_ex.close()
elif choice ==2 and name ==3:
    kamesh_fo = open("d:/prj_exerc/kamesh_food.txt","a")
    food = input("Enter Food : ")
    kamesh_fo.write(food)
    kamesh_fo.close()
else:
    print("Wrong Choice")


