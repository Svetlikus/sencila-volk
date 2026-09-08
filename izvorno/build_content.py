from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parent.parent

ICONS = {
    'arrow': '<path d="M4 12h15M13 5l7 7-7 7"/>',
    'up': '<path d="M6 18 18 6M6 6h12v12"/>',
    'check': '<path d="m5 12 4 4L19 6"/>',
    'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    'shield': '<path d="m12 3 8 3v6c0 4-5 8-8 9-3-1-8-5-8-9V6l8-3Z"/><path d="m8 12 3 3 5-6"/>',
    'pin': '<path d="M19 10c0 6-7 11-7 11S5 16 5 10a7 7 0 1 1 14 0Z"/><circle cx="12" cy="10" r="2.5"/>',
    'upload': '<path d="M12 16V3m-5 5 5-5 5 5M4 15v6h16v-6"/>',
    'phone': '<path d="m8 3 3 5-3 3a17 17 0 0 0 5 5l3-3 5 3-1 4c-8 3-20-9-17-17Z"/>',
    'mail': '<rect x="3" y="5" width="18" height="14" rx="1"/><path d="m3 6 9 7 9-7"/>',
    'plus': '<path d="M12 5v14M5 12h14"/>',
    'close': '<path d="m6 6 12 12M6 18 18 6"/>',
}

def icon(name):
    return f'<svg class="icon" viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'

CONTENT = {
 'sl': {
  'title':'Senčila Volk | Screen roloji, pergole in senčila po meri',
  'desc':'Dobava, montaža in servis senčil. Screen roloji, pergole, rolete, žaluzije, tende in komarniki. Več kot 10 let izkušenj, 5-letna garancija. Slovenija, Istra in Dalmacija.',
  'top':'DOBAVA · MONTAŽA · SERVIS', 'area':'Slovenija · Istra · Dalmacija',
  'brand':'SENČILA', 'brand_sub':'MATEJ VOLK S.P.', 'nav':['Senčila','Pergole','O nas','Kontakt'],
  'cta':'Pošlji povpraševanje', 'menu':'Meni','nav_label':'Glavna navigacija', 'language_label':'Izbira jezika', 'skip':'Na vsebino',
  'hero_label':'SENČILA PO MERI. MONTAŽA Z OBČUTKOM.',
  'hero':'Senca, kot<br>se spodobi.',
  'hero_desc':'Več udobja doma. Več življenja na terasi.<br>Screen roloji, pergole in druga senčila z zanesljivo montažo in osebnim pristopom.',
  'explore':'Razišči ponudbo', 'hero_note':'Od prvega dogovora do zadnjega vijaka.',
  'illustration':'Ilustrativni prikaz · AI',
  'stats':[('10+','let izkušenj'),('5 let','garancije na izdelke in montažo'),('Držimo besedo.','In dogovorjene termine.')],
  'products_label':'REŠITVE ZA VAŠ DOM', 'products_title':'Prava senca.<br>Za vaš način življenja.',
  'products_intro':'Za teraso, kjer se radi zadržite. Za dom, v katerem vam je prijetno. Skupaj izberemo rešitev, ki ustreza vašemu prostoru in proračunu.',
  'screen_label':'ZA PRIJETNEJŠI DOM', 'screen_title':'Screen roloji',
  'screen_desc':'Ustavite sonce pred steklom. Zunanja tekstilna senčila pomagajo zmanjšati bleščanje in pregrevanje prostorov ter ohranijo čist videz fasade.',
  'screen_tags':['Zunanja tekstilna senčila','Izdelava po meri'], 'screen_link':'Zanimajo me screen roloji',
  'screen_alt':'Ilustrativni prikaz zunanjih screen rolojev na oknih sodobne hiše',
  'pergola_label':'VAŠA TERASA. VEČ ČASA ZUNAJ.', 'pergola_title':'Pergole',
  'pergola_desc':'Naj terasa postane del doma, ki ga res uporabljate. Izberite bioklimatsko pergolo z vrtljivimi lamelami ali pergolo s pomično platneno streho.',
  'pergola_tags':['Bioklimatske pergole','Pomična platnena streha'], 'pergola_link':'Zanima me pergola',
  'pergola_alt':'Ilustrativni prikaz antracitne bioklimatske pergole ob hiši z vrtom',
  'other_title':'Dobra rešitev za vsako okno.', 'other_intro':'Celovita ponudba senčil, prilagojena vašemu domu.',
  'other':[
    ('zunanje-zaluzije','Zunanje žaluzije','Svetloba pod vašim nadzorom. Z nastavitvijo lamel uravnavate senco in pogled navzven.'),
    ('rolete','Rolete','Za zatemnitev prostorov, več zasebnosti in preprost vsakdan.'),
    ('komarniki','Komarniki','Svež zrak v hiši. Mrčes zunaj. Rešitev za okna in vrata po vaših merah.'),
    ('tende','Tende','Prijetna senca na balkonu ali terasi, ko jo potrebujete.'),
    ('notranja-sencila','Notranja senčila','Roloji, žaluzije in druga notranja senčila za prijetno svetlobo in zasebnost.'),
  ],
  'other_link':'Povpraševanje za',
  'about_label':'ZA IMENOM VOLK STOJI MATEJ.',
  'about_title':'Osebni dogovor.<br>Pošteno opravljeno delo.',
  'about_p':'Pri Senčilih Volk se za svoj projekt dogovarjate z Matejem. Z več kot desetletjem izkušenj pri senčilih vam pomaga izbrati smiselno rešitev in poskrbi za kakovostno izvedbo.',
  'about_p2':'Pomembno nam je, da veste, kaj dobite, koliko bo stalo in kdaj bo narejeno. Če po montaži potrebujete pomoč, smo tu tudi takrat.',
  'promises':[('Držimo se dogovora.','Spoštujemo dogovorjene termine in vaš čas.'),('Cena, ki ima smisel.','Ponudba glede na vaše potrebe in kakovost izvedbe.'),('Pomoč tudi po montaži.','Servis in reševanje težav pri naših izdelkih.')],
  'guarantee_kicker':'BREZ SKRBI TUDI PO MONTAŽI', 'years':'let',
  'guarantee_title':'Garancija na vse<br>izdelke in montažo.',
  'guarantee_note':'Za svojo izbiro stojimo.<br>Za svojim delom tudi.',
  'process_label':'OD POVPRAŠEVANJA DO SENCE', 'process_title':'Jasen dogovor.<br>Na vsakem koraku.',
  'steps':[('Opišite nam svoj projekt.','Izberite senčilo, napišite kraj montaže in dodajte okvirne mere ali fotografije, če jih imate.'),('Dogovorimo se o rešitvi.','Matej pregleda povpraševanje. Skupaj razjasnimo podrobnosti in se po potrebi dogovorimo za ogled in izmero.'),('Poskrbimo za izvedbo.','Po potrjeni ponudbi se dogovorimo za termin, dobavimo izdelke in jih strokovno montiramo.')],
  'coverage_title':'Od domačega vrta<br>do terase ob morju.',
  'coverage_desc':'Dobavo in montažo izvajamo po vsej Sloveniji ter v Istri in Dalmaciji. V obrazcu nam povejte kraj montaže, da lahko načrtujemo izvedbo.',
  'coverage_badges':['Vsa Slovenija','Istra','Dalmacija'],
  'faq_label':'DOBRO JE VEDETI', 'faq_title':'Še kaj pred<br>povpraševanjem?',
  'faqs':[('Nimam natančnih mer. Lahko vseeno pošljem povpraševanje?','Seveda. Za prvi stik zadoščajo kratek opis želja, kraj montaže in fotografija prostora, če jo imate. Okvirne mere so dobrodošle, niso pa obvezne.'),('Kako poteka priprava ponudbe?','Začnemo z vašim povpraševanjem. Matej pregleda podatke in vas kontaktira za podrobnosti. O morebitnem ogledu in izmeri se dogovorimo glede na projekt.'),('Kaj zajema petletna garancija?','Petletna garancija velja za vse naše izdelke in montažo. Podrobnosti garancije vam pojasnimo ob ponudbi.'),('Servisirate tudi senčila drugih izvajalcev?','Servis zagotavljamo za senčila, ki smo jih dobavili ali montirali pri Senčilih Volk.')],
  'form_label':'POVEJTE NAM, KAJ IMATE V MISLI.', 'form_title':'Vaš projekt se<br>začne z dogovorom.',
  'form_intro':'Nekaj podatkov o vašem domu je dovolj za prvi korak. Matej bo pregledal povpraševanje in se vam oglasil.',
  'contact_small':'Raje najprej pokličete?', 'phone':'030 305 338',
  'form_legend':'Povpraševanje brez obveznosti', 'required_note':'Polja z * so obvezna.',
  'fields':{'product':'Kaj vas zanima?','name':'Ime in priimek','email':'E-pošta','phone':'Telefon','location':'Kraj montaže','measurements':'Okvirne mere','message':'Vaše želje'},
  'solutions_hint':'Izberite eno ali več rešitev.', 'unsure':'Potrebujem nasvet', 'service':'Servis izdelkov Senčila Volk',
  'optional':'neobvezno','phone_hint':'Za lažji dogovor.', 'location_ph':'npr. Ljubljana, Pula ali Zadar',
  'measurements_ph':'npr. terasa 4 × 3 m ali okno 180 × 150 cm',
  'message_ph':'Kaj želite zasenčiti? Imate v mislih določeno izvedbo, barvo ali okviren termin?',
  'photos':'Fotografije prostora', 'photo_hint':'Do 3 fotografije · JPG, PNG ali WebP · skupaj do 10 MB',
  'photo':'Dodaj fotografijo', 'photo_more':'Dodaj še fotografiji', 'remove':'Odstrani fotografijo',
  'privacy_line':'Podatke in fotografije uporabimo za obravnavo vašega povpraševanja. Brez prijave na oglasna sporočila.',
  'privacy_link':'Kako ravnamo z vašimi podatki', 'submit_note':'Z oddajo povpraševanja se še ne zavežete k naročilu.',
  'footer_tagline':'Dobra senca.<br>Dober dogovor.', 'footer_nav':'RAZIŠČITE', 'footer_contact':'POVEŽIMO SE', 'footer_company':'PODJETJE',
  'privacy_title':'Zasebnost', 'rights':'Senčila Volk · Matej Volk s.p.',
  'images_notice':'Prikazi senčil so ustvarjeni z AI in so ilustrativni. Ne predstavljajo izvedenih projektov Senčil Volk.',
  'home':'Nazaj na prvo stran', 'thanks_title':'Hvala za povpraševanje.', 'thanks_desc':'Vaš naslednji korak je pogovor z Matejem. Če želite dodati še kakšno podrobnost, nam pišite na info@sencilavolk.si ali pokličite.',
 },
 'hr': {
  'title':'Senčila Volk | Screen roloi, pergole i sjenila po mjeri',
  'desc':'Dobava, montaža i servis sjenila. Screen roloi, pergole, rolete, žaluzine, tende i komarnici. Više od 10 godina iskustva, 5 godina jamstva. Slovenija, Istra i Dalmacija.',
  'top':'DOBAVA · MONTAŽA · SERVIS', 'area':'Slovenija · Istra · Dalmacija',
  'brand':'SENČILA','brand_sub':'MATEJ VOLK S.P.', 'nav':['Sjenila','Pergole','O nama','Kontakt'],
  'cta':'Pošalji upit', 'menu':'Izbornik','nav_label':'Glavna navigacija','language_label':'Odabir jezika','skip':'Na sadržaj',
  'hero_label':'SJENILA PO MJERI. PAŽLJIVA MONTAŽA.',
  'hero':'Hlad, kako<br>i treba.',
  'hero_desc':'Više udobnosti kod kuće. Više života na terasi.<br>Screen roloi, pergole i druga sjenila uz pouzdanu montažu i osoban pristup.',
  'explore':'Istraži ponudu', 'hero_note':'Od prvog dogovora do posljednjeg vijka.',
  'illustration':'Ilustrativni prikaz · AI',
  'stats':[('10+','godina iskustva'),('5 godina','jamstva na proizvode i montažu'),('Držimo riječ.','I dogovorene rokove.')],
  'products_label':'RJEŠENJA ZA VAŠ DOM','products_title':'Pravi hlad.<br>Za vaš način života.',
  'products_intro':'Za terasu na kojoj volite boraviti. Za dom u kojem vam je ugodno. Zajedno odabiremo rješenje koje odgovara vašem prostoru i budžetu.',
  'screen_label':'ZA UGODNIJI DOM','screen_title':'Screen roloi',
  'screen_desc':'Zaustavite sunce prije stakla. Vanjska tekstilna sjenila pomažu smanjiti odsjaj i pregrijavanje prostorija te čuvaju čist izgled fasade.',
  'screen_tags':['Vanjska tekstilna sjenila','Izrada po mjeri'],'screen_link':'Zanimaju me screen roloi',
  'screen_alt':'Ilustrativni prikaz vanjskih screen roloa na prozorima suvremene kuće',
  'pergola_label':'VAŠA TERASA. VIŠE VREMENA VANI.','pergola_title':'Pergole',
  'pergola_desc':'Neka terasa postane dio doma koji zaista koristite. Odaberite bioklimatsku pergolu s pomičnim lamelama ili pergolu s pomičnim platnenim krovom.',
  'pergola_tags':['Bioklimatske pergole','Pomični platneni krov'],'pergola_link':'Zanima me pergola',
  'pergola_alt':'Ilustrativni prikaz antracitne bioklimatske pergole uz kuću s vrtom',
  'other_title':'Dobro rješenje za svaki prozor.','other_intro':'Cjelovita ponuda sjenila, prilagođena vašem domu.',
  'other':[
    ('zunanje-zaluzije','Vanjske žaluzine','Svjetlost pod vašom kontrolom. Položajem lamela regulirate hlad i pogled prema van.'),
    ('rolete','Rolete','Za zamračenje prostorija, više privatnosti i jednostavnu svakodnevicu.'),
    ('komarniki','Komarnici','Svjež zrak u kući. Kukci vani. Rješenje za prozore i vrata po vašim mjerama.'),
    ('tende','Tende','Ugodan hlad na balkonu ili terasi kad ga trebate.'),
    ('notranja-sencila','Unutarnja sjenila','Rolo zavjese, žaluzine i druga unutarnja sjenila za ugodno svjetlo i privatnost.'),
  ],
  'other_link':'Upit za',
  'about_label':'IZA IMENA VOLK STOJI MATEJ.','about_title':'Osoban dogovor.<br>Pošteno obavljen posao.',
  'about_p':'U tvrtki Senčila Volk svoj projekt dogovarate s Matejem. S više od deset godina iskustva u sjenilima pomaže vam odabrati smisleno rješenje i brine o kvalitetnoj izvedbi.',
  'about_p2':'Važno nam je da znate što dobivate, koliko će koštati i kada će biti gotovo. Ako nakon montaže trebate pomoć, tu smo i tada.',
  'promises':[('Držimo se dogovora.','Poštujemo dogovorene rokove i vaše vrijeme.'),('Cijena koja ima smisla.','Ponuda prema vašim potrebama i kvaliteti izvedbe.'),('Pomoć i nakon montaže.','Servis i rješavanje problema s našim proizvodima.')],
  'guarantee_kicker':'BEZ BRIGE I NAKON MONTAŽE','years':'godina',
  'guarantee_title':'Jamstvo na sve<br>proizvode i montažu.',
  'guarantee_note':'Stojimo iza svog izbora.<br>I iza svog rada.',
  'process_label':'OD UPITA DO HLADA','process_title':'Jasan dogovor.<br>U svakom koraku.',
  'steps':[('Opišite nam svoj projekt.','Odaberite sjenilo, napišite mjesto montaže i dodajte okvirne mjere ili fotografije ako ih imate.'),('Dogovaramo rješenje.','Matej pregledava upit. Zajedno razjašnjavamo pojedinosti te po potrebi dogovaramo obilazak i izmjeru.'),('Brinemo o izvedbi.','Nakon prihvaćene ponude dogovaramo termin, dobavljamo proizvode i stručno ih montiramo.')],
  'coverage_title':'Od kućnog vrta<br>do terase uz more.',
  'coverage_desc':'Dobavu i montažu obavljamo diljem Slovenije te u Istri i Dalmaciji. U obrascu navedite mjesto montaže kako bismo mogli planirati izvedbu.',
  'coverage_badges':['Cijela Slovenija','Istra','Dalmacija'],
  'faq_label':'DOBRO JE ZNATI','faq_title':'Još nešto<br>prije upita?',
  'faqs':[('Nemam točne mjere. Mogu li ipak poslati upit?','Naravno. Za prvi kontakt dovoljni su kratak opis želja, mjesto montaže i fotografija prostora ako je imate. Okvirne mjere su dobrodošle, ali nisu obvezne.'),('Kako se priprema ponuda?','Počinjemo vašim upitom. Matej pregledava podatke i kontaktira vas radi pojedinosti. Obilazak i izmjeru dogovaramo ovisno o projektu.'),('Što obuhvaća petogodišnje jamstvo?','Petogodišnje jamstvo vrijedi za sve naše proizvode i montažu. Pojedinosti jamstva objašnjavamo uz ponudu.'),('Servisirate li i sjenila drugih izvođača?','Servis osiguravamo za sjenila koja smo dobavili ili montirali u tvrtki Senčila Volk.')],
  'form_label':'RECITE NAM ŠTO IMATE NA UMU.','form_title':'Vaš projekt<br>počinje dogovorom.',
  'form_intro':'Nekoliko podataka o vašem domu dovoljno je za prvi korak. Matej će pregledati upit i javiti vam se.',
  'contact_small':'Radije biste prvo nazvali?','phone':'+386 30 305 338',
  'form_legend':'Upit bez obveze','required_note':'Polja s * su obvezna.',
  'fields':{'product':'Što vas zanima?','name':'Ime i prezime','email':'E-pošta','phone':'Telefon','location':'Mjesto montaže','measurements':'Okvirne mjere','message':'Vaše želje'},
  'solutions_hint':'Odaberite jedno ili više rješenja.','unsure':'Trebam savjet','service':'Servis proizvoda Senčila Volk',
  'optional':'neobvezno','phone_hint':'Za lakši dogovor.','location_ph':'npr. Pula, Zadar ili Ljubljana',
  'measurements_ph':'npr. terasa 4 × 3 m ili prozor 180 × 150 cm',
  'message_ph':'Što želite zasjeniti? Imate li na umu određenu izvedbu, boju ili okviran termin?',
  'photos':'Fotografije prostora','photo_hint':'Do 3 fotografije · JPG, PNG ili WebP · ukupno do 10 MB',
  'photo':'Dodaj fotografiju','photo_more':'Dodaj još fotografija','remove':'Ukloni fotografiju',
  'privacy_line':'Podatke i fotografije koristimo za obradu vašeg upita. Bez prijave na promotivne poruke.',
  'privacy_link':'Kako postupamo s vašim podacima','submit_note':'Slanjem upita još se ne obvezujete na narudžbu.',
  'footer_tagline':'Dobar hlad.<br>Dobar dogovor.','footer_nav':'ISTRAŽITE','footer_contact':'POVEŽIMO SE','footer_company':'TVRTKA',
  'privacy_title':'Privatnost','rights':'Senčila Volk · Matej Volk s.p.',
  'images_notice':'Prikazi sjenila izrađeni su pomoću AI-ja i ilustrativni su. Ne predstavljaju izvedene projekte tvrtke Senčila Volk.',
  'home':'Natrag na početnu stranicu','thanks_title':'Hvala na upitu.','thanks_desc':'Vaš sljedeći korak je razgovor s Matejem. Želite li dodati još neku pojedinost, pišite nam na info@sencilavolk.si ili nazovite.',
 }
}

def head(lang, title, desc, prefix, asset_version=''):
    asset_query = f'?v={asset_version}' if asset_version else ''
    return f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(desc, quote=True)}">
  <!-- Preview on GitHub: remove noindex only after the final site is approved. -->
  <meta name="robots" content="noindex, nofollow">
  <meta name="theme-color" content="#201e1d">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="{'sl_SI' if lang == 'sl' else 'hr_HR'}">
  <meta property="og:title" content="{escape(title, quote=True)}">
  <meta property="og:description" content="{escape(desc, quote=True)}">
  <link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{prefix}assets/styles.css{asset_query}">
  <script src="{prefix}assets/site.js{asset_query}" defer></script>
</head>'''

def brand(prefix, light=False):
    return f'''<span class="brand"><img src="{prefix}assets/volk-{'light' if light else 'dark'}.svg" width="106" height="42" alt="Volk"><span class="brand-type">SENČILA<small>MATEJ VOLK S.P.</small></span></span>'''

def header(lang, t, prefix, internal=False):
    home = './index.html' if internal else '#top'
    anchor_prefix = './index.html' if internal else ''
    links = ''.join(f'<a href="{anchor_prefix}{a}">{n}</a>' for a,n in zip(['#resitve','#pergole','#o-nas','#povprasevanje'],t['nav']))
    sl_href = '../index.html' if lang == 'hr' else './index.html'
    hr_href = './index.html' if lang == 'hr' else './hr/index.html'
    return f'''<a class="skip" href="#main">{t['skip']}</a>
<div class="topline"><div class="wrap"><span>{t['top']}</span><span>{t['area']}</span></div></div>
<header class="site-header">
 <div class="wrap header-inner">
  <a class="brand-link" href="{home}" aria-label="Senčila Volk — {'domov' if lang=='sl' else 'početna'}">{brand(prefix)}</a>
  <nav id="navigation" aria-label="{t['nav_label']}">{links}</nav>
  <div class="header-actions">
   <div class="languages" aria-label="{t['language_label']}"><a href="{sl_href}" lang="sl" aria-label="Slovenščina" { 'aria-current="page"' if lang=='sl' else '' }>SL</a><span aria-hidden="true">/</span><a href="{hr_href}" lang="hr" aria-label="Hrvatski" { 'aria-current="page"' if lang=='hr' else '' }>HR</a></div>
   <a class="button header-cta" href="{anchor_prefix}#povprasevanje">{t['cta']}{icon('arrow')}</a>
   <button class="menu-toggle" type="button" data-menu aria-label="{t['menu']}" aria-expanded="false" aria-controls="navigation"><span></span><span></span></button>
  </div>
 </div>
</header>'''

def footer(lang, t, prefix, internal=False):
    anchor = './index.html' if internal else ''
    links=''.join(f'<a href="{anchor}{a}">{n}</a>' for a,n in zip(['#resitve','#pergole','#o-nas','#povprasevanje'],t['nav']))
    return f'''<footer class="site-footer">
 <div class="wrap footer-main">
  <div class="footer-brand"><a href="./index.html" aria-label="Senčila Volk">{brand(prefix,True)}</a><p>{t['footer_tagline']}</p></div>
  <div class="footer-col"><h2>{t['footer_nav']}</h2>{links}</div>
  <div class="footer-col"><h2>{t['footer_contact']}</h2><a href="mailto:info@sencilavolk.si">info@sencilavolk.si</a><a href="tel:+38630305338">{t['phone']}</a><p>{t['area']}</p></div>
  <div class="footer-col"><h2>{t['footer_company']}</h2><p>Matej Volk s.p.<br>Fani Grumove ulica 6<br>1000 Ljubljana, Slovenija</p></div>
 </div>
 <div class="wrap footer-bottom"><span>© 2026 {t['rights']}</span><a href="./zasebnost.html">{t['privacy_title']}</a></div>
 <div class="wrap image-disclosure">{t['images_notice']}</div>
</footer>'''

def photo(prefix, stem, alt, caption, hero=False):
    width,height = (1672,941) if stem=='pergola' else (1448,1086)
    return f'''<figure class="{'hero-image' if hero else 'product-image'}">
 <img src="{prefix}assets/{stem}.webp" srcset="{prefix}assets/{stem}-small.webp 850w, {prefix}assets/{stem}.webp {width}w" sizes="{'100vw' if hero else '(max-width: 760px) 100vw, 50vw'}" width="{width}" height="{height}" alt="{alt}" {'fetchpriority="high"' if hero else 'loading="lazy"'}>
 <figcaption>{caption}</figcaption>
</figure>'''

def main_page(lang,t,prefix):
    stats=''.join(f'<div class="trust-item"><strong>{a}</strong><span>{b}</span></div>' for a,b in t['stats'])
    products=''
    for stem,id_,key in [('screen','screen-roloji','screen'),('pergola','pergole','pergola')]:
        tags=''.join(f'<span>{x}</span>' for x in t[key+'_tags'])
        products+=f'''<article class="product-card" id="{id_}">{photo(prefix,stem,t[key+'_alt'],t['illustration'])}<div class="product-body"><span class="product-kicker">{t[key+'_label']}</span><h3>{t[key+'_title']}</h3><p>{t[key+'_desc']}</p><div class="tags">{tags}</div><a class="text-link" href="#povprasevanje" data-product="{id_}">{t[key+'_link']}{icon('up')}</a></div></article>'''
    other=''.join(f'''<a class="other-item" href="#povprasevanje" data-product="{id_}" aria-label="{t['other_link']} {name}"><span class="item-no">{i+3:02d}</span><h3>{name}</h3><p>{desc}</p>{icon('up')}</a>''' for i,(id_,name,desc) in enumerate(t['other']))
    promises=''.join(f'<li>{icon("check")}<div><strong>{a}</strong><span>{b}</span></div></li>' for a,b in t['promises'])
    steps=''.join(f'<li><span class="step-number">{i+1:02d}</span><h3>{a}</h3><p>{b}</p></li>' for i,(a,b) in enumerate(t['steps']))
    faqs=''.join(f'<details><summary>{q}{icon("plus")}</summary><p>{a}</p></details>' for q,a in t['faqs'])
    badges=''.join(f'<span>{icon("pin")}{x}</span>' for x in t['coverage_badges'])
    options=[('screen-roloji',t['screen_title']),('pergole',t['pergola_title'])]+[(a,b) for a,b,_ in t['other']]+[('servis',t['service']),('nasvet',t['unsure'])]
    # Each checkbox has a distinct submitted name so the email service retains
    # every choice, including when JavaScript is unavailable.
    options='\n'.join(
        f'<label class="solution-option{" solution-option-wide" if v in ("servis", "nasvet") else ""}" for="solution-{v}">'
        f'<input id="solution-{v}" type="checkbox" name="Resitev {i} / Rjesenje {i}" value="{escape(label, quote=True)}" data-solution="{v}" aria-describedby="solutions-hint solutions-error">'
        f'<span>{escape(label)}</span></label>'
        for i,(v,label) in enumerate(options,1)
    )
    fields=t['fields']
    file_rows=''
    for i in range(1,4):
        if i==2: file_rows+=f'<details class="extra-photos"><summary>{t["photo_more"]}{icon("plus")}</summary>'
        file_rows+=f'''<div class="file-row"><label for="photo-{i}">{icon('upload')}<span data-filename>{t['photo']} {i}</span></label><input id="photo-{i}" type="file" name="attachment{'' if i==1 else i}" accept="image/jpeg,image/png,image/webp" aria-describedby="photo-hint"><button type="button" class="remove-file" aria-label="{t['remove']} {i}" hidden>{icon('close')}</button></div>'''
    file_rows+='</details>'
    return f'''{head(lang,t['title'],t['desc'],prefix,asset_version='multi-solutions-1')}
<body id="top">
{header(lang,t,prefix)}
<main id="main">
 <section class="hero" aria-labelledby="hero-heading">
  {photo(prefix,'pergola',t['pergola_alt'],t['illustration'],True)}
  <div class="hero-shade"></div>
  <div class="wrap hero-content">
   <p class="eyebrow">{t['hero_label']}</p><h1 id="hero-heading">{t['hero']}</h1>
   <p class="hero-description">{t['hero_desc']}</p>
   <div class="hero-buttons"><a class="button" href="#povprasevanje">{t['cta']}{icon('arrow')}</a><a class="hero-secondary" href="#resitve">{t['explore']}</a></div>
   <p class="hero-note">{t['hero_note']}</p>
  </div>
 </section>
 <div class="trust-strip"><div class="wrap trust-grid">{stats}</div></div>
 <section class="section solutions wrap" id="resitve" aria-labelledby="solutions-heading">
  <div class="section-intro"><div><p class="eyebrow">{t['products_label']}</p><h2 id="solutions-heading">{t['products_title']}</h2></div><p>{t['products_intro']}</p></div>
  <div class="product-grid">{products}</div>
  <div class="other-heading"><h3>{t['other_title']}</h3><p>{t['other_intro']}</p></div>
  <div class="other-products">{other}</div>
 </section>
 <section class="section about" id="o-nas" aria-labelledby="about-heading"><div class="wrap about-grid">
  <div class="about-copy"><p class="eyebrow">{t['about_label']}</p><h2 id="about-heading">{t['about_title']}</h2><p>{t['about_p']}</p><p>{t['about_p2']}</p><ul class="promises">{promises}</ul></div>
  <div class="guarantee"><div class="guarantee-top">{icon('shield')}<span>{t['guarantee_kicker']}</span></div><div class="guarantee-number">5<span>{t['years']}</span></div><h3>{t['guarantee_title']}</h3><div class="guarantee-bottom"><p>{t['guarantee_note']}</p><img src="{prefix}assets/volk-light.svg" width="80" height="32" alt="Volk" loading="lazy"></div></div>
 </div></section>
 <section class="section process wrap" aria-labelledby="process-heading"><div class="section-intro"><div><p class="eyebrow">{t['process_label']}</p><h2 id="process-heading">{t['process_title']}</h2></div></div><ol class="steps">{steps}</ol></section>
 <section class="coverage"><div class="wrap coverage-grid"><div><h2>{t['coverage_title']}</h2></div><div><p>{t['coverage_desc']}</p><div class="coverage-badges">{badges}</div></div></div></section>
 <section class="section faq wrap" aria-labelledby="faq-heading"><div><p class="eyebrow">{t['faq_label']}</p><h2 id="faq-heading">{t['faq_title']}</h2></div><div class="faq-list">{faqs}</div></section>
 <section class="section inquiry" id="povprasevanje" aria-labelledby="inquiry-heading"><div class="wrap inquiry-grid">
  <div class="inquiry-copy"><p class="eyebrow">{t['form_label']}</p><h2 id="inquiry-heading">{t['form_title']}</h2><p>{t['form_intro']}</p><div class="direct-contact"><span>{t['contact_small']}</span><a class="contact-phone" href="tel:+38630305338">{t['phone']}{icon('up')}</a><a class="contact-email" href="mailto:info@sencilavolk.si">info@sencilavolk.si</a></div><p class="inquiry-area">{icon('pin')}{t['area']}</p></div>
  <form id="inquiry-form" class="inquiry-form" action="https://formsubmit.co/info@sencilavolk.si" method="POST" enctype="multipart/form-data">
   <div class="form-heading"><h3>{t['form_legend']}</h3><p>{t['required_note']}</p></div>
   <input type="hidden" name="_subject" value="Senčila Volk — novo povpraševanje / upit ({lang.upper()})">
   <input type="hidden" name="_template" value="table"><input type="hidden" name="Jezik / Jezik" value="{'Slovenščina' if lang=='sl' else 'Hrvatski'}">
   <div class="honey" aria-hidden="true"><label for="website">Website</label><input id="website" type="text" name="_honey" tabindex="-1" autocomplete="off"></div>
   <fieldset class="solution-field" aria-describedby="solutions-hint">
    <legend>{fields['product']} <span aria-hidden="true">*</span></legend>
    <p id="solutions-hint" class="solutions-hint">{t['solutions_hint']}</p>
    <div class="solution-options">{options}</div>
    <p id="solutions-error" class="solutions-error" hidden></p>
   </fieldset>
   <div class="form-row"><div class="field"><label for="name">{fields['name']} <span aria-hidden="true">*</span></label><input id="name" name="Ime / Ime" autocomplete="name" maxlength="120" required></div><div class="field"><label for="email">{fields['email']} <span aria-hidden="true">*</span></label><input id="email" name="email" type="email" autocomplete="email" maxlength="254" required></div></div>
   <div class="form-row"><div class="field"><label for="phone">{fields['phone']} <span class="optional">({t['optional']})</span></label><input id="phone" name="Telefon" type="tel" autocomplete="tel" maxlength="40"></div><div class="field"><label for="location">{fields['location']} <span aria-hidden="true">*</span></label><input id="location" name="Kraj / Mjesto" autocomplete="address-level2" placeholder="{t['location_ph']}" maxlength="180" required></div></div>
   <div class="field"><label for="measurements">{fields['measurements']} <span class="optional">({t['optional']})</span></label><input id="measurements" name="Okvirne mere / mjere" placeholder="{t['measurements_ph']}" maxlength="300"></div>
   <div class="field"><label for="message">{fields['message']} <span class="optional">({t['optional']})</span></label><textarea id="message" name="Sporocilo / Poruka" rows="4" maxlength="5000" placeholder="{t['message_ph']}"></textarea></div>
   <fieldset class="photo-field"><legend>{t['photos']} <span class="optional">({t['optional']})</span></legend><p id="photo-hint">{t['photo_hint']}</p>{file_rows}</fieldset>
   <p class="privacy-note">{t['privacy_line']} <a href="./zasebnost.html" target="_blank" rel="noopener">{t['privacy_link']}</a>.</p>
   <p id="form-status" class="form-status" role="alert" tabindex="-1" hidden></p>
   <button class="button submit-button" type="submit"><span>{t['cta']}</span>{icon('arrow')}</button><p class="submit-note">{t['submit_note']}</p>
  </form>
 </div></section>
</main>
{footer(lang,t,prefix)}
</body>
</html>'''

PRIVACY = {
 'sl': '''<p class="legal-lead">Podatke iz obrazca uporabljamo, da se z vami dogovorimo o senčilih in pripravimo ponudbo.</p>
<h2>Kdo obravnava vaše podatke?</h2><p>Matej Volk s.p., Fani Grumove ulica 6, 1000 Ljubljana, Slovenija. Za vprašanja o podatkih pišite na <a href="mailto:info@sencilavolk.si">info@sencilavolk.si</a> ali pokličite <a href="tel:+38630305338">+386 30 305 338</a>.</p>
<h2>Kaj pošljete in zakaj?</h2><p>Obrazec zbere ime, e-pošto, vrsto izdelka in kraj montaže. Telefon, okvirne mere, opis želja in fotografije dodate prostovoljno. Podatki so namenjeni odgovoru na vašo zahtevo in pripravi ponudbe pred morebitno sklenitvijo pogodbe. Brez obveznih podatkov povpraševanja prek obrazca ne moremo obravnavati. Pošiljajte fotografije prostora, za katere imate dovoljenje; osebni dokumenti in fotografije drugih oseb niso potrebni.</p>
<h2>Kako se povpraševanje posreduje?</h2><p>Ob oddaji se vsebina in izbrane fotografije posredujejo storitvi <a href="https://formsubmit.co/" rel="noopener">FormSubmit</a>, ki jih pošlje na naš e-poštni naslov. Za preprečevanje neželenih sporočil lahko ta storitev prikaže Google reCAPTCHA. Veljajo tudi <a href="https://formsubmit.co/privacy.pdf" rel="noopener">pravila zasebnosti FormSubmit</a> in <a href="https://policies.google.com/privacy" rel="noopener">pravila zasebnosti Google</a>. Ponudniki lahko podatke obdelujejo zunaj Evropskega gospodarskega prostora; informacije o lokacijah obdelave in zaščitnih ukrepih poiščite v njihovih pravilih ali nam pišite.</p>
<h2>Hramba in vaše pravice</h2><p>Podatke potrebujemo za obravnavo povpraševanja in nadaljnji dogovor. Ob sklenitvi posla se za poslovno dokumentacijo upoštevajo veljavne obveznosti hrambe. Za informacije o hrambi konkretnega povpraševanja se obrnite na nas. V okviru veljavnih pravil lahko zahtevate dostop, popravek, izbris ali omejitev obdelave ter uveljavljate pravico do prenosljivosti ali ugovora, kadar je to primerno. Pritožbo lahko vložite pri <a href="https://www.ip-rs.si/">Informacijskem pooblaščencu</a>.</p>
<h2>Obisk strani</h2><p>Ta različica strani ne uporablja oglasnih sledilnikov, analitike ali lastnih piškotkov. Fotografije in logotip se nalagajo z iste strani. Gostovanje lahko obdeluje običajne tehnične podatke obiska; pri začetni objavi na GitHub Pages veljajo <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">pravila zasebnosti GitHub</a>. Po oddaji obrazca lahko ponudniki uporabljajo svoje tehnične in varnostne piškotke. Podatkov iz povpraševanja ne uporabljamo za avtomatizirano odločanje ali profiliranje.</p>''',
 'hr': '''<p class="legal-lead">Podatke iz obrasca koristimo kako bismo s vama dogovorili sjenila i pripremili ponudu.</p>
<h2>Tko obrađuje vaše podatke?</h2><p>Matej Volk s.p., Fani Grumove ulica 6, 1000 Ljubljana, Slovenija. Za pitanja o podacima pišite na <a href="mailto:info@sencilavolk.si">info@sencilavolk.si</a> ili nazovite <a href="tel:+38630305338">+386 30 305 338</a>.</p>
<h2>Što šaljete i zašto?</h2><p>Obrazac prikuplja ime, e-poštu, vrstu proizvoda i mjesto montaže. Telefon, okvirne mjere, opis želja i fotografije dodajete dobrovoljno. Podaci služe za odgovor na vaš zahtjev i pripremu ponude prije mogućeg sklapanja ugovora. Bez obveznih podataka ne možemo obraditi upit putem obrasca. Šaljite fotografije prostora za koje imate dopuštenje; osobni dokumenti i fotografije drugih osoba nisu potrebni.</p>
<h2>Kako se upit prosljeđuje?</h2><p>Slanjem obrasca sadržaj i odabrane fotografije prosljeđuju se servisu <a href="https://formsubmit.co/" rel="noopener">FormSubmit</a>, koji ih šalje na našu e-poštu. Za sprječavanje neželjenih poruka servis može prikazati Google reCAPTCHA. Primjenjuju se i <a href="https://formsubmit.co/privacy.pdf" rel="noopener">pravila privatnosti servisa FormSubmit</a> te <a href="https://policies.google.com/privacy" rel="noopener">pravila privatnosti Googlea</a>. Pružatelji mogu obrađivati podatke izvan Europskog gospodarskog prostora; informacije o mjestima obrade i zaštitnim mjerama potražite u njihovim pravilima ili nam pišite.</p>
<h2>Pohrana i vaša prava</h2><p>Podatke trebamo za obradu upita i daljnji dogovor. Ako dođe do sklapanja posla, na poslovnu dokumentaciju primjenjuju se važeće obveze čuvanja. Za informacije o čuvanju konkretnog upita obratite nam se. U okviru važećih pravila možete zatražiti pristup, ispravak, brisanje ili ograničenje obrade te ostvariti pravo na prenosivost ili prigovor, kada je to primjenjivo. Pritužbu možete podnijeti <a href="https://www.ip-rs.si/">slovenskom Informacijskom pooblaščencu</a> ili <a href="https://azop.hr/">Agenciji za zaštitu osobnih podataka</a>.</p>
<h2>Posjet stranici</h2><p>Ova verzija stranice ne koristi oglasne alate za praćenje, analitiku ni vlastite kolačiće. Fotografije i logotip učitavaju se s iste stranice. Hosting može obrađivati uobičajene tehničke podatke posjeta; pri početnoj objavi na GitHub Pages primjenjuju se <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">pravila privatnosti GitHuba</a>. Nakon slanja obrasca pružatelji mogu koristiti svoje tehničke i sigurnosne kolačiće. Podatke iz upita ne koristimo za automatizirano odlučivanje ni profiliranje.</p>'''
}

for lang,t in CONTENT.items():
    folder=ROOT if lang=='sl' else ROOT/'hr'
    folder.mkdir(parents=True,exist_ok=True)
    prefix='./' if lang=='sl' else '../'
    (folder/'index.html').write_text(main_page(lang,t,prefix),encoding='utf-8')
    legal=f'''{head(lang,t['privacy_title']+' | Senčila Volk',t['privacy_link'],prefix)}<body id="top">{header(lang,t,prefix,True)}<main id="main" class="legal-page wrap"><a class="back-link" href="./index.html">← {t['home']}</a><p class="eyebrow">SENČILA VOLK</p><h1>{t['privacy_title']}</h1><div class="legal-body">{PRIVACY[lang]}</div></main>{footer(lang,t,prefix,True)}</body></html>'''
    (folder/'zasebnost.html').write_text(legal,encoding='utf-8')
    thanks=f'''{head(lang,t['thanks_title']+' | Senčila Volk',t['thanks_desc'],prefix)}<body id="top">{header(lang,t,prefix,True)}<main id="main" class="thanks-page wrap"><span class="thanks-icon">{icon('check')}</span><p class="eyebrow">SENČILA VOLK</p><h1>{t['thanks_title']}</h1><p>{t['thanks_desc']}</p><a class="button" href="./index.html">{t['home']}{icon('arrow')}</a></main>{footer(lang,t,prefix,True)}</body></html>'''
    (folder/'hvala.html').write_text(thanks,encoding='utf-8')
print('Created six static pages: Slovenian and Croatian home, privacy and thank-you pages.')
