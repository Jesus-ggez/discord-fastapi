def is_valid_password(s: str) -> str:
    use_number: bool = True
    use_symbol: bool = True
    use_alpha: bool = True

    for char in s:
        if not char.isalnum() and use_symbol:
            use_symbol = False
            continue

        if char.isnumeric() and use_number:
            use_number = False
            continue

        if not char.isalpha() and use_alpha:
            use_alpha = False
            continue

    if use_number == use_symbol == use_alpha == True:
        raise ValueError(
            'Invalid Password, must be contain one letter, one number and one symbol',
        )

    return s
