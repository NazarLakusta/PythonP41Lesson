class Course:
    def __init__(self,name,instructor,duration):
        self.name = name
        self.instructor = instructor
        self.duration = duration

    def about_course(self):
        print(f"course: {self.name} instructor: {self.instructor} "
              f"duration: {self.duration}")

    def is_long_course(self):
        return self.duration>40



#Створити клас Course
# Атрибути (
# name - назвар курсу,
# instructor - викладач,
# duration - тривалість
# Методи
# course_info() - виводить інформацію про курс
# is_long_course() - перевіряє чи курс більше 40 годин,
# якщо так  - True, якщо ні False

#Створити як мінімум три курса, показати інформацію про них
# та перевірити на довготривалість




course1 = Course("Python","Nazar",45)
course1.about_course()
print(course1.is_long_course())


