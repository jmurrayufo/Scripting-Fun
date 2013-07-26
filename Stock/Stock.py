import urllib
import json
from pprint import pprint
import time
import datetime

def GetQuote( symbols ):
   symbols = FormatSymbolList( symbols )
   baseURL = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quote%20where%20symbol%20in%20(" + symbols + ")&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="
   content = urllib.urlopen(baseURL).read()
   return content

def FormatSymbolList( symbols ):
   if type( symbols ) == str :
      return "%22"+symbols.upper()+"%22"
   return ','.join("%22" + item.upper() + "%22" for item in symbols)

def FloatToDollars( amount ):
   return "$" + '{:,.2F}'.format(amount)

def IsStockExchOpen( ):
   clock = time.localtime()
   if( clock.tm_hour < 7 ):
      return False
   elif( clock.tm_hour == 7 and clock.tm_min < 30 ):
      return False
   elif( clock.tm_hour >= 14 ):
      return False
   else:
      return True

def SleepUntilOpen( ):
   print "Time is",datetime.datetime.now().replace( microsecond = 0 )
   if( time.localtime( ).tm_hour >= 14 ):
      midnight = ( datetime.datetime.now( ) + datetime.timedelta( days = 1 )).replace( hour = 0, minute = 0, second = 0, microsecond = 0)
      wait = midnight - datetime.datetime.now( )
      print "Sleep for", wait/2
      time.sleep( wait.total_seconds( )/2 )
      # Sleep Until midnight
   if( time.localtime().tm_hour < 7 ):
      openTime = datetime.datetime.now().replace( hour = 7, minute = 0, second = 0 )
      wait = openTime - datetime.datetime.now()
      print "Sleep for", wait/2
      # Sleep until 7 AM
      time.sleep( wait.total_seconds( )/2 )

def NextTime( minutes = None ):
   now = datetime.datetime.now()
   dMinutes = ( minutes - ( now.minute % minutes ) )
   targetTime = now + datetime.timedelta( minutes = dMinutes )
   targetTime = targetTime.replace( second = 0, microsecond = 0)
   return ( targetTime - now ).total_seconds()


lastPrice = None
while(1):
   if( not IsStockExchOpen() ):
      print "\nStock Exchange is Closed...."
      SleepUntilOpen()
      continue
   data = GetQuote(["stx"])
   data = json.loads(data)
   stxPrice = float(data['query']['results']['quote']['LastTradePriceOnly'])
   if( not lastPrice ):
      lastPrice = stxPrice
   # shares = 3000 / 28.62
   # print shares
   now = time.localtime()
   if( stxPrice > lastPrice ):
      change = "+"
   if( stxPrice == lastPrice ):
      change = "="
   if( stxPrice < lastPrice ):
      change = "-"
   print "t: %02d:%02d   Now: %6s%s   Profit: %9s   PerShare: %s (%.2f%%)"%(
         now.tm_hour,
         now.tm_min,
         FloatToDollars( stxPrice ), 
         change,
         FloatToDollars( (stxPrice - 28.62) * 104 ),
         FloatToDollars( stxPrice - 28.62 ),
         ( stxPrice / 28.62 - 1 ) * 100
         )
   lastPrice = stxPrice
   time.sleep( NextTime( 5 ) )