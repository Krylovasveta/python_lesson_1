from student import Student
from CourseGroup import CourseGroup

s=Student("Anna","Ivanova", 25, "testirovshik")

cl1 = Student("Ola", "Ptrova", 25, "testirovshik")
cl2 = Student("Svera", "Krylova", 45, "testirovshik")
cl3 = Student("Svera", "Krylova", 45, "testirovshik")

cg  = CourseGroup(s, [cl1, cl2, cl3])

print (cg)

