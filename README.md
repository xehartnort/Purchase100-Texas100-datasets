# Purchase100 dataset

A repo to preprocess the Purchase100 dataset extracted from Kaggle: Acquire Valued Shoppers Challenge

## Download preprocessed dataset

 - [purchase100.npz](https://github.com/xehartnort/Purchase100-dataset/releases/download/v1.0/purchase100.npz)

The authenticity of the downloaded files can be checked with the following md5 hashes

 - purchase100.npz : `0d7538b9806e7ee622e1a252585e7768`

## Steps to preprocess the dataset

 1. Download the `transactions.csv.gz` file from https://www.kaggle.com/c/acquire-valued-shoppers-challenge/data
 2. Run `preprocess_dataset.py <path_to_transactions.csv.gz>` to generate `purchase100.npz`

## How to use it

 - You can import them in your code using [numpy.load function](https://numpy.org/doc/stable/reference/generated/numpy.load.html)

 ```python
    data = np.load('./purchase100.npz')
    features = data['features']
    labels = data['labels']
 ```

## Requirements

This work is tested with Python 3.8.5.

The requirements.txt file is automatically generated with [pipreqs](https://github.com/bndr/pipreqs).

## References

The code in this repo is based on the preprocessing scripts given in https://github.com/bargavj/EvaluatingDPML
