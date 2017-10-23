import v20
class StreamFXPrices(object):

    def __init__(self,hostname,account_id,access_token,instruments,port):

        self.hostname = hostname
        self.access_token = access_token
        self.account_id = account_id
        self.instruments = instruments
        self.port = port

    def connect_to_stream(self):
        try:
            api = v20.Context(
                self.hostname,
                self.port,
                token=self.access_token
            )
            return api
        except Exception as e:
            print ('An error acorred in the api: ' + str(e))

    def stream_to_queue(self, api, account_id, instruments):
        response = api.pricing.stream(
            account_id,
            snapshot=True,
            instruments=instruments)
        return response


