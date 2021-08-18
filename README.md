# pandas_helpers

Pandas-derived tools



### Funcs:

pd_read_file(filename, **kwarg): Determines which pd.read_xxx (_csv vs _excel) to use depending on file extension

lookup_match(lookup_col, match_col, match_return): Performs like a lookup. 



## Import to another dir:

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'Filepath/to/Pandas_Helper')
from pandas_helpers import PandaHelpers as ph
