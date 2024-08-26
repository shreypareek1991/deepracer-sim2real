def reward_function(params):
    """
    Example of fast agent that leaves the track and also is crash prone.
    But it is FAAAST
    """

    # Steering penality threshold
    ABS_STEERING_THRESHOLD = 15

    reward = 1e-3
    # Read input parameters
    track_width = params["track_width"]
    distance_from_center = params["distance_from_center"]

    # Penalize if the car goes off track
    if not params["all_wheels_on_track"]:
        return float(1e-3)

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward += 1.0
    elif distance_from_center <= marker_2:
        reward += 0.5
    elif distance_from_center <= marker_3:
        reward += 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    # fast on straights and slow on curves
    steering_angle = params["steering_angle"]
    speed = params["speed"]

    # straights
    if -5 < steering_angle < 5:
        if speed > 2.5:
            reward += 2.0
        elif speed > 2:
            reward += 1.0
    elif steering_angle < -15 or steering_angle > 15:
        if speed < 1.8:
            reward += 1.0
        elif speed < 2.2:
            reward += 0.5

    # Penalize reward if the car is steering too much
    if abs(steering_angle) > ABS_STEERING_THRESHOLD:
        reward *= 0.75

    # Reward lower steps
    steps = params["steps"]
    progress = params["progress"]
    step_reward = (progress / steps) * 5 * speed * 2

    reward += step_reward

    return float(reward)
