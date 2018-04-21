from flask import request
from services import PubSubHelper
import logging
import multiprocessing
import time

# projects/capitalinside-testing/topics/my-new-topic
# capitalinside-testing:my_new_dataset.my_new_table
# gs://capitalinside-test/tmp

class SendController:

    def __init__(self):
        self.counter = 0
        self.pubsub = PubSubHelper()

    def index(self):
        p = multiprocessing.Process(target=self.loop)
        p.start()
        # Wait for 10 seconds or until process finishes
        p.join(60)
        # If thread is still active
        if p.is_alive():
            # Terminate
            p.terminate()
            p.join()

    def loop(self):
        self.counter += 1
        logging.warning('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
        logging.warning(self.counter)
        self.pubsub.send()
        time.sleep(.33)
        self.loop()
        #self.pubsub.start()
