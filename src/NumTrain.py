import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

d={42:0,84:0}
data_dict = pickle.load(open('D:\\img_num\\data.pickle', 'rb'))
# حذف العينات ذات الطول 84
print(data_dict)
for item in data_dict['data']:
    print(len(item))
filtered_data = [item for item in data_dict['data'] if len(item) == 42]
filtered_labels = [label for i, label in enumerate(data_dict['labels']) if len(data_dict['data'][i]) == 42]

# تحويل البيانات إلى مصفوفة NumPy
data = np.asarray(filtered_data)
labels = np.asarray(filtered_labels)
print(data)

# print(f"عدد العينات بعد التصفية: {len(data)}")

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

model = RandomForestClassifier()

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

score = accuracy_score(y_predict, y_test)

print('{}% of samples were classified correctly !'.format(score * 100))

f = open('D:\\img_num\\model.p', 'wb')
pickle.dump({'model': model}, f)
f.close()