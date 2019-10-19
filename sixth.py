Alfavet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


str = input("Please write the sentences:\n").lower()

for i in range(26):
    print("Count of " , Alfavet[i], " =",str.count(Alfavet[i]))