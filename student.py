class Student:
    def __init__(self,name,age,course,student_id=None):

        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def to_dict(self):

        return {
            "id":self.student_id,
            "name":self.name,
            "age":self.age,
            "course":self.course
        }   

    @classmethod
    def from_tuple(cls,data):

        return cls(
            student_id = data[0],
            name = data[1],
            age = data[2],
            course = data[3]
        )
    
    def __str__(self):

        return (

            f"ID : {self.student_id}/n"
            f"Name : {self.name}/n"
            f"Age : {self.age}/n"
            f"Course : {self.course}/n"
        )

        