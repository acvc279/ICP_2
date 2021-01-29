file = open("sample.txt", "r")
a = dict()
for line in file:
        line = line.strip()
        words = line.split(" ")
        for word in words:
                if word in a:
                        a[word] = a[word] + 1
                else:
                        a[word] = 1
for key in list(a.keys()):
        print(key, ":", a[key])