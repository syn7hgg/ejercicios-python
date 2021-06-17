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

    def get_avg(self):
        marks = self.marks
        marks = [float(x) for x in marks]
        avg = round(marks[0] * .2 + marks[1] * .2 + marks[2] * .05 + marks[3] * .2 + marks[4] * .25 + marks[5] * .1, 1)
        return avg


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


def generate_lines(data):
    lines = []
    for x in data:
        line = x.get_name()+';'+x.get_rut()+';'+str(x.get_avg())
        lines.append(line)
    return lines


def save_filtered(data):
    file_ap = open('aprobados.txt', 'w')
    file_ex = open('examen.txt', 'w')
    for x in data:
        line = x.get_name() + ';' + x.get_rut() + ';' + str(x.get_avg())
        if x.get_avg() >= 5:
            file_ap.write(line+'\n')
        else:
            file_ex.write(line+'\n')
    return print("Archivos de filtro generados correctamente.")


def save_data(data, filename):
    file = open(filename+'.txt', 'w')
    for x in data:
        file.write(x+'\n')
    return print("Archivo generado correctamente.")


students = parse_data('estudiantes')
lines = generate_lines(students)
save_data(lines, 'NP')
save_filtered(students)
