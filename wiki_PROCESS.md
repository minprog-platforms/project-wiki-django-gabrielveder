# Dit is het procesboek voor de Wiki opdracht.

## In dit procesboek zal ik bijhouden welke veranderingen ik maak aan mijn opdracht en hoe ik verschillende problemen probeer op te lossen. 

#### 25 - 11 - 2022
Vandaag ging ik aan de slag met het maken van een design document voor de wiki pagina. 
Sketches maken van websites had ik nog niet eerder gedaan en zou een uitdaging vormen. 
Ik koos er voor om te werken met de software van JustinMind. 
Het maken van drie sketches was een redelijke uitdaging aangezien ik de software nog niet beheerste. Het is echter wel gelukt om de sketches te maken en toe te voegen aan de readme. 

Vervolgens ben ik begonnen met het implementeren van functionaliteit. Eerst moest de juiste entry pagina worden getoond bij invoer van een
geldige url. Dit is met behulp van een begeleider gelukt. Het lastigste deel was het begrijpen van de derde argument in de Django 'render' functie.

#### 02 - 12 - 2022
Zojuist heb ik meer functionaliteit toegevoegd aan de index pagina. Na een aantal aanpassingen is het nu mogelijk om op entries te klikken en
naar deze entry pagina genomen te worden. De titels van de wiki entries zijn links geworden. Om dit voor elkaar te krijgen was wat nieuwe syntax
nodig. 

De volgende uitdaging zal zijn om een werkende search-bar te maken. De HttpResponseRedirect functie kon gebruikt worden om gebruik te maken van
de query van de gebruiker. Ook heb ik een functie geschreven in de util.py file om substrings van strings te zoeken. Deze functie wordt gebruikt
in de search functie van het views.py bestand. 

#### 06 - 12 - 2022
Om nieuwe entries te kunnen toevoegen, was weer nieuwe functionaliteit nodig. Hiervoor waren een nieuwe url, een nieuwe functie in views.py
en een nieuwe helperfunctie in util.py vereist. De helperfunctie in util.py werd geschreven om te kunnen controlleren of een entry met de ingevoerde titel al bestond.

#### 07 - 12 - 2022
Om een werkende 'create new entry' pagina te maken, was het nodig om een onderscheid te maken tussen een
'get' en een 'post' methode. Samen met Max werd het voor mij duidelijk dat de request.method 'get' moet zijn wanneer de 'create new entry' pagina wordt aangevraagd en dat de request.method 'post' moet zijn wanneer men bijvoorbeeld een formulier invuld. Dit nieuwe inzicht kon in de new_page functie worden toegepast om nieuwe entries te kunnen maken door de gebruiker.