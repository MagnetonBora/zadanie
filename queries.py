queries = [ "CREATE TABLE IF NOT EXIST Student(id INTEGER PRIMARY KEY AUTOINCREMENT, firstname VARCHAR, last_name VARCHAR, Pesel INTEGER, Phone_number INTEGER, address VARCHAR)",
            " CREATE TABLE IF NOT EXIST Administrator(stuff_id PRIMARY KEY AUTOINCREMENT,  deperment_id INTEGER, enrollment_date DATETIME",
            " CREATE TABLE IF NOT EXIST DEPARTMENT(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR, budget FLOAT, address VARCHAR)",
            " CREATE TABLE IF NOT EXIST StudentsGrade(enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT, student_id INTEGER, coaurse_id INTEGER, grade FLOAT)",
            " CREATE TABLE IF NOT EXIST Coarse(course_id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR, credits INTEGER, deperment_id INTEGER, start_date DATETIME, end_date DATETIME, price INTEGER)",
            " CREATE TABLE IF NOT EXIST CourseInstructor(course_id INTEGER PRIMARY KEY AUTOINCREMENT,staff_id INTEGER, enrollment_date DATETIME)"]


""" 
Zapytania sqlowe, nie wiem czy o to dokładnie chodziło w tym zadaniu, aby stworzyć zapytania sql w osobnym pliku
"""