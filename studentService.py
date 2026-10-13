from student import Student
import uuid


class studentService:

    def __init__(self):
        self.storage = {}

    def create_student(self):
        new_student = Student()
        new_student.id = uuid.uuid4()
        self.storage[new_student.id] = new_student
        return new_student

    def get_student(self, id):
        student = self.storage[id]
        return student

    def delete_student(self, id):
        del self.storage[id]

