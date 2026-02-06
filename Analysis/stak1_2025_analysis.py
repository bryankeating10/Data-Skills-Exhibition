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