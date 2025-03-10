from pandas import (DataFrame, to_datetime)

from .data import (
    eligible_or_not,
    eligible,
    to_be_served,
    served
)






#screended
screened_FY18 = eligible_or_not[(eligible_or_not.interview_date >="2017-10-01") & (eligible_or_not.interview_date <="2018-09-30")]
screened_FY19 = eligible_or_not[(eligible_or_not.interview_date >="2018-10-01") & (eligible_or_not.interview_date <="2019-09-30")]
screened_FY20 = eligible_or_not[(eligible_or_not.interview_date >="2019-10-01") & (eligible_or_not.interview_date <="2020-09-30")]
screened_FY21 = eligible_or_not[(eligible_or_not.interview_date >="2020-10-01") & (eligible_or_not.interview_date <="2021-09-30")]
screened_FY22 = eligible_or_not[(eligible_or_not.interview_date >="2021-10-01") & (eligible_or_not.interview_date <="2022-09-30")]
screened_FY23 = eligible_or_not[(eligible_or_not.interview_date >="2022-10-01") & (eligible_or_not.interview_date <="2023-09-30")]
screened_FY24 = eligible_or_not[(eligible_or_not.interview_date >="2023-10-01") & (eligible_or_not.interview_date <="2024-09-30")]
screened_FY25 = eligible_or_not[(eligible_or_not.interview_date >="2024-10-01") & (eligible_or_not.interview_date <="2025-09-30")]
SCREENED = DataFrame(
  {
    "FY18":[screened_FY18.shape[0]],
    "FY19":[screened_FY19.shape[0]],
    "FY20":[screened_FY20.shape[0]],
    "FY21":[screened_FY21.shape[0]],
    "FY22":[screened_FY22.shape[0]],
    "FY23":[screened_FY23.shape[0]],
    "FY24":[screened_FY24.shape[0]],
    "FY25":[screened_FY25.shape[0]]
  }
)

# eligible
eligible_FY18 = eligible[(eligible.interview_date >="2017-10-01") & (eligible.interview_date <="2018-09-30")]
eligible_FY19 = eligible[(eligible.interview_date >="2018-10-01") & (eligible.interview_date <="2019-09-30")]
eligible_FY20 = eligible[(eligible.interview_date >="2019-10-01") & (eligible.interview_date <="2020-09-30")]
eligible_FY21 = eligible[(eligible.interview_date >="2020-10-01") & (eligible.interview_date <="2021-09-30")]
eligible_FY22 = eligible[(eligible.interview_date >="2021-10-01") & (eligible.interview_date <="2022-09-30")]
eligible_FY23 = eligible[(eligible.interview_date >="2022-10-01") & (eligible.interview_date <="2023-09-30")]
eligible_FY24 = eligible[(eligible.interview_date >="2023-10-01") & (eligible.interview_date <="2024-09-30")]
eligible_FY25 = eligible[(eligible.interview_date >="2024-10-01") & (eligible.interview_date <="2025-09-30")]
ELIGIBLE = DataFrame(
  {
    "FY18":[eligible_FY18.shape[0]],
    "FY19":[eligible_FY19.shape[0]],
    "FY20":[eligible_FY20.shape[0]],
    "FY21":[eligible_FY21.shape[0]],
    "FY22":[eligible_FY22.shape[0]],
    "FY23":[eligible_FY23.shape[0]],
    "FY24":[eligible_FY24.shape[0]],
    "FY25":[eligible_FY25.shape[0]]
  }
)

#to be served
to_be_served_FY18 = to_be_served[(to_be_served.interview_date >="2017-10-01") & (to_be_served.interview_date <="2018-09-30")]
to_be_served_FY19 = to_be_served[(to_be_served.interview_date >="2018-10-01") & (to_be_served.interview_date <="2019-09-30")]
to_be_served_FY20 = to_be_served[(to_be_served.interview_date >="2019-10-01") & (to_be_served.interview_date <="2020-09-30")]
to_be_served_FY21 = to_be_served[(to_be_served.interview_date >="2020-10-01") & (to_be_served.interview_date <="2021-09-30")]
to_be_served_FY22 = to_be_served[(to_be_served.interview_date >="2021-10-01") & (to_be_served.interview_date <="2022-09-30")]
to_be_served_FY23 = to_be_served[(to_be_served.interview_date >="2022-10-01") & (to_be_served.interview_date <="2023-09-30")]
to_be_served_FY24 = to_be_served[(to_be_served.interview_date >="2023-10-01") & (to_be_served.interview_date <="2024-09-30")]
to_be_served_FY25 = to_be_served[(to_be_served.interview_date >="2024-10-01") & (to_be_served.interview_date <="2025-09-30")]
TOBESERVED = DataFrame(
  {
    "FY18":[to_be_served_FY18.shape[0]],
    "FY19":[to_be_served_FY19.shape[0]],
    "FY20":[to_be_served_FY20.shape[0]],
    "FY21":[to_be_served_FY21.shape[0]],
    "FY22":[to_be_served_FY22.shape[0]],
    "FY23":[to_be_served_FY23.shape[0]],
    "FY24":[to_be_served_FY24.shape[0]],
    "FY25":[to_be_served_FY25.shape[0]]
  }
)

TOBESERVEDFY23 = to_be_served_FY23.fillna(-1)
TOBESERVEDFY23.dob = to_datetime(TOBESERVEDFY23.dob, utc=True)
TOBESERVEDFY24 = to_be_served_FY24.fillna(-1)
TOBESERVEDFY24.dob = to_datetime(TOBESERVEDFY24.dob, utc=True)
TOBESERVEDFY25 = to_be_served_FY25.fillna(-1)
TOBESERVEDFY25.dob = to_datetime(TOBESERVEDFY25.dob, utc=True)

# served
served_FY18 = served[(served.interview_date >="2017-10-01") & (served.interview_date <="2018-09-30")]
served_FY19 = served[(served.interview_date >="2018-10-01") & (served.interview_date <="2019-09-30")]
served_FY20 = served[(served.interview_date >="2019-10-01") & (served.interview_date <="2020-09-30")]
served_FY21 = served[(served.interview_date >="2020-10-01") & (served.interview_date <="2021-09-30")]
served_FY22 = served[(served.interview_date >="2021-10-01") & (served.interview_date <="2022-09-30")]
served_FY23 = served[(served.interview_date >="2022-10-01") & (served.interview_date <="2023-09-30")]
served_FY24 = served[(served.interview_date >="2023-10-01") & (served.interview_date <="2024-09-30")]
served_FY25 = served[(served.interview_date >="2024-10-01") & (served.interview_date <="2025-09-30")]
SERVED = DataFrame(
  {
    "FY18":[served_FY18.shape[0]],
    "FY19":[served_FY19.shape[0]],
    "FY20":[served_FY20.shape[0]],
    "FY21":[served_FY21.shape[0]],
    "FY22":[served_FY22.shape[0]],
    "FY23":[served_FY23.shape[0]],
    "FY24":[served_FY24.shape[0]],
    "FY25":[served_FY25.shape[0]]
  }
)

# to be served per Quater
unserved_FY23 = to_be_served[(to_be_served.interview_date >="2022-10-01") & (to_be_served.interview_date <="2023-09-30")]
unserved_FY24 = to_be_served[(to_be_served.interview_date >="2023-10-01") & (to_be_served.interview_date <="2024-09-30")]
unserved_FY25 = to_be_served[(to_be_served.interview_date >="2024-10-01") & (to_be_served.interview_date <="2025-09-30")]


unserved_Q1FY24 = to_be_served[(to_be_served.interview_date >="2023-10-01") & (to_be_served.interview_date <="2023-12-31")]
unserved_Q2FY24 = to_be_served[(to_be_served.interview_date >="2024-01-01") & (to_be_served.interview_date <="2024-03-31")]
unserved_Q3FY24 = to_be_served[(to_be_served.interview_date >="2024-04-01") & (to_be_served.interview_date <="2024-06-30")]
unserved_Q4FY24 = to_be_served[(to_be_served.interview_date >="2024-07-01") & (to_be_served.interview_date <="2024-09-30")]




TOBESERVEDPERQUARTER = DataFrame.from_dict(
  {
    "unserved_FY25":[unserved_FY24.shape[0]],
    "unserved_Q1FY24":[unserved_Q1FY24.shape[0]],
    "unserved_Q2FY24":[unserved_Q2FY24.shape[0]],
    "unserved_Q3FY24":[unserved_Q3FY24.shape[0]],
    "unserved_Q4FY24":[unserved_Q4FY24.shape[0]]
  },
  orient='index',
  columns=["donnee"]
)



