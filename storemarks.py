class Student:
    def __init__(self, sid, name, dob):
        self.id = sid
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, cid, name):
        self.id = cid
        self.name = name

class Mark:
    def __init__(self, course):
        self.course = course
        self.data = {}   # {student_id: mark} tạo dict data rỗng

class StudentMarkSystem: # tạo list rỗng
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []     # list of Mark objects

    # ---- Input functions ----
    def input_students(self):  #input từng element student vào list students
        n = int(input("Number of students: "))
        for _ in range(n):
            sid = input("Student ID: ")
            name = input("Name: ")
            dob = input("DoB: ")
            self.students.append(Student(sid, name, dob))

    def input_courses(self):  #input từng element course vào list courses
        n = int(input("Number of courses: "))
        for _ in range(n):
            cid = input("Course ID: ")
            name = input("Course Name: ")
            self.courses.append(Course(cid, name))

#---------------------------------------------------------
    def input_marks(self):
        while True:
            # Hiển thị danh sách course
            print("Courses:")
            for i in range(len(self.courses)):
                print(str(i+1) + ". " + self.courses[i].name)  
                # str(i+1) để chuyển số thứ tự thành chuỗi rồi nối với tên course

            print("0. Exit")  # Thêm lựa chọn thoát

            choice = int(input("Select course (0 to exit): ")) - 1   
            # Người dùng nhập số thứ tự course, trừ đi 1 để ra index (0-based)
            if choice == -1:  # Nếu chọn 0 thì thoát vòng lặp
                break

            course = self.courses[choice]  
            # Lấy course tương ứng với index đã chọn trong list self.courses
            #courses[i], i là 0,1,2,3,... tương ứng với course(element của courses)
            mark_obj = Mark(course)  
            # Tạo object Mark để lưu điểm cho course này
            # mark_obj sẽ chứa thông tin của course và data(gồm s)
            print("Input marks:")  
            # Nhập điểm cho từng student trong course đã chọn
            for s in self.students:
                m = float(input("Mark for " + s.name + ": "))  
                # Nhập điểm cho student, ép kiểu sang float
                mark_obj.data[s.id] = m  
                # Lưu vào dict data: key = student id, value = mark

            self.marks.append(mark_obj)  
            # Sau khi nhập xong, lưu mark_obj vào list self.marks

#---------------------------------------------------

    def show_marks(self):
        # In danh sách courses
        print("Courses:")
        for i in range(len(self.courses)):
            print(str(i+1) + ". " + self.courses[i].name) #courses[i] để truy cập các course trong list courses

        # Người dùng chọn course
        idx = int(input("Select course: ")) - 1                
        cid = self.courses[idx].id

        # Tìm marks cho course đó
        for m in self.marks:
            if m.course.id == cid:
                for s in self.students:
                    print(s.name, m.data[s.id])    
                return

        print("No marks for this course.")
    #---------------------------------------------------------
    def list_students(self):
        for s in self.students:
            print(s.id, s.name, s.dob)

    def list_courses(self):
        for c in self.courses:
            print(c.id, c.name)

#--------------------------------------------------------
system = StudentMarkSystem() #new object system, system là 1 object có 3 list students, courses, marks
system.input_students() # thêm các student vào list
system.input_courses() # thêm các course vào list
system.input_marks() # thêm mark của mỗi course cho từng học sinh


print("\nStudents:")
system.list_students()

print("\nCourses:")
system.list_courses()

print("\nMarks:")
system.show_marks()
