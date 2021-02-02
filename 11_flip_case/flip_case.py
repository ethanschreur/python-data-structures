def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    def swap(to_swap):
        if (to_swap.islower()):
            return to_swap.upper()
        elif (to_swap.isupper()):
            return to_swap.lower()
    lst = list(phrase);
    for index in range(len(lst)):
        if (to_swap.lower() == lst[index].lower()):
             lst[index] = swap(lst[index])
    return ''.join(lst)

