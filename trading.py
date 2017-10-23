from settings import ACCOUNT_ID, ACCESS_TOKEN,STREAM_DOMAIN,API_DOMAIN
from stream import StreamFXPrices
from utils import pricetoString

INSTRUMENTS = 'EUR_USD,GBP_USD'
PORT = '443'
prices = StreamFXPrices(STREAM_DOMAIN, ACCOUNT_ID,ACCESS_TOKEN, INSTRUMENTS, PORT)


api = prices.connect_to_stream()
response = prices.stream_to_queue(api,ACCOUNT_ID,INSTRUMENTS)
while True:
    for msg_type,msg in response.parts():
        if msg_type == 'pricing.PricingHeartbeat':
            pass
        if msg_type == 'pricing.Price':
            pricetoString(msg)



