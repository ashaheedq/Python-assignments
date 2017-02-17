#
# ps7pr4.py (Problem Set 7, Problem 4)
#
# TT Securities
#
# Computer Science 111
#

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    print('(3) Find the average price')
    print('(4) Find the standard deviation')
    print('(5) Find the min and its day')
    print('(6) Find the max and its day')
    print('(7) Test a theshold')
    print('(8) Your TT investment plan')
    print('(9) Quit')
    print()

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    print('Day Prices')
    print('--- -----')
    for i in range(len(prices)):
        print('%3.0f' % i, '%5.2f' % prices[i])
        
def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your helper functions for options 3-8 below.
def average_price(prices):
    """ returns the average price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    total = 0
    length = len(prices)
    for i in range(length):
         total += prices[i]
    average = total/length
    return average

def standard_deviation(prices):
    """ returns the standard deviation in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    total = 0
    
    for i in prices:
        total += (i - average_price(prices))**2
        
    stndrdv = (total/len(prices))**0.5
    return stndrdv

def min_max(prices):
    """ returns the min and the max price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    minima = prices[0]
    maxima = prices[0]
    max_day = [maxima,0]
    min_day = [minima, 0]
    length = len(prices)
    
    for i in range(length):

        if prices[i] < minima:
            minima = prices[i]
            min_day = [minima, i]
        if prices[i] > maxima:
            maxima = prices[i]
            max_day = [maxima, i]
            
    max_min = [max_day, min_day]
    return max_min

def test_threshold(prices):
    """ ask the user to enter a threshold and use a loop to determine if there are any prices above that threshold,
        and print an appropriate message.
        input: prices is a list of 1 or more numbers.
    """
    threshold = int(input('Enter your threshold: '))
    for i in prices:
        if threshold > i:
            print('There are no prices over', threshold)
            return
        elif threshold < i:
            print('There is at least one price over', threshold)
            return

def diff(prices):
    """ use loops to find the best days on which to buy and sell the stock
        input: prices is a list of 1 or more numbers.
    """
    l2 = prices[1:]
    maxdiff = ((prices[-1])-(l2[-1]))
    pos1 = 0
    pos2 = 0
    
    for x in range(len(prices)):
        for y in range(len(l2)):
            
            d = (l2[y] - prices[x])
            if d > maxdiff:
                maxdiff = d
                pos1 = x
                pos2 = y + 1
                
    maxdiff = [maxdiff, [prices[pos1], pos1], [prices[pos2], pos2]]
    return maxdiff

    
def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 9:
            break
        elif choice < 9 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            average = average_price(prices)
            print('The average price is', '%3.1f' % average)
        elif choice == 4:
            standard = standard_deviation(prices)
            print('The standard deviation is', standard)
        elif choice == 5:
            minima = min_max(prices)
            print ('The min price is', minima[1][0], 'on day', minima[1][1])
        elif choice == 6:
            maxima = min_max(prices)
            print ('The max price is', maxima[0][0], 'on day', maxima[0][1])
        elif choice == 7:
            threshold = test_threshold(prices)
        elif choice == 8:
            maxdiff = diff(prices)
            print(' Buy on day', maxdiff[1][1], 'at price', maxdiff[1][0])
            print('Sell on day', maxdiff[2][1], 'at price', maxdiff[2][0])
            print('Total profit:', maxdiff[0])
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
