class student:
    id:int
    name:str
    department:str
    age:int
    gender:str


    def create(self,id,name,dept,age,gender):
        self.id=id
        self.name=name
        self.department=dept
        self.age=age
        self.gender=gender

    def display_std(self):
        print(self.id,self.name,self.department,self.age,self.gender)


obj=student()
obj.create(100,"kishor","hr",22,"male")     
obj.display_std()       