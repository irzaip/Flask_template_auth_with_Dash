import yfinance as yf
import pandas as pd
import time

lst = pd.read_csv('all_list.csv')
slist = list(lst['Kode']+".JK")

def full_download():
    for i, item in enumerate(slist):
        try:
            tick = yf.Ticker(str(slist[i]))
            da = tick.history(period="max")
            da.to_csv("./stock/"+ str(slist[i])+".csv")
            print("downloaded", str(slist[i]))
            time.sleep(3)
        except:
            print("Error loading:" , str(slist[i]))
    return print("Done loading")

def range_download(start="2020-08-09", end="2020-08-30"):
    for i, item in enumerate(slist):
        try:
            tick = yf.Ticker(str(slist[i]))
            da = tick.history(start=start, end=end)
            da.to_csv("./stock_new/"+ str(slist[i])+".csv")
            print("downloaded", str(slist[i]))
            time.sleep(3)
        except:
            print("Error loading:" , str(slist[i]))
    return print("Done loading")

def downloads():
    all = input("Download all? (Y/N): ")
    if all=="Y":
        full_download()
    else:
        start = str(input("Masukkan tanggal awal (YYYY-MM-DD): "))
        end = str(input("Masukkan tanggal akhir (YYYY-MM-DD): "))
        range_download(start=start,end=end)
    
if __name__ == "__main__":
    downloads()
    