a=int(input('Введите первую стороону '))
b=int(input('Введите вторую сторону '))
c=int(input('Введите третью сторону '))

if a+b>c and a+c>b and b+c>a:

    if a==b==c:
     print("Равносторонний")
    elif a!=b and a!=c and b!=c:
     print("Разносторонний")
    else:
     print("Равнобедренный")

else:
    print('Такого треугольника не существует')
