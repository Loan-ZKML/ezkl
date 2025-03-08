import json
import random

# The simple model expects shape [batch_size, input_size] = [1, 10]
num_calibration_examples = 2

calibration_data = []
for _ in range(num_calibration_examples):
    # Generate a random sample with 10 features
    sample_input = [random.random() for _ in range(10)]
    # Wrap the sample in another list to represent batch size = 1
    calibration_data.append([sample_input])

# calibration_data is now a list of shape:
# [
#   [[x1, x2, ..., x10]],   # example 1
#   [[x1, x2, ..., x10]],   # example 2
#   ...
# ]

with open("calibration.json", "w") as f:
    json.dump(calibration_data, f, indent=2, separators=(',', ': '))

print("calibration.json generated!")
