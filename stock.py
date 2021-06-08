from nsetools import Nse
import sys

ns = Nse()
args = sys.argv
args.remove(args[0])

if len(args) == 0:
    print("Enter stock name")
else:
    for item in args:
        stock = ns.get_quote(item)
        if ns.is_valid_code(item) == True:
            print("====================")
            print(f"Company Name: {stock['companyName']}")
            print(f"Last Price: {stock['lastPrice']}")
            print(f"Day High: {stock['dayHigh']}")
            print(f"52wk High: {stock['high52']}")
            print(f"52wk Low: {stock['low52']}")
            print("====================")
        else:
            print(f"{item} stock doesnt exist")



    
    
