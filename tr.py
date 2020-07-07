import nltk
from nltk.corpus import genesis,names,webtext,brown
from random import shuffle,sample
from decimal import Decimal
import operator
#nltk.download('webtext')
wt = brown.words()
data = nltk.FreqDist((wt))
corpus=['<s>'+m.lower()+'</s>' for m, n in data.items()]
#corpus=sample(corpus,len(corpus))
wor=[wor.lower() for wor in input("\nenter some mis-spelt words: ").split(',')]
ogword=['<s>'+ogword.lower()+'</s>' for ogword in input("\nwhat do you think the og words are: ").split(',')]
n=[int(n)for n in input("\nenter what kind of gramming scheme (integer) : ").split(',')]
mrr=0
for i in range(len(n)):
    z=wor[i]
    lis=['<s>'+z[:n[i]-1]]
    while len(z)>n[i]-1:
        lis.append(z[:n[i]])
        z=z[1:]
    lis.append(z+'</s>')
    print("\nthe given word's {}-grams are: ".format(n[i]),lis,'\n')
    wordsfreq={}
    for word in corpus:
        if word not in wordsfreq:
            wordsfreq[word]=0
        for bigram in lis:
            if bigram in word:
                wordsfreq[word]=wordsfreq[word]+1
    wordscon=sorted(wordsfreq.items(), key=operator.itemgetter(1), reverse=True)
    print("let's consider top 20 words:\n\n",wordscon[:20])
    for w in range(len(wordscon[:20])):
        if wordscon[:20][w][0]==ogword[i]:
            mrr+=Decimal(1/(w+1))
    if i==len(n)-1:
        mrr/=(i+1)
        mrr= round(mrr,2)
print('\nmrr is: ',mrr)


