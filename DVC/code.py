import pandas as pd
import os

# create a simple dataframe

data = {'Name': ['Kunal', 'Ajgaonkar', 'John', 'Doe'],
        'Age': [24, 25, 26, 27],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
        }

df = pd.DataFrame(data)

# Adding new row to df for V2
new_row_loc = {'Name': 'Jane', 'Age': 28, 'City': 'San Francisco'}
df.loc[len(df.index)] = new_row_loc

# Adding new row to df for V3
new_row_loc2= {'Name': 'Shane', 'Age': 22, 'City': 'Californai'}
df.loc[len(df.index)] = new_row_loc2

#Ensure the data directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

#Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

#Save the dataframe to a csv file, including column names
df.to_csv(file_path, index=False)

print(f"Data saved to {file_path}")