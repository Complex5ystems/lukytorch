import torch
import torch.nn as nn

####init_model_node####
def init_model(features, neurons, output, learning_rate):
    global model, optimiser, loss_func
    model = nn.Sequential(nn.Linear(features, neurons), nn.ReLU(), nn.Linear(neurons, output))
    loss_func = nn.MSELoss()
    optimiser = torch.optim.Adam(model.parameters(), lr=learning_rate)

def run_model(input_data, raw_target):
    global model, optimiser, loss_func
    real_data = torch.FloatTensor([input_data])
    target = torch.FloatTensor([raw_target])
    prediction = model(real_data)
    optimiser.zero_grad()
    loss = loss_func(prediction, target)
    loss.backward()
    optimiser.step()
    print(prediction)
    print("target: ", target)
    print("loss: ", loss)
