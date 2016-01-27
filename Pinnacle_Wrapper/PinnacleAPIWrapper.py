import requests
import json
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import re
import pandas as pd
import datetime
import dateutil
import uuid

class ActivatePinnacle:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def getsports(self):
        url = 'https://api.pinnaclesports.com/v1/sports'
        r = requests.get(url, auth=HTTPBasicAuth(self.username, self.password))
        soup = BeautifulSoup(r.text)
        list1 = soup.findAll('sport')
        cleanlist = []
        for l in list1:
            temp = []
            temp.append(l.attrs['id'])
            temp.append(str(l.text))
            temp.append(l.attrs['feedcontents'])
            cleanlist.append(temp)
        df = pd.DataFrame(data=cleanlist, columns=['ID', 'Sport', 'Lines'])
        return df

    def getleaguesbysportid(self, sportid):
        url = 'https://api.pinnaclesports.com/v1/leagues'
        PARAMS = {'sportId':sportid}
        r = requests.get(url, params=PARAMS, auth=HTTPBasicAuth(self.username, self.password))
        soup = BeautifulSoup(r.text)
        leagues = soup.findAll('league')
        cleanlist = []
        for league in leagues:
            temp = []
            temp.append(league.attrs['id'])
            temp.append(league.text)
            temp.append(league.attrs['hometeamtype'])
            temp.append(league.attrs['feedcontents'])
            cleanlist.append(temp)
        df = pd.DataFrame(data=cleanlist,columns=['ID', 'League', 'HomeTeam', 'Lines'])
        return df

    def getsportid(self, sport):
        sportdf = self.getsports()
        sportid = sportdf[sportdf['Sport']==sport]['ID'].values[0]
        return sportid

    def getleaguename(self,leagueid, sportid):
        df = self.getleaguesbysportid(sportid)
        leaguename = df[df['ID']==leagueid]['League'].values[0]
        return leaguename

    def getleaguesbysportname(self, sport):
        sportid= self.getsportid(sport)
        df = self.getleaguesbysportid(sportid)
        return df

    def getbalance(self):
        url = 'https://api.pinnaclesports.com/v1/client/balance'
        r = requests.get(url,  auth=HTTPBasicAuth(self.username, self.password))
        r = r.json()
        list1 = []
        list1.append(float(r['availableBalance']))
        list1.append(float(r['outstandingTransactions']))
        list1.append(str(r['currency']))
        return list1

    def getbets(self, days, betlist=None):
        url = 'https://api.pinnaclesports.com/v1/bets'
        toDate = datetime.datetime.today().date()
        toDate = toDate.isoformat()
        fromDate = datetime.datetime.today().date() - datetime.timedelta(days=days)
        fromDate= fromDate.isoformat()
        PARAMS = {'betlist':betlist, 'fromDate':fromDate, 'toDate':toDate}
        r = requests.get(url, params=PARAMS, auth=HTTPBasicAuth(self.username, self.password))
        r = r.json()
        cleanlist=[]
        for bet in r['bets']:
            temp = []
            temp.append(bet['betId'])
            temp.append(bet['betStatus'])
            temp.append(bet['betType'])
            temp.append(bet['eventId'])
            temp.append(bet['handicap'])
            temp.append(bet['team1'])
            temp.append(bet['team2'])
            temp.append(bet['isLive'])
            temp.append(bet['oddsFormat'])
            temp.append(dateutil.parser.parse(bet['placedAt']))
            temp.append(bet['price'])
            temp.append(bet['risk'])
            temp.append(bet['sportId'])
            cleanlist.append(temp)
        df = pd.DataFrame(data=cleanlist, columns=['BetID', 'Status', 'Type', 'EventID', 'Handicap', 'Team1', 'Team2', 'Live', 'OddsFormat', 'TimeStamp', 'Price', 'Risk', 'sportID'])
        return df

    def getfixtures(self, sportname=None, sportid=None, leagueids=None, since=None, islive=None):
        url = 'https://api.pinnaclesports.com/v1/fixtures'
        if sportname is not None:
            sportid = self.getsportid(sportname)
        PARAMS = {'sportId':sportid, 'leagueIds': leagueids, 'since':since, 'islive':islive}
        r = requests.get(url, params=PARAMS, auth=HTTPBasicAuth(self.username, self.password))
        r = r.json()
        cleanlist = []
        sport1 = r['sportId']
        for league in r['league']:
            for event in league['events']:
                temp = []
                temp.append(sport1)
                temp.append(league['id'])
                temp.append(event['id'])
                temp.append(event['home'])
                temp.append(event['away'])
                temp.append(event['liveStatus'])
                temp.append(dateutil.parser.parse(event['starts']))
                temp.append(event['status'])
                cleanlist.append(temp)
        df = pd.DataFrame(data=cleanlist, columns=['sportID', 'LeagueID', 'GameID', 'HomeTeam', 'AwayTeam', 'IsLive', 'Starts', 'Status'])
        return df

    def getodds(self, sportname=None, sportid=None, leagueids=None, since=None, islive=None, oddsFormat=None):
        url = 'https://api.pinnaclesports.com/v1/odds'
        if sportname is not None:
            sportid = self.getsportid(sportname)
        PARAMS = {'sportId':sportid, 'leagueIds': leagueids, 'since':since, 'islive':islive, 'oddsFormat': oddsFormat}
        r = requests.get(url, params=PARAMS, auth=HTTPBasicAuth(self.username, self.password))
        r = r.json()
        cleanlist = []
        for league in r['leagues']:
            for event in league['events']:
                for period in event['periods']:
                    if period['number'] != 0:
                        continue
                    else:
                        try:
                            temp = []
                            temp.append(r['sportId'])
                            temp.append(league['id'])
                            temp.append(event['id'])
                            temp.append(r['last'])
                            temp.append(period['lineId'])
                            temp.append(dateutil.parser.parse(period['cutoff']))
                            temp.append(period['maxMoneyline'])
                            temp.append(period['maxSpread'])
                            temp.append(period['maxTotal'])
                            temp.append(period['moneyline']['home'])
                            temp.append(period['moneyline']['away'])
                            temp.append(period['spreads'][0]['hdp'])
                            temp.append(period['spreads'][0]['home'])
                            temp.append(period['spreads'][0]['away'])
                            temp.append(period['totals'][0]['points'])
                            temp.append(period['totals'][0]['over'])
                            temp.append(period['totals'][0]['under'])
                            cleanlist.append(temp)
                        except:
                            continue
        df = pd.DataFrame(data=cleanlist, columns=['sportID', 'LeagueID', 'GameID', 'Updated', 'LineID', 'CutOff', 'MLMax', 'SpreadMax', 'TotalMax', 'HomeOdds', 'AwayOdds', 'Hcap', 'HomeHcapOdds', 'AwayHcapOdds', 'Total', 'OverOdds', 'UnderOdds'])
        return df

    def getalllines(self, sport):
        df = self.getodds(sportname=sport, oddsFormat=1)
        df2 = self.getfixtures(sportname=sport)
        df3 = self.getleaguesbysportname(sport)
        df = df2.merge(df, how='inner', on=['GameID','LeagueID', 'sportID'])
        return df

    def placebet(self, stake, sportid, gameid, lineid, bettype, team):
        bet = {}
        bet['uniqueRequestId'] = str(uuid.uuid4())
        bet['acceptBetterLine'] = "TRUE"
        bet['stake'] = float(stake)
        bet['oddsFormat'] = 'DECIMAL' #AMERICAN, DECIMAL
        bet['winRiskStake'] = 'RISK'
        bet['sportId'] = int(sportid)
        bet['eventId'] = int(gameid)
        bet['lineId'] = int(lineid)
        bet['periodNumber'] = 0
        bet['betType'] = bettype #SPREAD, MONEYLINE, TOTAL_POINTS, TEAM_TOTAL_POINTS
        bet['team'] = team #Team1, Team2, DRAW 
        #bet['side'] = side #OVER, UNDER only for totals
        url = 'https://api.pinnaclesports.com/v1/bets/place'
        r = requests.post(url, json=bet, auth=HTTPBasicAuth(self.username, self.password))
        print r.text
        return r


