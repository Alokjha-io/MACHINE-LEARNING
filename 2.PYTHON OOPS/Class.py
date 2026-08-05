class school:
    school_name = "DMS"
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showdata(self):
        print("School name:",self.school_name)
        print("Student name is:",self.name)
        print("Student id is:",self.id)
        
        
s1 = school("Alok jha", 25131181960)
s1.showdata()

