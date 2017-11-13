# Processing of OntoNotes 5.0 Dataset (Chinese)

### OntoNotes 5.0 Chinese Release Notes
The Chinese portion of OntoNotes 5.0 includes 250K words of newswire data, 270K
words of broadcast news, and 170K of broadcast conversation. <br/>

The newswire data is taken from the Chinese Treebank 5.0. That 250K includes 100K of
Xinhua news data (chtb_001.fid to chtb_325.fid) and 150K of data from the Sinorama
news magazine (chtb_1001.fid to chtb_1078.fid). <br/>

The broadcast news data is 274K words taken from TDT4, and selected from data that
was annotated by the LDC for the Automatic Content Extraction (ACE) program. These
files have been assigned numbers chtb_2000.fid to chtb_3145.fid. <br/>

The broadcast conversation data is 170K words, taken from LDC’s GALE data. 50K of
the originally-Chinese data has also be annotated in English, and another 55K of the
Chinese data represents translations into Chinese from originally-English broadcast
conversations. <br/>

The Web data includes 215K tokens of which 15K are from the P2.5 evaluation and 86K
are from the Dev09 data. Futher, the 110K of Web data consists of 40K parallel Chinese
origin data and 70K parallel English origin data. <br/>

The telephone conversation corpus comprises about 100K of Chinese CallHome data
annotated with parse, proposition, name and coreference information. <br/>

### Sources
> BC = Broadcast Conversation <br/>
> BN = Broadcast News <br/>
> MZ = Magazine <br/>
> NW = News <br/>
> TC = Telephone Calls <br/>
> WB = Web Blog <br/>

### Entity Names Annotation
Named entity types:

|Type| Description|
|---|---|
|PERSON| People, including fictional|
|NORP| Nationalities or religious or political groups|
|FACILITY| Buildings, airports, highways, bridges, etc.|
|ORGANIZATION| Companies, agencies, institutions, etc.|
|GPE| Countries, cities, states|
|LOCATION| Non-GPE locations, mountain ranges, bodies of water|
|PRODUCT| Vehicles, weapons, foods, etc. (Not services)|
|EVENT| Named hurricanes, battles, wars, sports events, etc.|
|WORK OF ART| Titles of books songs, etc.|
|LAW| Named documents made into laws.|
|LANGUAGE| Any named language|

Other values annotated in a similar style:

|Type| Description|
|---|---|
|Date| Absolute or relative dates or periods|
|TIME| Times smaller than a day|
|PERCENT| Percentage (including '%')|
|MONEY| Monetary values, including unit|
|QUANTITY| Measurements, as of weight or distance|
|ORDINAL| 'first', 'second'|
|CARDINAL| Numerals that do not fall under another type|

