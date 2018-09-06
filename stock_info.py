#Reference: https://addisonlynch.github.io/iexfinance/stable/usage.html
from iexfinance import Stock

myList = ['DATA','CRM','SPLK','WDAY','HLT','BLL','MFGP','WEX',
	  'DXC', 'MSFT','AAPL','SBUX','NKE','T','GOOGL','FB',
	  'TWTR','AKAM','LLNW','GD','LDOS','BA','MSTR','BMCH',
	  'CTSH','WIT','OTEX', 'SPOT', 'AYX', 'SATS', 'MAR',
	  'TENB','CBLK','ZS', 'GCI', 'VRNT']

# Create separate Dictionaries for 'Open' and 'Close' prices
qOpen = {}
qClose = {}
qNews = {}      # Attributes={datetime, headline, source, url, summary, related}
for x in myList:
	print ('Retrieving quote info for %s...' % x)
	theQuote = Stock(x)             #x, output_format='pandas')

	resOpen = theQuote.get_open()
	resClose = theQuote.get_close()  #get_quote(filter_=['ytdChange', 'open', 'close', 'avgTotalVolume']) 
	qOpen[x] = resOpen
	qClose[x] = resClose
	newsList = theQuote.get_news(last=7)

print ('')
print ('Formatting output...')
for key in qOpen.keys():
	val = qOpen[key]
	print("\t Close:", qClose[key])
	#print("Key: ", key, "\t Open:", val, "\t Close:", qClose[key]) #, "\t News:", qNews[key])
	
print('')
del qOpen
del qClose
#End
