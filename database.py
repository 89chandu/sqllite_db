import sqlite3

class Database:

    DB_NAME = "school.db"

    @classmethod 
    def connect(cls):
        return sqlite3.connect(cls.DB_NAME)
    
    @classmethod
    def create_table(cls):
        connection = cls.connect()

        cursor = connection.cursor()

        cursor.execute("""

            CREATE TABLE IF NOT EXISTS students(
                       
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       age INTEGER NOT NULL,
                       course TEXT NOT NULL
                       
                       )
                """)
        
        connection.commit()
        connection.close()


        @classmethod
        def add_student(cls,name,age,course):

            connection = cls.connect()

            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO students(name,age,course)

                VALUES(?,?,?)
                """,
                (name,age,course)
            )

            connection.commit()
            connection.close()


        @classmethod   
        def get_students(cls):

            connection = cls.connect()

            cursor = connection.cursor()

            cursor.execute(

                "SELECT *FROM students"
            )

            students = cursor.fetchall()
            connection.close()

            return students
        
        @classmethod
        def update_student(cls,student_id,name,age,course):

            connection = cls.connect()

            cursor = connection.cursor()

            cursor.execute(
                """

                UPDATE students

                SET 

                    name = ?,
                    age = ?,
                    course = ?

                WHERE id = ?    
                """,
                (name,age,course,student_id)
            )

            connection.commit()
            rows = cursor.rowcount
            connection.close()

            return rows > 0





    


