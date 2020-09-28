import operator
import numpy as np
from sklearn.preprocessing import normalize
from sklearn.cluster import KMeans
import gzip
import sys

IT_NUM = 100

def normalizeDataset(X):
    mods = np.linalg.norm(X, axis=1)
    return X / mods[:, np.newaxis]

def populate_and_make_dataset(dataset_path):    
    cnt, cust_cnt, it_cnt = 0, 0, 0
    items = dict()
    customer = dict()
    last_cust = ''
    with gzip.open(dataset_path) as fp:
        for line in fp:
            cnt += 1
            if cnt == 1:
                continue
            lin = str(line).split(',')
            cust = lin[0]
            it = lin[3]
            if it not in items and it_cnt < IT_NUM:
                items[it] = it_cnt
                it_cnt += 1
            if cust not in customer:
                customer[cust] = [0]*IT_NUM
                cust_cnt += 1
                last_cust = cust
            if cust_cnt > 250000:
                break
            if it in items:
                customer[cust][items[it]] = 1
    del customer[last_cust]

    no_purchase = []
    for key, val in customer.items():
        if 1 not in val:
            no_purchase.append(key)
    for cus in no_purchase:
        del customer[cus]

    dataset = []
    for key, val in customer.items():
        dataset.append(val)
    dataset = np.array(dataset)
    dataset = normalizeDataset(dataset)

    np.save('purchase100_features.npy', dataset)
    X = KMeans(n_clusters=100, random_state=0).fit(dataset)
    np.save('purchase100_labels.npy', X.labels_)
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit("Error: A valid path to transaction.csv.gz file must be provided as argument")
    else:
        populate_and_make_dataset(sys.argv[1])