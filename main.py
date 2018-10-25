

'''
2018-10-25 - kl. 19.27:
chr: jeg har lavet en ny klasse "dictlist"
metoden create_dictlist i bs4dictionary
tager en liste af hjemmesider (strings)
som skal crawles, samt en integer (antal søge generationer)

den returnese et dictlist objekt som skal
indeholde en liste med samtlige links der er fundet,
samt en dictionary hvor values
er alle "child" links og
keys er alle "parent" links.

for eksempel:
    hvis man køre den med 1 generationer,
    får man start linket som key og alle
    de fundne links som values.
    f.eks. 1 key med 8 values.

    køre man den med 2 generatioer, får man
    9 keys og 71 values
    
    71 values er også det totale amtal links in objektets liste.
    Det betyder at nogle af 8 1. generations links,
    selv linker tilbage til start linket, som dermed bliver en value.
        Jeg har forsøgt at undgå dette ved at have et "old_links"
        argument, men det ser ikke ud til at virke. 

'''

import temp_run_bs4dict as tempBS

tempBS.run()
