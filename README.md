# Purchase100 and Texas100 dataset

This repository preprocess the datasets downloaded from: [https://github.com/privacytrustlab/datasets](https://github.com/privacytrustlab/datasets)

## How to use it

 - You can import them in your code using [numpy.load function](https://numpy.org/doc/stable/reference/generated/numpy.load.html)

 ```python
    data = np.load('./purchase100.npz')
    features = data['features']
    labels = data['labels']
 ```

Note that labels are one hot encoded.

## Requirements

This work is tested with Python 3.8.5.

The requirements.txt file is automatically generated with [pipreqs](https://github.com/bndr/pipreqs).