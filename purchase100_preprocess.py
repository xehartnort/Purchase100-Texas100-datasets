import numpy as np
from tensorflow.keras.utils import to_categorical


if __name__ == "__main__":
    extracted_filename = "./dataset_purchase"

    features = []
    labels = []
    with open(extracted_filename, 'r') as f:
        for line in f:
            line = line.strip()
            splitted_line = line.split(",")
            labels.append(int(splitted_line[0]) - 1)
            features.append(list(map(int, splitted_line[1:])))

    data = np.array(features)
    labels = to_categorical(labels)

    data = np.array(features)
    labels = to_categorical(labels)
    np.savez_compressed('purchase100', features=data, labels=labels)