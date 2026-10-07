## Manuaalisen julkaisun mittaus
| # | Aika | Kommentit |
|---|---|---|
| 1 | 6 min 42 s | Komentoja piti tarkistella kesken testin ajon ja kirjoittaa uudestaan |
| 2 | 6 min 18 s | Docker komentojen kanssa kirjoitusvirheitä |
| 3 | 6 min 26 s | Kirjoitusvirheitä komennoissa |
| 4 | 2 min 58 s | Kaikki sujui ongelmitta |
| 5 | 2 min 48 s | Komentojen kirjoittaminen helpottuu toistojen myötä |

**Keskiarvo, kerrat 1-3:** 6 min 29 s
**Keskiarvo, kerrat 4-5:** 2 min 53 s
**Havainto:** oppimisvaikutus lyhensi kierroksen kestoa yli 50 %.

## Havaitut virheet ja ongelmat

| # | Päivämäärä | Havaittu missä | Virhe | Korjaus |
|---|---|---|---|---|
| 1 | 2026-10-07 | Paikallinen ajo (ruff) | Ruff ilmoitti kolmesta UP045-virheestä tiedostossa `monitor/checker.py`: `Optional[X]`-tyyppimerkinnät tulee kirjoittaa muotoon `X \| None` | Korjattu komennolla `ruff check . --fix`, minkä jälkeen testit ajettiin uudelleen |

| 2 | 2026-10-07 | Paikallinen Docker-ajo | `ENV PYTHONUNBUFFERED=1` oli kirjoitettu väärin Dockerfileen, joten Pythonin tuloste ei näkynyt `docker logs` -komennossa | Kirjoitusvirhe korjattu ja image rakennettu uudelleen |

### Havainto 1: tyylivirhe linttauksessa

Sovelluksen ensimmäisessä versiossa tyyppimerkinnät oli kirjoitettu `typing.Optional`-tavalla. Paikallisesti ajettu `ruff check .` ilmoitti kolme virhettä (UP045), vaikka kaikki neljä yksikkötestiä menivät läpi. Virhe ei vaikuttanut ohjelman toimintaan, vaan koski koodin tyyliä nykyaikaisen Python-syntaksin mukaan.

Havainto osoittaa, että linttaus löytää eri asioita kuin testit. Testit varmistavat toiminnallisuuden, linter koodin yhtenäisyyden. Kun linttaus on osa CI-putkea, tällainen virhe ei pääse pääkoodihaaraan huomaamatta, vaikka kehittäjä unohtaisi ajaa tarkistuksen paikallisesti.

Korjaus oli automaattinen (`--fix`) ja vei alle minuutin.