def maxSatisfied(customers: list[int], grumpy: list[int], minutes: int) -> int:
    """
    Calculates the maximum number of satisfied customers using a sliding window
    to optimize the special ability.

    Args:
        customers: A list of integers representing the number of customers at each minute.
        grumpy: A list of 0s and 1s, where 1 means the owner is grumpy.
        minutes: The duration in minutes for which the special ability can be used.

    Returns:
        The maximum number of customers that can be satisfied.
    """
    n = len(customers)

    # Step 1: Calculate the baseline number of customers that are always satisfied.
    # These are the customers served when the owner is not grumpy (grumpy[i] == 0).
    satisfied_customers = 0
    for i in range(n):
        if grumpy[i] == 0:
            satisfied_customers += customers[i]

    # Step 2: Use a sliding window to find the maximum number of customers
    # that can be saved (i.e., the maximum gain).
    # These are the customers lost when the owner is grumpy (grumpy[i] == 1)
    # within a continuous window of 'minutes'.
    
    # Calculate the initial gain for the first window of size `minutes`.
    current_gain = 0
    for i in range(minutes):
        if grumpy[i] == 1:
            current_gain += customers[i]

    max_gain = current_gain

    # Slide the window from the start to the end of the arrays.
    for i in range(minutes, n):
        # Add the potential gain from the new element entering the window.
        if grumpy[i] == 1:
            current_gain += customers[i]

        # Subtract the potential gain from the element leaving the window.
        if grumpy[i - minutes] == 1:
            current_gain -= customers[i - minutes]

        # Update the maximum gain found so far.
        max_gain = max(max_gain, current_gain)

    # Step 3: The total number of satisfied customers is the sum of the
    # baseline satisfied customers and the maximum potential gain.
    return satisfied_customers + max_gain


# Example usage with a dry-run scenario
if __name__ == "__main__":
    customers_example = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy_example = [0, 1, 0, 1, 0, 1, 0, 1]
    minutes_example = 3

    result = maxSatisfied(customers_example, grumpy_example, minutes_example)

    print(f"Customers: {customers_example}")
    print(f"Grumpy: {grumpy_example}")
    print(f"Minutes: {minutes_example}")
    print(f"Maximum number of satisfied customers: {result}")
    
    # Another example
    print("\n--- Another example ---")
    customers_example_2 = [4, 10, 5, 2, 3]
    grumpy_example_2 = [0, 1, 0, 1, 0]
    minutes_example_2 = 2
    
    result_2 = maxSatisfied(customers_example_2, grumpy_example_2, minutes_example_2)
    
    print(f"Customers: {customers_example_2}")
    print(f"Grumpy: {grumpy_example_2}")
    print(f"Minutes: {minutes_example_2}")
    print(f"Maximum number of satisfied customers: {result_2}")
