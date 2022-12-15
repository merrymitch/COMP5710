from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets, linear_model
import pandas as pd
import numpy as np 
import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.keras.utils import to_categorical
import SQA_logger

def readData():
    iris = datasets.load_iris()

    # Log iris dataset since datasets are used in poisoning attacks
    log0 = SQA_logger.getSQALogger()
    log0.debug('{}*{}*{}*{}'.format('workshop9.py', 'readData_dataset', str(iris)))

    print(type(iris.data), type(iris.target))
    X = iris.data
    Y = iris.target
    df = pd.DataFrame(X, columns=iris.feature_names)
    print(df.head())

    return df 

def makePrediction():
    iris = datasets.load_iris()

    # Log iris dataset since datasets are used in poisoning attacks
    log1 = SQA_logger.getSQALogger()
    log1.debug('{}*{}*{}*{}'.format('workshop9.py', 'makePrediction_dataset', str(iris)))

    knn = KNeighborsClassifier(n_neighbors=6)
    knn.fit(iris['data'], iris['target'])
    X = [
        [5.9, 1.0, 5.1, 1.8],
        [3.4, 2.0, 1.1, 4.8],
    ]
    prediction = knn.predict(X)
    print(prediction)    

def doRegression():
    diabetes = datasets.load_diabetes()

    # Log diabetes dataset since datasets are used in poisoning attacks
    log2 = SQA_logger.getSQALogger()
    log2.debug('{}*{}*{}*{}'.format('workshop9.py', 'doRegression_diabetes', str(diabetes)))

    diabetes_X = diabetes.data[:, np.newaxis, 2]
    diabetes_X_train = diabetes_X[:-20]

    # Log diabetes_X_train since it comes from the diabetes dataset and datasets are used in poisoning attacks
    log3 = SQA_logger.getSQALogger()
    log3.debug('{}*{}*{}*{}'.format('workshop9.py', 'doRegression_diabetes_X_train', str(diabetes_X_train)))

    diabetes_X_test = diabetes_X[-20:]
    diabetes_y_train = diabetes.target[:-20]

    # Log diabetes_y_train since it comes from the diabetes dataset and datasets are used in poisoning attacks
    log4 = SQA_logger.getSQALogger()
    log4.debug('{}*{}*{}*{}'.format('workshop9.py', 'doRegression_diabetes_y_train', str(diabetes_y_train)))

    diabetes_y_test = diabetes.target[-20:]
    regr = linear_model.LinearRegression()
    regr.fit(diabetes_X_train, diabetes_y_train)
    diabetes_y_pred = regr.predict(diabetes_X_test)


def doDeepLearning():
    train_images = mnist.train_images()
    train_labels = mnist.train_labels()
    test_images = mnist.test_images()
    test_labels = mnist.test_labels()


    train_images = (train_images / 255) - 0.5
    test_images = (test_images / 255) - 0.5


    train_images = np.expand_dims(train_images, axis=3)
    test_images = np.expand_dims(test_images, axis=3)

    num_filters = 8
    filter_size = 3
    pool_size = 2

    model = Sequential([
    Conv2D(num_filters, filter_size, input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=pool_size),
    Flatten(),
    Dense(10, activation='softmax'),
    ])

    # Log models since they are used in model tricking - log the model's initialization
    log5 = SQA_logger.getSQALogger()
    log5.debug('{}*{}*{}*{}'.format('workshop9.py', 'model_initialized', str(model)))

    # Compile the model.
    model.compile(
    'adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'],
    )

    # Log models since they are used in model tricking - log the model after compiled
    log6 = SQA_logger.getSQALogger()
    log6.debug('{}*{}*{}*{}'.format('workshop9.py', 'model_compiled', str(model)))

    # Train the model.
    model.fit(
    train_images,
    to_categorical(train_labels),
    epochs=3,
    validation_data=(test_images, to_categorical(test_labels)),
    )

    # Log models since they are used in model tricking - log the model after it's trained
    log7 = SQA_logger.getSQALogger()
    log7.debug('{}*{}*{}*{}'.format('workshop9.py', 'model_trained', str(model)))

    model.save_weights('cnn.h5')

    predictions = model.predict(test_images[:5])

    print(np.argmax(predictions, axis=1)) # [7, 2, 1, 0, 4]

    print(test_labels[:5]) # [7, 2, 1, 0, 4]


if __name__=='__main__': 
    data_frame = readData()
    makePrediction() 
    doRegression() 
    doDeepLearning() 