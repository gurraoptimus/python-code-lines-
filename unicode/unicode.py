def truncate_with_ellipsis(s, max_length):
    if len(s) > max_length:
        return s[:max_length - 3] + '...'
    else:
        return s