class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

    @classmethod
    def view_all_students(cls):
        for student in cls.student_list:
            student.view_student_info()