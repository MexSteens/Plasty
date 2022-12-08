def LevelChecker(user):
    levels_gained = 0

    while user.experience >= user.exp_needed():
        exp_needed = user.experience - user.exp_needed()

        user.level_up()
        user.experience = exp_needed
        levels_gained += 1

    return levels_gained
