herf = input('Bir herf daxil edin ')



if ( herf in "aıou" ) or ( herf in "AIOU" ):

    print('Bu qalin saitdir')

elif ( herf in "eəiöü" ) or ( herf in "EƏİÖÜ" ):
    print('Bu incə saitdir')

else:
    print('Heç biridir')