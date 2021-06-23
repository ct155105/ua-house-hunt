import pandas as pd
from timeit import default_timer as timer

start = timer()
full_df = pd.read_csv('Parcel_Boundaries.csv')
end = timer()
print(end - start)

#UA TAX CODE IS 070
ua_df = full_df[full_df['CVTTXCD'] == 70]

#KENSINGTON ONLY
ken_df = ua_df[ua_df['SITEADDRESS'].str.contains('SOUTHWAY',na=False)][['PARCELID','SALEDATE','SITEADDRESS','SALEPRICE']]

#TRANSACTIONS
tran_df = pd.read_csv('Property_Sales_Transactions.csv')
ua_tran_df = tran_df[tran_df['CVTTXCD'] == 70]

#GET PRICE BY
#FIND SQUARE FOOTAGE
#FIND NUMBER BEDROOMS
#FIND NUMBER BATHS
#STREET
#YEAR

#ShapeSTArea
#TOTVALUEBASE
#Price Per Square Foot
#ua_df['PPSF'] = ( ua_df['TOTVALUEBASE'] / ua_df['ShapeSTArea'] )

#Residential only
#ua_df_resi = ua_df[ua_df['BLDTYP'].str.contains('Dwelling',na=False)]

#to numpy
#import numpy as np
#np_array_x = ua_df_resi['ShapeSTArea'].to_numpy()
#np_array_y = ua_df_resi['TOTVALUEBASE'].to_numpy()

