print("Students Detail \n")
name = input("Name: ")
class_ = int(input("Class: "))
sec = input("Section: ")
addr = input("Address: ")
f= open("students_slip.txt","w")
f.writelines(name)
f.writelines(str(class_))
f.writelines(sec)
f.writelines(addr)
f.close()