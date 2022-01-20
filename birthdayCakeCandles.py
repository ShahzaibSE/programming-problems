def birthdayCakeCandles(candles):
    candle_with_max_height = max(candles)
    max_candle_counter = 0
    for candle in candles:
        if(candle == candle_with_max_height):
            max_candle_counter += 1
    return max_candle_counter

print("Tallest candle: {}".format(birthdayCakeCandles([4,4,1,3])))