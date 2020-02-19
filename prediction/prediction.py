import pandas
import _pickle as pkl

loc='yoyo.csv'
dataset = pandas.read_csv(loc)
pandas.set_option('display.max_columns',40)


model_pkl = open("my_rf_classifier30.pkl", "rb")
model = pkl.load(model_pkl)

dataset=dataset[['time','domain','source','bigramWt','trigramWt','bigramNS','trigramNS','bigramEntropy1','trigramEntropy1','a','e','i','o','u','0','1','2','3','4','5','6','7','8','9','-']].copy()
array = dataset.values
X_validation=array[:,3:25]
dataset['predictions'] = model.predict(X_validation)
infected=[]
for i in range(0,len(dataset)):
    if (dataset.at[i,'predictions']=='dga' and dataset.at[i,'source'] not in infected):
        infected.append(dataset.at[i,'source'])
print(infected)

