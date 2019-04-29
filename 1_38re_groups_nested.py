from re_test_patterns_groups import test_patterns

test_patterns(
    'abbaabbba',
    [(r'a((a*)(b*))','a fllowed by 0-n a and 0-n b')]
    )
