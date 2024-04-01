from statistics import mean


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.grade = 101

    def setGrade(self, grade):
        if 0 <= int(grade) <= 100:
            self.grade = int(grade)
            return True
        return False

    def get_course_name(self):
        """Returns the name of the course."""
        return self.course_name


class Student:
    def __init__(self, student_name, student_id):
        self.name = student_name
        self._id = student_id
        self.courses = []

    def getStudentID(self):
        return self._id

    def getStudentName(self):
        return self.name

    def addCourse(self, course, grade):
        course = Course(course)
        if course.setGrade(grade):
            self.courses.append(course)
            return True
        else:
            return False

    def get_course(self, course_target_name):
        course_list = list(filter(lambda x: x.course_name == course_target_name, self.courses))
        return course_list[0] if course_list else None

    def gradeAverage(self):
        sum_grade = sum(map(lambda x: x.grade, self.courses))
        count_grade = len(self.courses)
        return sum_grade / count_grade if count_grade != 0 else None


def extract_students_from_file(file_path):
    students = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split('\t')
                name, ID = data[0], data[1]
                student = Student(name, ID)
                courses_data = data[2].split(';')
                for course_info in courses_data:
                    course_name, grade = course_info.split('#')
                    student.addCourse(course_name, grade)
                students.append(student)
            return students
    except Exception as e:
        print(e)


def student_average(students):
    name = input("enter student name: ")
    student = students[0]
    filter_stud = dict(map(lambda student: (student.name, student), students))
    if name not in filter_stud:
        print("Student not found")
    else:
        total_grade = sum(int(course.grade) for course in filter_stud[name].courses)
        average_grade = total_grade / len(student.courses)
        print(f"The ID is: {filter_stud[name].getStudentID()}, the average is: {average_grade}")


def course_average(students):
    name = input("enter course name: ")
    filter_course = list(map(lambda student: student.get_course(name), students))
    if filter_course[0] is None:
        print("\nCourse not found! \n")
        return False
    valid_courses = list(filter(lambda course: course.get_course_name() is not None, filter_course))
    grades = list(map(lambda courses: courses.grade, valid_courses))
    average = sum(grades) / len(grades)
    print("\n" f"The name of the course is: {name}")
    print(f"The average grade is: {average} \n")


def class_average_file(students):
    file_path_open = input("Enter full path to the file you want to create: ")
    try:
        filter_stud = list(
            map(lambda student: f"The ID is: {student.getStudentID()}, the average is: {student.gradeAverage()}\n",
                students))
        with open(file_path_open, "w") as file:
            file.writelines(filter_stud)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    filePath = input("Please enter full path of the file you wish to extract the information from: ")
    students = extract_students_from_file(filePath)

    if students is not None:
        Exit = False
        while not Exit:
            choice = input("Which option would you like to execute? \n"
                           "1. Calculate average Grades of a specific student. \n"
                           "2. Calculate average Grades of a specific course. \n"
                           "3. Create file of the average Grades of all students. \n"
                           "4. exit the program. \n")
            if choice == "1":
                student_average(students)

            if choice == "2":
                course_average(students)

            if choice == "3":
                class_average(students)

            if choice == "4":
                Exit = True
