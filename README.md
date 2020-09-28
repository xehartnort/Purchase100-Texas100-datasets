# Purchase100 dataset

A repo to preprocess the Purchase100 dataset extracted from Kaggle: Acquire Valued Shoppers Challenge

## Steps

 1. Download the `transactions.csv.gz` file from https://www.kaggle.com/c/acquire-valued-shoppers-challenge/data
 2. Run `preprocess_dataset.py <path_to_transactions.csv.gz>` to generate numpy binary files .npy
 3. In the root folder of your local copy of this repository, two new files are created: `purchase100-features.npy` and `purchase100-labels.npy`
 4. Now you can import them in your code using [numpy.load function](https://numpy.org/doc/stable/reference/generated/numpy.load.html)

## References

The code in this repo is based on the preprocessing scripts given in https://github.com/bargavj/EvaluatingDPML
