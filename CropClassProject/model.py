import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv(r"C:\CropClassProject\Iris.csv")
df.dropna(inplace=True)
x = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y = df['Species']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=50)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)  # Use transform, not fit_transform

classifier = RandomForestClassifier()
classifier.fit(x_train, y_train)  # Fit on feature variables, not target

# Dumping the classifier object
with open("model.pkl", "wb") as f:
    pickle.dump(classifier, f)
