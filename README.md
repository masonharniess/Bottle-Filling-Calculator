# Bottle-Filling-Calculator

Implementation of a programming challenge where the goal is to calculate the total time for a collection of bottles to be filled. 

## Task Overview

There is a queue for people to fill their water bottles. Your task is to calculate the total time required for every bottle to be filled. 

### Function Requirements

**Inputs**:
- An integer array representing the queue, where each integer denotes the size of a water bottle in milliliters. For example, [400, 750, 1000] indicates three people with water bottles of 400ml, 750ml, and 1000ml, respectively.
- An integer representing the number of available taps for filling the bottles.

**Outputs**:
- A numerical value representing the total time in seconds required for all individuals to fill their bottles.

### Bonus Challenges:

- Input Validation: Implement checks to ensure the function is used correctly, throwing errors for invalid inputs.
- Set-up Time: Modify the function to include a delay (e.g., 2 or 5 seconds) representing the time it takes for each person to walk to the tap.
- Variable Flow Rates: Adapt the function to accommodate taps with varying flow rates, such as 50ml/s and 200ml/s.
- Flow Rate Analysis: Analsze whether increasing the flow rate of one or more taps could result in a longer overall time to fill the bottles. If the answer is yes, provide an example. If the answer is no, prove that this is the case.
