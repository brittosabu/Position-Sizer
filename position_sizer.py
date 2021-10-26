import pandas as pd


def postiion_sizing(buy_price,stop_loss,max_loss):
    return int(max_loss/(buy_price-stop_loss))

def all_positions():
    return 0

def main():

    all_eqs = all_equities()
    print("Ticker of STOCK: ")
    nse_ticker = input()
    print("Name of stock is ",all_eqs[nse_ticker])

    print("Enter your entry amount: ")
    bp = float(input())
    print("Enter your Stop Loss: ")
    sl = float(input())
    print("Enter your Max Loss: ")
    ml = float(input())

    print(postiion_sizing(bp,sl,ml))

if __name__ == "__main__":
    main()