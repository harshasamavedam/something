from wrogn_extract import raw_to_gold, wrogn_extract_raw
from datetime import datetime as dt

wrogn_extract_raw()
print('wrogn_extract_raw.py executed successfully')
print('Now running raw_to_gold function...')
print(f'at {dt.now()}')
raw_to_gold()

# a='sri|sama'
# print(a.split('|')[0])