def study_schedule(permanence_period, target_time):
    if type(target_time) is not int:
        return None

    count = 0

    for get_entrance, get_exit in permanence_period:
        if type(get_entrance) is not int or type(get_exit) is not int:
            return None
        if get_entrance <= target_time <= get_exit:
            count += 1

    return count
