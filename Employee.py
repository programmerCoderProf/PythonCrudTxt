from pathlib import Path
class Employee:
    def __init__(self):
        self.employees={}
    #load txt file to a dictionary
    def loadFile(self):
        path = Path('employee.txt')
        contents = path.read_text().rstrip()
        lines = contents.splitlines()
        for line in lines:
            data = line.strip().split(',')
            id=data[0]
            self.employees[id]=data
        return  self.employees
    #search for an employee:
    def search(self,id):
        return  self.employees.get(id,"Employee not found")
    #show all employees
    def showAll(self):
        for v in self.employees.values():
                print(f"ID:{v[0]}, Name:{v[1]}, Salary:{v[2]}")


    # add new Employee
    def addEmployee(self):
        empdata=[]
        id=input("Enter Id:")
        if id in self.employees.keys():
            print("Employee Already exit")
        else:
            empdata.append(id)

            empdata.append(input("Enter Name:"))
            empdata.append(input("Enter Salary:"))
            self.employees[id]=empdata
            print("Added Successfully")
            self.saveChanges()

    #save changes in file:
    def saveChanges(self):
        path=Path("employee.txt")
        allData = ''
        for i in self.employees.values():
            allData+=f"{i[0]},{i[1]},{i[2]}\n"
        path.write_text(allData)
    #delete employee:
    def deleteEmployee(self):
        id=input("Enter id to delete: ")
        if id in self.employees.keys():
            print(self.employees.get(id),"Deleted Successfully")
            del self.employees[id]
            self.saveChanges()

        else:
            print("Employee not found!")




#end class Employee
emp= Employee()
emp.loadFile()
while True:
       print("--------------------------------------------")
       print('1. Add employee')
       print('2. Search by ID')
       print('3. Show all')
       print('4. Delete employee')
       print('5. Quit')
       choice = input('Enter your choice: ')
       print("--------------------------------------------")
       if choice == '1':
           emp.addEmployee()
           emp.saveChanges()
       elif choice == '2':
           id = input('Enter ID: ')
           searched= emp.search(id)
           print(searched)
       elif choice == '3':
           emp.showAll()
       elif choice == '4':
           emp.deleteEmployee()
       elif choice == '5':
           break
