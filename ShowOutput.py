import json
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from LSTMmodel import build_lstm_model

def trainModel(lstm_neurons, dropout, loss, optimizer, batch_size, epochs, X_train, y_train, X_test, y_test):

    model = build_lstm_model(X_train, output_size=1, neurons=lstm_neurons, dropout=dropout, loss=loss,optimizer=optimizer)
    history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=epochs, batch_size=batch_size, verbose=2, shuffle=True)

    plt.plot(history.history['loss'],'r',linewidth=2, label='Train loss')
    plt.plot(history.history['val_loss'], 'g',linewidth=2, label='Validation loss')
    plt.title('LSTM')
    plt.xlabel('Epochs')
    plt.ylabel(loss.upper())
    plt.show()

    return model

        
def predictModel(test, model,target_col,window_len,X_test,line_plot):

    targets = test[target_col][window_len:]
    preds = model.predict(X_test).squeeze()
    preds = test[target_col].values[:-window_len] * (preds + 1)
    preds = pd.Series(index=targets.index, data=preds)
    line_plot(targets, preds, 'actual', 'prediction', lw=3)
    print("Accuracy ->",100 *(r2_score(targets, preds)))


    
