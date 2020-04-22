import pandas as pd
import os
admin_daily = pd.read_parquet(os.getcwd() + '/gzip/admin_daily.gzip')

print(admin_daily)
