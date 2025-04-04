numar = input("Introduceti un numar: \n")
ramun = ""

i = 0

while i < len(numar):
    ramun = numar[i] + ramun
    i += 1

if numar == ramun:
    print("True")
else:
    print("False")
