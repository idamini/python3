from re_test_patterns  import test_patterns

test_patterns(
    'A prime #1 example!',
    [(r'\d+','sequence of digits'),
     (r'\D+','sequence of non-digits'),
     (r'\s+','sequence of withespace'),
     (r'\S+','sequence of non_withespace'),
     (r'\w+','alphanumberic characters'),
     (r'\W+','non-alphanumberic')]
    )
