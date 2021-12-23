# Laskin

Sovellus on peruslaskin, jossa on enemmän toiminnallisuuksia kuin taskulaskimessa (eli +,-,*,/) ja vähemmän kuin esimerkiksi peruskoulun laskimessa. 

## Releases
[Releases](https://github.com/TuomasVaara/ot-harjoitustyo/releases)

## Dokumentaatio


- [Vaatimusmäärittely](https://github.com/TuomasVaara/ot-harjoitustyo/blob/master/Dokumentaatio/Vaatimusm%C3%A4%C3%A4rittely.md)
- [Työaikakirjanpito](https://github.com/TuomasVaara/ot-harjoitustyo/blob/master/Dokumentaatio/tuntikirjanpito.md)
- [Arkkitehtuurikuvaus](https://github.com/TuomasVaara/ot-harjoitustyo/blob/master/Dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](https://github.com/TuomasVaara/ot-harjoitustyo/blob/master/Dokumentaatio/testausdokumentti.md)
- [Käyttöohje](https://github.com/TuomasVaara/ot-harjoitustyo/blob/master/Dokumentaatio/K%C3%A4ytt%C3%B6ohje.md)

## Asennus

1. Asenna riippuvuudet komennolla: 
```bash
poetry install
```
2. Käynnistä sovellus komennolla: 
```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen
Ohjelma pystytään suorittamaan komennolla:
```bash
poetry run invoke start
```
### Testaus
Testit voi suorittaa komennolla: 
```bash
poetry run invoke test
```
### Testikattavuus
Testikattavuusraportin voi generoida komennolla:
```bash
poetry run coverage-report
```
Raportti generoituu _htmlcov_-hakemistoon.

### Pylint
Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla: 
```bash
poetry run invoke lint
```
