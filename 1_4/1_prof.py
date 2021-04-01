a = eval(input("ingrese un numero: "))

b = eval(input("ingrese un numero: "))

c = eval(input("ingrese un numero: "))

if (a > b and b > c):

  print("",a ,b ,c)

else:

  if(a > c and c > b):

    print("",a ,c ,b)

  else:

    if(b > a and a > c):

      print("",b ,a ,c)

    else:

      if(b > c and c > a):

        print("",b ,c ,a)

      else:

        if(c > a and a > b):

          print("",c ,a ,b)

        else:

          (c > b and b > a)

          print("",c ,b ,a)