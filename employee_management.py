class Employee:

    def __init__(self, name, eid):
        self.__name = name
        if len(eid) < 1:
            self.__eid = "9999"
        else:
            self.__eid = eid

    @property
    def name(self):
        return self.__name.capitalize()

    @name.setter
    def name(self, new_name):
        if new_name.isalpha():
            self.__name = new_name
        else:
            self.__name = "Unknown"

    @property
    def eid(self):
        return self.__eid.zfill(4)

    @eid.setter
    def eid(self, new_eid):
        if len(new_eid) == 0:
            self.__eid = "9999"
        else:
            self.__eid = new_eid

    def __str__(self):
        return f'{self.eid}: {self.name}'


class Manager(Employee):

    def __init__(self, name, eid):
        super().__init__(name, eid)
        self.subordinates = []

    def print_subordinates(self):
        for sub in self.subordinates:
            print(f'\t{sub}')

    def add_subordinates(self):
        name = input('Enter subordinate name: ')
        eid = input('Enter subordinate id: ')
        tempEmployee = Employee(name, eid)
        self.subordinates.append(tempEmployee)


class WrongInput(Exception):
    def __init__(self, msg):
        self.msg = msg


def add_employee():
    name = input('Enter name: ')
    eid = input('Enter id: ')
    while True:
        try:
            ismanager = input('Is the employee a manager? (Y/N) ').upper()
            if ismanager == 'Y':
                tempEmployee = Manager(name, eid)
                while True:
                    try:
                        sub_count = int(input('How many subordinates? '))
                    except ValueError:
                        print('Invalid input! Try again!')
                    else:
                        for i in range(1, sub_count + 1):
                            tempEmployee.add_subordinates()
                        break
            elif ismanager == 'N':
                tempEmployee = Employee(name, eid)
            else:
                raise WrongInput('Selection must be Y or N! Try again!')
        except ValueError:
            print('Invalid selection! Try again!')
        except WrongInput as excp:
            print(excp)
        else:
            return tempEmployee


def main():
    employees = []

    print(f'{"Employee Management System": ^50}\n\nAdding Employee...\n')

    while True:
        employees.append(add_employee())
        continue_loop = input('Do you want to enter more? (Y/N) ').upper()
        if continue_loop != 'Y':
            break
        print()

    print()

    print('Printing Employee List')
    for emp in employees:
        print(emp)
        if isinstance(emp, Manager):
            print(f"\t{emp.name}'s Employees")
            emp.print_subordinates()


if __name__ == '__main__':
    main()
