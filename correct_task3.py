# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
def average_valid_measurements(values):
    """
    Calculates the average of valid measurements, ignoring None and non-numeric values.
    
    Args:
        values (list): A list of measurements which may include None or non-numeric types.
        
    Returns:
        float: The average of valid numeric measurements. Returns 0.0 if no valid measurements are found.
    """
    if not values:
        return 0.0

    valid_measurements = []
    for v in values:
        if v is not None:
            try:
                valid_measurements.append(float(v))
            except (ValueError, TypeError):
                # Skip values that cannot be converted to float
                continue
    
    if not valid_measurements:
        return 0.0
        
    return sum(valid_measurements) / len(valid_measurements)
