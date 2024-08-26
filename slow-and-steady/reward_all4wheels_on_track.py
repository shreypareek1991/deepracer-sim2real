def reward_function(params):
    '''
    Example of penalizing the agent if all four wheels are off track.
    '''
    reward = 1e-3
    
    # Penalize if the car goes off track
    if not params['all_wheels_on_track']:
        # large penaly for off track
        return float(-20)

    # positive reward if stays on track
    reward += 1
  
    return float(reward)
