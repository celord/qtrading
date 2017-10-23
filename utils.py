def pricetoString(price):
    print ('{} {} {}/{}'.format(
        price.instrument,
        price.time,
        price.bids[0].price,
        price.asks[0].price,
    ))
