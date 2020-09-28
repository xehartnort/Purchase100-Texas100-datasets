# Purchase100 dataset

A repo to preprocess the Purchase100 dataset extracted from Kaggle: Acquire Valued Shoppers Challenge

## Download preprocessed dataset

 - [purchase100_features.npy.zip](https://github.com/xehartnort/Purchase100-dataset/blob/master/purchase100_features.npy.zip?raw=true)
 - [purchase100_labels.npy.zip](https://github.com/xehartnort/Purchase100-dataset/blob/master/purchase100_labels.npy.zip?raw=true)

## Steps to preprocess the dataset

 1. Download the `transactions.csv.gz` file from https://www.kaggle.com/c/acquire-valued-shoppers-challenge/data
 2. Run `preprocess_dataset.py <path_to_transactions.csv.gz>` to generate numpy binary files .npy
 3. In the root folder of your local copy of this repository, two new files are created: `purchase100-features.npy` and `purchase100-labels.npy`
 
## How to use it

 - You can import them in your code using [numpy.load function](https://numpy.org/doc/stable/reference/generated/numpy.load.html)

 ```python
    features = np.load('./purchase_100_features.npy')
    labels = np.load('./purchase_100_labels.npy')
 ```

## Requirements

This work is tested with Python 3.8.5.

The requirements.txt file is automatically generated with [pipreqs](https://github.com/bndr/pipreqs).

## References

The code in this repo is based on the preprocessing scripts given in https://github.com/bargavj/EvaluatingDPML
