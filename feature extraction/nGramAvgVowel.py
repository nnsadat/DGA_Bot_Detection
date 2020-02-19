import pandas



loc = 'alexa14-VowelCount.csv'
dataset = pandas.read_csv(loc, dtype='str')

pandas.set_option('display.max_columns',10)
pandas.set_option('display.max_rows',100)
pandas.set_option('display.max_colwidth',100)

for i in range(0,len(dataset)):
    vc=int(float(dataset.at[i,'vowelCount']))
    blen = int(dataset.at[i,'bigramLen'])
    tlen = int(dataset.at[i,'trigramLen'])
    if (blen==0):
        avg=vc
    else:
        avg=vc/blen
    dataset.at[i,'bigramAvgVowel']=avg
    if (tlen==0):
        avg=tlen
    else:
        avg=vc/tlen
    dataset.at[i,'trigramAvgVowel']=avg
         
print(dataset.head(5))
dataset=dataset.astype('str')
dataset.to_csv('alexa15-NgramAvgVowel.csv',index=False)

loc = 'dga14-VowelCount.csv'
dataset = pandas.read_csv(loc, dtype='str')

for i in range(0,len(dataset)):
    vc=int(float(dataset.at[i,'vowelCount']))
    blen = int(dataset.at[i,'bigramLen'])
    tlen = int(dataset.at[i,'trigramLen'])
    if (blen==0):
        avg=vc
    else:
        avg=vc/blen
    dataset.at[i,'bigramAvgVowel']=avg
    if (tlen==0):
        avg=tlen
    else:
        avg=vc/tlen
    dataset.at[i,'trigramAvgVowel']=avg
         
print(dataset.head(5))
dataset=dataset.astype('str')
dataset.to_csv('dga15-NgramAvgVowel.csv',index=False)
