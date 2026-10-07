## Havaitut virheet ja ongelmat

| # | Päivämäärä | Havaittu missä | Virhe | Korjaus |
|---|---|---|---|---|
| 1 | 2026-10-07 | Paikallinen ajo (ruff) | Ruff ilmoitti kolmesta UP045-virheestä tiedostossa `monitor/checker.py`: `Optional[X]`-tyyppimerkinnät tulee kirjoittaa muotoon `X \| None` | Korjattu komennolla `ruff check . --fix`, minkä jälkeen testit ajettiin uudelleen |

### Havainto 1: tyylivirhe linttauksessa

Sovelluksen ensimmäisessä versiossa tyyppimerkinnät oli kirjoitettu `typing.Optional`-tavalla. Paikallisesti ajettu `ruff check .` ilmoitti kolme virhettä (UP045), vaikka kaikki neljä yksikkötestiä menivät läpi. Virhe ei vaikuttanut ohjelman toimintaan, vaan koski koodin tyyliä nykyaikaisen Python-syntaksin mukaan.

Havainto osoittaa, että linttaus löytää eri asioita kuin testit. Testit varmistavat toiminnallisuuden, linter koodin yhtenäisyyden. Kun linttaus on osa CI-putkea, tällainen virhe ei pääse pääkoodihaaraan huomaamatta, vaikka kehittäjä unohtaisi ajaa tarkistuksen paikallisesti.

Korjaus oli automaattinen (`--fix`) ja vei alle minuutin.