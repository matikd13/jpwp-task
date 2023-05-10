# Podstawy Flaska i http proxy

***

Autorzy: **Kacper Kwaśny, Mateusz Jakubowski**

***
https://flask.palletsprojects.com/ tutaj znajdziesz prawie wszystkie informacje potrzebne 
do zrobienia zadania.

***
### Zadanie 1: utworzenie środowiska i uruchomienie Flaska
Utwórz środowisko wirtualne i zainstaluj Flaska przy użyciu pip.
***
Pomocne komendy:
>python -m venv venv

Tworzy wirtualne środowisko

> .venv\Scripts\activate 

Aktywacja środowiska dla systemów Windows

>  . .venv/bin/activate
 
Aktywacja środowiska dla systemów linux/macos

> pip install Flask

Instalacja Flaska

***
Po instalacji napisz prosty skrypt, taki jak w pliku `zad1.py`, a nastepnie
uruchom serwer tą komendą 

>flask --app `nazwa pliku` run

Prześlij zdjęcie konsoli, strony i kodu.
***
### Zadanie 2: proste przekierowanie 

Nauczysz się teraz wysyłać i przekazywać proste requesty przy użyciu Flaska. 

Stwórz funckję i dodaj do niej dekorator, który akceptuje tylko zapytania GET oraz przyjmuje URL requestu i zapisuje ją do zmiennej.   

Przykład takiego dekoratora:
>@app.route('/<<span>path:sciezka</span>>',methods=['GET'])

Nasza funkcja nie zadziała jednak gdy, w przeglądarkę wpiszemy sam adres, aby to naprawić, dodaj nad
wcześniej stworzony dekorator nowy, który będzie działał, kiedy wpiszemy sam adres.

Następnie w utworzonej funkcji zrób request do dowolnej strony, np. AGH.
Użyj do tego biblioteki `requests`

Przykład zapytania:
>resp = requests.get(f<span>'https:/</span>/agh.edu.pl/{zmienna z url}')

Następnym krokiem jest zwrócenie responsu ze strony do naszego klienta. Aby to zrobić, należy
stworzyć obiekt `Response`
>response = Response(resp.content, resp.status_code, headers)

Zgodnie z RFC, musimy usunąć także hop-by-hop headers.
Spróbuj usunąć z naszego responsa te nagłówki:
- content-encoding
- content-length
- transfer-encoding
- connection

Oryginalne nagłówki znajdują się w zmiennej `resp.raw.headers.items()`

Teraz wchodzą na serwer utworzony przez flaska, przeglądarka powinna zwrócić stronę AGH.

Prześlij zdjęcie strony i kodu.
***
### Zadanie 3: przekierowanie na różne strony na podstawie nagłówka `Host`

Teraz kiedy umiesz już przekierować ruch, dodamy sprawdzanie, na jaką domenę chcemy się dostać i przekierujemy 
ruch na dwie różne strony.

Dla ułatwienia zadania przyjmujemy, że istnieją dwie domeny:
- 127.0.0.1
- localhost

W zmiennej `request.headers['Host']` możemy sprawdzić, na jaką chcemy wysłać requesta. 
Należy usunąć z niej port. 

Następnie w if sprawdzamy, na jaką stronę chcemy przekierować użytkownika i zapisujemy to w zmiennej.
Przykładowy kod:

>    if domain == "127.0.0.1":<br>
>    &nbsp;&nbsp;&nbsp;&nbsp;target = "h<span>ttps://agh.edu.pl"

Teraz wystarczy mienić URL w naszym requescie.
>resp = requests.get(f'{target}/{path}')

Prześlij zdjęcie kodu.
***
### Zadanie 4: blokowanie zbyt dużej ilości zapytań

Na sam koniec dodamy bardzo proste zabezpieczenie. Dodaj zmienną globalną, w której będziesz liczył 
ilość zapytań wysłanych do serwera. Jeżeli ilość przekroczy wybraną maksymalną, zwróć błąd. 

Zadanie powinno być już proste, dlatego nie dajemy podpowiedzi :stuck_out_tongue:

Prześlij zdjęcie kodu.

#### Zadanie dla ambitnych
Dodaj funkcję, która po kilku sekundach od zablokowania zapytań, zresetuje nasze zabezpieczenie.
Może ci się przydać wiedza z poprzednich prezentacji.