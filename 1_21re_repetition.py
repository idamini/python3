from re_test_patterns import test_patterns


test_patterns(
    
    'abbaabbba',
    [('ab*','a follow by zero or more b'),
     ('ab+','a follow by one or more b'),
     ('ab?','a follow by zero or more b'),
     ('ab{3}','a follow by three b'),
     ('ab{2,3}','a follow by two to three b')
        ]
    )
