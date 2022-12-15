import numpy as np
from . import forensic_logging

def random_label_perturbation(y_train, change_unit):    

    # Initialize the logger
    log4 = forensic_logging.getLoggerObj()

    for index in np.random.randint(0,y_train.size-1, int(y_train.size * change_unit)):
        # y_train[index] = np.random.randint(0, 9)
        y_train.iloc[index] ^= 1
        
#     print(y_train.shape)
    print("after perturbation y_train count: ", np.unique(y_train,return_counts=True))
    
    # Once the for-loop is finished log the value of y_train
    log4.debug('{}*{}*{}'.format('random_label_perturbation.py', 'random_label_perturbation', str(y_train)))
    
    return y_train