def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[-1][1]


def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    racers[0], racers[-1] = racers[-1], racers[0]
    
def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    if name in arrivals:
        guests = len(arrivals) # num de invitados
        arrival = arrivals.index(name) # orden en el que llego [name]
        fashion_limit = guests/2 if guests % 2 == 0 else guests/2 + 1
        if arrival + 1 > fashion_limit:
            if arrivals[arrival] != arrivals[-1]:
                return True
            else: 
                return False
        else:
            return False
            
# print(fashionably_late(["Ana", "Damian", "Juan", "Pedro", "Luisa", "Carlos"], "Carlos"))