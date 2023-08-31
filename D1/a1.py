f = open("test.txt", "w")
f.write("Zeile1\n")
f.write("Zeile2\n")
f.write("Zeile3\n")
f.write("Zeile4\n")
f.write("Zeile5\n")
f.close()

f = open("test.txt", "r")
lines = f.readlines()
print("-------------")
c = 0
while c < len(lines):
    print(lines[c])
    c += 1
f.close()

f = open("test.txt", "a")
f.write("Zeile6\n")
f.write("Zeile7\n")
f.write("Zeile8\n")
f.close()
f = open("test.txt", "r")
lines = f.readlines()
print("-------------")
c = 0
while c < len(lines):
    print(lines[c])
    c += 1

f = open("test.txt", "w")
f.write("Neuer Inhalt")
f.close()
f = open("test.txt", "r")
lines = f.readlines()
print("-------------")
c = 0
while c < len(lines):
    print(lines[c])
    c += 1
