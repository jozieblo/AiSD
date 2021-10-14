# zad1

# def funkcja(x,y):
#     return x+"."+y
# print(funkcja("J","Kowalski"))

# zad2
# def funkcja(x,y):
#     return x[0].capitalize()+"."+y.capitalize()
# print(funkcja("jan","nowak"))

# zad3
# def funkcja(x,y,z):
#     rok=x+y
#     return int(rok)-int(z)
#
# print(funkcja("20","21","21"))

# zad4
# def funkcja2(x,y,funkcja):
#     return funkcja(x,y)
# print(funkcja2("jan","bytom",funkcja))

# zad5
# def funkcja(x,y):
#     if (x & y >=0) and (y!=0) :
#         return x/y
# print(funkcja(12,5))

# zad6
# def funkcja(suma):
#     x=0
#     while (suma<100):
#         print("Wprowadz liczbe: ")
#         x=int(input())
#         suma+=x
#     return "Suma wynosi: ",suma
# print(funkcja(0))

# zad7
# def funkcja(lista):
#     return tuple(lista)
#
# lista=[1,2,3,4,5,"panda"]
# print(funkcja(lista))

# zad8
# def funkcja():
#     lista = []
#     for i in range(0,5):
#         print("Wprowadz element: ")
#         i=input()
#         lista.append(i)
#     return tuple(lista)
# print(funkcja())

# zad9
# def funkcja(x):
#     dzien={
#            1:"Poniedzialek",
#            2:'Wtorek',
#            3: 'Sroda',
#            4: 'Czwartek',
#            5: 'Piatek',
#            6: 'Sobota',
#            7: 'Niedziela',
#            }
#     return dzien.get(x,"Nie ma takiego dnia tygodnia")
# print(funkcja(int(4)))

# zad10
# def funkcja(napis):
#
#     if napis == napis[::-1]:
#         return True
#     else:
#         return False
# print(funkcja("okak"))