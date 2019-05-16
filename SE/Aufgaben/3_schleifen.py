"""array=[4,5,7,11,21]

for a in array:
    result=a+2
    print(result)

for i in range(1,101, 5):
    print(i)

for i in range(0,100, 5):
    print(i)

number=int(input("Geben Sie bitte an, wie viele Wörter Sie eingeben wollen: "))

words=[]
for i in range(number):
    words.append(input("Bitte geben Sie ein Wort ein: "))

print(words)

antwort=input("Sind Sie cool. Bitte antworten Sie mit J/N:")
antworten=["J","N","j","n"]
while antwort not in antworten:
    antwort=input("Sind Sie cool. Bitte antworten Sie mit J/N:")"""

number=int(input("Bis zu welcher Fibonacci Zahl brauchen Sie ein Ergebnis?"))
result1=0
result2=1
print(result1)
print(result2)
while result2<number:
    result2+=result1
    print(result2)
    result1=result2-result1






