def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    earliest_index = 0
    return_tuple = ()
    for index in range(len(nums) - 1):
        for after in range(index + 1, len(nums)):
            if (nums[index] + nums[after] == goal):
                if (earliest_index == 0):
                    earliest_index = after
                    return_tuple = (nums[index], nums[after])
                if (earliest_index != 0 and after < earliest_index):
                    earliest_index = after
                    return_tuple = (nums[index], nums[after])
                
    if (earliest_index == 0):
        return ()
    else:
        return return_tuple

