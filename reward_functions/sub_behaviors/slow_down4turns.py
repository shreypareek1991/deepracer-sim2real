def reward_function(params):
    """
    Example of rewarding the agent to slow down for turns
    """
    reward = 1e-3

    # fast on straights and slow on curves
    steering_angle = params["steering_angle"]
    speed = params["speed"]

    # set a steering threshold above which angles are considered large
    # you can change this based on your action space
    STEERING_THRESHOLD = 15

    if abs(steering_angle) > STEERING_THRESHOLD:
        if speed < 1:
            # slow speeds are awarded large positive rewards
            reward += 2.0
        elif speed < 2:
            # faster speeds are awarded smaller positive rewards
            reward += 0.5
        # reduce zigzagging behavior by penalizing large steering angles
        reward *= 0.85

    return float(reward)
