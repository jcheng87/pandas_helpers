import pandas as pd
import numpy as np
import os


class PandaHelpers:


    def pd_read_file(filename, **kwarg):
        """
        Determines which pd.read_xxx (_csv vs _excel) to use depending on file extension
        
        Parameters
        -----------
        fileame (str): Filename of file to pass through pd.read_xxx
        **kwarg : These parameters will be passed to DataFrame.to_csv or DataFrame.to_excel
        
        
        Returns
        --------
        pd.Dataframe
        
        """
        
        file_ext = os.path.splitext(filename)[1]
        
        if file_ext == '.csv':
            return pd.read_csv(filename, **kwarg)
        
        elif file_ext == '.xlsx':
            return pd.read_excel(filename, **kwarg)
        
        else: 
            raise ValueError(f'Not csv or Xlsx filetype; File type is {file_ext}')


    def lookup_match(lookup_col, match_col, match_return):
        """
        Performs like a lookup. 

        Parameters
        -----------
        lookup_col (pd.Series) = Column to look up
        match_col (pd.Series) = column to match lookup
        match_return (pd.Series) = column to return value

        Returns
        ---------
        Series : Series of match_return

        """
        # create Series using match columns
        lookup_series = pd.Series(match_return.values, index=match_col)

        #drop NA indexes in lookup_series and convert to dict
        match_dict = lookup_series.loc[lookup_series.index.dropna()].to_dict()
        
        #map look_col to match_dict
        return lookup_col.map(match_dict)


    def filter_and_rename(dataframe, filter_columns, rename_cols= None):
        """
        Takes df and returns df with only columns in filter_columns (list)and then renaming the columns based on mapping in mapping_dict

        Parameters
        -----------
        dataframe (pd.DataFrame) = Dataframe to convert
        filter_columns (list) = [filter df for these cols]
        mapping_dict (dict, optional) = {columns in df to be in return df (keys): new column name to appear in df (values)}

        Returns
        ---------
        DataFrame : Dataframe with new column names

        """

        if rename_cols is None: 
            # just return columns in filter column list if col rename dict is not provided
            return dataframe[filter_columns]
        else:  
            return dataframe[filter_columns].rename(columns=rename_cols)


            