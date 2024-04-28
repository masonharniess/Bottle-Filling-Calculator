import random


# Function to calculate the total time it takes to fill a collection of bottles given a number of taps
def calculate_seconds_to_fill_bottles(bottle_sizes, taps_quantity, flow_rates=None):
    # Validate bottle_sizes input
    if not isinstance(bottle_sizes, list):
        raise ValueError("The bottle_sizes argument must be a list.")

    # Validate values in bottle_sizes input
    if not all(isinstance(bottle, (int, float)) and bottle >= 0 for bottle in bottle_sizes):
        raise ValueError("The size of each bottle in bottle_sizes must be a non-negative number.")

    # Validate taps_quantity input
    if not isinstance(taps_quantity, int) or taps_quantity <= 0:
        raise ValueError("The taps_quantity argument must be a positive integer.")

    # If flow_rates input is not provided, provide default value of 100ml for each tap
    if flow_rates is None:
        flow_rates = [100] * taps_quantity
    else:
        # Validate flow_rates input
        if not isinstance(flow_rates, list) or len(flow_rates) != taps_quantity:
            raise ValueError("The flow_rates must be a list with a length equal to taps_quantity.")

        # Validate values in flow_rates input
        if not all(isinstance(rate, (int, float)) and rate > 0 for rate in flow_rates):
            raise ValueError("The flow rate in flow_rates of each tap must be a positive number.")

    # Calculate how many times flow_rates need to be repeated to ensure there is at least one flow rate for each bottle
    repeats_needed = (len(bottle_sizes) // len(flow_rates)) + 1

    # Create a list of flow rates repeated by the value derived in the calculation above.
    extended_flow_rates = flow_rates * repeats_needed

    # Pair each bottle size with a flow rate in a tuple.
    paired_bottles_and_rates = zip(bottle_sizes, extended_flow_rates)

    # Calculate time required to fill each bottle and
    times_to_fill = []
    for bottle, rate in paired_bottles_and_rates:
        time_to_fill_one_bottle = (bottle / rate) + 5  # calculate filling time for a singular bottle + set up time
        times_to_fill.append(time_to_fill_one_bottle)  # append each calculated time to the list of fill times

    # If the number of taps is equal or greater than the number of bottles, return the longest time to fill a bottle
    if taps_quantity >= len(times_to_fill):
        return max(times_to_fill)

    # Distribute workload amongst taps to ensure minimum amount of time possible
    active_tap_times = [0] * taps_quantity  # initialise list to hold times that each tap has been active
    for bottle in times_to_fill:
        shortest_time_index = active_tap_times.index(min(active_tap_times))  # find tap index with smallest active time
        active_tap_times[shortest_time_index] += bottle  # update cumulative active time of tap with smallest active time

    # Return the time active of the busiest tap
    return max(active_tap_times)


# Function to return situations where increasing flow rate of at least one tap increases the total time needed
def test_flow_rates(taps_quantity, max_bottle_size, num_permutations, max_flow_rate):
    # Loop through as many tests as was specified by num_permutations
    for _ in range(num_permutations):
        # Generate a list of random bottles sizes for the current test
        bottle_sizes = [random.randint(100, max_bottle_size) for _ in range(taps_quantity + random.randint(0, 2))]

        # Generate a list of flow rates, one for each tap
        flow_rates = [random.randint(50, 100) for _ in range(taps_quantity)]

        # Call function to get an initial time with specified values
        initial_time = calculate_seconds_to_fill_bottles(bottle_sizes, taps_quantity, flow_rates)

        # Calculate how many taps will be increased
        num_taps_to_increase = random.randint(1, taps_quantity)
        print(num_taps_to_increase)

        # Select which taps will be increased
        taps_to_increase = random.sample(range(taps_quantity), num_taps_to_increase)

        # Increase the flow rate of the selected taps
        new_flow_rates = flow_rates.copy()  # copy list of flow rates into new list
        for tap_index in taps_to_increase:
            new_flow_rates[tap_index] = random.randint(flow_rates[tap_index] + 1, max_flow_rate)  # increase the flow rate of a tap

        # Call function to get a new time with specified values and at least one increased flow rate
        new_time = calculate_seconds_to_fill_bottles(bottle_sizes, taps_quantity, new_flow_rates)

        # Print results if a case is found where increasing a flow rate leads to a longer time
        if new_time > initial_time:
            print(f"Found a case where increasing flow rate increases total time:")
            print(f"Bottle sizes: {bottle_sizes}")
            print(f"Initial rates: {flow_rates}, Modified rates: {new_flow_rates}")
            print(f"Initial time: {initial_time}, New time: {new_time}")


# Call function to calculate time needed
time_to_fill_bottles = (
    calculate_seconds_to_fill_bottles(bottle_sizes=[300, 500, 800], taps_quantity=2, flow_rates=[100, 100]))

# Print results of function
print(f"Time required to fill bottles: {time_to_fill_bottles}s")

# Call test
test_flow_rates(taps_quantity=3, max_bottle_size=1500, num_permutations=10, max_flow_rate=200)
