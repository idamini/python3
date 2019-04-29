from re_test_patterns import test_patterns


test_patterns(
    
    'abbaabbba',
    [('[ab]','either a or b'),
     ('a[ab]+','a follow by 1 or more a or b'),
     ('a[ab]+?','a follow by 1 or more a or b,notgreedy')
        ]
    )
