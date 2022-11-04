import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
digits = datasets.load_digits()
_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, label in zip(axes, digits.images, digits.target):
    ax.set_axis_off()
    ax.set_title('Trainig: %i ' % label)
n_samples= len(digits.images)
data = digits.images.reshape((n_samples,-1))
clf=svm.SVC(gamma=0.001)
X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.5, shuffle=False)
clf.fit(X_train, y_train)
predicted = clf.predict(X_test)
_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10,3))
for ax, image, prediction in zip(axes, X_test, predicted):
  ax.set_axis_off()
  image = image.reshape(8,8)
  ax.set_title(f'Predição: {prediction}')
print(f'Relatório de classificação para classificador {clf}:\n'
  f'{metrics.classification_report(y_test, predicted)}\n')
import pickle
modelo_treinado=pickle.dumps(clf)
modelo_carregado = pickle.loads(modelo_treinado)
modelo_carregado.predict([X_test[0]])
#X_test[0]
modelo_carregado.predict([X_test[0]])
disp = metrics.plot_confusion_matrix(clf, X_test, y_test)
disp.figure_.suptitle('Confusion Matriz')
print(f'Confusion Matriz:\n{disp.confusion_matrix}')

plt.show()