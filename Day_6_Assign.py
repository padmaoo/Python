# 1. Department- deptid,head,location,deptname
    # through the constructor initialize the department, attributes
    # create a method to display the department info
    # display total departments in the company / organization
# 2.
    # user input
    # ask for no.of departments from user
    # use dict/list/tuple to store the data about departments
    # use 'for loop' to get the dept info
    # display all dept info in the form of list
    # search dept by deptid if yes print details, if not 'given dept is not available with us'
    # search dept by deptname

# Question - 1
class Dept:
    dept_count = 0
    def __init__(self,deptid,deptname,depthead,deptloc): 
        self.deptid = deptid
        self.deptname = deptname
        self.depthead = depthead
        self.deptloc = deptloc
        Dept.dept_count += 1

    def display_dept_info(self):
        print('Department Information : ')
        print('-----------------------')
        print(f'Department ID : {self.deptid}')
        print(f'Department Name : {self.deptname}')
        print(f'Department Head : {self.depthead}')
        print(f'Department Location : {self.deptloc}')

    @classmethod
    def get_total_dept(cls):
        return cls.dept_count
    
dept1 = Dept('D001','IT','Padma','Hyd') 
dept1.display_dept_info() # Prints - Department Information : 
                                    # -----------------------
                                    # Department ID : D001
                                    # Department Name : IT
                                    # Department Head : Padma
                                    # Department Location : Hyd

print(f"Total Departments: {Dept.get_total_dept()}") # Prints - Total Departments: 1

# Question - 2 
class Dept1:
    dept_count = 0

    def __init__(self, deptid, deptname, depthead, deptloc): 
        self.deptid = deptid
        self.deptname = deptname
        self.depthead = depthead
        self.deptloc = deptloc
        Dept.dept_count += 1

    def display_dept_info(self):
        print('Department Information : ')
        print('-----------------------')
        print(f'Department ID : {self.deptid}')
        print(f'Department Name : {self.deptname}')
        print(f'Department Head : {self.depthead}')
        print(f'Department Location : {self.deptloc}')
        print()

    @classmethod
    def get_total_dept(cls):
        return cls.dept_count

departments = []

while True:
    print("\n----- Department Menu -----")
    print("1. Add Department")
    print("2. Display All Departments")
    print("3. Search by Department ID")
    print("4. Search by Department Name")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        n = int(input("How many departments do you want to add? "))
        for i in range(n):
            print(f"\nEnter details for department {i+1}:")
            deptid = input("Enter Dept ID: ")
            deptname = input("Enter Dept Name: ")
            depthead = input("Enter Dept Head: ")
            deptloc = input("Enter Dept Location: ")
            dept = Dept1(deptid, deptname, depthead, deptloc)
            departments.append(dept)
        print(f"{n} department(s) added successfully.")

    elif choice == '2':
        if departments:
            print("\nAll Department Details:")
            for dept in departments:
                dept.display_dept_info()
            print(f"Total Departments: {Dept1.get_total_dept()}")
        else:
            print("No departments to display.")

    elif choice == '3':
        search_id = input("Enter Department ID to search: ")
        found = False
        for dept in departments:
            if dept.deptid == search_id:
                dept.display_dept_info()
                found = True
                break
        if not found:
            print("Given department ID is not available with us.")

    elif choice == '4':
        search_name = input("Enter Department Name to search: ")
        found = False
        for dept in departments:
            if dept.deptname.lower() == search_name.lower():
                dept.display_dept_info()
                found = True
        if not found:
            print("Given department name is not available with us.")

    elif choice == '5':
        print("Exiting program!!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

# Output ---> ----- Department Menu -----
                    # 1. Add Department
                    # 2. Display All Departments
                    # 3. Search by Department ID
                    # 4. Search by Department Name
                    # 5. Exit
                    # Enter your choice (1-5): 2
                    # No departments to display.

                    # ----- Department Menu -----
                    # 1. Add Department
                    # 2. Display All Departments
                    # 3. Search by Department ID
                    # 4. Search by Department Name
                    # 5. Exit
                    # Enter your choice (1-5): 1
                    # How many departments do you want to add? 2

                    # Enter details for department 1:
                    # Enter Dept ID: D102
                    # Enter Dept Name: CSE
                    # Enter Dept Head: Sree
                    # Enter Dept Location: Bangalore

                    # Enter details for department 2:
                    # Enter Dept ID: D103
                    # Enter Dept Name: Avi
                    # Enter Dept Head: Avi
                    # Enter Dept Location: Mysore
                    # 2 department(s) added successfully.

                    # ----- Department Menu -----
                    # 1. Add Department
                    # 2. Display All Departments
                    # 3. Search by Department ID
                    # 4. Search by Department Name
                    # 5. Exit
                    # Enter your choice (1-5): 3
                    # Enter Department ID to search: D101
                    # Given department ID is not available with us.

                    # ----- Department Menu -----
                    # 1. Add Department
                    # 2. Display All Departments
                    # 3. Search by Department ID
                    # 4. Search by Department Name
                    # 5. Exit
                    # Enter your choice (1-5): 4
                    # Enter Department Name to search: CSE
                    # Department Information :
                    # -----------------------
                    # Department ID : D102
                    # Department Name : CSE
                    # Department Head : Sree
                    # Department Location : Bangalore

                    # ----- Department Menu -----
                    # 1. Add Department
                    # 2. Display All Departments
                    # 3. Search by Department ID
                    # 4. Search by Department Name
                    # 5. Exit
                    # Enter your choice (1-5): 5
                    # Exiting program!!
