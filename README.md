# Laskin

Laskin toimii kuin normaali laskin eli sillä pystyy laskemaan peruslaskutoimitukset ja muita toiminnallisuuksia, kuten sin,cos,tan. 


## Dokumentaatio


- [Vaatimusmäärittely](https://github.com/TuomasVaara/ot-harjoitustyo/blob/master/Dokumentaatio/Vaatimusm%C3%A4%C3%A4rittely.md)
- [Työaikakirjanpito](https://github.com/TuomasVaara/ot-harjoitustyo/blob/master/Dokumentaatio/tuntikirjanpito.md)
- [Arkkitehtuurikuvaus](https://github.com/TuomasVaara/ot-harjoitustyo/blob/master/Dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Asenna riippuvuudet komennolla: poetry install

2. Käynnistä sovellus komennolla: poetry run invoke start


## Komentorivitoiminnot

### Ohjelman suorittaminen
Ohjelma pystytään suorittamaan komennolla: poetry run invoke start

### Testaus
Testi voi suorittaa komennolla: poetry run invoke test

### Testikattavuus
Testikattavuusraportin voi generoida komennolla: poetry run coverage-report

Raportti generoituu _htmlcov_-hakemistoon.
