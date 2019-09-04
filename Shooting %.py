from nba_api.stats.endpoints import commonallplayers
from nba_api.stats.endpoints import playercareerstats
import pandas

# Retrieve a data frame containing every player in NBA history
allPlayers = commonallplayers.CommonAllPlayers()
allPlayers = allPlayers.get_data_frames()[0]




# Sanitize and filter data to find all players who joined the NBA after the year 2000
allPlayers["FROM_YEAR"] = pandas.to_numeric(allPlayers["FROM_YEAR"], errors='ignore')
currentPlayers = allPlayers.query('FROM_YEAR>2000')
currentPlayersID = currentPlayers['PERSON_ID']

# Store the average change in PPG in a list


# Begin loop
for ID in currentPlayersID:
   player_info = playercareerstats.PlayerCareerStats(player_id=str(ID), per_mode36=  'PerGame')
   player_info = player_info.get_data_frames()[0]
   print(player_info['PTS'])
   print(ID)
   # Skip players who have only played one season
   if len(player_info.index) < 2:
       continue
   for j in range (len(player_info.index) - 1):
       currentPPG = player_info.at[j,'PTS']



# End loop
