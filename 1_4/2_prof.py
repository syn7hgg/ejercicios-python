x= eval(input("Ingrese el primer numero: "))

y= eval(input("Ingrese el segundo numero: "))

z= eval(input("Ingrese el tercer numero: "))

a=min(x,y,z)#menor

c=max(x,y,z)#mayor

b= (x + y + z) - a - c #en medio

if(x==y==z):

  print(x,y,z)

else:

  if (x == y > z):

    print(x, y)

    print(z)

  else:

    if (x == y < z):

      print(z)

      print(x, y)

    else:

      if (y == z < x):

        print(x)

        print(y, z)

      else:

        if (y == z > x):

          print(y, z)

          print(x)

        else:

          if(x==z>y):

            print(x,z)

            print(y)

          else:

            if(x==z<y):

              print(y)

              print(x,z)

            else:

              print(c)

              print(b)

              print(a)