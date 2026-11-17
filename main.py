from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, f1_score, balanced_accuracy_score, precision_score
import pandas as pd
from collections import Counter
import joblib
model = RandomForestClassifier(
    n_estimators=500,
    max_depth=4,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1)
data = pd.read_csv('data.csv',index_col=False)
x = data
x = x.drop(columns=['Password','Strength'])
y = data['Strength']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
model.fit(x_train,y_train)
pred = model.predict(x_test)
acc = accuracy_score(y_test,pred)
rec = recall_score(y_test,pred,average='macro')
f1 = f1_score(y_test,pred,average='macro')
bal = balanced_accuracy_score(y_test,pred)
prec = precision_score(y_test,pred,average='macro')
print("ACCURACY SCORE: " + str(acc))
print("RECALL SCORE: " + str(rec))
print("F1 SCORE: " + str(f1))
print("BALANCED ACCURACY SCORE: " + str(bal))
print("PRECISION SCORE: " + str(prec))
joblib.dump(model,'predictor.pkl')