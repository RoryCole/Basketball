# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 08:49:20 2015

@author: rorycole
"""
#PARAMS AND CONSTANTS
class _DefaultN:
    Default = 'N'

class _DefaultBlank:
    Default = ''

class _DefaultZero:
    Default = '0'

class leagueid:
    NBA = '00'
    Default = NBA

class weight(_DefaultBlank):
    All = ''
    Over200 = 'GT 200'
    Under200 = 'LT 200'
    Over225 = 'GT 225'
    Under225 = 'LT 225'
    Over250 = 'GT 250'
    Under250 = 'LT 250'
    Over275 = 'GT 275'
    Under275 = 'LT 275'
    Over300 = 'GT 300'
    Under300 = 'LT 300'

class season:
    Current = '2015-16'
    Default = Current
    
class ptmeasuretype():
    CatchAndShoot = 'CatchShoot'
    Defense = 'Defense'
    Drives = 'Drives'
    Passing = 'Passing'
    TouchesAndPossessions = 'Possessions'
    PullUpShooting = 'PullUpShot'
    Rebounding = 'Rebounding'
    ShootingEfficiency = 'Efficiency'
    SpeedAndDistance = 'SpeedDistance'
    ElbowTouch = 'ElbowTouch'
    PostTouch = 'PostTouch'
    PaintTouch = 'PaintTouch'

class poround(_DefaultBlank):
    All = ''
    ConferenceQuarters = '1'
    ConferenceSemis = '2'
    ConferenceFinals = '3'
    Finals = '4'

class height(_DefaultBlank):
    All = ''
    Over6 = 'GT 6-0'
    Under6 = 'LT 6-0'
    Over63 = 'GT 6-3'
    Under63 = 'LT 6-3'
    Over67 = 'GT 6-7'
    Under67 = 'LT 6-7'
    Over610 = 'GT 6-10'
    Under610 = 'LT 6-10'
    Over7 = 'GT 7-0'
    Under7 = 'LT 7-0'

class country(_DefaultBlank):
    pass

class playerexperience(_DefaultBlank):
    All = ''
    Rookie = 'Rookie'
    Sophomore = 'Sophomore'
    Veteran = 'Veteran'
    
class playerposition(_DefaultBlank):
    All = ''
    Centre = 'C'
    Guard = 'G'
    Forward = 'F'
    
class college(_DefaultBlank):
    pass

class conference(_DefaultBlank):
    All = ''
    East = 'East'
    West = 'West'

class draftpick(_DefaultBlank):
    pass

class draftyear(_DefaultBlank):
    pass

class division(_DefaultBlank):
    All = ''
    Atlantic = 'Atlantic'
    Central = 'Central'
    Northwest = 'Northwest'
    Pacific = 'Pacific'
    Southeast = 'Southeast'
    Southwest = 'Southwest'

class pointdiff:
    LessThan5 = '5'
    LessThan4 = '4'
    LessThan3 = '3'
    LessThan2 = '2'
    LessThan1 = '1'
    Default = LessThan5

class clutchtime:
    mins5 = 'Last 5 Minutes'
    mins4 = 'Last 4 Minutes'
    mins3 = 'Last 3 Minutes'
    mins2 = 'Last 2 Minutes'
    mins1 = 'Last 1 Minutes'
    secs30 = 'Last 30 Seconds'
    secs10 = 'Last 10 Seconds'
    Default = mins5
    
class aheadbehind:
    All = 'Ahead or Behind'
    BehindOrTied = 'Behind or Tied'
    AheadOrTied = 'Ahead or Tied'
    Default = All
    
class permode:
    Totals = 'Totals'
    PerGame = 'PerGame'
    MinutesPer = 'MinutesPer'
    Per48 = 'Per48'
    Per40 = 'Per40'
    Per36 = 'Per36'
    PerMinute = 'PerMinute'
    PerPossession = 'PerPossession'
    PerPlay = 'PerPlay'
    Per100Possessions = 'Per100Possessions'
    Per100Plays = 'Per100Plays'
    Default = Totals

class seasontype:
    Regular = 'Regular Season'
    Playoffs = 'Playoffs'
    Default = Regular

class measuretype:
    Traditional = 'Base'
    Advanced = 'Advanced'
    Misc = 'Misc'
    FourFactors = 'Four Factors'
    Scoring = 'Scoring'
    Opponent = 'Opponent'
    Usage = 'Usage'
    Default = Traditional

class groupquantity:
    Default = 5

class outcome(_DefaultBlank):
    Win = 'W'
    Loss = 'L'

class location(_DefaultBlank):
    Home = 'Home'
    Away = 'Away'

class seasonsegment(_DefaultBlank):
    EntireSeason = ''
    PreAllStar = 'Pre All-Star'
    PostAllStar = 'Post All-Star'

class datefrom(_DefaultBlank):
    pass

class dateto(_DefaultBlank):
    pass

class vsconference(_DefaultBlank):
    All = ''
    East = 'East'
    West = 'West'

class vsdivision(_DefaultBlank):
    All = ''
    Atlantic = 'Atlantic'
    Central = 'Central'
    Northwest = 'Northwest'
    Pacific = 'Pacific'
    Southeast = 'Southeast'
    Southwest = 'Southwest'

class gamesegment(_DefaultBlank):
    EntireGame = ''
    FirstHalf = 'First Half'
    SecondHalf = 'Second Half'
    Overtime = 'Overtime'

class shotclockrange(_DefaultBlank):
    AllRanges = ''
    ShotClockOff = 'ShotClock Off'

    def get(self, n):
        if n > 24 or n < 0:
            return ''
        elif 22 <= n <= 24:
            return '24-22'
        elif 18 <= n < 22:
            return '22-18 Very Early'
        elif 15 <= n < 18:
            return '18-15 Early'
        elif 7 <= n < 15:
            return '15-7 Average'
        elif 4 <= n < 7:
            return '7-4 Late'
        elif 0 <= n < 4:
            return '4-0 Very Late'

class dribblerange:
    All = ''
    NoDribble = '0 Dribbles'
    Dribble1 = '1 Dribble'
    Dribble2 = '2 Dribbles'
    Between3and6Dribbles = '3-6 Dribbles'
    Over7Dribbles = '7+ Dribbles'

class closedefdistrange:
    All = ''
    VeryTight = '0-2 Feet - Very Tight'
    Tight = '2-4 Feet - Tight'
    Open = '4-6 Feet - Open'
    WideOpen = '6+ Feet - Wide Open'
    Between2And4 = '2-4 Feet - Tight'
    
    Default = All
    
class generalrange:
    All = ''
    Overall = 'Overall'
    CatchAndShoot = 'Catch and Shoot'
    PullUp = 'Pull Up'
    Under10Ft = 'Less than 10 ft'
    Default = All

class plusminus(_DefaultN):
    pass

class paceadjust(_DefaultN):
    pass

class rank(_DefaultN):
    pass

class opponentteamid(_DefaultZero):
    pass

class period(_DefaultZero):
    AllQuarters = '0'
    FirstQuarter = '1'
    SecondQuarter = '2'
    ThirdQuarter = '3'
    FourthQuarter = '4'
    def Overtime(self, n):
        return str(4 + n)

class lastngames(_DefaultZero):
    pass

class playoffround(_DefaultZero):
    All = '0'
    QuarterFinals = '1'
    SemiFinals = '2'
    ConferenceFinals = '3'
    Finals = '4'

class month(_DefaultZero):
    All = '0'
    October = '1'
    Novemeber = '2'
    December = '3'
    January = '4'
    February = '5'
    March = '6'
    April = '7'
    May = '8'
    June = '9'
    July = '10'
    August = '11'
    September = '12'

class rangetype(_DefaultZero):
    pass

class startrange(_DefaultZero):
    pass

class endrange(_DefaultZero):
    pass

class startperiod(period):
    pass

class endperiod(period):
    pass

class stat:
    PTS = 'PTS'
    FGM = 'FGM'
    FGA = 'FGA'
    FG_PCT = 'FG%'
    FG3M = '3PM'
    FG3A = '3PA'
    FG3_PCT = '3P%'
    FTM = 'FTM'
    FTA = 'FTA'
    FT_PCT = 'FT%'
    OREB = 'OREB'
    DREB = 'DREB'
    REB = 'REB'
    AST = 'AST'
    STL = 'STL'
    BLK = 'BLK'
    TOV = 'TOV'
    EFF = 'EFF'
    AST_TOV = 'AST/TO'
    STL_TOV = 'STL/TOV'
    PF = 'PF'
    Default = PTS
    
class statcategory:
    Points = 'Points'
    Rebounds = 'Rebounds'
    Assists = 'Assists'
    Defense = 'Defense'
    Clutch = 'Clutch'
    Playmaking = 'Playmaking'
    Efficiency = 'Efficiency'
    FastBreak = 'Fast Break'
    Scoring = 'ScoringBreakdown'
    Default = Points
    
class scope:
    AllPlayers = 'S'
    Rookies = 'Rookies'
    Default = AllPlayers

class playerscope:
    AllPlayers = 'All Players'
    Rookies = 'Rookie'
    Default = AllPlayers

class playerorteam:
    Player = 'Player'
    Team = 'Team'
    Default = Player

class gamescope:
    Season = 'Season'
    Last10 = 'Last 10'
    Yesterday = 'Yesterday'
    Finals = 'Finals'
    Default = Season
    
class distancerange:
    Zone = 'By Zone'
    Ft5 = '5ft Range'
    Ft8 = '8ft Range'
    Default = Zone
    
class counter:
    Default = 1500
    
class direction:
    Desc = 'DESC'
    Asc = 'ASC'
    Default = Desc
    
class defensecategory:
    Overall = 'Overall'
    Point2 = '2 Pointers'
    Point3 = '3 Pointers'
    Under6Ft = 'Less Than 6Ft'
    Under10Ft = 'Less Than 10Ft'
    Over15Ft = 'Greater Than 15Ft'
    Default = Overall
    
class starterbench:
    All = ''
    Default=All
    
class teamid:
    All = '0'
    Default=All