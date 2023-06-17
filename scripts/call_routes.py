
import requests
from pprint import pprint
import time

import numpy as np
import matplotlib.pyplot as plt


URL_BASE = 'http://127.0.0.1:48515/'


def main_predict():
    # status
    res = requests.get(URL_BASE + 'status').json()
    pprint(res)

    # get example
    dictToSend = dict(
        example_idxs=[103, 110],
        dataset_type='test'
    )
    res = requests.post(URL_BASE + 'get_examples', json=dictToSend)
    dictFromServer = res.json()
    examples = np.array(dictFromServer['examples'])
    temp = {key: val for key, val in dictFromServer.items() if key != 'examples'}
    temp['examples.shape'] = examples.shape
    pprint(temp)

    if 0:
        for i in range(len(examples)):
            plt.figure(figsize=(2, 2))
            plt.imshow(np.transpose(examples[i], (1, 2, 0)))
        plt.show()

    # predict on example
    dictToSend = dict(
        model_id='cifar10_003',
        examples=examples.tolist()
    )
    res = requests.post(URL_BASE + 'predict', json=dictToSend)
    dictFromServer = res.json()
    pprint(dictFromServer)

def main_train():
    # status
    res = requests.get(URL_BASE + 'status').json()
    pprint(res)

    # train
    model_id = str(int(time.time() * 1e6))
    # model_id = '1687044056050585'
    dictToSend = dict(
        model_type="NNConvResNetRGB",
        model_id=model_id,
        example_idxs=[0, 1000],
        train_opts=dict(num_epochs=1)
    )
    res = requests.post(URL_BASE + 'train', json=dictToSend)
    dictFromServer = res.json()
    pprint(dictFromServer)




if __name__ == '__main__':
    main_predict()
    main_train()