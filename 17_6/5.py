def read_file(filename):
    file = open(filename+'.csv', 'r')
    data = file.readlines()
    return data


def print_data(data):
    for x in data:
        print(x)


data = read_file('NP_csv')
print_data(data)