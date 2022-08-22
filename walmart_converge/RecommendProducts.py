import pandas as pd
import sqlalchemy
def recommendProducts(params,filter):
    # Create the base query
    data_df=params.sort_values(filter,ascending=False)
    return data_df.head(4)