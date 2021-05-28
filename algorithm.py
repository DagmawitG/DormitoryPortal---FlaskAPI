


def compareNandD(a, b):
    if a.year == b.year:
        return b.dep - a.dep
    return 1 if a.year > b.year else -1

def compareNames(a, b):
    if a.name < b.name:
        return -1
    if a.name> b.name:
        return 1
    return 0

def compareDepartment(a, b):
    if a.dep < b.dep:
      return -1
    
    if a.dep > b.dep:
      return 1

    return 0

def cloneArray(oArray, cArray):
    cArray = []
    cArray= oArray.copy()
    return cArray

def assign(list, pd):
    newArray = []
    while (len(list)):
        newArray.append(list[:pd])
    return

def display(array, campusName):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print (array[i][j] + "has been assigned to" + i+1 + "at" + campusName)


def main():

    students = [
    {
        "name": "Nardos",
        "id": 3456,
        "sex": "F",
        "year": 3,
        "department": "mechanical",
    },
    {
        "name": "Alemu",
        "id": 3686,
        "sex": "M",
        "year": 2,
        "department": "biomedical",
    },
    {
        "name": "Saron",
        "id": 1016,
        "sex": "F",
        "year": 2,
        "department": "chemical",
    },
    {
        "name": "Abebe",
        "id": 4556,
        "sex": "M",
        "year": 1,
        "department": "civil",
    },
    {
        "name": "Lili",
        "id": 3009,
        "sex": "F",
        "year": 5,
        "department": "software",
    },
    {
        "name": "Chala",
        "id": 1056,
        "sex": "M",
        "year": 4,
        "department": "electrical",
    }
    #   {
    #     name: "Liya",
    #     id: 8976,
    #     sex: "F",
    #     Year: 4,
    #     department: "civil",
    #   },
    #   {
    #     name: "Kebede",
    #     id: 4545,
    #     sex: "M",
    #     Year: 5,
    #     department: "software",
    #   },
    #   {
    #     name: "Ethiopia",
    #     id: 7878,
    #     sex: "M",
    #     Year: 4,
    #     department: "software",
    #   },
    #   {
    #     name: "Zara",
    #     id: 1010,
    #     sex: "F",
    #     Year: 4,
    #     department: "biomedical",
    #   },
    ]


    fkilo_students = []
    rStudents = []
    mstudents = []
    fstudents= []

    fkilo, fkilopd, skilopd, fbepd = 4, 2, 2, 2

    for x in students:
        if x['year'] ==5 and len(fkilo_students) < fkilo and x['sex'] == "M":
            fkilo_students.append(x)

        else:
            rStudents.append(x)

    students.sort(key = compareNames)

    for i in range(len(students)):
        if students[i].year == 5 and len(fkilo_students) < fkilo and students[i].gen == "M":
            fkilo_students.append(students[i])
        else:
            rStudents.append(students[i])

    students=cloneArray(rStudents, students)
    students.sort(key = compareNames)
    rStudents = []

    if fkilo-len(fkilo_students>0):
        spacesleft = fkilo - len(fkilo_students)

        for i in range(len(students)):
            if spacesleft>0:
                if students.year==4 and students[i].gen == "M":
                    fkilo_students.append(students[i]);
                    spacesleft-=1
                else:
                    rStudents.append(students[i])

            else:
                rStudents.append(students[i])

    students = cloneArray(rStudents, students)

    for i in range(len(students)):
        if students[i].gen=="M":
            mstudents.append(students[i])
        else:
            fstudents.append(students[i])


    mstudents.sort(key = compareNandD)
    fstudents.sort(key = compareNandD)

    fiveKiloStudents = assign(fkilo_students, fkilopd);
    fbeStudents = assign(fstudents, fbepd);
    sixKiloStudents = assign(mstudents, skilopd);

    display(fiveKiloStudents, "5-kilo campus");
    display(fbeStudents, "FBE campus");
    display(sixKiloStudents, "6-kilo campus");
    
        

main()