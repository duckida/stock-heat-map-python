import yfinance as yf
import pandas as pd
import turtle
from time import sleep
import requests

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
    "A", "AAPL", "ABBV", "ABNB", "ABT", "ACN", "ADBE", "ADI", "ADM", "ADP",
    "ADSK", "AEE", "AEP", "AES", "AFL", "AIG", "AIZ", "AJG", "AKAM", "ALB",
    "ALGN", "ALL", "ALLE", "AMAT", "AMCR", "AMD", "AME", "AMGN", "AMP", "AMT",
    "AMZN", "ANET", "ANSS", "AON", "AOS", "APA", "APD", "APH", "APO", "APP",
    "ARE", "ATO", "AVB", "AVGO", "AVY", "AWK", "AXON", "AXP", "AZO", "BA",
    "BAC", "BALL", "BAX", "BBWI", "BBY", "BDX", "BEN", "BF.B", "BG", "BIIB",
    "BIO", "BK", "BKNG", "BKR", "BLK", "BLDR", "BMY", "BR", "BRK.B", "BSX",
    "BWA", "BX", "C", "CAG", "CAH", "CARR", "CAT", "CB", "CBOE", "CBRE", "CCI",
    "CCL", "CDNS", "CDW", "CE", "CEG", "CF", "CFG", "CHD", "CHRW", "CHTR",
    "CI", "CINF", "CL", "CLX", "CMA", "CMCSA", "CME", "CMG", "CMI", "CMS",
    "CNC", "CNP", "COF", "COIN", "COO", "COP", "COST", "CPAY", "CPB", "CPRT",
    "CPT", "CRL", "CRM", "CRWD", "CSCO", "CSGP", "CSX", "CTAS", "CTRA", "CTSH",
    "CTVA", "CVS", "CVX", "D", "DAL", "DASH", "DAY", "DD", "DE", "DELL", "DFS",
    "DG", "DGX", "DHI", "DHR", "DIS", "DLR", "DLTR", "DOC", "DOV", "DOW",
    "DPZ", "DRI", "DTE", "DUK", "DVA", "DVN", "DXCM", "EA", "EBAY", "ECL",
    "ED", "EFX", "EG", "EIX", "EL", "ELV", "EME", "EMN", "EMR", "ENPH", "EOG",
    "EPAM", "EQIX", "EQT", "ERIE", "ES", "ESS", "ETN", "ETR", "ETSY", "EVRG",
    "EW", "EXC", "EXPD", "EXPE", "EXR", "F", "FANG", "FAST", "FCX", "FDS",
    "FDX", "FE", "FFIV", "FI", "FICO", "FIS", "FITB", "FMC", "FOX", "FOXA",
    "FRT", "FSLR", "FTNT", "FTV", "GD", "GE", "GEV", "GILD", "GIS", "GL",
    "GLW", "GM", "GNRC", "GOOG", "GOOGL", "GPC", "GPN", "GRMN", "GS", "GWRE",
    "GWW", "HAL", "HAS", "HBAN", "HCA", "HD", "HIG", "HII", "HLT", "HOLX",
    "HON", "HOOD", "HPE", "HPQ", "HRL", "HSIC", "HST", "HSY", "HUBB", "HUM",
    "HWM", "IBM", "IBKR", "ICE", "IDXX", "IEX", "IFF", "INTC", "INTU", "INVH",
    "IP", "IPG", "IQV", "IR", "IRM", "ISRG", "IT", "ITW", "IVZ", "J", "JBHT",
    "JBL", "JCI", "JKHY", "JNJ", "JNPR", "JPM", "K", "KDP", "KEY", "KEYS",
    "KHC", "KIM", "KKR", "KLAC", "KMB", "KMI", "KMX", "KO", "KR", "KVUE", "L",
    "LDOS", "LEN", "LH", "LHX", "LIN", "LKQ", "LLY", "LMT", "LNT", "LOW",
    "LRCX", "LULU", "LUV", "LVS", "LW", "LYB", "LYV", "MA", "MAA", "MAR",
    "MAS", "MCD", "MCHP", "MCK", "MCO", "MDLZ", "MDT", "MET", "META", "MGM",
    "MHK", "MKC", "MKTX", "MLM", "MMC", "MMM", "MNST", "MO", "MOH", "MOS",
    "MPC", "MPWR", "MRK", "MRNA", "MS", "MSI", "MSFT", "MTB", "MTD", "MU",
    "NCLH", "NDAQ", "NDSN", "NEE", "NEM", "NFLX", "NI", "NKE", "NOC", "NOW",
    "NRG", "NSC", "NTAP", "NTRS", "NUE", "NVDA", "NVR", "NWS", "NWSA", "NXPI",
    "O", "ODFL", "OKE", "OMC", "ON", "ORCL", "ORLY", "OTIS", "OXY", "PANW",
    "PARA", "PAYC", "PAYX", "PCAR", "PCG", "PEG", "PEP", "PFE", "PFG", "PG",
    "PGR", "PH", "PHM", "PKG", "PLD", "PLTR", "PM", "PNC", "PNR", "PNW",
    "POOL", "PPG", "PPL", "PRU", "PSA", "PSX", "PTC", "PWR", "PYPL", "QCOM",
    "QRVO", "RCL", "REG", "REGN", "RF", "RJF", "RL", "RMD", "ROK", "ROL",
    "ROP", "ROST", "RSG", "RTX", "RVTY", "SBAC", "SBUX", "SCHW", "SHW", "SJM",
    "SLB", "SMCI", "SNA", "SNPS", "SO", "SPG", "SPGI", "SRE", "STE", "STT",
    "STX", "STZ", "SWK", "SWKS", "SYK", "SYY", "T", "TAP", "TDG", "TDY",
    "TECH", "TEL", "TER", "TFC", "TFX", "TGT", "TJX", "TMO", "TMUS", "TROW",
    "TRV", "TSCO", "TSLA", "TSN", "TT", "TTWO", "TXN", "TXT", "TYL", "UAL",
    "UBER", "UDR", "UHS", "ULTA", "UNH", "UNP", "UPS", "URI", "USB", "V",
    "VICI", "VLO", "VMC", "VRSK", "VRSN", "VRTX", "VST", "VTR", "VZ", "WAB",
    "WAT", "WBA", "WBD", "WDC", "WDAY", "WEC", "WELL", "WFC", "WHR", "WM",
    "WMB", "WMT", "WRB", "WST", "WTW", "WY", "WYNN", "XEL", "XOM", "XYL",
    "YUM", "ZBH", "ZBRA", "ZTS"
]
tickers = [t.replace('.', '-') for t in tickers]


def fetch_stocks_yfinance(tickers):
  print(f"Fetching data for {len(tickers)} stocks...")

  # Step 2: Download data for all tickers (last 1 day of data)
  # This returns a multi-index dataframe
  data = yf.download(tickers, period="1d", interval="1m", group_by='ticker')

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
          "Current": round(current_price, 2)
      })
    except:
      # Skip tickers with missing data
      continue

    return results


def fetch_stocks_api(tickers):
  ticker_string = ",".join(tickers)
  url = f"https://stock-prices.on99.app/quotes?symbols={ticker_string}"
  try:
    # Step 1: Fetch the raw data
    response = requests.get(url)
    response.raise_for_status()  # Check for errors (404, 500, etc.)
    raw_data = response.text

    # Step 2: Extract the rows
    # We split by lines and ignore the header line starting with "quotes["
    lines = [
        line.strip() for line in raw_data.strip().split('\n')
        if line and not line.startswith('quotes[')
    ]

    results = []
    for line in lines:
      # SKIP the header line that defines the columns
      if line.startswith("quotes[") or "currentPrice" in line:
        continue

      # Split the line by comma
      parts = line.split(',')

      # According to your data:
      # Index 0: Ticker (AAPL)
      # Index 3: currentPrice (264.58)
      # Index 8: openPrice (258.955)

      try:
        ticker = parts[0]
        current_val = float(parts[3])
        open_val = float(parts[8])

        results.append({
            "Ticker": ticker,
            "Open": round(open_val, 2),
            "Current": round(current_val, 2)
        })
      except (ValueError, IndexError):
        # This skips the line if a value is 'null' or missing
        continue

    return results

  except Exception as e:
    print(f"Error fetching data: {e}")
    return []


up = []
down = []


def calculate_up_down(results):
  for stock in results:
    if stock["Current"] > stock["Open"]:
      up.append(stock)
    elif stock["Current"] < stock["Open"]:
      down.append(stock)


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
                    </style></head>
                    <body>"""
    html_middle = ""
    html_end = "</body></html>"

    for stock in up:
        html_middle += "<div class='green'></div>"
        count += 1

        if count > width_max:
          html_middle += "<div class='space'></div>"
          count = 0
      
    for stock in down:
        html_middle += ("<div class='red'></div>")
        count += 1
        
        if count > width_max:
          html_middle += ("<div class='space'></div>")
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

