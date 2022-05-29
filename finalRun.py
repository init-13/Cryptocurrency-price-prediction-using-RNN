
from dataprepare import getRawData, prepare_data, line_plot
from ShowOutput import trainModel,predictModel

def finalOutput(window_len = 5, test_size = 0.1, zero_base = True, lstm_neurons = 300, epochs = 50, batch_size = 36, loss = 'mse', dropout = 0.2, optimizer = 'adam'):
    
    
    
    print("Neurons -> ",lstm_neurons,"\nEpoch -> " ,epochs , "\nBatch Size -> ",batch_size , "\nLoss Function -> ",loss,"\nOptimizer-> ", optimizer )
    
    optimizer = optimizer.lower()
    
    mapper = {'Mean Squared Error (MSE)':'mse', 'Mean Absolute Error (MAE)':'mae', 'Huber Loss':'huberloss',"Binary Cross Entropy" : 'binary_crossentropy',"Hinge Loss" : 'hinge'}
    
    if loss in mapper:
        print(True)
        loss = mapper[loss]
        
   # print("Neurons -> ",lstm_neurons,"Epoch -> " ,epochs , "Batch Size -> ",batch_size , "Loss Function -> ",loss,"Optimizer-> ", optimizer )
    

    target_col = "close"
    
    hist = getRawData()

    train, test, X_train, X_test, y_train, y_test = prepare_data(hist, target_col, window_len=window_len, zero_base=zero_base, test_size=test_size)

    model = trainModel(lstm_neurons, dropout, loss, optimizer, batch_size, epochs, X_train, y_train, X_test, y_test)

    predictModel(test, model,target_col,window_len,X_test,line_plot)

    

    

    
    
