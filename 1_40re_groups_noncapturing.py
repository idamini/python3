from re_test_patterns_groups import test_patterns

test_patterns(
    'abbaabbba',
    [(r'a((a+)|(b+))','apturing from'),
     (r'a((?:a+)|(?:b+))','noncapturing')
    ]
    )
