import os
import pandas as pd

#get directory contents - csv files from goodx reports

directory = os.getcwd() + '/raw_data/'

if (os.path.isdir(directory)==False):
    os.mkdir(directory)

files = os.listdir(directory)


csv_list = [(directory + x) for x in files if '.csv' in x]
admin_list = [x for x in csv_list if 'admin_daily' in x]
edu_list = [x for x in csv_list if 'edu_daily' in x]

def data_handler(path_list, output_name):
    count = 0
    print('Reading', output_name, 'data')
    for x in path_list:
        count = count + 1
        print('Reading file:', x)
        print('Number', count, 'of', len(path_list))
        if (count == 1):
            data = pd.read_csv(x, index_col=False,low_memory=False)
        else:
            data = pd.concat([data, pd.read_csv(x, index_col=False,
                                                low_memory=False)])
        print('Done!')

    print('Dropping redundant rows and columns...')
    data = data.drop(['ICD10 Description', 'Student No', 'Provider',
                      'Proc Description'], 1)
    data = data[~data['File Number'].str.contains('GDX', na=False)]
    data.drop_duplicates(inplace=True)
    print('Done!')

    print('Suppressing errors related to NaN values...')
    #To prevent future issues with NaN values
    data['Patient Tel1'].fillna('None', inplace=True)
    print('Done!')
    print('Writing dataframe to parquet file...')
    data.to_parquet(output_name, compression='gzip')
    print('Done!')

    print('Removing variables from memory...')
    del data
    print('Done!')

export_directory = os.getcwd() + '/gzip/'

if (os.path.isdir(export_directory)==False):
    os.mkdir(export_directory)

data_handler(admin_list, export_directory + 'admin_daily.gzip')
data_handler(edu_list, export_directory + 'edu_daily.gzip')
