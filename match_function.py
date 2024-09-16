#parent -- class
#secA -- child class


class Sslc:
    def __init__(self,total_stu,total_teachers):
        self.total_stu = total_stu
        self.total_teachers = total_teachers

    def sslc_main_class(self):
        print(self.total_teachers)
        print(self.total_stu)

#child class

class SecA(Sslc):
    def __init__(self,total_stu,total_teachers, secA_stu):
        self.secA_stu = secA_stu
        Sslc.__init__(self, total_stu,total_teachers)

    def secA_students(self):
        print(self.secA_stu)

vv = SecA(20,50,100)
print(vv.total_teachers)
print(vv.total_stu)
print(vv.secA_stu)



