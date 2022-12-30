import datetime
import pandas_datareader.data as web
import pandas as pd

start = datetime.datetime(2022, 1, 1)
end = datetime.datetime(2022, 12, 30)
sotck = web.DataReader("588080.ss", "yahoo", start, end)
print(sotck.head(5))
print(sotck.tail(5))
