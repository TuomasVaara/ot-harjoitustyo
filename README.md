# Laskin

Sovellus on peruslaskin, jossa on enemmän toiminnallisuuksia kuin taskulaskimessa (eli +,-,*,/) ja vähemmän kuin esimerkiksi peruskoulun laskimessa. 

## Release1
[Release1](https://github.com/TuomasVaara/ot-harjoitustyo/releases/tag/viikko5)

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
Testit voi suorittaa komennolla: poetry run invoke test

### Testikattavuus
Testikattavuusraportin voi generoida komennolla: poetry run coverage-report

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint
Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla: poetry run invoke lint
