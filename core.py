class classModule:
    courseCM = "B.Sc(CS)"
    teacherCM = "Mr Chani"
    classCM = "A-512"

    def PrintData(self):
        print(self.courseCM, self.teacherCM, self.classCM)


classTable = [[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0]]

for index1 in range(5):
    for index2 in range(9):
        classTable[index1][index2] = classModule()

for index1 in range(5):
    for index2 in range(9):
        print(classTable[index1][index2].courseCM)
        print(classTable[index1][index2].teacherCM)
        print(classTable[index1][index2].classCM)
    print("\n")