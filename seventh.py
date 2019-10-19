str = input("Please write the sentences:\n")
Alfavet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
mas = str.split()
mas.sort()
for i in range(26):
    print(Alfavet[i]+": ")
    for j in range(len(mas)):
        if mas[j].lower().startswith(Alfavet[i]):
            print(mas[j])

