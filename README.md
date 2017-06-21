# Tiingo
Python module to use Tiingo as replacement for Pandas DataReader with Yahoo

Since stupid Yahoo/Verizon stopped their Stock API last month without notice, we can't use Pandas DataReader procedure anymore to get quotes data.
This simple module is meant to be a drop-in replacement and uses Tiingo as provider: https://www.tiingo.com/

It is free (? for now). You need to register and then you get an API key which needs to be inserted into the module.

NOTE: my module is NOT foolproof or dummy proof, it has bugs for sure but it works for me. I don't need intraday data, just historical close data. Your mileage may vary.

NOTE: I did notice that the data provided by Tiingo is not as reliable as Yahoo. For example, after a first run, some tickers returned less data (less days) as Yahoo and not even all columns (sometimes Adj Close is missing, but if it is missing , it is copied from Close if that one exists)

To convert or fix a script:

BEFORE:<BR><BR>
 prices = web.DataReader(ticker, 'yahoo', d_start, d_end)
 
AFTER:<BR><BR>
 import tiingo
 
 prices = tiingo.DataReader(ticker, d_start, d_end)
 
 Get your scripts back up and running :-)
 NOTE: no more options supported today !
