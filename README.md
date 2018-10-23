# simpel_webcrawl
2018-10-23-python simpelt webcraweksempel - gruppe ImpossibleCollege

python kursus - 2018-10-23
gruppe impossible college

https://github.com/BoMarconiHenriksen/dat4sem2018fall-python/blob/master/lecture_notes/18-Web%20Scraping%20Basics.ipynb

opgave til næste gang: 
skriv en simpel web crawler.
Med beautiful soup.

Find alle links på siden,
find alle de sider disse sider linker til
vi vælger sælg den dybde vi vil stoppe ved.
(vi skal finde en måde at undgå uendelige løgger hvor siderne linker tilbage til den gamle)

Linkene lægger vi i en flad dictioanry (key er url, value er en liste ad de urls som key linker til).

Vi skal lave et billede som afspejler det vi har fundet,
dvs vi skal lave en "directed graph".


Det vil give mening at vi ikke gør det serielt, men prøver at parallelisere søgningen.
