import uuid
from student import Student
from studentService import studentService
from schoolClass import SchoolClass

class classService():

    def __init__(self):
        self.storage = {}

    def create_class(self):
        new_class = SchoolClass()
        new_class.id = uuid.uuid4()
        self.storage[new_class.id] = new_class
        return new_class

    def add_student_to_class(self, student_id, class_id):
        student_service = studentService()
        student = student_service.get_student(student_id)
        class_to_work = self.storage[class_id]
        dict_of_students = class_to_work.students
        dict_of_students[student_id] = student
        student.school_class_id = class_id

    def get_class(self, class_id):
        school_class = self.storage[class_id]
        return school_class


    def delete_student_from_class(self, student_id, class_id):
        student_service = studentService()
        student = student_service.get_student(student_id)
        student_class_id = student.school_class_id
        student.school_class_id = None
        student_class = self.get_class(class_id)
        del student_class.students[student_class_id]

    def get_student_roster(self, class_id):
        class_to_explore = self.get_class(class_id)
        return class_to_explore.students.values()








