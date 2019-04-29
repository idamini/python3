from re_test_patterns import test_patterns

test_patterns(
    'abbaaabbbbaaaaa',
    [('a(ab)','a fllowed by literal ab'),
     ('a(a*b*)','a fllowed by 0-n a and 0-n b'),
     ('a(ab)*','a fllowed by 0-n ab'),
     ('a(ab)+','a fllowed by 1-n ab')]
    )
