from aiohttp import web, ClientSession
from functools import partial
from modules.helpers import pprint
import logging



logger = logging.getLogger(__name__)


class WebServer:
    """
    Listens on a port for incoming webhook POST requests
    """
    _application = None
    _port        = None
    # _processors  = None

    def __init__(self, port: int=8080):
        self._port        = port
        self._application = web.Application(logger=logger)
        # self._processors  = {}
        # self._application.add_routes(routes=[web.post("/*", self.webhook_request)])

    def register_webhook_for(self, webhook: str, destination: str, processor: object):
        """
        Register local webhook URL to forward it processed into destination
        """
        function = partial(self.webhook_request, processor=processor, destination=destination)
        route = web.post(webhook, function)
        self._application.add_routes(routes=[route])

        # if webhook in self._processors:
        #     raise ValueError("The '{}' webhook is already registered".format(webhook))
        # self._processors[webhook] = processor
        # route = web.post(webhook, self.webhook_request)
        # self._application.add_routes(routes=[route])

    # async def webhook_request(self, request):
    #     """
    #     Processing webhooks
    #     """
    #     print(request)
    #     pprint(request, "REQUEST")
    #
    #     print(self._processors[request.path](request))
    #     return web.Response(text="Hello, world")

    async def webhook_request(self, request, processor, destination: str):
        """
        Processing webhooks
        """
        print(processor)
        print(request)
        pprint(request, "REQUEST")
        try:
            data = await request.read()
        except Exception as err:
            print("Failed to read request data: {}".format(err))
            data = {
                "title": "Failed to process incoming webhook",
                "text": str(request)
            }
            print("--------- FAILURE")
            await self.forward_message(data=data, destination=destination)
            return web.Response(text="Failure during processing step")
        # data =
        # print(data)
        #

        try:
            result = await processor(data)
        except Exception as err:
            print("--------- FAILURE")
            result = {
                "title": "Failed to parse JSON data that came to webhook",
                "text": "Error: {}\n\nData: {}".format(err, data)
            }
        print("--------- READY: {}".format(result))
        result = await self.forward_message(data=result, destination=destination)
        return web.Response(text=result)

    async def forward_message(self, data: dict, destination: str):
        """
        Send message to Teams webhook address
        """

        print("FORWARD: {} to {}".format(data, destination))
        async with ClientSession() as session:
            async with session.post(url=destination, data=str(data)) as resp:
                pprint(resp, "TEAMS ANSWER")
                print(resp.status)
                print(await resp.text())
        return "OK"

    def run(self):
        print("Starting")
        web.run_app(
            app  = self._application,
            port = self._port
        )
