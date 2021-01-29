list = []
l = []
n = int(input("Enter no. of students:"))
print("Enter the height in feet")
for i in range(0, n):
    m = float(input())
    list.append(m)
print(list)
for j in list:
    cm = j * 30.48
    l.append(cm)
print(l)