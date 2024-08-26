def reward_function(params):
    """
    Example reward function to train a slow and steady agent
    """
    STEERING_THRESHOLD = 15
    OFFTRACK_PENALTY = -20

    # initialize small non-zero positive reward
    reward = 1e-3

    # Read input parameters
    track_width = params["track_width"]
    distance_from_center = params["distance_from_center"]

    # Penalize if the car goes off track
    if not params["all_wheels_on_track"]:
        return float(OFFTRACK_PENALTY)

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward += 2.0
    elif distance_from_center <= marker_2:
        reward += 0.25
    elif distance_from_center <= marker_3:
        reward += 0.05
    else:
        reward = OFFTRACK_PENALTY  # likely crashed/ close to off track

    # fast on straights and slow on curves
    steering_angle = params["steering_angle"]
    speed = params["speed"]

    if abs(steering_angle) > STEERING_THRESHOLD:
        if speed < 1:
            reward += 2.0
        elif speed < 2:
            reward += 0.5
        # reduce zigzagging behavior
        reward *= 0.85

    return float(reward)
