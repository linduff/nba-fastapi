from fastapi import FastAPI
from nba_api.stats.endpoints import scoreboardv2, teamgamelog
from datetime import datetime

teams = {'CLE': 1610612739, 'OKC': 1610612760, 'BOS': 1610612738, 'DEN': 1610612743, 'NYK': 1610612752, 'MEM': 1610612763, 'HOU': 1610612745, 'IND': 1610612754, 'LAL': 1610612747, 'MIL': 1610612749, 'LAC': 1610612746, 'DET': 1610612765, 'MIN': 1610612750, 'ORL': 1610612753, 'DAL': 1610612742, 'MIA': 1610612748, 'ATL': 1610612737, 'SAC': 1610612758, 'CHI': 1610612741, 'GSW': 1610612744, 'PHI': 1610612755, 'PHX': 1610612756, 'BKN': 1610612751, 'SAS': 1610612759, 'POR': 1610612757, 'TOR': 1610612761, 'UTA': 1610612762, 'CHA': 1610612766, 'NOP': 1610612740, 'WAS': 1610612764}

app = FastAPI()

@app.get("/scoreboard")
async def get_scoreboard(game_date: str | None = None, day_offset: str | None = None, league_id: str | None = None):
    if date == None:
        date = datetime.now().date()
    return scoreboardv2.ScoreboardV2(game_date=game_date, day_offset=day_offset, league_id=league_id)

@app.get("/gamelog")
async def get_gamelog(team_id: str):
    return teamgamelog.TeamGameLog(team_id=teams[team_id.upper()])
