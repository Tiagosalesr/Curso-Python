#set não aceita duplicatas

filmSet = {"GOT","AOT","TBATE","TMNT", "AOT"}
print(filmSet)

print(len(filmSet))

#True e 1 são considerados o mesmo valor
exampleSet = {"Inception", True, 1, 8.7}
print(exampleSet)

filmSet.update(exampleSet)
print(filmSet)

filmSet.remove(True)
print(filmSet)