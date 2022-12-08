import glob
import pandas as pd
from sklearn.model_selection import train_test_split
import unidecode
import os

# Defining empty data frame
data = pd.DataFrame(columns = ['Image Path','Pop','Hip Hop','Country','Jazz','Rock','Alternative'])

# Append pop
folder_dir = 'INSERT_FILEPATH_HERE'
for image in glob.iglob(f'{folder_dir}/*'):
    
    data2 = {'Image Path': unidecode.unidecode(image), 'Pop':1, 'Hip Hop':0, 'Country':0, 'Jazz':0,
             'Rock':0, 'Alternative':0}
    data = data.append(data2, ignore_index = True)
    os.rename(image,unidecode.unidecode(image))
    
# Append hip hop
folder_dir = 'INSERT_FILEPATH_HERE'
for image in glob.iglob(f'{folder_dir}/*'):
    
    data2 = {'Image Path': unidecode.unidecode(image), 'Pop':0, 'Hip Hop':1, 'Country':0, 'Jazz':0,
             'Rock':0, 'Alternative':0}
    data = data.append(data2, ignore_index = True)
    os.rename(image,unidecode.unidecode(image))
    
# Append country
folder_dir = 'INSERT_FILEPATH_HERE'
for image in glob.iglob(f'{folder_dir}/*'):
    
    data2 = {'Image Path': unidecode.unidecode(image), 'Pop':0, 'Hip Hop':0, 'Country':1, 'Jazz':0,
             'Rock':0, 'Alternative':0}
    data = data.append(data2, ignore_index = True)
    os.rename(image,unidecode.unidecode(image))
    
# Append jazz
folder_dir = 'INSERT_FILEPATH_HERE'
for image in glob.iglob(f'{folder_dir}/*'):
    
    data2 = {'Image Path': unidecode.unidecode(image), 'Pop':0, 'Hip Hop':0, 'Country':0, 'Jazz':1,
             'Rock':0, 'Alternative':0}
    data = data.append(data2, ignore_index = True)
    os.rename(image,unidecode.unidecode(image))
    
# Append rock
folder_dir = 'INSERT_FILEPATH_HERE'
for image in glob.iglob(f'{folder_dir}/*'):
    
    data2 = {'Image Path': unidecode.unidecode(image), 'Pop':0, 'Hip Hop':0, 'Country':0, 'Jazz':0,
             'Rock':1, 'Alternative':0}
    data = data.append(data2, ignore_index = True)
    os.rename(image,unidecode.unidecode(image))
    
# Append alt
folder_dir = 'INSERT_FILEPATH_HERE'
for image in glob.iglob(f'{folder_dir}/*'):
    
    data2 = {'Image Path': unidecode.unidecode(image), 'Pop':0, 'Hip Hop':0, 'Country':0, 'Jazz':0,
             'Rock':0, 'Alternative':1}
    data = data.append(data2, ignore_index = True)
    os.rename(image,unidecode.unidecode(image))

# Split data into training and testing
train = data.sample(frac=0.8, random_state=25)
test = data.drop(train.index)

# Write dataframes to csv format
data.to_csv('INSERT_FILEPATH_HERE/classifiedData.csv',
            index=False)

train.to_csv('INSERT_FILEPATH_HERE/trainingData.csv',
            index=False)

test.to_csv('INSERT_FILEPATH_HERE/testingData.csv',
            index=False)
