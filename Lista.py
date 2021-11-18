# Lista jednokierunkowa - zadanie 1
# miałem problem z assert wiec printowalem sobie wynik funkcji za kazdym razem

# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.next = None
#
# class ListaJednokierunkowa:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def push(self, wartosc):
#         dodaj = Node(wartosc)
#         dodaj.next = self.head
#         self.head = dodaj
#
#     def append(self, wartosc):
#         dodaj = Node(wartosc)
#         if(self.head!=None):
#             akt= self.head
#             while (akt.next!=None):
#              akt = akt.next
#             akt.next = dodaj
#         else:
#             self.head = dodaj
#
#     def node(self, index):
#         akt = self.head
#         liczba = 0
#         while (akt!=None):
#             if (liczba == index):
#                 return akt.value
#             liczba = liczba+1
#             akt = akt.next
#
#     def insert(self,wartosc,poprzedni):
#         if (poprzedni == None ):
#             print("Bledna instrukcja")
#             return 0
#         nowy= Node(wartosc)
#         nowy.next = poprzedni.next
#         poprzedni.next = nowy
#     def pop(self):
#         if(self.head == None):
#             print("Pierwszy element nie istnieje!")
#         else:
#             pierwszy = self.head
#             print("Pierwszy element to: ", pierwszy.value)
#             self.head = self.head.next
#             pierwszy = None
#
#     def remove_last(self):
#         if(self.head == None):
#             print("Ostatni element nie istnieje!")
#         else:
#             pierwszy = self.head
#             while(pierwszy.next.next != None):
#                 pierwszy = pierwszy.next
#             print("Ostatni element to: ", pierwszy.next.value)
#             pierwszy.next = None
#
#     def remove(self, nr_elementu):
#         if (nr_elementu == self.head.value):
#             self.head = self.head.next
#             return
#         wybrany=self.head
#         while(wybrany.next != None):
#             if(nr_elementu == wybrany.next.value):
#                 break
#             wybrany=wybrany.next.next
#         if (wybrany.next == None):
#             print("Zla liczba!")
#         else:
#             wybrany.next=wybrany.next.next
#
#     def print(self):
#         wsk = self.head
#         while (wsk!=None):
#             print(wsk.value, " -> ", end='')
#             wsk = wsk.next
#         print("")
#     def lenn(self):
#         wsk = self.head
#         licznik = 0
#         while(wsk!=None):
#             licznik= licznik+1
#             wsk = wsk.next
#         return licznik




# lista = ListaJednokierunkowa()
# assert lista.head == None
# lista.push(4)
# lista.push(3)
# assert str(lista) == '3 -> 4'
# lista.append(10)
# lista.append(12)
# print(lista.node(2))
# lista.pop()
# print(lista.remove_last())
# print(lista.lenn())
# lista.print()


#Stos - zadanie 2

# class Stack:
#     def __init__(self):
#         self.stos =  []
#     def push(self, wartosc):
#         self.stos.append(wartosc)
#     def pop(self):
#         if(len(self.stos)==0):
#             wynik="Dlugosc rowna zero, nie ma czego usunac"
#             return wynik
#         else:
#             return self.stos.pop()
#     def lenn(self):
#         return len(self.stos)
#     def print(self):
#             for i in range(len(self.stos)):
#                 print(self.stos[i])
#
#     def __str__(self):
#         return str(self.stos)
# stos = Stack()
# stos.push(1)
# stos.push(2)
# stos.push(3)
# stos.push(4)
# print(stos.pop())
# print(stos.lenn())
# stos.print()



#Kolejka- zadanie 3
# class Queue:
#     def __init__(self):
#         self.kolejka = []
#     def peek(self):
#         return self.kolejka[len(self.kolejka)-1]
#     def enqueue(self,wartosc):
#         self.kolejka.insert(0,wartosc)
#     def dequeue(self):
#           if(len(self.kolejka)==0):
#             wynik="Dlugosc rowna zero, nie ma czego usunac"
#             return wynik
#           else:
#             return self.kolejka.pop()
#     def print(self):
#             print(self.kolejka[::-1])
#     def lenn(self):
#         return len(self.kolejka)
#
# kolej=Queue()
# kolej.enqueue("Pierwszy")
# kolej.enqueue("Drugi")
# kolej.enqueue("Trzeci")
# print(kolej.peek())
# print(kolej.dequeue())
# print(kolej.lenn())
# kolej.print()


