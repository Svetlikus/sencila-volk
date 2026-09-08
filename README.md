# Senčila Volk — prva različica spletne strani

Stran je pripravljena za GitHub Pages. Vključuje slovensko in hrvaško različico, prikaz celotne ponudbe, predstavitev Mateja in obrazec za povpraševanje s fotografijami. Deluje brez namestitve dodatnih programov ali sestavljanja kode.

## Najprej si jo oglej

1. Razširi datoteko ZIP.
2. Odpri mapo `sencila-volk`.
3. Dvoklikni `index.html`. Odpre se slovenska stran; povezava **HR** odpre hrvaško.

Za pravilen prikaz naj datoteke in mapi `assets` ter `hr` ostanejo skupaj. Obrazec v lokalnem ogledu ne pošilja sporočil; delovanje e-pošte preverimo po objavi na GitHub Pages.

## Objava na GitHub Pages

### 1. Ustvari repozitorij

Prijavi se na [GitHub](https://github.com/) in odpri [ustvarjanje novega repozitorija](https://github.com/new).

- Ime: `sencila-volk`
- Vidnost: **Public** za uporabo GitHub Pages z brezplačnim računom.
- Vključi **Add README**, nato izberi **Create repository**.

Ta repozitorij in spletna stran bosta javna. Objavljena stran bo najprej na naslovu v obliki `https://TVOJE-UPORABNISKO-IME.github.io/sencila-volk/`. To je vzorec naslova; dejanski naslov bo prikazan v nastavitvah Pages. [Uradna navodila GitHub](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).

### 2. Naloži spletno stran

V repozitoriju izberi **Add file → Upload files**. V okno povleci **vsebino** razširjene mape `sencila-volk`, skupaj z mapama `assets` in `hr`. Ne naloži ZIP-a in ne dodaj še ene zunanje mape: `index.html` mora biti na vrhu repozitorija.

Priloženi `README.md` lahko zamenja začetnega. Če skrite datoteke `.nojekyll` ne vidiš, bo tudi osnovna stran brez nje delovala, saj ne uporablja datotek z začetnim podčrtajem; po želji jo ustvariš z **Add file → Create new file**.

V sporočilo spremembe napiši `Prva različica spletne strani` in potrdi nalaganje na vejo `main`. [Navodila za nalaganje datotek](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository).

### 3. Vključi Pages

Odpri **Settings → Pages** in v delu **Build and deployment** nastavi:

| Nastavitev | Vrednost |
| --- | --- |
| Source | Deploy from a branch |
| Branch | main |
| Folder | / (root) |

Klikni **Save**. Ko je objava pripravljena, izberi **Visit site**. Objava lahko traja nekaj minut. Če dobiš napako 404, najprej preveri, da je `index.html` na vrhu veje `main` in da se je opravilo v zavihku **Actions** zaključilo. [Nastavitev vira objave](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

Polje **Custom domain** za zdaj pusti prazno. Domena `sencilavolk.si` in obstoječa stran ostaneta nespremenjeni.

### 4. Aktiviraj prejemanje povpraševanj

GitHub Pages streže spletno stran. Za pošiljanje e-pošte je obrazec pripravljen s storitvijo **FormSubmit** in naslovom **info@sencilavolk.si**.

1. Na objavljeni strani oddaj testno povpraševanje s svojimi podatki, za začetek brez fotografij.
2. V nabiralniku `info@sencilavolk.si` poišči aktivacijsko sporočilo FormSubmit in potrdi naslov. Preveri tudi neželeno pošto.
3. Zdaj oddaj novo testno povpraševanje z majhno fotografijo ter preveri, da prispejo vsa polja in priponka.
4. Enako preveri na hrvaški različici. Če FormSubmit zahteva dodatno aktivacijo za ta obrazec ali pozneje za drugo domeno, jo potrdi.

Prva oddaja sproži aktivacijo. Pred potrditvijo se na poslane priponke ne zanašaj: FormSubmit navaja, da jih ne zadrži za poznejše posredovanje. Skupna meja treh priponk na strani je 10 MB; sprejeti so JPG, PNG in WebP. Storitev ob oddaji lahko prikaže preverjanje reCAPTCHA. [FormSubmit: aktivacija](https://formsubmit.co/), [pomoč](https://formsubmit.co/help), [priponke](https://formsubmit.co/documentation).

Nobenega pravega povpraševanja še nismo poslali. Prejemanja e-pošte ni mogoče potrditi, dokler ne aktiviraš naslova in preveriš testne oddaje. Stran ne prikazuje izmišljene potrditve pošiljanja; oddajo obravnava FormSubmit. Stran `hvala.html` se odpre po povratni preusmeritvi ponudnika in sama ne dokazuje dostave v nabiralnik.

## Kaj je v paketu

| Datoteka ali mapa | Namen |
| --- | --- |
| `index.html` | Slovenska spletna stran |
| `hr/index.html` | Hrvaška spletna stran |
| `zasebnost.html`, `hr/zasebnost.html` | Obvestilo o podatkih iz obrazca |
| `hvala.html`, `hr/hvala.html` | Zaključek po oddaji obrazca |
| `assets/styles.css` | Videz in prilagoditev velikosti zaslona |
| `assets/site.js` | Mobilni meni, izbira izdelka, fotografije in oddaja |
| `assets/volk-*.svg`, `assets/favicon.svg` | Vektorski logotip iz priložene podobe |
| `assets/pergola*.webp`, `assets/screen*.webp` | Optimizirani ilustrativni prikazi |
| `izvorno/build_content.py` | Izvorna vsebina za skupno urejanje obeh jezikov |

Za običajno objavo ni treba zaganjati skript. Za razvijalca: zagon `python izvorno/build_content.py` ponovno ustvari šest strani in prepiše ročne spremembe njihovega HTML-ja. Videz in delovanje se urejata neposredno v `assets`.

## Podoba in vsebina

- Izvirna oblika logotipa Volk je ohranjena iz PDF-ja Anžeta Svetlika, 29. 9. 2021. Oznaka podjetja je Senčila Volk.
- Osnova so grafitna `#201e1d`, bela in izvirna rdeča `#e32227`. Rdeča na gumbih je temnejša `#cf191e`, da je belo besedilo bolj berljivo.
- Za splet je uporabljena sistemska pisava Arial/Helvetica brez zunanjega nalaganja pisav.
- Obe fotografiji sta ustvarjeni z AI za prvo različico, označeni kot ilustrativni in ne predstavljata izvedenih montaž ali tehnične specifikacije izdelkov.
- Ni izmišljenih ocen strank, referenc, znamk proizvajalcev, cen ali zagotovljenih odzivnih časov.
- Vključene so potrjene informacije: 10+ let izkušenj, 5 let garancije na vse izdelke in montažo, vsa Slovenija, Istra in Dalmacija, osebni pristop in servis lastnih izvedb.

## Naslednje dopolnitve

Pozneje zamenjamo ilustracije s fotografijami vaših montaž in dodamo znamke proizvajalcev. Pri zamenjavi slik popravimo tudi opise in odstranimo oznako AI samo pri zamenjanih prikazih. Obstoječih captionov ne odstranimo, dokler ostanejo ilustracije.

Obvestilo o zasebnosti je začetni osnutek glede na trenutno izvedbo obrazca. Pred končno poslovno objavo dopolnimo dejansko politiko hrambe povpraševanj in pogoje obdelave pri ponudniku obrazca ter potrdimo poslovne podatke in podrobne garancijske pogoje. Nobena certifikacija skladnosti ni navedena. Pojasnila Informacijskega pooblaščenca: [informacije ob zbiranju podatkov](https://www.ip-rs.si/mnenja-zvop-2/informacije-o-obdelavi-osebnih-podatkov-1692596271).

### Ko potrdiš zamenjavo obstoječe strani

Takrat uredimo vezavo domene, dejanske kanonične naslove in jezikovne povezave za iskalnike ter odstranimo oznako `noindex, nofollow` s potrjenih javnih strani. Ta oznaka trenutno zmanjšuje možnost indeksiranja osnutka; stran na GitHub Pages je kljub temu javno dosegljiva.

Pri prenosu domene ohranimo obstoječe e-poštne zapise MX in pripadajoče zapise TXT, da `info@sencilavolk.si` še naprej deluje. Prenos izvedemo šele po tvoji izrecni potrditvi in ponovnem preverjanju obrazca na novi domeni.

## Opravljena preverjanja

Preverjeni so JavaScript, vse lokalne povezave in sidra na šestih straneh, jezikovne oznake, obstoj slik ter pravilna polja obrazca, tri ločene priponke in način `multipart/form-data`. Stran uporablja relativne poti za objavo v podmapi GitHub Pages. E-poštno dostavo preveriš po aktivaciji; pregled v dejanskem brskalniku na telefonu in računalniku sledi ob prvem predogledu.
