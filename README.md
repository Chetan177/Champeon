# Champeon
PUBG Win prediction system
## About
Champeon is based on a Dense Neural Network model which has accuracy rate of more than 94%. It uses Keras model running on a Tensorflow backend which is GPU accelerated. The DataSet which is used to develop the DNN model is consist of more than 4 million examples.

## Tensorflow model used:
### The DNN is made up of 5 layers with 4 in between batch normalization layer 
1. Input layer with 32 units
2. Hidden layer with 64 units
3. Hidden layer with 64 units
4. Hidden layer with 64 units
5. Output layer with 1 units

Input layer and all the 3 hidden layers uses the relu activation function
The output layers uses sigmoid function as activation fucntion.
<a href="https://ibb.co/k45KkjW"><img src="https://i.ibb.co/7njv8P6/Pubg-DNN.png" alt="Pubg-DNN" border="0"></a>
