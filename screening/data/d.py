from pandas import read_sql_query, to_datetime
from numpy import nan
# Removed: from siuba import _
from ..db import SDATA, engine

from sqlalchemy import text

# all recorded beneficiaires screened
sdata = read_sql_query(text(SDATA), engine.connect(), parse_dates=True)
engine.dispose()
sdata.replace(r'^\s*$', nan, regex=True, inplace=True)
sdata.code = sdata.code.fillna('---')
sdata.interview_date = sdata.loc[:, 'interview_date'].apply(to_datetime)
# screened
eligible_or_not = sdata

# eligible
eligible = sdata[
    (sdata['total'] >= 14) &
    (sdata['age_range'] != "not_valid_age") &
    (sdata['age_range'] != "25-29")
]

# to be served
to_be_served = sdata[
    (sdata['code'] == "---") &
    (sdata['total'] >= 14) &
    (sdata['age_range'] != "not_valid_age") &
    (sdata['age_range'] != "25-29")
]

# already served
served = sdata[
    (sdata['code'] != "---") &
    (sdata['total'] >= 14) &
    (sdata['age_range'] != "not_valid_age") &
    (sdata['age_range'] != "25-29")
]

""" ecommune = [
    'kenscoff',
     'petion_ville',
     'port-au-prince',
     'tabarre',
     'cit_soleil',
     'carrefour',
     'croix-des-bouquets',
     'ption-ville',
     'pointe--raquette',
    'les_anglais',
    'jrmie',
    'chantal',
    'logne',
    'cabaret',
    'grand-gove',
    'petit-gove',
    'chambellan',
    'cayes-jacmel', 
    'cavaillon',
    'fonds-verrettes',
    'petite-rivire-de-nippes',
    'bainet',
    'torbeck',
    'vallires',
    'anse--galets',
    'tiburon',
    'copy-1-of-ganthier',
    'les_cayes',
    'port--piment',
    'port-salut',

]
eligible = eligible[~eligible.commune.isin(ecommune)]
eligible_or_not = eligible_or_not[~eligible_or_not.commune.isin(ecommune)]
served = served[~served.commune.isin(ecommune)]
to_be_served = to_be_served[~to_be_served.commune.isin(ecommune)] """