# Zero Knowledge Layer (EZKL)
- Import ONNX model to EZKL
- Generate proving system
- Create a verifier contract template
- Depends on output fromn the [model repo](https://github.com/Loan-ZKML/model).

# Notes while experimenting with `ezkl`.

## Installing

- I installed `ezkl` on my local machine.
- Installed `rust` 1.85.0. This initially allows me to run `cargo doc --open` (? when do I run this ? It is supposed to be returning the EZKL Rust documentation, so, I guess
that this is useful if one downloads the EZKL repository and install from source).

## Setup - Done at the Development Time by Developers

Ref: [Setup](https://docs.ezkl.xyz/getting-started/setup/) phase.

### Installed Python And Libraries

- Installed and pin Python 3. This will allow me to generate a sample ONNX file using [PyTorch](https://pytorch.org/).
- Installed PyTorch: `python -m pip install torch`.
- Installed `onnx`: `python -m pip install onnx`.

### Neural Network Model

- I just need a model in order to be able to generate an ONNX file. I created the model in PyTorch: [./feed-forward-network.py](./feed-forward-network.py)
- I also created a training program([./train-model.py](./train-model.py)), but only for illustrating how one can train a model. This is not necessary to generate an ONNX file, because a randomly
initialized model can still be exported to ONNX. *Note:* However, for our zkML Bootcamp, we will need a trained model (which happens in the `model` repository).
- I created the [./generate_onnx.py](./generate_onnx.py) which takes the trained model instance and exports it
in ONNX format: `python ./generate_onnx.py` generates the file `simple_model.onnx`.
- I validated the model with this:
    ```python
    import onnx

    onnx_model = onnx.load("simple_model.onnx")
    onnx.checker.check_model(onnx_model)
    print("ONNX model is valid")
    ```
### `ezkl` Setup

- Structured Reference String (SRS): `ezkl get-srs`.
- Generate settings: `ezkl gen-settings --model ./simple_model.onnx`
- Generate calibration data: I created the file [./generate_calibration_data.py](./generate_calibration_data.py) and ran it with `python ./generate_calibration_data.py`.
- Calibrate settings: `ezkl calibrate-settings --model ./simple_model.onnx`.
- Compile model: `ezkl compile-circuit --model simple_model.onnx`. This generates the file `model.compiled`.
- Run setup: `ezkl setup`. This generates
    - [pk.key](./pk.key): key needed for proving
    - [vk.key](./vk.key): key needed for verifying

## Prove - Done by the User

### Generate Witness

I provided the `input.json` file. This is supposed to be **private** data:

```json
{
  "input_data": [
    [0.15, 0.23, 0.32, 0.45, 0.57, 0.63, 0.78, 0.82, 0.94, 0.99]
  ]
}
```
to the command:

```bash
ezkl gen-witness --compiled-circuit ./model.compiled
```

This generated the file `witness.json`. This now contains the intermediate outputs (out of running the private data via the neural network) including potential public ones depending on the settings

### Generate Proof

```bash
ezkl prove --compiled-sircuit model.compiled
```

This generates the file `proof.json`.

## Verify - Done by the User

### Verify On CLI

```bash
ezkl verify
```

### Verify Onchain

```bash
ezkl create-evm-verifier
```

This created the file `evm_deploy.sol`.
