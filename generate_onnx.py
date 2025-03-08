import torch.onnx
from feed_forward_network import SimpleModel
from train_model import train_model

model = SimpleModel()

model = train_model(model)

# make sure the model is in evaluation mode (particularly important for e.g. BatchNorm/Dropout layers).
model.eval()

# Create a dummy input tensor matching the input shape I used for the network.
# For the example model we have, the input shape is torch.Size([1, 10]).
dummy_input = torch.randn(1, 10)

# Export the model to ONNX format
torch.onnx.export(
  model,
  dummy_input,
  "simple_model.onnx",
  opset_version=10,
  input_names=["input"],
  output_names=["output"],
)
