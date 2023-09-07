total_days = input()
stock_price = list(map(int,input().split()))

def descending(stock_price):
    desc_ord = True
    for i in range(len(stock_price)-1):
        if stock_price[i] < stock_price[i+1]:
            desc_ord = False
    return(desc_ord)

desc_ord = descending(stock_price)
min_price = min(stock_price)
max_price = max(stock_price)
index_min = stock_price.index(min_price)
index_max = stock_price.index(max_price)
if desc_ord or (min_price == max_price):
    print(0)
else:
    if index_min < index_max:
        print(max_price-min_price)
    elif index_min > index_max and index_min < (len(stock_price)-1):
        frst_half = stock_price[:index_min]
        scnd_half = stock_price[(index_min + 1):]
        new_min_1 = min(frst_half)
        new_max_2 = max(scnd_half)
        profit1 = max_price - new_min_1
        profit2 = new_max_2 - min_price
        if profit1 > profit2:
            print(profit1)
        else:
            print(profit2)
    elif index_min == (len(stock_price)-1):
        stock_price.pop()
        new_min = min(stock_price)
        new_idx_min = stock_price.index(new_min)
        desc_ord = descending(stock_price)
        while new_idx_min == (len(stock_price)-1) and not desc_ord:
            stock_price.pop()
            new_min = min(stock_price)
            new_idx_min = stock_price.index(new_min)
            desc_ord = descending(stock_price)
        if new_idx_min < index_max:
            print(max_price - new_min)
        elif new_idx_min < (len(stock_price)-1):
            frst_half = stock_price[:new_idx_min]
            scnd_half = stock_price[(new_idx_min + 1):]
            new_min_1 = min(frst_half)
            new_max_2 = max(scnd_half)
            profit1 = max_price - new_min_1
            profit2 = new_max_2 - min_price
            if profit1 > profit2:
                print(profit1)
            else:
                print(profit2)
        elif desc_ord:
            print(0)