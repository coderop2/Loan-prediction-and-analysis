from datetime import date
from nsepy import get_history
def drop_null(df):
    data=df.dropna()
def data(stock,indexx=False):
    if indexx:
        df = get_history(symbol='stock',
                   start=date(2014,5,1),
                   end=date(2016,4,30),index=True)
    else:
        df = get_history(symbol='stock',
                   start=date(2014,5,1),
                   end=date(2016,4,30))
    return df