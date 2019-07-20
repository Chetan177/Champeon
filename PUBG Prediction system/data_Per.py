class data_per:
    def __init__(self,userid):
        self.userid = userid
        
        # performance information   json structure : match_stat['included']['attributes']['stats']
        self.assists=list()         #  "assists": 0
        self.boosts=list()          #  "boosts": 1
        self.damageDealt=list()     #  "damageDealt": 51.5855179   
        self.DBNOs=list()           #  "DBNOs": 0  
        self.headshotKills=list()   #  "headshotKills": 0
        self.heals=list()           #  "heals": 4
        self.killPlace=list()       #  "killPlace": 63 
        self.kills=list()           #   "killStreaks": 0
        self.killStreaks=list()     #   "kills": 0
        self.longestKill=list()     #   "longestKill": 0
        self.revives=list()         #   "revives": 1
        self.rideDistance=list()    #   "rideDistance": 0
        self.roadKills=list()       #   "roadKills": 0
        self.swimDistance=list()    #   "swimDistance": 0
        self.teamKills=list()       #   "teamKills": 0
        self.vehicleDestroys=list() #   "vehicleDestroys": 0
        self.walkDistance=list()    #   "walkDistance": 453.932983
        self.weaponsAcquired=list() #   "weaponsAcquired": 2
        # match Information             json structure : match_stat['data']
        self.matchDuration=list()   #   "duration": 1828,
        
        
        # return object conatiner
        self.data = tuple()

    def set_perf_info(self,per_info):
        self.assists.append(per_info["assists"])
        self.boosts.append(per_info["boosts"])
        self.damageDealt.append(per_info["damageDealt"])  
        self.DBNOs.append(per_info["DBNOs"]) 
        self.headshotKills.append(per_info["headshotKills"])
        self.heals.append(per_info["heals"])
        self.killPlace.append(per_info["killPlace"]) 
        self.kills.append(per_info["killStreaks"])
        self.killStreaks.append(per_info["kills"])
        self.longestKill.append(per_info["longestKill"])
        self.revives.append(per_info["revives"])
        self.rideDistance.append(per_info["rideDistance"])
        self.roadKills.append(per_info["roadKills"])
        self.swimDistance.append(per_info["swimDistance"])
        self.teamKills.append(per_info["teamKills"])
        self.vehicleDestroys.append(per_info["vehicleDestroys"])
        self.walkDistance.append( per_info["walkDistance"])
        self.weaponsAcquired.append(per_info["weaponsAcquired"])




    def set_match_stat(self,match_id,match_attributes):
        self.matchDuration.append(match_attributes["duration"])
        
            #   "match_id":"caa3ffcf-cecf-4ade-8cfc-e3f45b9eb4c1"

    def return_data(self):
                                            # INDECES
        self.data = (   self.assists,       # 0 
                        self.boosts,        # 1
                        self.damageDealt,   # 2
                        self.DBNOs,         # 3
                        self.headshotKills, # 4
                        self.heals,         # 5
                        self.killPlace,     # 6
                        self.kills,         # 7
                        self.killStreaks,   # 8
                        self.longestKill,   # 9
                        self.matchDuration, # 10
                        self.revives,       # 11
                        self.rideDistance,  # 12
                        self.roadKills,     # 13
                        self.swimDistance,  # 14
                        self.teamKills,     # 15
                        self.vehicleDestroys,# 16
                        self.walkDistance,  # 17
                        self.weaponsAcquired,# 18
                        
                )

        return self.data
