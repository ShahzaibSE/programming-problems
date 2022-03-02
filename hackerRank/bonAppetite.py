# Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

# For example, assume the bill has the following prices: . Anna declines to eat item  which costs . If Brian calculates the bill correctly, Anna will pay . If he includes the cost of , he will calculate . In the second case, he should refund  to Anna.

# Function Description

# Complete the bonAppetit function in the editor below. It should print Bon Appetit if the bill is fairly split. Otherwise, it should print the integer amount of money that Brian owes Anna.

# bonAppetit has the following parameter(s):

# bill: an array of integers representing the cost of each item ordered
# k: an integer representing the zero-based index of the item Anna doesn't eat
# b: the amount of money that Anna contributed to the bill

def bonAppetit(bill, k, b):
    # Write your code here
    anna_bill = sum([bill[i] for i in range(len(bill)) if i != k]) // 2
    return 'Bon Appetit' if (anna_bill == b) else str(anna_bill - b)

# def bonAppetit(bill, k, b):
#     anna_bill = 0
#     for i in range(len(bill)):
#         if(i == k):
#             bill.remove(bill[k])
#     anna_bill = sum(bill) // 2
#     #     
#     if(anna_bill == b):
#         return 'Bon Appetit'
#     else:
#         return abs(anna_bill - b)


print(bonAppetit([2,4,6], 2, 10))