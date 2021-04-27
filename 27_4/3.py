PI = 3.141559


def deg2rad(n):
    return ((n * PI) / 180)


def rad2deg(n):
    return ((n * 180) / PI)


print("180 grados    son", deg2rad(180), " radianes")

print("PI/4 radianes  son", rad2deg(PI / 4), " grados")
