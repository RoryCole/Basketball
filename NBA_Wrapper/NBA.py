# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 08:51:08 2015

@author: rorycole
"""

import requests
import json
import re
import pandas as pd
import datetime
import sqlalchemy
import sys
sys.insert(0,r'/Users/rorycole/Desktop/PythonScripts/NBA')
import NBA_Constants as Constant

class BoxScores:
    def __init__(self, GameID, StartPeriod=Constant.startrange.Default, EndPeriod=Constant.endperiod.Default, StartRange=Constant.startrange.Default, EndRange = Constant.endrange.Default, RangeType=Constant.rangetype.Default):
        self.GameID = GameID
        self.StartPeriod = StartPeriod
        self.EndPeriod = EndPeriod
        self.StartRange = StartRange
        self.EndRange = EndRange
        self.RangeType = RangeType

    def boxscore(self):
        endpoint = 'boxscore'
        PARAMS = {'GameID':self.GameID, 'StartPeriod':self.StartPeriod,'EndPeriod':self.EndPeriod, 'RangeType':self.RangeType}
        r = self.response(PARAMS,endpoint)
        return r

    def boxscoreadvanced(self):
        endpoint = 'boxscoreadvanced'
        PARAMS = {'GameID':self.GameID, 'StartPeriod':self.StartPeriod,'EndPeriod':self.EndPeriod, 'RangeType':self.RangeType}
        r = self.response(PARAMS,endpoint)
        return r

    def boxscoreadvancedv2(self):    
        endpoint = 'boxscoreadvancedv2'
        PARAMS = {'GameID':self.GameID, 'StartPeriod':self.StartPeriod,'EndPeriod':self.EndPeriod, 'RangeType':self.RangeType}
        r = self.response(PARAMS,endpoint)
        return r

    def boxscorefourfactors(self):    
        endpoint = 'boxscorefourfactors'
        PARAMS = {'GameID':self.GameID, 'StartPeriod':self.StartPeriod,'EndPeriod':self.EndPeriod, 'RangeType':self.RangeType}
        r = self.response(PARAMS,endpoint)
        return r

    def boxscorefourfactorsv2(self):    
        endpoint = 'boxscorefourfactorsv2'
        PARAMS = {'GameID':self.GameID, 'StartPeriod':self.StartPeriod,'EndPeriod':self.EndPeriod, 'RangeType':self.RangeType}
        r = self.response(PARAMS,endpoint)
        return r

    def boxscoremisc(self):    
        endpoint = 'boxscoremisc'
        url = BoxScores.baseurl + '/' + endpoint
        PARAMS = {'GameID':self.GameID, 'StartPeriod':self.StartPeriod,'EndPeriod':self.EndPeriod, 'RangeType':self.RangeType}
        r = requests.get(url, params=PARAMS)
        r = r.json()
        return r

    def boxscoremiscv2(self):    
        endpoint = 'boxscoremiscv2'
        PARAMS = {'GameID':self.GameID, 'StartPeriod':self.StartPeriod,'EndPeriod':self.EndPeriod, 'RangeType':self.RangeType}
        r = self.response(PARAMS,endpoint)
        return r

    def boxscorescoring(self):    
        endpoint = 'boxscorescoring'
        PARAMS = {'GameID':self.GameID, 'StartPeriod':self.StartPeriod,'EndPeriod':self.EndPeriod, 'RangeType':self.RangeType}
        r = self.response(PARAMS,endpoint)
        return r

    def boxscorescoringv2(self):    
        endpoint = 'boxscorescoringv2'
        PARAMS = {'GameID':self.GameID, 'StartPeriod':self.StartPeriod,'EndPeriod':self.EndPeriod, 'RangeType':self.RangeType}
        r = self.response(PARAMS,endpoint)
        return r

    def boxscoretraditionalv2(self):    
        endpoint = 'boxscoretraditionalv2'
        PARAMS = {'GameID':self.GameID, 'StartPeriod':self.StartPeriod,'EndPeriod':self.EndPeriod, 'RangeType':self.RangeType}
        r = self.response(PARAMS,endpoint)
        return r

    def boxscoreusage(self):    
        endpoint = 'boxscoreusage'
        PARAMS = {'GameID':self.GameID, 'StartPeriod':self.StartPeriod,'EndPeriod':self.EndPeriod, 'RangeType':self.RangeType}
        r = self.response(PARAMS,endpoint)
        return r

    def boxscoreusagev2(self):
        endpoint = 'boxscoreusagev2'
        PARAMS = {'GameID':self.GameID, 'StartPeriod':self.StartPeriod,'EndPeriod':self.EndPeriod, 'RangeType':self.RangeType}
        r = self.response(PARAMS,endpoint)
        return r

    def boxscoresummaryv2(self):
        endpoint = 'boxscoresummaryv2'
        PARAMS = {'GameID':self.GameID}
        r = self.response(PARAMS,endpoint)
        return r

    def boxscoreplayertrackv2(self):
        endpoint = 'boxscoreplayertrackv2'
        PARAMS = {'GameID':self.GameID}
        r = self.response(PARAMS,endpoint)
        return r
    
    def response(self, params, endpoint):
        url = 'http://stats.nba.com/stats/' + endpoint
        try:
            r = requests.get(url, params=params)
            if r.status_code==200:
                r = r.json()
                return r
            else:
                print 'Error: %s' % r.status_code
                r = {}
                return r
        except:
            print 'Request Failed'
            r = {}
            return r    
    
class Common:
    def __init__(self, LeagueID=Constant.leagueid.Default, Season=Constant.season.Default, IsOnlyCurrentSeason='1', SeasonType=Constant.seasontype.Default):
        self.LeagueID = LeagueID
        self.Season = Season
        self.IsOnlyCurrentSeason = IsOnlyCurrentSeason
        self.SeasonType = SeasonType
        
    def commonTeamYears(self):
        endpoint = 'commonTeamYears'
        PARAMS = {'LeagueID':self.LeagueID}
        r = self.response(PARAMS,endpoint)
        return r

    def commonallplayers(self):
        endpoint = 'commonallplayers'
        PARAMS = {'LeagueID':self.LeagueID, 'Season':self.Season, 'IsOnlyCurrentSeason':self.IsOnlyCurrentSeason}
        r = self.response(PARAMS,endpoint)
        return r

    def commonplayerinfo(self, PlayerID):
        endpoint = 'commonplayerinfo'
        PARAMS = {'PlayerID':PlayerID}
        r = self.response(PARAMS,endpoint)
        return r

    def commonplayoffseries(self):
        endpoint = 'commonplayoffseries'
        PARAMS = {'LeagueID':self.LeagueID, 'Season':self.Season}
        r = self.response(PARAMS,endpoint)
        return r

    def commonteamroster(self, TeamID):
        endpoint = 'commonteamroster'
        PARAMS = {'Season':self.Season, 'TeamID':TeamID}
        r = self.response(PARAMS,endpoint)
        return r
    
    def teaminfocommon(self, TeamID):
        endpoint = 'teaminfocommon'
        PARAMS = {'TeamID':TeamID, 'Season':self.Season,'LeagueID':self.LeagueID, 'SeasonType':self.SeasonType} 
        r = self.response(PARAMS,endpoint)
        return r

    def response(self, params, endpoint):
        url = 'http://stats.nba.com/stats/' + endpoint
        try:
            r = requests.get(url, params=params)
            if r.status_code==200:
                r = r.json()
                return r
            else:
                print 'Error: %s' % r.status_code
                r = {}
                return r
        except:
            print 'Request Failed'
            r = {}
            return r
            
class Draft:
    def __init__(self, LeagueID=Constant.leagueid.Default, SeasonYear = '2015'):
        self.LeagueID = LeagueID
        self.SeasonYear = SeasonYear
        
    def draftcombinedrillresults(self):
        endpoint = 'draftcombinedrillresults'
        PARAMS = {'LeagueID':self.LeagueID, 'SeasonYear':self.SeasonYear}
        r = self.response(PARAMS,endpoint)
        return r

    def draftcombinenonstationaryshooting(self):
        endpoint = 'draftcombinenonstationaryshooting'
        PARAMS = {'LeagueID':self.LeagueID, 'SeasonYear':self.SeasonYear}
        r = self.response(PARAMS,endpoint)
        return r

    def draftcombineplayeranthro(self):
        endpoint = 'draftcombineplayeranthro'
        PARAMS = {'LeagueID':self.LeagueID, 'SeasonYear':self.SeasonYear}
        r = self.response(PARAMS,endpoint)
        return r

    def draftcombinespotshooting(self):
        endpoint = 'draftcombinespotshooting'
        PARAMS = {'LeagueID':self.LeagueID, 'SeasonYear':self.SeasonYear}
        r = self.response(PARAMS,endpoint)
        return r

    def draftcombinestats(self):
        endpoint = 'draftcombinestats'
        PARAMS = {'LeagueID':self.LeagueID, 'SeasonYear':self.SeasonYear}
        r = self.response(PARAMS,endpoint)
        return r

    def drafthistory(self):
        endpoint = 'drafthistory'
        PARAMS = {'LeagueID':self.LeagueID}
        r = self.response(PARAMS,endpoint)
        return r

    def franchisehistory(self):
        endpoint = 'franchisehistory'
        PARAMS = {'LeagueID':self.LeagueID}
        r = self.response(PARAMS,endpoint)
        return r

    def response(self, params, endpoint):
        url = 'http://stats.nba.com/stats/' + endpoint
        try:
            r = requests.get(url, params=params)
            if r.status_code==200:
                r = r.json()
                return r
            else:
                print 'Error: %s' % r.status_code
                r = {}
                return r
        except:
            print 'Request Failed'
            r = {}
            return r
    
class homepages:
    def __init__(self, Stat = Constant.stat.Default, StatCategory=Constant.statcategory.Default, Season=Constant.season.Default, PlayerOrTeam=Constant.playerorteam.Default, SeasonType=Constant.seasontype.Default, LeagueID=Constant.leagueid.Default, GameScope=Constant.gamescope.Default, PlayerScope=Constant.playerscope.Default):
        self.StatCategory = StatCategory
        self.Season = Season
        self.PlayerOrTeam = PlayerOrTeam
        self.SeasonType = SeasonType
        self.LeagueID = LeagueID
        self.GameScope = GameScope
        self.PlayerScope = PlayerScope
        self.Stat = Stat
    
    def homepageleaders(self):
        endpoint = 'homepageleaders'
        PARAMS = {'LeagueID':self.LeagueID, 'StatCategory':self.StatCategory, 'Season':self.Season,'SeasonType':self.SeasonType, 'PlayerOrTeam':self.PlayerOrTeam, 'GameScope':self.GameScope, 'PlayerScope':self.PlayerScope}
        r = self.response(PARAMS,endpoint)
        return r

    def homepagev2(self):
        endpoint = 'homepagev2'
        PARAMS = {'LeagueID':self.LeagueID, 'StatCategory':self.StatCategory, 'Season':self.Season,'SeasonType':self.SeasonType, 'PlayerOrTeam':self.PlayerOrTeam, 'GameScope':self.GameScope, 'PlayerScope':self.PlayerScope}
        r = self.response(PARAMS,endpoint)
        return r

    def leaderstiles(self):
        endpoint = 'leaderstiles'
        PARAMS = {'LeagueID':self.LeagueID, 'Stat':self.Stat, 'Season':self.Season,'SeasonType':self.SeasonType, 'PlayerOrTeam':self.PlayerOrTeam, 'GameScope':self.GameScope, 'PlayerScope':self.PlayerScope}
        r = self.response(PARAMS,endpoint)
        return r

    def response(self, params, endpoint):
        url = 'http://stats.nba.com/stats/' + endpoint
        try:
            r = requests.get(url, params=params)
            if r.status_code==200:
                r = r.json()
                return r
            else:
                print 'Error: %s' % r.status_code
                r = {}
                return r
        except:
            print 'Request Failed'
            r = {}
            return r

class Player:
    def __init__(self, Stat = Constant.stat.Default, closestDef10=Constant.closedefdistrange.Default, CloseDefDistRange=Constant.closedefdistrange.Default, MeasureType=Constant.measuretype.Default, DistanceRange=Constant.distancerange.Default, PlayerOrTeam=Constant.playerorteam.Player, College=Constant.college.Default, ClutchTime = Constant.clutchtime.Default, AheadBehind=Constant.aheadbehind.Default, PointDiff=Constant.pointdiff.Default, Conference=Constant.conference.Default, Country=Constant.country.Default, DateFrom=Constant.datefrom.Default, DateTo=Constant.dateto.Default, DefenseCategory=Constant.defensecategory.Default, Division=Constant.division.Default, DraftYear=Constant.draftyear.Default, DraftPick=Constant.draftpick.Default, GameScope=Constant.gamescope.Default, GameSegment=Constant.gamesegment.Default, Height=Constant.height.Default, LastNGames=Constant.lastngames.Default, LeagueID=Constant.leagueid.Default, Location=Constant.location.Default, Month=Constant.month.Default, OpponentTeamID=Constant.opponentteamid.Default,PORound=Constant.poround.Default, PerMode=Constant.permode.Default, Period=Constant.period.Default, PlayerExperience = Constant.playerexperience.Default, PlayerPosition=Constant.playerposition.Default, Season=Constant.season.Default, SeasonSegment=Constant.seasonsegment.Default, SeasonType=Constant.seasontype.Default, ShotClockRange=Constant.shotclockrange.Default, StarterBench=Constant.starterbench.Default, VsConference=Constant.vsconference.Default, VsDivision=Constant.vsdivision.Default, Weight=Constant.weight.Default, PlusMinus=Constant.plusminus.Default, PaceAdjust=Constant.paceadjust.Default, Rank=Constant.rank.Default, TeamID=Constant.teamid.Default):
        self.College = College
        self.Conference=Conference
        self.Country = Country
        self.DateFrom = DateFrom
        self.DateTo = DateTo
        self.Division = Division
        self.DraftPick = DraftPick
        self.DraftYear = DraftYear
        self.DefenseCategory = DefenseCategory
        self.GameScope = GameScope
        self.GameSegment = GameSegment
        self.Height = Height
        self.LastNGames = LastNGames
        self.LeagueID = LeagueID
        self.Location = Location
        self.Month = Month
        self.OpponentTeamID = OpponentTeamID
        self.PORound = PORound
        self.Period = Period
        self.PlayerExperience = PlayerExperience
        self.PerMode = PerMode
        self.PlayerPosition=PlayerPosition
        self.Season=Season
        self.SeasonSegment=SeasonSegment
        self.SeasonType=SeasonType
        self.ShotClockRange=ShotClockRange
        self.StarterBench=StarterBench
        self.VsConference = VsConference
        self.VsDivision = VsDivision
        self.Weight = Weight
        self.PaceAdjust = PaceAdjust
        self.PlusMinus = PlusMinus
        self.Rank = Rank
        self.TeamID = TeamID
        self.ClutchTime = ClutchTime
        self.AheadBehind = AheadBehind
        self.PointDiff = PointDiff
        self.PlayerOrTeam = PlayerOrTeam
        self.DistanceRange = DistanceRange
        self.MeasureType = MeasureType
        self.CloseDefDistRange = CloseDefDistRange
        self.closestDef10 = closestDef10
        self.Stat = Stat

    def leaguedashplayerbiostats(self):
        endpoint = 'leaguedashplayerbiostats'
        PARAMS = {'College':self.College,'Conference':self.Conference,'Country':self.Country, 'DateFrom':self.DateFrom,'DateTo':self.DateTo, 'Division':self.Division, 'DraftPick':self.DraftPick, 'DraftYear':self.DraftYear,'GameScope':self.GameScope,'GameSegment':self.GameSegment, 'Height':self.Height, 'LastNGames':self.LastNGames, 'LeagueID':self.LeagueID,'Location':self.Location, 'Month':self.Month, 'OpponentTeamID':self.OpponentTeamID, 'Outcome':self.Outcome, 'PORound':self.PORound, 'PerMode':self.PerMode, 'Period':self.Period,'PlayerExperience':self.PlayerExperience, 'PlayerPosition':self.PlayerPosition, 'Season':self.Season, 'SeasonSegment':self.SeasonSegment, 'SeasonType':self.SeasonType, 'ShotClockRange':self.ShotClockRange,'StarterBench':self.StarterBench, 'TeamID':self.TeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'Weight':self.Weight}
        r = self.response(PARAMS,endpoint)
        return r

    def leaguedashplayerclutch(self):
        endpoint = 'leaguedashplayerclutch'
        PARAMS = {'ClutchTime':self.ClutchTime, 'AheadBehind': self.AheadBehind, 'PointDiff':self.PointDiff, 'College':self.College,'Conference':self.Conference,'Country':self.Country, 'DateFrom':self.DateFrom,'DateTo':self.DateTo, 'Division':self.Division, 'DraftPick':self.DraftPick, 'DraftYear':self.DraftYear,'GameScope':self.GameScope,'GameSegment':self.GameSegment, 'Height':self.Height, 'LastNGames':self.LastNGames, 'LeagueID':self.LeagueID,'Location':self.Location, 'Month':self.Month, 'OpponentTeamID':self.OpponentTeamID, 'Outcome':self.Outcome, 'PORound':self.PORound, 'PaceAdjust':self.PaceAdjust, 'PerMode':self.PerMode, 'Period':self.Period,'PlayerExperience':self.PlayerExperience, 'PlayerPosition':self.PlayerPosition, 'PlusMinus':self.PlusMinus, 'Rank':self.Rank, 'Season':self.Season, 'SeasonSegment':self.SeasonSegment, 'SeasonType':self.SeasonType, 'ShotClockRange':self.ShotClockRange,'StarterBench':self.StarterBench, 'TeamID':self.TeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'Weight':self.Weight}
        r = self.response(PARAMS,endpoint)
        return r

    def leaguedashplayerptshot(self):
        endpoint = 'leaguedashplayerptshot'
        PARAMS = {'CloseDefDistRange':self.CloseDefDistRange, 'closestDef10':self.closestDef10, 'College':self.College,'Conference':self.Conference,'Country':self.Country, 'DateFrom':self.DateFrom,'DateTo':self.DateTo, 'Division':self.Division, 'DraftPick':self.DraftPick, 'DraftYear':self.DraftYear,'DribbleRange':self.DribbleRange, 'GameScope':self.GameScope,'GameSegment':self.GameSegment, 'GeneralRange':self.GeneralRange, 'Height':self.Height, 'LastNGames':self.LastNGames, 'LeagueID':self.LeagueID,'Location':self.Location, 'Month':self.Month, 'OpponentTeamID':self.OpponentTeamID, 'Outcome':self.Outcome, 'PORound':self.PORound, 'PaceAdjust':self.PaceAdjust, 'PerMode':self.PerMode, 'Period':self.Period,'PlayerExperience':self.PlayerExperience, 'PlayerPosition':self.PlayerPosition, 'PlusMinus':self.PlusMinus, 'Rank':self.Rank, 'Season':self.Season, 'SeasonSegment':self.SeasonSegment, 'SeasonType':self.SeasonType, 'ShotClockRange':self.ShotClockRange, 'ShotDistRange':self.ShotDistRange, 'StarterBench':self.StarterBench, 'TeamID':self.TeamID, 'TouchTimeRange':self.TouchTimeRange, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'Weight':self.Weight}
        r = self.response(PARAMS,endpoint)
        return r

    def leaguedashplayershotlocations(self):
        endpoint = 'leaguedashplayershotlocations'
        PARAMS = {'DistanceRange':self.DistanceRange, 'College':self.College,'Conference':self.Conference,'Country':self.Country, 'DateFrom':self.DateFrom,'DateTo':self.DateTo, 'Division':self.Division, 'DraftPick':self.DraftPick, 'DraftYear':self.DraftYear,'GameScope':self.GameScope,'GameSegment':self.GameSegment, 'Height':self.Height, 'LastNGames':self.LastNGames, 'LeagueID':self.LeagueID,'Location':self.Location, 'Month':self.Month, 'OpponentTeamID':self.OpponentTeamID, 'Outcome':self.Outcome, 'PORound':self.PORound, 'PaceAdjust':self.PaceAdjust, 'PerMode':self.PerMode, 'Period':self.Period,'PlayerExperience':self.PlayerExperience, 'PlayerPosition':self.PlayerPosition, 'PlusMinus':self.PlusMinus, 'Rank':self.Rank, 'Season':self.Season, 'SeasonSegment':self.SeasonSegment, 'SeasonType':self.SeasonType, 'ShotClockRange':self.ShotClockRange,'StarterBench':self.StarterBench, 'TeamID':self.TeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'Weight':self.Weight}
        r = self.response(PARAMS,endpoint)
        return r

    def leaguedashplayerstats(self):
        endpoint = 'leaguedashplayerstats'
        PARAMS = {'College':self.College,'Conference':self.Conference,'Country':self.Country, 'DateFrom':self.DateFrom,'DateTo':self.DateTo, 'Division':self.Division, 'DraftPick':self.DraftPick, 'DraftYear':self.DraftYear,'GameScope':self.GameScope,'GameSegment':self.GameSegment, 'Height':self.Height, 'LastNGames':self.LastNGames, 'LeagueID':self.LeagueID,'Location':self.Location, 'Month':self.Month, 'OpponentTeamID':self.OpponentTeamID, 'Outcome':self.Outcome, 'PORound':self.PORound, 'PaceAdjust':self.PaceAdjust, 'PerMode':self.PerMode, 'Period':self.Period,'PlayerExperience':self.PlayerExperience, 'PlayerPosition':self.PlayerPosition, 'PlusMinus':self.PlusMinus, 'Rank':self.Rank, 'Season':self.Season, 'SeasonSegment':self.SeasonSegment, 'SeasonType':self.SeasonType, 'ShotClockRange':self.ShotClockRange,'StarterBench':self.StarterBench, 'TeamID':self.TeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'Weight':self.Weight}
        r = self.response(PARAMS,endpoint)
        return r

    def leaguedashptdefend(self):
        endpoint = 'leaguedashptdefend'
        PARAMS = {'Conference':self.Conference, 'DateFrom':self.DateFrom,'DateTo':self.DateTo, 'DefenseCategory':self.DefenseCategory, 'Division':self.Division, 'GameSegment':self.GameSegment, 'LastNGames':self.LastNGames, 'LeagueID':self.LeagueID,'Location':self.Location, 'Month':self.Month, 'OpponentTeamID':self.OpponentTeamID, 'Outcome':self.Outcome, 'PORound':self.PORound, 'PerMode':self.PerMode, 'Period':self.Period, 'Season':self.Season, 'SeasonSegment':self.SeasonSegment, 'SeasonType':self.SeasonType, 'TeamID':self.TeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision}
        r = self.response(PARAMS,endpoint)
        return r

    def leaguedashptstats(self):
        endpoint = 'leaguedashptstats'
        PARAMS = {'SeasonType':self.SeasonType, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust': self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'DistanceRange':self.DistanceRange, 'GameScope':self.GameScope, 'PlayerExperience':self.PlayerExperience, 'PlayerPosition':self.PlayerPosition, 'StarterBench':self.StarterBench, 'PlayerOrTeam':self.PlayerOrTeam}
        r = self.response(PARAMS,endpoint)
        return r

    def playercareerstats(self, PlayerID):
        endpoint = 'playercareerstats'
        PARAMS = {'PlayerID':PlayerID, 'PerMode':self.PerMode}
        r = self.response(PARAMS,endpoint)
        return r

    def playercompare(self, PlayerIDList, VsPlayerIDList):
        endpoint = 'playercompare'
        PARAMS = {'PlayerIDList':PlayerIDList, 'VsPlayerIDList':VsPlayerIDList, 'MeasrureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType}
        r = self.response(PARAMS,endpoint)
        return r

    def playerdashboardbyclutch(self, PlayerID):
        endpoint = 'playerdashboardbyclutch'
        PARAMS = {'MeasureType':self.MeasureType, 'ClutchTime':self.ClutchTime, 'AheadBehind': self.AheadBehind, 'PointDiff':self.PointDiff, 'College':self.College,'Conference':self.Conference,'Country':self.Country, 'DateFrom':self.DateFrom,'DateTo':self.DateTo, 'Division':self.Division, 'DraftPick':self.DraftPick, 'DraftYear':self.DraftYear,'GameScope':self.GameScope,'GameSegment':self.GameSegment, 'Height':self.Height, 'LastNGames':self.LastNGames, 'LeagueID':self.LeagueID,'Location':self.Location, 'Month':self.Month, 'OpponentTeamID':self.OpponentTeamID, 'Outcome':self.Outcome, 'PORound':self.PORound, 'PaceAdjust':self.PaceAdjust, 'PerMode':self.PerMode, 'Period':self.Period,'PlayerExperience':self.PlayerExperience, 'PlayerPosition':self.PlayerPosition, 'PlusMinus':self.PlusMinus, 'Rank':self.Rank, 'Season':self.Season, 'SeasonSegment':self.SeasonSegment, 'SeasonType':self.SeasonType, 'ShotClockRange':self.ShotClockRange,'StarterBench':self.StarterBench, 'TeamID':self.TeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'Weight':self.Weight}
        r = self.response(PARAMS,endpoint)
        return r

    def playerdashboardbygamesplits(self, PlayerID):
        endpoint = 'playerdashboardbygamesplits'
        PARAMS = {'PlayerID':PlayerID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType}
        r = self.response(PARAMS,endpoint)
        return r

    def playerdashboardbygeneralsplits(self, PlayerID):
        endpoint = 'playerdashboardbygeneralsplits'
        PARAMS = {'PlayerID':PlayerID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType}
        r = self.response(PARAMS,endpoint)
        return r

    def playerdashboardbylastngames(self, PlayerID):
        endpoint = 'playerdashboardbylastngames'
        PARAMS = {'PlayerID':PlayerID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType}
        r = self.response(PARAMS,endpoint)
        return r

    def playerdashboardbyopponent(self, PlayerID):
        endpoint = 'playerdashboardbyopponent'
        PARAMS = {'PlayerID':PlayerID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType}
        r = self.response(PARAMS,endpoint)
        return r

    def playerdashboardbyshootingsplits(self, PlayerID):
        endpoint = 'playerdashboardbyshootingsplits'
        PARAMS = {'PlayerID':PlayerID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType}
        r = self.response(PARAMS,endpoint)
        return r

    def playerdashboardbyteamperformance(self, PlayerID):
        endpoint = 'playerdashboardbyteamperformance'
        PARAMS = {'PlayerID':PlayerID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType}
        r = self.response(PARAMS,endpoint)
        return r

    def playerdashboardbyyearoveryear(self, PlayerID):
        endpoint = 'playerdashboardbyyearoveryear'
        PARAMS = {'PlayerID':PlayerID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType}
        r = self.response(PARAMS,endpoint)
        return r

    def playerdashptpass(self, PlayerID, TeamID):
        endpoint = 'playerdashboardbyyearoveryear'
        PARAMS = {'PlayerID':PlayerID, 'TeamID':TeamID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType}
        r = self.response(PARAMS,endpoint)
        return r

    def playerdashptreb(self, PlayerID, TeamID):
        endpoint = 'playerdashptreb'
        PARAMS = {'PlayerID':PlayerID, 'TeamID':TeamID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType}
        r = self.response(PARAMS,endpoint)
        return r

    def playerdashptreboundlogs(self, PlayerID, TeamID):
        endpoint = 'playerdashptreboundlogs'
        PARAMS = {'PlayerID':PlayerID, 'TeamID':TeamID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType}
        r = self.response(PARAMS,endpoint)
        return r

    def playerdashptshotdefend(self, PlayerID, TeamID):
        endpoint = 'playerdashptshotdefend'
        PARAMS = {'PlayerID':PlayerID, 'TeamID':TeamID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType}
        r = self.response(PARAMS,endpoint)
        return r

    def playerdashptshots(self, PlayerID, TeamID):
        endpoint = 'playerdashptshots'
        PARAMS = {'PlayerID':PlayerID, 'TeamID':TeamID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType}
        r = self.response(PARAMS,endpoint)
        return r

    def playerdashptshotlog(self, PlayerID, TeamID):
        endpoint = 'playerdashptshotlog'
        PARAMS = {'PlayerID':PlayerID, 'TeamID':TeamID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType}
        r = self.response(PARAMS,endpoint)
        return r

    def playergamelog(self, PlayerID):
        endpoint = 'playerdashptshotlog'
        PARAMS = {'PlayerID':PlayerID, 'Season':self.Season, 'SeasonType':self.SeasonType}
        r = self.response(PARAMS,endpoint)
        return r

    def playerprofile(self, PlayerID, GraphStartSeason='', GraphEndSeason=''):
        endpoint = 'playerprofile'
        PARAMS = {'PlayerID':PlayerID, 'Season':self.Season, 'GraphStartSeason':GraphStartSeason, 'GraphEndSeason':GraphEndSeason, 'GraphStat':self.Stat, 'SeasonType':self.SeasonType}
        r = self.response(PARAMS,endpoint)
        return r

    def playerprofilev2(self, PlayerID):
        endpoint = 'playerprofilev2'
        PARAMS = {'PlayerID':PlayerID,'PerMode':self.PerMode}
        r = self.response(PARAMS,endpoint)
        return r

    def playersvsplayers(self, PlayerTeamID, PlayerID1, PlayerID2, PlayerID3, PlayerID4, PlayerID5, VsTeamID, VsPlayerID1, VsPlayerID2, VsPlayerID3, VsPlayerID4, VsPlayerID5):
        endpoint = 'playersvsplayers'
        PARAMS = {'PlayerTeamID':PlayerTeamID, 'PlayerID1':PlayerID1, 'PlayerID2':PlayerID2, 'PlayerID3':PlayerID3, 'PlayerID4':PlayerID4, 'PlayerID5':PlayerID5, 'VsTeamID':VsTeamID, 'VsPlayerID1':VsPlayerID1, 'VsPlayerID2':VsPlayerID2, 'VsPlayerID3':VsPlayerID3, 'VsPlayerID4':VsPlayerID4, 'VsPlayerID5':VsPlayerID5, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'LastNGames':self.LastNGames}
        r = self.response(PARAMS,endpoint)
        return r

    def playervsplayer(self, PlayerID, VsPlayerID):
        endpoint = 'playervsplayer'
        PARAMS = {'PlayerID':PlayerID, 'VsPlayerID':VsPlayerID, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'LastNGames':self.LastNGames, 'GameSegment':self.GameSegment, 'SeasonType':self.SeasonType, 'MeasureType':self.MeasureType}
        r = self.response(PARAMS,endpoint)
        return r
    
    def shotchartdetail(self, TeamID, PlayerID, GameID, RookieYear='', ContextMeasure=''):
        endpoint = 'shotchartdetail'
        PARAMS = {'TeamID':TeamID, 'PlayerID':PlayerID, 'GameID':GameID, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'Position':self.PlayerPosition, 'RookieYear':RookieYear, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'ContextMeasure':ContextMeasure, 'SeasonType':self.SeasonType} 
        r = self.response(PARAMS,endpoint)
        return r
    
    def leaguegamelog(self, Counter=5000):
        endpoint = 'leaguegamelog'
        PARAMS = {'Counter':Counter, 'Sorter':self.Stat, 'PlayerOrTeam':self.PlayerOrTeam, 'Direction':self.Direction, 'MeasureType':self.MeasureType, 'ClutchTime':self.ClutchTime, 'AheadBehind': self.AheadBehind, 'PointDiff':self.PointDiff, 'College':self.College,'Conference':self.Conference,'Country':self.Country, 'DateFrom':self.DateFrom,'DateTo':self.DateTo, 'Division':self.Division, 'DraftPick':self.DraftPick, 'DraftYear':self.DraftYear,'GameScope':self.GameScope,'GameSegment':self.GameSegment, 'Height':self.Height, 'LastNGames':self.LastNGames, 'LeagueID':self.LeagueID,'Location':self.Location, 'Month':self.Month, 'OpponentTeamID':self.OpponentTeamID, 'Outcome':self.Outcome, 'PORound':self.PORound, 'PaceAdjust':self.PaceAdjust, 'PerMode':self.PerMode, 'Period':self.Period,'PlayerExperience':self.PlayerExperience, 'PlayerPosition':self.PlayerPosition, 'PlusMinus':self.PlusMinus, 'Rank':self.Rank, 'Season':self.Season, 'SeasonSegment':self.SeasonSegment, 'SeasonType':self.SeasonType, 'ShotClockRange':self.ShotClockRange,'StarterBench':self.StarterBench, 'TeamID':self.TeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'Weight':self.Weight}
        r = self.response(PARAMS,endpoint)
        return r
        
    def response(self, params, endpoint):
        url = 'http://stats.nba.com/stats/' + endpoint
        try:
            r = requests.get(url, params=params)
            if r.status_code==200:
                r = r.json()
                return r
            else:
                print 'Error: %s' % r.status_code
                r = {}
                return r
        except:
            print 'Request Failed'
            r = {}
            return r
class Team:
    def __init__(self, Scope=Constant.scope.Default, StatCategory=Constant.statcategory.Default, Stat=Constant.stat.Default, PlayerOrTeam=Constant.playerorteam.Team, GroupQuantity = Constant.groupquantity.Default,closestDef10=Constant.closedefdistrange.Default, CloseDefDistRange=Constant.closedefdistrange.Default, MeasureType=Constant.measuretype.Default, DistanceRange=Constant.distancerange.Default,College=Constant.college.Default, ClutchTime = Constant.clutchtime.Default, AheadBehind=Constant.aheadbehind.Default, PointDiff=Constant.pointdiff.Default, Conference=Constant.conference.Default, Country=Constant.country.Default, DateFrom=Constant.datefrom.Default, DateTo=Constant.dateto.Default, DefenseCategory=Constant.defensecategory.Default, Division=Constant.division.Default, DraftYear=Constant.draftyear.Default, DraftPick=Constant.draftpick.Default, GameScope=Constant.gamescope.Default, GameSegment=Constant.gamesegment.Default, Height=Constant.height.Default, LastNGames=Constant.lastngames.Default, LeagueID=Constant.leagueid.Default, Location=Constant.location.Default, Month=Constant.month.Default, OpponentTeamID=Constant.opponentteamid.Default,PORound=Constant.poround.Default, PerMode=Constant.permode.Default, Period=Constant.period.Default, PlayerExperience = Constant.playerexperience.Default, PlayerPosition=Constant.playerposition.Default, Season=Constant.season.Default, SeasonSegment=Constant.seasonsegment.Default, SeasonType=Constant.seasontype.Default, ShotClockRange=Constant.shotclockrange.Default, StarterBench=Constant.starterbench.Default, VsConference=Constant.vsconference.Default, VsDivision=Constant.vsdivision.Default, Weight=Constant.weight.Default, PlusMinus=Constant.plusminus.Default, PaceAdjust=Constant.paceadjust.Default, Rank=Constant.rank.Default):
        self.PlayerOrTeam = PlayerOrTeam
        self.GroupQuantity = GroupQuantity
        self.College = College
        self.Conference=Conference
        self.Country = Country
        self.DateFrom = DateFrom
        self.DateTo = DateTo
        self.Division = Division
        self.DraftPick = DraftPick
        self.DraftYear = DraftYear
        self.DefenseCategory = DefenseCategory
        self.GameScope = GameScope
        self.GameSegment = GameSegment
        self.Height = Height
        self.LastNGames = LastNGames
        self.LeagueID = LeagueID
        self.Location = Location
        self.Month = Month
        self.OpponentTeamID = OpponentTeamID
        self.PORound = PORound
        self.Period = Period
        self.PlayerExperience = PlayerExperience
        self.PerMode = PerMode
        self.PlayerPosition=PlayerPosition
        self.Season=Season
        self.SeasonSegment=SeasonSegment
        self.SeasonType=SeasonType
        self.ShotClockRange=ShotClockRange
        self.StarterBench=StarterBench
        self.VsConference = VsConference
        self.VsDivision = VsDivision
        self.Weight = Weight
        self.PaceAdjust = PaceAdjust
        self.PlusMinus = PlusMinus
        self.Rank = Rank
        self.ClutchTime = ClutchTime
        self.AheadBehind = AheadBehind
        self.PointDiff = PointDiff
        self.PlayerOrTeam = PlayerOrTeam
        self.DistanceRange = DistanceRange
        self.MeasureType = MeasureType
        self.CloseDefDistRange = CloseDefDistRange
        self.closestDef10 = closestDef10
        self.Stat = Stat
        self.StatCategory = StatCategory
        self.Scope = Scope
        
    def leagueleaders(self):
        endpoint = 'leagueleaders'
        PARAMS = {'LeagueID':self.LeagueID, 'PerMode':self.PerMode, 'Season':self.Season, 'SeasonType':self.SeasonType, 'StatCategory':self.StatCategory, 'Scope':self.Scope}
        r = self.response(PARAMS,endpoint)
        return r

    def leaguedashlineups(self):
        endpoint = 'leaguedashlineups'
        PARAMS = {'GroupQuantity':self.GroupQuantity, 'SeasonType':self.SeasonType, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames}
        r = self.response(PARAMS,endpoint)
        return r

    def leaguedashteamstats(self):
        endpoint = 'leaguedashteamstats'
        PARAMS = {'GroupQuantity':self.GroupQuantity, 'SeasonType':self.SeasonType, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames}
        r = self.response(PARAMS,endpoint)
        return r

    def leaguedashteamshotlocations(self):
        endpoint = 'leaguedashteamshotlocations'
        PARAMS = {'SeasonType':self.SeasonType, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust': self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'DistanceRange':self.DistanceRange, 'GameScope':self.GameScope, 'PlayerExperience':self.PlayerExperience, 'PlayerPosition':self.PlayerPosition, 'StarterBench':self.StarterBench}
        r = self.response(PARAMS,endpoint)
        return r

    def leaguedashteamptshot(self):
        endpoint = 'leaguedashteamptshot'
        PARAMS = {'LeagueID':self.LeagueID, 'PerMode':self.PerMode, 'Season':self.Season, 'SeasonType':self.SeasonType}
        r = self.response(PARAMS,endpoint)
        return r

    def leaguedashptteamdefend(self):
        endpoint = 'leaguedashptteamdefend'
        PARAMS = {'College':self.College,'Conference':self.Conference,'Country':self.Country, 'DateFrom':self.DateFrom,'DateTo':self.DateTo, 'DefenseCategory':self.DefenseCategory, 'Division':self.Division, 'DraftPick':self.DraftPick, 'DraftYear':self.DraftYear,'GameScope':self.GameScope,'GameSegment':self.GameSegment, 'Height':self.Height, 'LastNGames':self.LastNGames, 'LeagueID':self.LeagueID,'Location':self.Location, 'Month':self.Month, 'OpponentTeamID':self.OpponentTeamID, 'Outcome':self.Outcome, 'PORound':self.PORound, 'PerMode':self.PerMode, 'Period':self.Period,'PlayerExperience':self.PlayerExperience, 'PlayerPosition':self.PlayerPosition, 'Season':self.Season, 'SeasonSegment':self.SeasonSegment, 'SeasonType':self.SeasonType, 'StarterBench':self.StarterBench, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'Weight':self.Weight}
        r = self.response(PARAMS,endpoint)
        return r

    def leaguedashteamclutch(self):
        endpoint = 'leaguedashteamclutch'
        PARAMS = {'ClutchTime':self.ClutchTime, 'AheadBehind': self.AheadBehind, 'PointDiff':self.PointDiff, 'GameScope': self.GameScope, 'PlayerExperience':self.PlayerExperience, 'PlayerPosition':self.PlayerPosition, 'StarterBench':self.StarterBench, 'SeasonType':self.SeasonType, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust': self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames}
        r = self.response(PARAMS,endpoint)
        return r

    def shotchartdetail(self, TeamID, GameID):
        endpoint = 'shotchartdetail'
        PARAMS = {'TeamID':TeamID, 'GameID':GameID, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'GROUP_ID':'', 'ContextMeasure':'', 'ContextFilter':'', 'SeasonType':self.SeasonType} 
        r = self.response(PARAMS,endpoint)
        return r

    def teamdashboardbyclutch(self, TeamID):
        endpoint = 'teamdashboardbyclutch'
        PARAMS = {'TeamID':TeamID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType} 
        r = self.response(PARAMS,endpoint)
        return r

    def teamdashboardbygamesplits(self, TeamID):
        endpoint = 'teamdashboardbygamesplits'
        PARAMS = {'TeamID':TeamID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType} 
        r = self.response(PARAMS,endpoint)
        return r

    def teamdashboardbygeneralsplits(self, TeamID):
        endpoint = 'teamdashboardbygeneralsplits'
        PARAMS = {'TeamID':TeamID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType} 
        r = self.response(PARAMS,endpoint)
        return r

    def teamdashboardbylastngames(self, TeamID):
        endpoint = 'teamdashboardbylastngames'
        PARAMS = {'TeamID':TeamID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType} 
        r = self.response(PARAMS,endpoint)
        return r

    def teamdashboardbyopponent(self, TeamID):
        endpoint = 'teamdashboardbyopponent'
        PARAMS = {'TeamID':TeamID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType} 
        r = self.response(PARAMS,endpoint)
        return r

    def teamdashboardbyshootingsplits(self, TeamID):
        endpoint = 'teamdashboardbyshootingsplits'
        PARAMS = {'TeamID':TeamID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType} 
        r = self.response(PARAMS,endpoint)
        return r

    def teamdashboardbyteamperformance(self, TeamID):
        endpoint = 'teamdashboardbyteamperformance'
        PARAMS = {'TeamID':TeamID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType} 
        r = self.response(PARAMS,endpoint)
        return r

    def teamdashboardbyyearoveryear(self, TeamID):
        endpoint = 'teamdashboardbyyearoveryear'
        PARAMS = {'TeamID':TeamID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType} 
        r = self.response(PARAMS,endpoint)
        return r

    def teamdashlineups(self, GameID, TeamID):
        endpoint = 'teamdashlineups'
        PARAMS = {'GroupQuantity':self.GroupQuantity, 'GameID':GameID, 'TeamID':TeamID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType}
        r = self.response(PARAMS,endpoint)
        return r

    def teamdashptpass(self, TeamID):
        endpoint = 'teamdashlineups'
        PARAMS = {'TeamID':TeamID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType} 
        r = self.response(PARAMS,endpoint)
        return r

    def teamdashptreb(self, TeamID):
        endpoint = 'teamdashptreb'
        PARAMS = {'TeamID':TeamID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType} 
        r = self.response(PARAMS,endpoint)
        return r

    def teamdashptshots(self, TeamID):
        endpoint = 'teamdashptshots'
        PARAMS = {'TeamID':TeamID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType} 
        r = self.response(PARAMS,endpoint)
        return r

    def teamgamelog(self, TeamID):
        endpoint = 'teamgamelog'
        PARAMS = {'TeamID':TeamID, 'Season':self.Season, 'SeasonType':self.SeasonType} 
        r = self.response(PARAMS,endpoint)
        return r

    def teamplayerdashboard(self, TeamID):
        endpoint = 'teamplayerdashboard'
        PARAMS = {'TeamID':TeamID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType} 
        r = self.response(PARAMS,endpoint)
        return r

    def teamplayeronoffdetails(self, TeamID):
        endpoint = 'teamplayeronoffdetails'
        PARAMS = {'TeamID':TeamID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType} 
        r = self.response(PARAMS,endpoint)
        return r

    def teamvsplayer(self, TeamID, VsPlayerID):
        endpoint = 'teamvsplayer'
        PARAMS = {'TeamID':TeamID, 'VsPlayerID':VsPlayerID, 'MeasureType':self.MeasureType, 'PerMode':self.PerMode, 'PlusMinus':self.PlusMinus, 'PaceAdjust':self.PaceAdjust, 'Rank':self.Rank, 'Season':self.Season, 'Outcome':self.Outcome, 'Location':self.Location, 'Month':self.Month, 'SeasonSegment':self.SeasonSegment, 'DateFrom':self.DateFrom, 'DateTo':self.DateTo, 'OpponentTeamID':self.OpponentTeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'GameSegment':self.GameSegment, 'Period':self.Period, 'LastNGames':self.LastNGames, 'SeasonType':self.SeasonType} 
        r = self.response(PARAMS,endpoint)
        return r

    def teamyearbyyearstats(self, TeamID):
        endpoint = 'teamyearbyyearstats'
        PARAMS = {'TeamID':TeamID, 'PerMode':self.PerMode, 'LeagueID':self.LeagueID, 'SeasonType':self.SeasonType} 
        r = self.response(PARAMS,endpoint)
        return r
    
    def leaguegamelog(self, Counter='5000'):
        endpoint = 'leaguegamelog'
        PARAMS = {'Counter':Counter, 'Sorter':self.Stat, 'PlayerOrTeam':self.PlayerOrTeam, 'Direction':self.Direction, 'MeasureType':self.MeasureType, 'ClutchTime':self.ClutchTime, 'AheadBehind': self.AheadBehind, 'PointDiff':self.PointDiff, 'College':self.College,'Conference':self.Conference,'Country':self.Country, 'DateFrom':self.DateFrom,'DateTo':self.DateTo, 'Division':self.Division, 'DraftPick':self.DraftPick, 'DraftYear':self.DraftYear,'GameScope':self.GameScope,'GameSegment':self.GameSegment, 'Height':self.Height, 'LastNGames':self.LastNGames, 'LeagueID':self.LeagueID,'Location':self.Location, 'Month':self.Month, 'OpponentTeamID':self.OpponentTeamID, 'Outcome':self.Outcome, 'PORound':self.PORound, 'PaceAdjust':self.PaceAdjust, 'PerMode':self.PerMode, 'Period':self.Period,'PlayerExperience':self.PlayerExperience, 'PlayerPosition':self.PlayerPosition, 'PlusMinus':self.PlusMinus, 'Rank':self.Rank, 'Season':self.Season, 'SeasonSegment':self.SeasonSegment, 'SeasonType':self.SeasonType, 'ShotClockRange':self.ShotClockRange,'StarterBench':self.StarterBench, 'TeamID':self.TeamID, 'VsConference':self.VsConference, 'VsDivision':self.VsDivision, 'Weight':self.Weight}
        r = self.response(PARAMS,endpoint)
        return r
        
    def response(self, params, endpoint):
        url = 'http://stats.nba.com/stats/' + endpoint
        try:
            r = requests.get(url, params=params)
            if r.status_code==200:
                r = r.json()
                return r
            else:
                print 'Error: %s' % r.status_code
                r = {}
                return r
        except:
            print 'Request Failed'
            r = {}
            return r

class playbyplay:
    def __init__(self, StartPeriod=Constant.startperiod.Default, EndPeriod= Constant.endperiod.Default):
        self.StartPeriod = StartPeriod
        self.EndPeriod = EndPeriod
        
    def playbyplay(self, GameID):
        endpoint = 'playbyplay'
        PARAMS = {'GameID':GameID, 'StartPeriod':self.StartPeriod, 'EndPeriod':self.EndPeriod}
        r = self.response(PARAMS, endpoint)
        if len(r)>0:
            try:
                df = pd.DataFrame(data=r['resultSets'][0]['rowSet'], columns=r['resultSets'][0]['headers'])
            except:
                df = pd.DataFrame()
        else:
            df=pd.DataFrame()
        return df

    def playbyplayv2(self, GameID):
        endpoint = 'playbyplayv2'
        PARAMS = {'GameID':GameID, 'StartPeriod':self.StartPeriod, 'EndPeriod':self.EndPeriod}
        r = self.response(PARAMS, endpoint)
        if len(r)>0:
            try:
                df = pd.DataFrame(data=r['resultSets'][0]['rowSet'], columns=r['resultSets'][0]['headers'])
            except:
                df = pd.DataFrame()
        else:
            df=pd.DataFrame()
        return df
    
    def response(self, params, endpoint):
        url = 'http://stats.nba.com/stats/' + endpoint
        try:
            r = requests.get(url, params=params)
            if r.status_code==200:
                r = r.json()
                return r
            else:
                print 'Error: %s' % r.status_code
                r = {}
                return r
        except:
            print 'Request Failed'
            r = {}
            return r
    
class misc:
    def __init__(self, LeagueID = Constant.leagueid.Default):
        self.LeagueID = LeagueID
        
    def playoffpicture(self, SeasonID):
        endpoint = 'playoffpicture'
        PARAMS = {'SeasonID':SeasonID, 'LeagueID':self.LeagueID}
        r = self.response(PARAMS, endpoint)
        return r
    
    def videoStatus(self, GameDate):
        endpoint = 'videoStatus'
        PARAMS = {'GameDate':GameDate, 'LeagueID':self.LeagueID} 
        r = self.response(PARAMS, endpoint)
        return r
        
    def response(self, params, endpoint):
        url = 'http://stats.nba.com/stats/' + endpoint
        try:
            r = requests.get(url, params=params)
            if r.status_code==200:
                r = r.json()
                return r
            else:
                print 'Error: %s' % r.status_code
                r = {}
                return r
        except:
            print 'Request Failed'
            r = {}
            return r

class scoreboard:
    baseurl = 'http://stats.nba.com/stats/'
    def __init__(self, LeagueID = Constant.leagueid.Default):
        self.LeagueID = LeagueID
        
    def scoreboard(self, GameDate, DayOffSet='0'):
        endpoint = 'scoreboard'
        PARAMS = {'GameDate':GameDate, 'DayOffset':DayOffSet, 'LeagueID':self.LeagueID}
        try:
            r = self.response(PARAMS, endpoint)
            df = pd.DataFrame(data=r['resultSets'][0]['rowSet'], columns=r['resultSets'][0]['headers'])
            df = df[['GAME_DATE_EST', 'GAME_ID', 'GAMECODE', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'SEASON']]
            df["VISITOR_TEAM_ABBREVIATION"] = df["GAMECODE"].str.extract('.*?/(\w{3}).+')
            df["HOME_TEAM_ABBREVIATION"] = df["GAMECODE"].str.extract('.+/.+(\w{3})')
            df = df[(df['VISITOR_TEAM_ID']>13000)]
            df = df[df['HOME_TEAM_ID']>13000]
            engine = sqlalchemy.create_engine("postgresql+psycopg2://postgres:Rory09074830@localhost:5432/Basketball")
            df.to_sql('NBA_Schedule', engine, schema='public', if_exists='append', index =False)
            engine.dispose()
        except:
            df=pd.DataFrame()
        return df
    
    def response(self, params, endpoint):
        url = 'http://stats.nba.com/stats/' + endpoint
        try:
            r = requests.get(url, params=params)
            if r.status_code==200:
                r = r.json()
                return r
            else:
                print 'Error: %s' % r.status_code
                r = {}
                return r
        except:
            print 'Request Failed'
            r = {}
            return r

class events:
    def locations_getmoments(self, GameID, EventID):
        endpoint = 'locations_getmoments'
        PARAMS = {'GameID':GameID, 'EventID':EventID} 
        r = self.response(PARAMS, endpoint)
        if len(r)>0:
            try:
                headers = ["TeamID", "PlayerID", "x_loc", "y_loc", 
                   "Radius", "MomentID", "GameClock", "ShotClock", "EventID"]
                player_moments = []
                moments = r['moments']
                for moment in moments:
                    for player in moment[5]:
                        player.extend((moments.index(moment), moment[2], moment[3], EventID))
                        player_moments.append(player)
                df = pd.DataFrame(player_moments, columns=headers)
            except:
                df = pd.DataFrame()
        else:
            df=pd.DataFrame()
        return df

    def locations_getallmoments(self, GameID, limit):
        endpoint = 'locations_getmoments'
        df = pd.DataFrame()
        for i in range(1,int(limit)):
            PARAMS = {'GameID':GameID, 'EventID':str(i)} 
            r = self.response(PARAMS, endpoint)
            if len(r)>0:
                try:
                    headers = ["TeamID", "PlayerID", "x_loc", "y_loc", 
                       "Radius", "MomentID", "GameClock", "ShotClock", "EventID"]
                    player_moments = []
                    moments = r['moments']
                    for moment in moments:
                        for player in moment[5]:
                            player.extend((moments.index(moment), moment[2], moment[3], i))
                            player_moments.append(player)
                    temp = pd.DataFrame(player_moments, columns=headers)
                    df = pd.concat([df, temp])
                    print i
                except:
                    continue
            else:
                continue
        return df
    
    def response(self, params, endpoint):
        url = 'http://stats.nba.com/stats/' + endpoint
        try:
            r = requests.get(url, params=params)
            if r.status_code==200:
                r = r.json()
                return r
            else:
                print 'Error: %s' % r.status_code
                r = {}
                return r
        except:
            print 'Request Failed'
            r = {}
            return r