# Import dependencies
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the processed game data
trun_usr = 'stak1' # Truncated username for file naming
game_data = pd.read_csv(f'Data/Gold/{trun_usr}_game_data_gold.csv')

# Display summary statistics of the game data
print("\n📊 Game Data Summary:")
print(game_data.describe())

# Display column headers and data types
print("\n📋 Game Data Columns and Types:")
print(game_data.dtypes)

# Print unique time control values
print("\n⏱️ Unique Time Controls:")
print(game_data['TimeControl'].unique())

# # Curious
# print("\n Unique Dates")
# print(
#     game_data[game_data['TimeControl'].isin(['1/86400', '1/259200'])]['UTCDate']
# )

# Describe games by time control
print("\n📈 Descriptive Statistics for Games by Time Control:")
print('Rapid:')
print(game_data[game_data['TimeControl'].isin(['600', '900+10'])].describe())

print('\nBlitz:')
print(game_data[game_data['TimeControl'].isin(['180+2', '300+2','300+5'])].describe())

print('\nBullet:')
print(game_data[game_data['TimeControl'].isin(['120+1','60+1'])].describe())