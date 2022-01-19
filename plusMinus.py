def plusMinus(arr):
    positive_counter = 0
    negative_counter = 0
    zero_counter = 0
    # 
    for num in arr:
        if(num > 0):
            positive_counter = positive_counter + 1
        elif(num < 0):
            negative_counter = negative_counter + 1
        else:
            zero_counter = zero_counter + 1
    # 
    print("{:.6f}".format(positive_counter/len(arr)))
    print("{:.6f}".format(negative_counter/len(arr)))
    print("{:.6f}".format(zero_counter/len(arr)))

plusMinus([1,1,0,-1,-1])