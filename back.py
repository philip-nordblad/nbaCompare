from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playercareerstats
import nba_api

from pandas import DataFrame

import pandas as pd


from nba_api.stats.static import players

custom_headers = {
    'Host': 'stats.nba.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}


# Nikola Jokić
career = playercareerstats.PlayerCareerStats(player_id='2544')

# pandas data frames (optional: pip install pandas)
# career.get_data_frames()[0]

df = pd.DataFrame(career.get_data_frames()[0])

playerinfo = commonplayerinfo.CommonPlayerInfo(
    player_id=2544, proxy='127.0.0.1:80', headers=custom_headers, timeout=100)

print(df)

playerinfo.get_data_frames()

arwa = playerinfo.get_data_frames()


##################
## WORK STATION ##
##              ##
##################


# Be Clear!


######################
