def get_input():
    f_name = input("Enter first name : ")
    l_name = input("Enter last name : ")
    salary = float(input("Enter current salary : "))

    return f_name, l_name, salary

def calculate_salary(salary):
    if salary <= 40000:
        new_salary = salary * 1.05
    else:
        new_salary = salary + 2000 + (salary - 40000) * 0.02

    return new_salary

def main():
    f_name, l_name, salary = get_input()
    new_salary = calculate_salary(salary)

    print("New salary for {} {} : ${:,.2f}".format(
        f_name, l_name, new_salary
    ))

main()