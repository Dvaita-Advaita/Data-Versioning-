import pandas as pd
import os

# Create a sample dataframe with column names
data = {"Name":["Ram","Shayam","Mohan"],
    "Age":[22,23,24],
    "City":["Patna","Gaya","Muzz"]}

df = pd.DataFrame(data)

# Adding new_row to df for v2
new_row1 = {"Name":"Nobita","Age":21,"City":"Tokyo"}
df.loc[len(df.index)] = new_row1
#
# Adding new_roe to df for v3
new_row2 = {"Name":"Amit","Age":25,"City":"Dumka"}
df.loc[len(df.index)] = new_row2
#
# Ensure the "data"directory exists at the root level
data_dir = "data"
os.makedirs(data_dir,exist_ok=True)

# Define the fle path
file_path = os.path.join(data_dir,"sample_data.csv")

# Save the DataFrame to a CSV file
df.to_csv(file_path,index=False)
