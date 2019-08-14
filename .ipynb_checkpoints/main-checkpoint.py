from yahoo_oauth import OAuth2
import os
import json
import league, game, team

# oauth = OAuth2(None, None, from_file='oauth2.json')



# if not oauth.token_is_valid():
#     oauth.refresh_access_token()
# # Example
# response = oauth.session.get(url, params=payload)


# if not os.path.exists('oauth2.json'):
#     creds = {'consumer_key': 'my_key', 'consumer_secret': 'my_secret'}
#     with open(args['<json>'], "w") as f:
#         f.write(json.dumps(creds))

sc = OAuth2(None, None, from_file='oauth2.json')

# get nfl game
gm = game.Game(sc, 'nfl')
print(gm)
league_ids = gm.league_ids()

kffl_league_id = '390.l.707700'


lg = gm.to_league(kffl_league_id)
print(f"scoring categories: {lg.stat_categories()}")
print(f"standings:{lg.standings()}")
print(f"teams:{lg.teams()}")
print(f"current user team:{lg.team_key()}")
print(f"current week:{lg.current_week()}")
team = lg.to_team(lg.team_key())
week = 1
print(f"roster week {week}: {team.roster(week)}")
matchup = lg.to_team(team.matchup(week))
print(f"matchup week {week}:{matchup.name}")

# missing functionality
# add name property to team
# add players class
# add custom data for team
# save data to database
