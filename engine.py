import torch
import torch.nn as nn

def init_model():
    globals()['neurons'] = 64
    globals()['input_data'] = torch.FloatTensor([[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]])
    real_neurons = globals()['neurons']
    real_data = globals()['input_data']
    model = nn.Sequential(nn.Linear(10, real_neurons), nn.ReLU(), nn.Linear(real_neurons,2))
    prediction = model(real_data)
    print(prediction)
init_model()
