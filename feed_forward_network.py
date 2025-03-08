import torch
import torch.nn as nn
import torch.optim as optim

class SimpleModel(nn.Module):
    # +input_size+ equals 10 by default. We expect 10 features as input.
    # +hidden_size+ equals 10 by default. We have 10 hidden units which is arbitrary, just to have a hidden layer of 20 neurons.
    # +output_size+ equals 2 by default. It represents the number of classes we have in our dataset.
    #
    def __init__(self, input_size=10, hidden_size=10, output_size=2):
        super(SimpleModel, self).__init__()

        self.layer1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        return x
