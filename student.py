class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value):
        self.__student_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        self.__department = value

    @property
    def is_enrolled(self):
        return self.__is_enrolled

    @is_enrolled.setter
    def is_enrolled(self, value):
        self.__is_enrolled = value

    def enroll_student(self):
        if self.is_enrolled:
            print(f'{self.student_id} is already enrolled.')
        else:
            self.is_enrolled = True
            print(f'{self.student_id} has been enrolled.')

    def drop_student(self):
        if not self.is_enrolled:
            print(f'{self.student_id} is not enrolled.')
        else:
            self.is_enrolled = False
            print(f'{self.student_id} has been dropped.')

    def view_student_info(self):
        status = 'Enrolled' if self.is_enrolled else 'Not Enrolled'
        print(f'ID: {self.student_id}, Name: {self.name}, Department: {self.department}, Status: {status}')