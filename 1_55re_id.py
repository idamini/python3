import re

address = re.compile(
    '''
    ^
    (?P<name>
    ([\w.]+\s+)*[\w.]+
    )?
    \s*

    (?(name)
        (?P<brackets>(?=(<.*>)))
        |
        (?=([^<].*[^>]$))
    )
    (?(brackets)<|\s*)
    
    # The address: itself:username@domain.tld
    (?P<email>
        [\w\d.+ -]+               #Username
        @
        ([\w\d.]+\.)+      #Domain name prefix
        (com|org|edu)      # Limit the allowed top-level domains.
    )
   (?(brackets)>|\s*)
   $
    ''',
    re.VERBOSE
    )

candidates = [
    u'First Last <first.last@example.com>',
    u'No Brackets first.last@example.com',
    u'Open bracket <first.last@example.com',
    u'Close bracket first.last@example.com>',
    u'no.brackets@example.com'
    ]

for candidate in candidates:
    print('Candidate:',candidate)
    match = address.search(candidate)
    if match:
        print('  Match name:',match.groupdict()['name'])
        print('  Match email:',match.groupdict()['email'])
    else:
        print('  No match')
