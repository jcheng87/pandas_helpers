import pandas as pd
import numpy as np
import os


class PandaHelpers:


    def pd_read_file(filename, **kwarg):
        """
        Determines which pd.read_xxx (_csv vs _excel) to use depending on file extension
        
        
        Parameters
        -----
        filename (str): Filename of file to pass through pd.read_xxx
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


            