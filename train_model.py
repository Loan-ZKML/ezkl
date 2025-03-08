import torch
import torch.nn as nn
import torch.optim as optim
from feed_forward_network import SimpleModel

def train_model(model, epochs=10):
    # Define the loss function and the optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    # Generate some fake data and labels(batch_size=5, each sample has input_size=10 features)
    # The number of features is the one we give to the model as input_size.
    # The number of classes is the one we give to the model as output_size.
    dummy_data = torch.randn(5, 10)
    dummy_labels = torch.randint(0, 2, (5,)) # random labels in {0, 1} for output_size = 2

    # A very small training loop for demonstration purposes
    for epoch in range(10): # train for 10 epochs
        optimizer.zero_grad()
        outputs = model(dummy_data) # default values for input_size and output_size
        loss = criterion(outputs, dummy_labels)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch + 1}, Loss: {loss.item():.4f}")

    return model
