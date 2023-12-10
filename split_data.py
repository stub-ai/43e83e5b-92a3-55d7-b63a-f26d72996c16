import pandas as pd
from sklearn.model_selection import train_test_split

# Assuming that df is your DataFrame
df = pd.read_csv('your_data.csv')  # replace 'your_data.csv' with your actual csv file

train, test = train_test_split(df, test_size=0.3)

# Now, 'train' and 'test' are your training and testing data.