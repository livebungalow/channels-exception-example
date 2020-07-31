from channels.routing import ChannelNameRouter, ProtocolTypeRouter
import app.consumers

channels = {
    "less-broken-consumer": app.consumers.LessBrokenConsumer,
    "broken-consumer": app.consumers.BrokenConsumer,
}

application = ProtocolTypeRouter({"channel": ChannelNameRouter(channels)})
