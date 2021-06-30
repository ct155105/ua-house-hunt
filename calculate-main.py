import pandas as pd
from timeit import default_timer as timer
from county_services.oh import franklin as fk
from models import linear_ai 
from ds_helpers import data_science_helpers as ds


start = timer()
df = pd.read_csv('data/oh/franklin/Parcel_Boundaries.csv')
end = timer()
print(end - start)

df = fk.get_neighborhood(df,'Upper Arlington')
df = fk.get_resi(df)

#attic column
df = fk.append_attic_cd(df)
# ds.get_plot_and_scatter_image(df,'attic_cd',fk.get_tax_value_column(),'_temp/helloworld.png')
ds.get_plot_and_scatter_image(df,'ACRES',fk.get_tax_value_column(),'_temp/helloworld.png')

ai = linear_ai.Linear_AI(df, fk.get_tax_value_column())

print('test')

#KENSINGTON ONLY
# ken_df = ua_df[ua_df['SITEADDRESS'].str.contains('SOUTHWAY',na=False)][['PARCELID','SALEDATE','SITEADDRESS','SALEPRICE']]

#TRANSACTIONS
# tran_df = pd.read_csv('Property_Sales_Transactions.csv')
# ua_tran_df = tran_df[tran_df['CVTTXCD'] == 70]

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

