import nltk
from nltk.corpus import genesis,names
#nltk.download('genesis')
wt = names.words()
data = nltk.FreqDist(sorted(wt))
corpus=['<s>'+m.lower()+'</s>' for m, n in data.items()]
word=input("\nenter the mis-spelt word to convert into bigrams: ").lower()
lis=['<s>'+word[0],word[-1]+'</s>']
while len(word)>1:
    lis.append(word[:2])
    word=word[1:]
print("\nthe given word's bigrams are: ",lis)
wordsassoc={}
for bigram in lis:
    if bigram not in wordsassoc:
        wordsassoc[bigram.upper()]=()
    for word in corpus:
        if bigram in word:
            wordsassoc[bigram.upper()]=wordsassoc[bigram.upper()]+(word,)
print('\nwords associated with respective bigrams:\n\n',wordsassoc,'\n')
freq={}
for words in wordsassoc.values():
    for wor in words:
        if wor not in freq:
            freq[wor]=0
for word in freq:
    for words in wordsassoc.values():
        if word in words:
            freq[word]=freq[word]+1
print('frequency of all the unique words: \n\n',freq,'\n') 
high=0
for fre in freq.values():
    if fre>high:
        high=fre
wordscon=[]
for word in freq:
    if freq[word]==high:
        wordscon.append(word)
print('words to consider:\n\n',wordscon)
print('\ntotal words to consider: ',len(wordscon))
