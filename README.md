# lukytorch

A Python package that makes creating neural network models less painful. — Quality of life.

<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/6341c9bb-9a65-4a4a-aba1-8e4524cd1c4f" />

# How to Install and Use the lukytorch Python Package

This section provides documentation on how to install and use the lukytorch Python library.

## Installing lukytorch

To install lukytorch, use the following command:

`pip install lukytorch`

Now that you have installed lukytorch, we can move on to a brief guide on how to use it.

## How to Use lukytorch

lukytorch consists of some basic proprietary functions for model initialization.

### The `init_model` function

`init_model(features, neurons, output, learning_rate)`

The `init_model` function is used to initialize a model using parameters such as:

* **Features:** How many input values the model takes from `input_data` in `run_model`.
* **Neurons:** How many neurons the model has.
* **Output:** How many values it predicts.
* **Learning rate:** How much the model adjusts its internal weights.

### The `run_model` function

`run_model(input_data, raw_target)`

The `run_model` function is used to train a model based on the input and target data provided, provided that the data meets the model's requirements.

For example, if `features` is set to `10`, `input_data` must contain 10 floating-point numbers wrapped in square brackets `[]`.

For `raw_target`, the number of values must match the `output` parameter. For example, if `output` is set to `2`, the target should contain 2 floating-point numbers wrapped in square brackets `[]`.

### Full Example Code

```python
import time

init_model(10, 6, 2, 0.001)

while True:
    run_model(
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10]
    )
    time.sleep(0.1)
```

> [!WARNING]
> Lukytorch is still in its early releases and will not receive much maintenance in the foreseeable future.
