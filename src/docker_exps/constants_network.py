
URL_BASE = 'http://127.0.0.1'
PORT_CONTROLLER = 48515
PORT_TRAIN = 48516

URL_BASE_IN_TRAIN = 'http://ml_train'

URL_CONTROLLER = URL_BASE + ':' + str(PORT_CONTROLLER) + '/'
URL_TRAIN = URL_BASE + ':' + str(PORT_TRAIN) + '/'
URL_TRAIN_INTERNAL = URL_BASE_IN_TRAIN + ':' + str(PORT_TRAIN) + '/'
