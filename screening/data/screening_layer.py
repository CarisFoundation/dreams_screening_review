from pandas import read_sql_query, to_datetime
from numpy import nan
from siuba import _
from ..db import SDATA, engine

# all recorded beneficiaires screened
sdata = read_sql_query(SDATA, engine, parse_dates=True)
engine.dispose()
sdata.replace(r'^\s*$', nan, regex=True, inplace=True)
sdata.code = sdata.code.fillna('---')
sdata.interview_date = sdata.loc[:, 'interview_date'].apply(to_datetime)
# screened
eligible_or_not =  sdata

# eligible
eligible = sdata[_.total >= 14]


# to be served
to_be_served = sdata[
    (_.code =="---")&
    (_.total>=14)    
]

# already served
served = sdata[
    (_.code!="---")&
    (_.total>=14)
]
