def safe_divide(numerator, denominator):
    """
    Safely divide two numbers, handling errors.
    Returns a meaningful message instead of raising exceptions.
    """

    # Step 1: Validate inputs are numeric
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    # Step 2: Handle division by zero
    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    # Step 3: Return result
    return f"The result of the division is {result}"
