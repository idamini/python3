from re_test_patterns  import test_patterns

test_patterns(
    'abbaabbba',
    [('a.','a fllowed by any one character'),
     ('b,','b fllowed by any one character'),
     ('a.*b','a fllowed by anything, ending in b'),
     ('a.*?b','a fllowed by anything, ending in b')]
    )
