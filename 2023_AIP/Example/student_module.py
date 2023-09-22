import student

# stu = student.Student('Kim', 10, 20)
lgstu = student.LGstudent('Park', 50, 80)
pfstu = student.PFstudent('Lee', 40, 90)

print(lgstu)
print(pfstu)

# pfstu.do_something()

student.PFstudent.do_something()

# print(stu)