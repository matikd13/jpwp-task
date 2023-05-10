# Podstawy Flaska i http proxy

***

Autorzy: **Kacper Kwaśny, Mateusz Jakubowski**

***

### Zadanie 1: utworzenie środowiska i uruchomienie Flaska
Utwórz środowisko wirtualne i zainstaluj Flaska przy użyciu pip.
Pomocne komendy:
>python3 -m venv venv

Tworzy wirtualne środowisko

> .venv\Scripts\activate 

Aktywacja środowiska dla systemów Windows

>  . .venv/bin/activate
 
Aktywacja środowiska dla systemów linux/macos

> pip install Flask

Instalacja Flaska

Po instalacji napisz prosty skrypt, taki jak w pliku `zad1.py`, a nastepnie
uruchom serwer tą komendą 

>flask --app `nazwa pliku` run