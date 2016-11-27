#Poraba.si

Projekt pri predmetu spletno programiranje

Opis:

Kot je že v opisu projekta zapisano se ne moremo zanesti na številke, ki jih napišejo proizvajalci vozil.
Zatorej je edina smiselna rešitev imeti spletno stran, na kateri bodo dostopni podatki iz prve roke. Aplikacija nudi računanje poti med dvema točkama.
Z vnosom imen točk in pritiskom na gumb izračunaj nam zemljevid prikaže pot, na zaslonu pa se nam izpiše dolžina potovanja in poraba bencina.
Aplikacija omogoča tudi komentiranje tako avtomobilov kot uporabnikovih strani, prav tako pa omogoča dodajanje avtomobilov.
Služi nam lahko kot pripomoček pri spremljanju porabe naših avtomobilov in računanje porabe vnaprej.


Ciljna publika in naprave:

Vsi vozniki, moški in ženske z vozniškim izpitom in dostopom do interneta. Ker je ciljna publika zelo široka stran ni usmerjena in je narejena za splošni profil uporabnika.
Napravo je mogoče uporabljati na vseh platformah (tablicah,računalnikih in mobilnih telefonih).


Težave:

Internet explorer ne podpira mnogo css3 gradnikov, ki jih ima novejši Edge. Pri Chromu je bilo najmanj težav, saj je bila aplikacija večinoma testirana na tem brskalniku.
Mozilla Firefox je malce drugačna od Chroma, predvsem glede velikosti elementov vendar pa posebnih težav tam ni bilo. Težave so bile v glavnem v Edgu pri uporabi animacij in nekaterih CSS ukazov(valid, hover).


Zmogljivosti:

Poseben trud sem vložil v iskanje avtomobilov, za to funkcionalnost je bilo potrebno napisati največ js kode. Predvsem sem s tem gradnikom hotel uporabnika voditi po posameznih elementih, da pride do končnega rezultata, ki ga je iskal.
Drugi gradnik pa je zemljevid, google ima sicer dober API, vendar ga je bilo potrebno precej raziskati, da sem razumel katere stvari iz njihove knjižnice mi koristijo. Tukaj ni bilo toliko kode, bolj je bilo potrebno razumeti napisano.


Komentarji in problemi:

Pri izdelavi aplikacije je bilo težko narediti dober dizajn, saj je bilo na voljo mnogo funckionalnosti, ki sem jih želel vključiti vendar jih zaradi težavnosti nisem uspel.
Največja težava je bila si predstavljati kako bo določena stvar delovala z neko bazo. Ko mi je uspel ta miselni preskok je bilo načrtovanje in programiranje aplikacije mnogo lažje.
Nekatere funkcionalnosti niso še popolnoma implementirane, saj se brez neke baze nisem niti želel ubadati z njimi. Npr. slika avtomobila je vedno ista, kasneje pa bo vezana na izbiro uporabnika.


Možno bo dodajati avtomobile, komentirati se bo dalo pod vse podatke uporabnika(kot neka knjiga gostov) ter pod avtomobil(skupna poraba premium uporabnikov).

###Funkcionalnosti:

	Registriran uporabnik
	
		- Lahko dodaja avtomobile
		- Dodaja podatke o porabi za vsak svoj avtomobil
		- Išče po podatkih drugih uporabnikov ali po posameznih avtomobilih
		- vidi podatke o porabi za zadnje polnjenje in zadnjih 5 polnjenj
		- Pod avtomobile lahko komentira ali označi, če je z avtomobilom zadovoljen ali ne
		- Kalkulator stroškov
		
		
	
	Neregistriran uporabnik
	
		- Lahko išče po avtomobilih
		- Kalkulator stroškov
		
		
		
	Premium uporabniki
	
		- Lahko dodajajo avtomobile
		- Dodajajo podatke o porabi za vsak svoj avtomobil
		- Iščejo po podatkih drugih uporabnikov ali po posameznih avtomobilih
		- Lahko primerjajo porabo po znamkah avtomobilov
		- Podatki o porabi so za zadnje polnjenje, za zadnjih 5 polnjenj, letni
		- Pod avtomobile lahko komentirajo, jih označijo kot priljubljene ali označijo,
			če so z avtomobilom zadovoljni ali ne
		- Izračunajo porabo za določeno pot (npr. poraba za 700 km)
		- Izbirajo tip avtomobila(mestni, 4x4, športni), ki bo vrnil avtomobile razvrščene po porabi
		- Kalkulator stroškov
		
Morebitne funkcinalnosti se bodo za določen tip uporabnika še spreminjale, lahko bo dodana tudi kakšna nova.
