# personaltrainerinamstelveen.nl

Statische informatie- en doorverwijssite over personal training in Amstelveen. Geen framework, geen buildstap op de server nodig: de generator `build.py` zet de complete site in de map `site/`.

## Wat zit erin

- Homepage met een uitleg waar een goede personal trainer aan voldoet, drie aanbevolen aanbieders en een korte keuzeaanpak.
- Keuzegids met criteria, stappen, veelgemaakte fouten en een FAQ.
- Drie aparte aanbiederspagina's, elk met een eigen kleur, badge en invalshoek, zodat de bedrijven als losse aanbieders overkomen.
- Contact, privacybeleid en cookiebeleid.
- 404, sitemap.xml, robots.txt, beveiligingsheaders en een www-naar-apex redirect.
- JSON-LD op elke pagina (Organization, WebSite, ItemList, Article, FAQPage, BreadcrumbList, WebPage, ContactPage). Bewust geen aggregateRating, want self-serving reviews leveren geen sterren op.
- Eigen huisstijl: ink met energiek oranje, en kleurcodering per aanbieder.

## De drie aanbieders en hun accent

- YourHealth Personal Training, kleur oranje, accent grootste netwerk en breedste keuze.
- LET'S DO IT Personal Training, kleur framboos, accent voor vrouwen door vrouwen.
- Jouw Personal Trainer aan Huis, kleur groen, accent sterk in 40-plus.

YourHealth en LET'S DO IT delen in de praktijk veel bronmateriaal. In de teksten zijn ze daarom op verschillende eigenschappen uitgewerkt, zodat ze als twee losse bedrijven lezen.

## Logo's

De logobestanden zaten niet bij de aanlevering. De aanbieders staan nu met een nette tekst-wordmark in de kaarten. Zet de logo's in `assets/img/logos/` en geef even door dat ze er zijn, dan plaats ik ze in de kaarten en op de aanbiederspagina's.

## Links naar de drie bedrijven

De links naar de Amstelveen-pagina's van de aanbieders zijn gewone gevolgde links, met `target="_blank"` en `rel="noopener"`. Dat past bij een redactionele aanbeveling en laat linkwaarde doorstromen naar de drie sites.

Is er sprake van een betaalde plaatsing of een andere commerciele afspraak, voeg dan `rel="noopener sponsored"` toe. Dat staat op twee plekken in `build.py`: in `provider_card()` (homepage) en in `provider_page()` plus de helper `ext()` (aanbiederspagina's). De keuze ligt bij de beheerder.

## E-mailadres

Het contactadres is `info@personaltrainerinamstelveen.nl`. Aanpassen kan via de variabele `EMAIL` boven in `build.py`, daarna opnieuw bouwen.

## Deployen via GitHub en Cloudflare Pages

1. Maak een repository op GitHub en zet de inhoud van `beterbody-project`, hier dus de projectmap met `build.py`, `assets/`, `README.md` en `.gitignore`, in de hoofdmap van de repo.
2. Ga in Cloudflare naar Workers and Pages, Create application, tab Pages, Connect to Git.
3. Kies de repository en de branch `main`.
4. Build settings: Framework preset op None, Build command `python3 build.py`, Build output directory `site`.
5. Save and Deploy. Daarna het domein koppelen onder Custom domains, met zowel `personaltrainerinamstelveen.nl` als `www.personaltrainerinamstelveen.nl`, zodat de www-redirect werkt.

Mocht de build vastlopen op de Python-versie, zet dan onder Settings, Environment variables een variabele `PYTHON_VERSION` op bijvoorbeeld `3.12`.

## Een aanbieder toevoegen of aanpassen

1. Open `build.py` en zoek de lijst `PROVIDERS`.
2. Pas een bestaand blok aan of voeg een nieuw blok toe met `slug`, `name`, `cc` (kleur), `badge`, `tagline`, `url`, `usp`, `for`, `lead` en `sections`.
3. Draai `python3 build.py`. De homepage, de aanbiederspagina, het menu en de sitemap worden automatisch bijgewerkt.

## Stijlregels in de teksten

De teksten houden zich aan vaste regels: geen liggende streepjes, geen emoji, geen tweede persoon (geen je, jij, jullie of uw), korte en duidelijke taal. De enige uitzondering op de tweede persoon is de bedrijfsnaam Jouw Personal Trainer aan Huis, want dat is een eigennaam.

## Lettertypen

Bricolage Grotesque en Hanken Grotesk worden geladen via Google Fonts. Wie geen externe verzoeken wil, kan de lettertypen zelf hosten en de `<link>` in `build.py` vervangen door een lokale `@font-face`.
