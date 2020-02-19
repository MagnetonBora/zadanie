from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Sequence, BigInteger, DateTime, Time, create_engine

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

class Administrator(Base):
    __tablename__ = "Administrator"
    staff_id = Column(Integer, Sequence("staff_id_seq"), primary_key = "TRU")
    department_id = Column(Integer, Sequence("department_id_seq"))
    enrollment_date = Column(DateTime, Sequence("enrolment_date_id"))

    def __repr__(self):
        return f"Administrator({self.staff_id}, {self.department_id}, {self.enrollment_date})"

class Students(Base):
    __tablename__ = 'Students'
    id = Column(Integer, Sequence("id_seq"), primary_key=True)
    fist_name = Column(String(50), Sequence("first_name_seq"))
    last_name = Column(String(50), Sequence("first_name_seq"))
    pesel = Column(BigInteger, Sequence("first_name_seq"))
    phone = Column(String(11), Sequence("phone_seq"))
    adres = Column(String(50, Sequence("adres_seq")))

    def __repr__(self):
        return f"User({self.id}, {self.first_name}, {self.last_name}," \
               f" {self.pesel}, {self.phone}, {self.adres})"


class StudentsGrade:
    __tablename__ = "StudentsGrade"
    enrollment_id = Column(Integer, Sequence("enrollment_id_seq"), primary_key = True)
    student_id = Column(Integer, Sequence("student_id_seq"))
    course_id = Column(Integer, Sequence("course_id_seq"))
    grade = Column(Integer, Sequence("grade_seq"))

    def __repr__(self):
        return f"StudentGrade({self.enrollment_id}, {self.student_id}, {self.course_id}, {self.grade})"

class Department:
    __tablename__ = "Department"
    id = Column(Integer, Sequence("id_seq"), primary_key=True)
    name = Column(String(50), Sequence("name_seq"))
    budget = Column(Integer, Sequence("budget_seq"))
    adress = Column(String(50), Sequence("adress_seq"))

    def __repr__(self):
        return f"Department({self.id}, {self.name}, {self.budget}, {self.adress})"


class Staff:
    __tablename__ = "Staff"
    id = Column(Integer, Sequence("id_seq"), primary_key=True)
    first_name = Column(String(50), Sequence("first_name_seq"))
    last_name = Column(String(50), Sequence("first_name_seq"))
    pesel = Column(BigInteger, Sequence("first_name_seq"))
    phone = Column(String(11), Sequence("phone_seq"))
    adres = Column(String(50, Sequence("adres_seq")))

    def __repr__(self):
        return f"User({self.id}, {self.first_name}, {self.last_name}," \
               f" {self.pesel}, {self.phone}, {self.adres})"

class Course:
    __tablename__ = "Course"
    course_id = Column(Integer, Sequence("course_id_seq"), primary_key = True)
    title = Column(String(50), Sequence("title_id"))
    credits = Column(Integer, Sequence("credits_id"))
    department_id = Column(Integer, Sequence("department_id_seq"))
    start_date = Column(DateTime, Sequence("start_date_seq"))
    end_date = Column(DateTime, Sequence("end_date_seq"))
    price = Column(Integer, Sequence("price_seq"))

    def __repr(self):
        return f"({self.course_id}, {self.title}, {self.credits}," \
               f" {self.department_id}, {self.start_date}, {self.end_date}, {self.price})"


class CourseInstructor:
    __tablename__ = "CourseInstructor"
    course_id = Column(Integer, Sequence("course_id_seq"), primary_key = True)
    staff_id = Column(Integer, Sequence("staff_id_seq"))
    enrollment_date = Column(DateTime, Sequence("enrollment_date"))

    def __repr__(self):
        return f"({self.course_id}, {self.staff_id}, {self.enrollment_date})"


class OnlineCourse:
    __tablename__ = "OnlineCourse"
    course_id = Column(Integer, Sequence("course_id_seq"))
    url = Column(String(50), Sequence("url_seq"))

    def __repr__(self):
        return f"({self.course_id}, {self.url})"


class OnsiteCourse:
    __tablename__ = "OnsiteCourse"
    course_id = Column(Integer, Sequence("course_id_seq"))
    adress = Column(String(45), Sequence("adress_seq"))
    days = Column(String(45), Sequence("days_seq"))
    time = Column(Time, Sequence("time_seq"))


if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    mateusz = Administrator(staff_id = "666", department_id = "5", enrollment_date = "22")
    session.add(mateusz)
    session.query(Administrator).all()

