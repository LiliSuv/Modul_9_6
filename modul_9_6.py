a="функции-генераторы"
def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text)-i):
            yield text[i:i+j+1]
for elem in all_variants(a):
    print(elem)