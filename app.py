import logging
import inspect
print(inspect.getsource(logging))
# Finally, calling the basicConfig explicitly will resolve the issue.

import logging
logging.basicConfig()
logger = logging.getLogger('logger')
logger.warning('The system may break down')
from pusher import Pusher
import pysher
import json 
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


class laboratorioRedes():
    pusher = None
    channel = None
    clientPusher = None
    

    def main(self):
            self.initPusher()
            self.connectHandler()
            # while True:
            #     self.getInput()
        
    ''' This function initializes both the Http server Pusher as well as the clientPusher'''
    def initPusher(self):
        self.pusher = Pusher(app_id=os.getenv('PUSHER_APP_ID', None), key=os.getenv('PUSHER_APP_KEY', None), secret=os.getenv('PUSHER_APP_SECRET', None), cluster=os.getenv('PUSHER_APP_CLUSTER', None))
        self.clientPusher = pysher.Pusher(os.getenv('PUSHER_APP_KEY', None), os.getenv('PUSHER_APP_CLUSTER', None))
        # self.clientPusher.connection.bind('report-created', self.connectHandler)
        self.clientPusher.connect()

    ''' This function is called once pusher has successfully established a connection'''
    def connectHandler(self):
        self.channel = self.clientPusher.subscribe('newReport')
        self.channel.bind('report-created', self.pusherCallback)

    ''' This function is called once pusher receives a new event '''
    def pusherCallback(self, message):
        message = json.loads(message)
        if message['user'] and message['report'] :
            print(colored("{}: {}".format(message['user'], message['report']), "blue"))


if __name__ == "__main__":
    laboratorioRedes().main()