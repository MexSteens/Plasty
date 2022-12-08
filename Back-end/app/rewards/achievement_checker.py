from app.database.model import Achievement, UserAchievement
import app.rewards.achievements
import logging


def AchievementChecker(user):
    # Read all rewards data.
    achievements = Achievement.read()

    # Read all achievements' user already has.
    user_achievements = [user_achievement.achievement_code for user_achievement in
                         UserAchievement.read(user_id=user.id)]

    achievements_rewarded = []

    for achievement in achievements:
        # If rewards is already owned by the user skip the rewards
        if achievement.code in user_achievements:
            continue

        # Retrieve the rewards function
        try:
            achievement_function = app.rewards.achievements.__getattribute__(achievement.code)

            # Execute the rewards function if successful the user will be rewarded with the rewards.
            if achievement_function(user):
                user.reward_achievement(achievement.code)
                achievements_rewarded.append([achievement.code, achievement.experience_given])
        except AttributeError:
            logging.error(f"Achievement {achievement} has no function to be executed.")

    return achievements_rewarded
