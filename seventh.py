
Alfavet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
str = input("Please write the sentences:\n").lower()

def first():
 mas = str.split()
 mas.sort()
 for i in range(26):
     print(Alfavet[i]+" : ")
     for j in range(len(mas)):
         if mas[j].lower().startswith(Alfavet[i]):
             print(mas[j])



def second():
 for i in range(26):
     print("Count of " , Alfavet[i], " =",str.count(Alfavet[i]))

if(int(input("Select 1 or another"))==1):
    first()
else:
    second()
