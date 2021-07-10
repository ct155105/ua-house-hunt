import pandas as pd
from timeit import default_timer as timer
from county_services.oh import franklin as bll
from models import linear_ai 
from ds_helpers import linear_regression as ds
from df_helpers import df_filters as df_fil
from ct_math import algebra as alg
from matplotlib import pyplot as plt
from data_science_models.models.dimension import Dimension as Dim
from dal.oh import franklin as dal



start = timer()
# df = dal.get_tax()
end = timer()

df = bll.get_resi(bll.get_neighborhood(dal.get_tax(),'Upper Arlington'))
# df = bll.get_resi(df)

dim = Dim(df,'BUILDING',bll.get_tax_value_column())

print(end - start)

# start = timer()
# transaction_df = pd.read_csv('data/oh/franklin/Property_Sales_Transactions.csv')
# end = timer()
# print(end - start)
# transaction_df = bll.get_neighborhood(transaction_df,'Upper Arlington')
# transaction_df = bll.get_resi(transaction_df)

#inner join transactions and tax roll
# joined_df = pd.merge(transaction_df[["SalePrice",'SALEDATE','PARCELID']],df,on='PARCELID')
# joined_df = df_fil.remove_zeros(joined_df,'SalePrice')

# #attic column
# #TODO all columns transform to code
# df = fk.append_attic_cd(df)

# ai = linear_ai.Linear_AI(df, fk.get_tax_value_column())

# #GET THE MODELED ASSESSED VALUE 
# #STORE VALUE IN PD SERIES
# ##STARTING BY ITERATING OVER EACH COLUMN INDIVIDUALLY UNTIL PROCESS IS BUILT TO CLEAN THE DATA
# properties = joined_df.to_dict('index')
# modeled_assessed_value = pd.Series()
# i=0
# for row in properties.keys():
#     print(i)
#     i+=1
#     results = []
#     for key in properties[row].keys():
#         try:
#             predicted = ds.get_predicted_house_price({key: properties[row][key]},vars(ai))
#             if predicted > 0:
#                 results.append(pd.Series([predicted], index=[row]))
#         except Exception as e:
#             pass
#     avg = alg.get_average_of_list_values(results)
#     modeled_assessed_value = modeled_assessed_value.append(pd.Series([avg], index=[row]))

# #APPEND THE MODELED ASSESSED VALUE
# joined_df = joined_df.merge(modeled_assessed_value.rename('modeled_assessed'), left_index=True, right_index=True)

# #BUILD THE MODEL FOR SALE PRICE BASED ON ASSESSED PRICE
# #REMOVE 0 Value Sale prices
# #REMOVE NON_ARMS LENGTH TRANSACTIONS
# dim = Dimension(joined_df, 'modeled_assessed', 'SalePrice')

# #PASS IN ASSESSED PRICE TO MODEL TO GET PREDICTED SALE PRICE

# #KENSINGTON ONLY
# #TODO function to get street
# ken_df = df[df['SITEADDRESS'].str.contains('KENSINGTON',na=False)]
# rcrds = ken_df.to_dict('records')

# property_values = []

# for prop in rcrds:
#     results = []
#     for key in prop.keys():
#         try:
#             predicted = ds.get_predicted_house_price({key: prop[key]},vars(ai))
#             if predicted > 0:
#                 results.append(predicted)
#         except Exception as e:
#             pass
#     avg = alg.get_average_of_list_values(results)

#     property_values.append({'SITEADDRESS': prop['SITEADDRESS'], 'modeled_value': avg })

# x = []
# y = []

# for prop in property_values:
#     x.append(prop['SITEADDRESS'])
#     y.append(dim.calc(prop['modeled_value']))

# y_pos = range(len(y))

# plt.bar(x,y)
# plt.xticks(y_pos, x, rotation=90)
# plt.tight_layout()
# plt.savefig('_temp/ct.png')

# print('test')

# #OWNERNME1


# #TRANSACTIONS
# # tran_df = pd.read_csv('Property_Sales_Transactions.csv')
# # ua_tran_df = tran_df[tran_df['CVTTXCD'] == 70]

# #GET PRICE BY
# #FIND SQUARE FOOTAGE
# #FIND NUMBER BEDROOMS
# #FIND NUMBER BATHS
# #STREET
# #YEAR

# #ShapeSTArea
# #TOTVALUEBASE
# #Price Per Square Foot
# #ua_df['PPSF'] = ( ua_df['TOTVALUEBASE'] / ua_df['ShapeSTArea'] )

# #Residential only
# #ua_df_resi = ua_df[ua_df['BLDTYP'].str.contains('Dwelling',na=False)]

# #to numpy
# #import numpy as np
# #np_array_x = ua_df_resi['ShapeSTArea'].to_numpy()
# #np_array_y = ua_df_resi['TOTVALUEBASE'].to_numpy()

