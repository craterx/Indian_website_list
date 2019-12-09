import pandas as pd
import sys

if(len(sys.argv) < 3):
    print('proivde input and output filenames')
    sys.exit()

file_name = sys.argv[1]
file_name_output = sys.argv[2]

df = pd.read_csv(file_name, sep=",",engine='python')

# Notes:
# - the `subset=None` means that every column is used 
#    to determine if two rows are different; to change that specify
#    the columns as an array
# - the `inplace=True` means that the data structure is changed and
#   the duplicate rows are gone  
df.drop_duplicates(subset=['Organization_Name'],inplace=True)
print(df.columns)
# Write the results to a different file
df.to_csv(file_name_output,index='false',sep=',')