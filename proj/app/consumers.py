from channels.consumer import SyncConsumer
import logging

log = logging.getLogger(__name__)

class BrokenConsumer(SyncConsumer):
    def __init__(self, *args, **kwargs):
        raise Exception("example exception")

    def test_print(self, message):
        raise Exception("breakage")


class LessBrokenConsumer(SyncConsumer):
    def test_print(self, message):
        raise Exception("not so broken")
