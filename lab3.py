import mysql.connector
from getpass import getpass


#connect to data base
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='employees'
)

class Employee:
    all_employees = [] 
    def __init__(self, first_name, last_name,age,dept,salary):
      self._id = None
      self.first_name = first_name
      self.last_name = last_name
      self.age = age
      self.dept = dept
      self.salary = salary
      Employee.all_employees.append(self)
      try:
        cur = mydb.cursor()
          # insert a new record in the employee table
        cur.execute("INSERT INTO employee (first_name, last_name, age, dept, salary) VALUES (%s, %s, %s, %s, %s)",
              (self.first_name, self.last_name, self.age, self.dept, self.salary))
          # commit the changes 
        mydb.commit()
        self._id = cur.lastrowid
      except Exception as e:
        print(e)


    def transfer(self, new_dept):
      self.dept = new_dept
      try:
        cur = mydb.cursor()
          #update the new department 
        cur.execute("UPDATE employee SET dept = %s WHERE id = %s ",
                      (self.dept, self._id))
        mydb.commit()
      except Exception as e:  
         print(e)

 
    def fire(self):
            # delete the record of the employee from the list
            Employee.all_employees.remove(self)
            try:
              cur = mydb.cursor()
              # delete the record of the employee from the database
              cur.execute("DELETE FROM employee WHERE id = %s", (self._id,))
              mydb.commit()  
            except Exception as e:  
               print(e) 

    def show(self):
        try:
          cur = mydb.cursor()
            #display the data for this object 
          sql = "SELECT * FROM employee WHERE id=%s"
          cur.execute("SELECT * FROM employee WHERE id=%s",(self._id,))
          data = cur.fetchall()
          for row in data:
            print(row)

        except Exception as e:  
          print(e)


    @classmethod
    def listEmployees(cls):
        try:
          cur = mydb.cursor()
            #display the data for all employees 
          cur.execute("SELECT * FROM employee")
          rows = cur.fetchall()
          for row in rows:
            print(row)
        except Exception as e:  
          print(e)    

# employee1 = Employee("Samar", "Samy", 23, "Sales", 5000)
# employee2 = Employee("Fatma", "Khaled", 23, "IT", 10000) 

# # employee1.transfer("IT")  
# employee2.fire()
# print(Employee.all_employees)
# # employee1.show()
# Employee.listEmployees() 
# ###close the connection
# mydb.close()  



class Manager(Employee): 
  def __init__(self, first_name, last_name, age, dept, salary, managed_department):
        super().__init__(first_name, last_name, age, dept, salary)
        self. managed_department =  managed_department


  def show(self):
    try:
      cur = mydb.cursor()
      cur.execute("SELECT * FROM employee WHERE id = %s", (self._id,))      
      data = cur.fetchone()   #the data returns in a tuple form 
        # replace salary value with "confidential" if is an instance of Manager class
      if isinstance(self, Manager):
        data = list(data) #convert the tuple form to list to can assign a value on the element because the tuple doesn't support that
        data[5] = "confidential"
        # data = tuple(data)
        print(data)
    except Exception as e:  
         print(e)  

# manager1=Manager("Samar", "Samy", 23, "Sales", 5000, "marketing")
# manager1.show()


def main():
    while True: #make the code run except the user wants to exit 
        print("Select an operation:")
        print(" Enter (e) to Add new employee")
        print(" Enter (m) to Add new manager")
        print(" Enter (t) to Transfer employee")
        print(" Enter (s) to Show employee/manager")
        print(" Enter (l) to List all employees/managers")
        print(" Enter (f) to Fire employee/manager")
        print(" Enter (q) to Quit")
        
        operation = input("Enter the operation you want: ")
        
        if operation == 'e':
            addEmployee()
        elif operation == 'm':
            addManager()
        elif operation == 't':
            transferEmployee()
        elif operation == 's':
            showEmployee()
        elif operation == 'l':
            listEmployees()
        elif operation == 'f':
            fireEmployee()
        elif operation == 'q':
            break
        else:
            print("Invalid operation")


#make an instance of employee class    
def addEmployee():
    print("Adding new employee:")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    age = int(input("Age: "))
    dept = input("Department: ")
    salary = int(input("Salary: "))
    Employee(first_name, last_name, age, dept, salary)
    print("Employee added successfully")

#make an instance of manager class  
def addManager():
    print("Adding new manager:")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    age = int(input("Age: "))
    dept = input("Department: ")
    salary = float(input("Salary: "))
    managed_department = input("Managed department: ")
    Manager(first_name, last_name, age, dept, salary, managed_department)
    print("Manager added successfully")


def transferEmployee():
    id = int(input("Enter employee/manager ID: "))
    dept = input("Enter new department: ")
    emp = findEmployee(id)
    if emp:
        emp.transfer(dept)
        print("Employee/manager transferred successfully")
    else:
        print("Employee/manager not found")

def showEmployee():
    id = int(input("Enter employee/manager ID: "))
    emp = findEmployee(id)
    if emp:
        emp.show()
    else:
        print("Employee/manager not found")

def listEmployees():
    print("All employees/managers:")
    Employee.listEmployees()

def fireEmployee():
    id = int(input("Enter employee/manager ID: "))
    emp = findEmployee(id)
    if emp:
        emp.fire()
        print("Employee/manager fired successfully")
    else:
        print("Employee/manager not found")

#find the employee/manager in the list 
def findEmployee(id):
    for emp in Employee.all_employees:
        if emp._id == id:
            return emp
    return None

if __name__ == '__main__':
    main()
