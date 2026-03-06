import yfinance as yf
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import turtle
from time import sleep
import requests
import io
import csv

def setup_turtle():
    screen = turtle.Screen()
    screen.setup(width=1000, height=500)
    screen.tracer(0, 0)

    drawer = turtle.Turtle()
    drawer.penup()

    drawer.hideturtle()
    drawer.speed(0)

    drawer.goto(-450, 240)

tickers = [
    "AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "GOOG", "META", "BRK-B", "TSLA", "AVGO",
    "LLY", "WMT", "JPM", "V", "XOM", "UNH", "MA", "ORCL", "COST", "HD",
    "PG", "NFLX", "JNJ", "ABBV", "CRM", "BAC", "KO", "CVX", "MRK", "ADBE",
    "AMD", "PEP", "TMO", "LIN", "WFC", "CSCO", "ACN", "MCD", "ABT", "DIS",
    "GE", "PM", "INTU", "TXN", "DHR", "CAT", "AXP", "VZ", "AMAT", "PLTR",
    "QCOM", "PFE", "UBER", "IBM", "UNP", "AMGN", "ISRG", "NOW", "LOW", "SPGI",
    "RTX", "HON", "COP", "NEE", "GS", "DELL", "BKNG", "T", "ELV", "SYK",
    "C", "TJX", "PGR", "LRCX", "VRTX", "MS", "LMT", "ETN", "BLK", "BSX",
    "BA", "REGN", "CI", "ADP", "MMC", "CB", "PLD", "PANW", "MDLZ", "ADI",
    "AMT", "SBUX", "GILD", "MU", "DE", "ZTS", "CIEN", "SYY", "MELI", "LRCX",
    "MO", "AEE", "AEP", "AIG", "AMP", "AME", "APH", "AON", "APA", "APO",
    "MMM", "AOS", "AES", "AFL", "A", "APD", "ABNB", "AKAM", "ALB", "ARE",
    "ALGN", "ALLE", "LNT", "ALL", "AMCR", "AMP", "AME", "AMG", "ANSS", "AOR",
    "APA", "APO", "AVY", "BALL", "BBWI", "BBY", "BDX", "BEN", "BF-B", "BG",
    "BIIB", "BIO", "BK", "BKR", "BLDR", "BMY", "BR", "BRO", "BWA", "BX",
    "BXP", "CAG", "CAH", "CARR", "CAT", "CBRE", "CCI", "CCL", "CDNS", "CDW",
    "CE", "CEG", "CF", "CFG", "CHD", "CHRW", "CHTR", "CI", "CINF", "CL",
    "CLX", "CMA", "CMCSA", "CME", "CMG", "CMI", "CMS", "CNC", "CNP", "COF",
    "CPAY", "CPB", "CPRT", "CPT", "CRL", "CTAS", "CTRA", "CTSH", "CTVA", "CVS",
    "D", "DAL", "DAY", "DD", "DE", "DECK", "DFS", "DG", "DGX", "DHI",
    "DHR", "DISH", "DLTR", "DOC", "DOV", "DOW", "DPZ", "DRI", "DTE", "DUK",
    "DVA", "DVN", "DXCM", "EA", "EBAY", "ECL", "ED", "EFX", "EG", "EIX",
    "EL", "EMN", "EMR", "ENPH", "EOG", "EPAM", "EQIX", "EQR", "EQT", "ERIE",
    "ES", "ESS", "ETN", "ETR", "ETSY", "EVRG", "EW", "EXC", "EXPD", "EXPE",
    "EXR", "F", "FANG", "FAST", "FCX", "FDS", "FDX", "FE", "FFIV", "FI",
    "FICO", "FIS", "FITB", "FMC", "FOXA", "FOX", "FRT", "FSLR", "FTNT", "FTV",
    "GD", "GDDY", "GEHC", "GEN", "GEV", "GH", "GL", "GLW", "GM", "GNRC",
    "GPC", "GPK", "GRMN", "GWW", "HAL", "HAS", "HBAN", "HCA", "HCP", "HES",
    "HIG", "HII", "HLT", "HOLX", "HRL", "HSIC", "HST", "HSY", "HUM", "HWM",
    "IBM", "ICE", "IDXX", "IEX", "IFF", "ILMN", "INCY", "INTC", "IP", "IPG",
    "IQV", "IR", "IRM", "IT", "ITW", "IVZ", "J", "JBHT", "JBL", "JKHY",
    "K", "KDP", "KEY", "KEYS", "KHC", "KIM", "KLAC", "KMB", "KMI", "KMX",
    "KR", "KUB", "L", "LDOS", "LEN", "LH", "LHX", "LKQ", "LLY", "LRCX",
    "LULU", "LUV", "LVS", "LW", "LYB", "LYV", "M", "MAA", "MAR", "MAS",
    "PAYC", "PAYX", "PCAR", "PCG", "PEAK", "PEG", "PENN", "PFE", "PFG", "PG",
    "PGR", "PH", "PHM", "PKG", "PKI", "PLD", "PLTR", "PM", "PNC", "PNR",
    "PNW", "POOL", "PPG", "PPL", "PRU", "PSA", "PSX", "PTC", "PWR", "PXD",
    "PYPL", "QCOM", "QRVO", "RCL", "RE", "REG", "REGN", "RF", "RHI", "RJF",
    "RL", "RMD", "ROK", "ROL", "ROP", "ROST", "RSG", "RTX", "RVTY", "SBAC",
    "SBUX", "SCHW", "SHW", "SJM", "SLB", "SNA", "SNPS", "SO", "SPG", "SPGI",
    "SRE", "STE", "STT", "STX", "STZ", "SWK", "SWKS", "SYF", "SYK", "SYY",
    "T", "TAP", "TDG", "TDY", "TECH", "TEL", "TER", "TFC", "TFX", "TGT",
    "TJX", "TMO", "TMUS", "TPR", "TRGP", "TRMB", "TROW", "TRV", "TSCO", "TSN",
    "TT", "TTWO", "TXN", "TXT", "TYL", "UAL", "UDR", "UHS", "ULTA", "UNM",
    "UNP", "UPS", "URI", "USB", "VFC", "VICI", "VLO", "VMC", "VNO", "VRSK",
    "VRSN", "VRTX", "VTR", "VTRS", "VZ", "WAB", "WAT", "WBA", "WBD", "WDC",
    "WEC", "WELL", "WES", "WFRD", "WHR", "WM", "WMB", "WST", "WTW", "WY",
    "WYNN", "XEL", "XLY", "XOM", "XRAY", "XYL", "YUM", "ZBH", "ZBRA", "ZTS"]

tickers = [t.replace('.', '-') for t in tickers]

def fetch_stocks_yfinance(tickers):
  print(f"Fetching data for {len(tickers)} stocks...")

  # Step 2: Download data for all tickers (last 1 day of data)
  # This returns a multi-index dataframe
  data = yf.download(tickers, period="2d", interval="1m", group_by='ticker')

  # Step 3: Extract Open and Current (Last) price
  results = []
  for ticker in tickers:
    try:
      # Get the dataframe for this specific ticker
      tick_data = data[ticker]

      # 'Open' is the first price of the day
      # 'Close' in the latest interval is the current price
      open_price = tick_data['Open'].iloc[0]
      current_price = tick_data['Close'].iloc[-1]

      results.append({
          "Ticker": ticker,
          "Open": round(open_price, 2),
          "Current": round(current_price, 2),
          "PrevClose": tick_data['Close'].iloc[-2]
      })
    except:
      # Skip tickers with missing data
      continue

    return results

def fetch_stocks_api(tickers):
    ticker_string = ",".join(tickers)
    url = f"https://stock-prices.on99.app/quotes?symbols={ticker_string}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # 1. The API returns a string. We use io.StringIO to make it act like a file
        # 2. We use csv.reader because it automatically handles commas inside quotes
        f = io.StringIO(response.text)
        reader = csv.reader(f)
        
        results = []
        for parts in reader:
            # Skip empty lines or malformed rows
            if not parts or len(parts) < 11: 
                continue
                
            try:
                # index 0: symbol
                # index 3: currentPrice
                # index 10: previousClosePrice
                ticker_symbol = parts[0]
                current_val = float(parts[3])
                prev_close_val = float(parts[10]) 

                results.append({
                    "Ticker": ticker_symbol,
                    "Current": current_val,
                    "PrevClose": prev_close_val
                })
            except (ValueError, IndexError):
                continue

        return results
    except Exception as e:
        print(f"Error fetching from API: {e}")
        return []

up = []
down = []

def percentage(item):
    return (item["Current"] / item["PrevClose"])

def calculate_up_down(results):
    for stock in results:
        if stock["Current"] > stock["PrevClose"]:
          up.append(stock)
        elif stock["Current"] < stock["PrevClose"]:
          down.append(stock)
      
    up.sort(key=percentage, reverse=True)
    down.sort(key=percentage, reverse=True)
      



count = 0
width_max = 40


def plot_up():
  global count, width_max
  for stock in up:
    drawer.begin_fill()
    drawer.color("green")

    for _ in range(4):
      drawer.forward(20)
      drawer.right(90)

    drawer.end_fill()
    drawer.penup()
    count += 1

    if count > width_max:
      drawer.right(90)
      drawer.forward(20)
      drawer.left(90)
      drawer.backward((count - 1) * 20)
      count = 0
    else:
      drawer.forward(20)


def plot_down():
  global count, width_max
  for stock in down:
    drawer.begin_fill()
    drawer.color("red")

    for _ in range(4):
      drawer.forward(20)
      drawer.right(90)

    drawer.end_fill()
    drawer.penup()
    count += 1

    if count > width_max:
      drawer.right(90)
      drawer.forward(20)
      drawer.left(90)
      drawer.backward((count - 1) * 20)
      count = 0
    else:
      drawer.forward(20)


def reset():
  global up, down, count
  up = []
  down = []

  count = 0

def reset_turtle():
  drawer.clear()
  drawer.penup()
  drawer.goto(-450, 240)
  drawer.setheading(0)  # Ensure it's facing East/Right


## -- HTML --

def create_html():
    global count, width_max
    
    html_start = """<html>
                    <head>
                    <meta http-equiv="refresh" content="2">
                    <style>
                    .green {
                    width: 20px;
                    height: 20px;
                    background-color: green;
                    display: inline-block;
                    }
                    .red {
                    width: 20px;
                    height: 20px;
                    background-color: red;
                    display: inline-block;
                    }
                    .space {
                    width: 20px;
                    height: 0;
                    }
                    p {
                    font-size: 6;
                    font-family: Helvetica, sans-serif;
                    text-align: center;
                    color: white;
                    }
                    </style></head>
                    <body>"""
    html_middle = ""
    html_end = "</body></html>"

    for stock in up:
        html_middle += f"<div class='green'><p>{stock["Ticker"]}<br>{round(((stock["Current"] / stock["PrevClose"]) - 1)*100)}%</p></div>" 
        count += 1

        if count > width_max:
          html_middle += "<div class='space'></div>"
          count = 0
      
    for stock in down:
        html_middle += f"<div class='red'><p>{stock["Ticker"]}<br>{round(((stock["Current"] / stock["PrevClose"]) - 1)*100)}%</p></div>" 
        count += 1
        
        if count > width_max:
          html_middle += "<div class='space'></div>"
          count = 0
          
          
    return html_start + html_middle + html_end



#setup_turtle()
while True:
  stocks = fetch_stocks_api(tickers)
  calculate_up_down(stocks)

  #plot_up()
  #plot_down()

  html = create_html()
  with open("index.html", "w") as f:
      f.write(html)

  #screen.update()
  sleep(2)

  reset()
  #reset_turtle()

