# Imports the Google Cloud client library
from google.cloud import pubsub_v1
import json
import datetime

class PubSubHelper:
    def __init__(self):
        self.like = {"type":"like","user_id":1,"article_id":2}
        self.read = {"type":"read","user_id":2,"article_id":3}
        self.click = {
          "url": {
            "info": {
              "path": "/",
              "domain": "staging.capitalinside.com",
              "protocol": "http",
              "anchor": "Null"
            },
            "full": "http://staging.capitalinside.com/"
          },
          "page": {
            "description": "CAPITALinside, das intelligente Finanznewsportal mit Zugang zu tausenden Fonds.",
            "title": "CAPITALinside"
          },
          "user": {
            "uuid": "26d6ce27-a58c-4742-ad2b-6559232f3db8"
          }
        }

    def start(self):
        self.send()

    def send(self):
        data = self.click
        data['created_at'] = str(datetime.datetime.now())
        data = json.dumps(data).encode('utf-8')
        # data = self.message.encode('utf-8')
        publisher = pubsub_v1.PublisherClient()
        topic = publisher.topic_path('capitalinside-testing', 'my-new-topic')
        # https://www.coursera.org/learn/building-resilient-streaming-systems-gcp/lecture/G5yxT/create-topic-and-publish-message
        # https://www.coursera.org/learn/building-resilient-streaming-systems-gcp/lecture/mYC60/need-to-process-variable-amounts-of-data-that-will-grow-over-time
        publisher.publish(topic, data=data)

# with topic.batch() as batch:
#     batch.publish(PAYLOAD1)
#     batch.publish(PAYLOAD2, extra=EXTRA)





# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# import time
# import gzip
# import logging
# import argparse
# import datetime
# from google.cloud import pubsub
# TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
# TOPIC = 'sandiego'
# INPUT = 'sensor_obs2008.csv.gz'
# def publish(topic, events):
#    numobs = len(events)
#    if numobs > 0:
#       with topic.batch() as batch:
#          logging.info('Publishing {} events from {}'.
#                     format(numobs, get_timestamp(events[0])))
#          for event_data in events:
#               batch.publish(event_data)
#
# def get_timestamp(line):
#    # look at first field of row
#    timestamp = line.split(',')[0]
#    return datetime.datetime.strptime(timestamp, TIME_FORMAT)
#
# def simulate(topic, ifp, firstObsTime, programStart, speedFactor):
#    # sleep computation
#    def compute_sleep_secs(obs_time):
#         time_elapsed = (datetime.datetime.utcnow() - programStart).seconds
#         sim_time_elapsed = (obs_time - firstObsTime).seconds / speedFactor
#         to_sleep_secs = sim_time_elapsed - time_elapsed
#         return to_sleep_secs
#    topublish = list()
#    for line in ifp:
#        event_data = line   # entire line of input CSV is the message
#        obs_time = get_timestamp(line) # from first column
#        # how much time should we sleep?
#        if compute_sleep_secs(obs_time) > 1:
#           # notify the accumulated topublish
#           publish(topic, topublish) # notify accumulated messages
#           topublish = list() # empty out list
#           # recompute sleep, since notification takes a while
#           to_sleep_secs = compute_sleep_secs(obs_time)
#           if to_sleep_secs > 0:
#              logging.info('Sleeping {} seconds'.format(to_sleep_secs))
#              time.sleep(to_sleep_secs)
#        topublish.append(event_data)
#    # left-over records; notify again
#    publish(topic, topublish)
#
# def peek_timestamp(ifp):
#    # peek ahead to next line, get timestamp and go back
#    pos = ifp.tell()
#    line = ifp.readline()
#    ifp.seek(pos)
#    return get_timestamp(line)
#
# if __name__ == '__main__':
#    parser = argparse.ArgumentParser(description='Send sensor data to Cloud Pub/Sub in small groups, simulating real-time behavior')
#    parser.add_argument('--speedFactor', help='Example: 60 implies 1 hour of data sent to Cloud Pub/Sub in 1 minute', required=True, type=float)
#    args = parser.parse_args()
#    # create Pub/Sub notification topic
#    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
#    psclient = pubsub.Client()
#    topic = psclient.topic(TOPIC)
#    if not topic.exists():
#       logging.info('Creating pub/sub topic {}'.format(TOPIC))
#       topic.create()
#    else:
#       logging.info('Reusing pub/sub topic {}'.format(TOPIC))
#
#    # notify about each line in the input file
#    programStartTime = datetime.datetime.utcnow()
#    with gzip.open(INPUT, 'rb') as ifp:
#       header = ifp.readline()  # skip header
#       firstObsTime = peek_timestamp(ifp)
#       logging.info('Sending sensor data from {}'.format(firstObsTime))
#       simulate(topic, ifp, firstObsTime, programStartTime, args.speedFactor)
