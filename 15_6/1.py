class Student:
    def __init__(self, name, rut, marks):
        self.name = name
        self.rut = rut
        self.marks = marks

    def get_name(self):
        return self.name

    def get_rut(self):
        return self.rut

    def get_marks(self):
        return self.marks


def parse_data(filename):
    students = []
    file = open(filename+'.txt', 'r')
    data = file.readlines()
    for x in data:
        parsed = x.split(';')
        students.append(Student(
            parsed[0],
            parsed[1],
            [
                parsed[2],
                parsed[3],
                parsed[4],
                parsed[5],
                parsed[6],
                parsed[7]
            ]
        ))
    return students


def calculate_average(data):
    lines = []
    for x in data:
        marks = [float(y) for y in x.get_marks()]
        # 20, 20, 5, 20, 25, 10
        avg = round(marks[0]*.2 + marks[1]*.2 + marks[2]*.05 + marks[3]*.2 + marks[4]*.25 + marks[5]*.1, 1)
        line = x.get_name()+';'+x.get_rut()+';'+str(avg)
        lines.append(line)
    return lines


def save_data(data, filename):
    file = open(filename+'.txt', 'w')
    for x in data:
        file.write(x+'\n')
    return print("Archivo generado correctamente.")


students = parse_data('estudiantes')
lines = calculate_average(students)
save_data(lines, 'NP')
