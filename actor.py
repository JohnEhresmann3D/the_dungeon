from Character_Options import Stats

class Actor():
    actor_stats = {}
    
    #setting stats
    actor_stats[Stats.Str] = 0
    actor_stats[Stats.Dex] = 0
    actor_stats[Stats.Con] = 0
    actor_stats[Stats.Int] = 0
    actor_stats[Stats.Wis] = 0
    actor_stats[Stats.Cha] = 0

    #setting hit_points
    actor_hit_dice = 0
    actor_hit_points = 0
