stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

#! << --- Primera_forma
def precio(d):
   return stock_prices[d-1]

def maximo(d1,d2):
    return max(stock_prices[d1-1:d2])
    '''maximo=None 
    for i in range(d1,d2+1):
        if maximo is None or stock_prices[i] > maximo:
            maximo=stock_prices[i]
    return maximo'''

def minimo(d1,d2):
    return min(stock_prices[d1-1:d2])
    '''min=None 
    for i in range(d1,d2+1):
        if min is None or stock_prices[i] < min:
            min=stock_prices[i]
    return minimo'''

print(precio(3))
print(minimo(5,10))
print(maximo(1,15))

#! << --- Segunda_Forma --->>

def price_at(i):
  return stock_prices[i-1]

def max_price(a, b):
  mx = 0
  for i in range(a, b + 1):
    mx = max(mx, price_at(i))
  return mx

def min_price(a, b):
  mn = price_at(a)
  for i in range(a, b + 1):
    mn = min(mn, price_at(i))
  return mn
print("-------------")
print(price_at(3))
print(min_price(5, 10))
print(max_price(1, 15))
