from student import Student
from database import StudentDatabase

def initialize_sample_data():
    s1 = Student("S101", "Alice Smith", "Computer Science", True)
    s2 = Student("S102", "Bob Johnson", "Mathematics", False)
    s3 = Student("S103", "Charlie Lee", "Physics", False)
    
    StudentDatabase.add_student(s1)
    StudentDatabase.add_student(s2)
    StudentDatabase.add_student(s3)

def main():
    initialize_sample_data()

    while True:
        print('\n--- Student Management Menu ---')
        print('1. View All Students\n2. Enroll Student\n3. Drop Student\n4. Exit')
        o = input('Enter your choice (1-4): ').strip()

        if o == '1':
            StudentDatabase.view_all_students()
        elif o == '2':
            student_id = input('Enter Student ID to enroll: ').strip()
            found = False
            for student in StudentDatabase.student_list:
                if student_id == student.student_id:
                    student.enroll_student()
                    found = True
                    break
            if not found:
                print('Invalid Student ID')
        elif o == '3':
            student_id = input('Enter Student ID to drop: ').strip()
            found = False
            for student in StudentDatabase.student_list:
                if student_id == student.student_id:
                    student.drop_student()
                    found = True
                    break
            if not found:
                print('Invalid Student ID.')
        elif o == '4':
            print('Exiting program...')
            break
        else:
            print('Please select among 1 to 4.')

if __name__ == '__main__':
    main()