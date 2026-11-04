import os
import subprocess
import psycopg2

connection = None
cursor = None


def clear_screen():
    os.system('cls')

def open_conn():
    # get globals
    global connection, cursor
    # Establish database connection
    connection = psycopg2.connect(
        host="localhost",  # Your VM's IP address
        port="5432",
        database="Assignment_3",
        user="postgres",
        password="postgres"
    )

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

def close_conn():
    # get globals
    global connection, cursor
    # Close connection
    cursor.close()
    connection.close()

def getAllStudents():
    cursor.execute("SELECT * FROM students;")
    results = cursor.fetchall()
    clear_screen()
    for row in results:
        print(row)
    g = input("\n\n____________________\nPress Enter to go back to the menu")
    clear_screen()

def addStudent(first_name, last_name, email, enrollment_date):
    cursor.execute(f"""INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{first_name}','{last_name}','{email}', '{enrollment_date}');""")
    connection.commit()
    clear_screen()

def updateStudentEmail(student_id, email):
    cursor.execute(f"""UPDATE students SET email = '{email}' WHERE student_id = {student_id}""")
    connection.commit()
    clear_screen()

def deleteStudent(student_id):
    cursor.execute(f"""DELETE FROM students WHERE student_id = {student_id}""")
    connection.commit()
    clear_screen()

def main():
    print("trying...")
    open_conn()

    loop_flag = True
    while loop_flag:
        choice = input("1. Display all students\n2. Add a student\n3. Update student email\n4. Delete student\n5. Quit \n______________\n Enter Selection: ")
        try:
            choice = int(choice)
            if choice > 5 or choice < 1:
                continue
            else:
                match choice:
                    case 1:
                        getAllStudents()
                    case 2:
                        first_name = input("Enter the student's first name: ")
                        last_name = input("Enter the student's last name: ")
                        email = input("Enter the student's email: ")
                        enrollment_date = input("Enter the student's enrollment date (yyyy-mm-dd): ")
                        addStudent(first_name, last_name, email, enrollment_date)
                    case 3:
                        student_id = input("Enter student id: ")
                        email = input("Enter new email: ")
                        updateStudentEmail(student_id, email)
                    case 4:
                        student_id = input("Enter student id: ")
                        deleteStudent(student_id)
                    case 5: 
                        loop_flag = False 
        except Exception as e:
            print(e)
            continue



    close_conn()

if __name__ == "__main__":
    main()