from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from math import sqrt


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            data = f.read()
        return data

    except IOError:
        print("Error opening or reading input file: ", filename)
        sys.exit()

entry=int(input("Enter the method to get input:\n1- Defulat sentances.\n2-User input.\n3-Files inputs.\n input:"))

if entry == 1:
    X = "you can go deaf by listening to overly loud music."
    Y = "you can go auditorily impaired by heedfully auricularly discerning inordinately loud music."
elif entry == 2:
    X = input("Enter first string: ").lower()
    Y = input("Enter second string: ").lower()
elif entry == 3:
    X=read_file('x.txt')
    Y=read_file('y.txt')
else:
    print('input not valed')
    exit()

X_list = word_tokenize(X)
Y_list = word_tokenize(Y)

sw = stopwords.words('english')
#print(sw)
l1 = [];
l2 = []

X_set = {w for w in X_list if not w in sw}
Y_set = {w for w in Y_list if not w in sw}

rvector = X_set.union(Y_set)
for w in rvector:
    if w in X_set:
        l1.append(1)
    else:
        l1.append(0)
    if w in Y_set:
        l2.append(1)
    else:
        l2.append(0)
c = 0

for i in range(len(rvector)):
    c += l1[i] * l2[i]
cosine = c / float(sqrt(sum(l1) * sum(l2)))
print("Cosine similarity:", "% 0.4f"%cosine)
