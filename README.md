# lukytorch
A package for Python that makes creating neural network models less painful. - Quality of life.

# How to install and use lukytorch python package.
This section provides documentation of how to install and use lukytorch Python library.

## Installing lukytorch
To install lukytorch use the following command:


`pip install lukytorch`


Now that you have installed lukytorch we can move on to a brief guide of how to use.

## How to use lukytorch
lukytorch consists of some basic proprietary functions for model initialisation.

### The model_init function
The model_init function:


`init_model()`


is used for initialising a model using basic pytorch, you can configure the initialisation.
using global variables like neurons:

`neurons = 64`

You can also use the input_data variable to specify the training data:
> [!IMPORTANT]
> You will NEED to input 10 float decimals in the tensor field.
> (10 features)

`input_data = torch.FloatTensor([[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]])`

Thank you for reading.

~Comlex5ystems

> [!WARNING]
Lukytorch is still in
its early releases and
will not be receiving
much maintenance in the
foreseeable future.


