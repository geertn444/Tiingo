import requests
import pandas as pd

yourtoken = '<INSERT YOUR TOKEN>'


def DataReader(ticker,d_start,d_end):

 #We are expecting DateTime type for input dates !! (just like original Pandas DataReader)
 
 d_end = d_end.strftime('%Y-%m-%d')
 d_start = d_start.strftime('%Y-%m-%d')
 #print d_start
 #print d_end
 
 headers = {
       'Content-Type': 'application/json',
       'Authorization' : 'Token ' + yourtoken
       }
 url = "https://api.tiingo.com/tiingo/daily/" + ticker + "/prices?startDate=" + d_start + "&endDate="+ d_end
 #requestResponse = requests.get(url,headers=headers)
 print url
 requestResponse = requests.get(url,headers=headers)
 #print requestResponse
 json_result = requestResponse.json()
 #print json_result


 
 #result = pd.read_json(json_result,orient='records')
 df = pd.DataFrame.from_records(json_result)
 
 #Check for existance of Adj Close column
 #If not, check for existance of Close column
 #If not -> throw error
 #If no Adj Close, but Close, copy Close to Adj close
 
  
 if not 'adjClose' in df.columns:
  if 'close' in df.columns:
   df['adjClose'] = df['close']
  else:
   print "Error: No Close information"
   return
   
 
 df['date']  = pd.to_datetime(df['date'])
 df = df.rename(columns={'date': 'Date', 'open': 'Open','adjClose':'Adj Close','volume':'Volume','high':'High','low':'Low','close':'Close'})
 a = df.set_index(['Date'])
 #print a
 return a

