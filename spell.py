import nltk
from nltk.corpus import genesis,names,brown,webtext
import operator
from random import shuffle,sample
from decimal import Decimal
#nltk.download('webtext')
wt = brown.words()
data = nltk.FreqDist(sorted(wt))
corpus=[m.lower() for m, n in data.items()]
#corpus=sample(corpus,len(corpus))
wor=[wor.lower() for wor in input("\nenter some mis-spelt words: ").split(',')]
ogword=[ogword.lower() for ogword in input("\nwhat do you think the og words are: ").split(',')]
n=[int(n)for n in input("\nenter what kind of gramming scheme (integer) : ").split(',')]
mrr=0
for i in range(len(n)):
    lis=[]
    while len(wor[i])>n[i]-1:
        lis.append(wor[i][:n[i]])
        wor[i]=wor[i][1:]
    print("\nthe given word's {}-grams are: ".format(n[i]),lis)
    wordsfreq={}
    for word in corpus:
        if word not in wordsfreq:
            wordsfreq[word]=0
        for bigram in lis:
            if bigram in word:
                wordsfreq[word]=wordsfreq[word]+1
    wordscon=sorted(wordsfreq.items(), key=operator.itemgetter(1), reverse=True)
    print("\nlet's consider top 20 words:\n\n",wordscon[:20])
    for w in range(len(wordscon[:20])):
        if wordscon[:20][w][0]==ogword[i]:
            mrr+=Decimal(1/(w+1))
    if i==len(n)-1:
        mrr/=(i+1)
        mrr= round(mrr,2)
print('\nmrr is: ',mrr)
