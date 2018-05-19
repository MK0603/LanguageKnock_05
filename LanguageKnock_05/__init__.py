def nGram(targetString ,n):
    for i in range(len(targetString)):
        ngram.append(targetString[i:i+n])
#         i=i+n

def nGramWord(targetString,n):
    modify=targetString.split()
    for i in range(len(modify)):
        result=[]
        for j in range(i,min(i+n,len(modify))):
            result.append(modify[j])
        str=" ".join(result)
        ngramword.append(str)



ngram=[]
ngramword=[]
target="I am an NLPer"
nGram(target, 3)
nGramWord(target, 3)
print(ngram)
print(ngramword)