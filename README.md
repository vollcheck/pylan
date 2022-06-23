# Pylan

<img src="https://img.shields.io/badge/tests-passed-green.svg" /> <img src="https://img.shields.io/badge/made%20with-Python-purple.svg" /> <img src="https://img.shields.io/badge/License-MIT-red.svg" />
           
<br />

## <p align="center">O aplikacji</p>

Aplikacja Pylan informuje użytkownika o nadchodzącym planie zajęć na Wydziale Zarządzania Uniwersytetu Gdańskiego. Możliwe jest ograniczenie wyszukiwań planu dzięki wgranym w aplikację komendom.

## <p align="center">Uruchomienie</p>
Aby uruchomić aplikację musimy przygotować wirtualne środowisko Pythona i w nim zainstalować potrzebne biblioteki. Aby to uczynić, musimy wykonać w CMD następujące komendy: 

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Po takim przygotowaniu możemy uruchomić aplikację:

```console
λ python pylan.py
```
```console
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┓
┃ Subject                                            ┃ Date       ┃ Start Time ┃ End Time ┃ Location ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━┩
│ Testowanie aplikacji                               │ 28/05/2022 │ 08.00      │ 09.30    │   C-2    │
│ Warsztaty z przedsiębiorczości [ćw]                │ 28/05/2022 │ 09.45      │ 11.15    │   C-4    │
│ Testowanie aplikacji                               │ 28/05/2022 │ 11.30      │ 15.00    │   C-25   │
│ Rachunkowość                                       │ 28/05/2022 │ 15.15      │ 16.45    │   C-20   │
│ Rachunkowość [ćw]                                  │ 28/05/2022 │ 17.00      │ 18.30    │   C-20   │
│ Serwisy e-learningowe 2.0                          │ 29/05/2022 │ 08.00      │ 11.15    │   C-36   │
│ Programowanie aplikacji wieloplatformowych         │ 29/05/2022 │ 11.30      │ 15.00    │   C-36   │
│ Programowanie aplikacji rozproszonych w C#         │ 29/05/2022 │ 15.15      │ 18.30    │   C-36   │
│ Programowanie aplikacji rozproszonych w C#         │ 11/06/2022 │ 08.00      │ 09.30    │   C-36   │
│ Programowanie aplikacji wieloplatformowych         │ 11/06/2022 │ 09.45      │ 13.00    │   C-36   │
│ Testowanie aplikacji                               │ 11/06/2022 │ 13.30      │ 15.00    │   C-24   │
│ Serwisy e-learningowe 2.0                          │ 11/06/2022 │ 15.15      │ 18.30    │   C-25   │
│ Serwisy e-learningowe 2.0                          │ 12/06/2022 │ 08.45      │ 13.00    │  A-118   │
│ Skalowanie sieci komputerowych - Scaling Networks  │ 12/06/2022 │ 13.30      │ 15.00    │  A-118   │
│ Metodyka pisania pracy dyplomowej [ćw]             │ 12/06/2022 │ 15.15      │ 16.45    │   C-21   │
│ Rachunkowość                                       │ 03/07/2022 │ 11.30      │ 13.00    │  WZ-310  │
└────────────────────────────────────────────────────┴────────────┴────────────┴──────────┴──────────┘
```

## <p align="center">Licencja</p>

Pylan jest open-sourcowym projektem na licencji MIT. Do utworzenia projektu został użyty Python w wersji 3.10 na licencji MIT, biblioteka [requests](https://pypi.org/project/requests/) na licencji Apache Software License (Apache 2.0).

## <p align="center">Autor</p> 
[Jacek Walczak](https://github.com/vollcheck)<br>

## <p align="center"> Specyfikacja wymagań </p>
<table>
  
  <tr>
    <th>Definicja wymagania(scenariusz)</th>
    <td>Użytkownik wyszukuje plan studiów na najbliższy weekend</td>
  </tr>
  
  <tr>
    <th>Aktorzy</th>
    <td>Użytkownik chcący wyszukać plan studiów</td>
  </tr>
  
   <tr>
    <th>Warunki początkowe</th>
    <td>Użytkownik wykorzystuje konsolę do interakcji z aplikacją</td>
  </tr>
   
  <tr>
    <th>Przebieg realizacji scenariusza</th>
    <td>
      <ul>
      <li>Użytkownik otwiera konsolę i przechodzi do katalogu zawierającego aplikację `pylan`</li>
      <li>Dokonuje także wprowadzenia potrzebnych komend dla uzyskania wymaganego wyniku</li>
      <li>System wyświetla plan zajęć na najbliższy weekend przekazując informacje w tabeli z podziałem na nazwę przedmiotu, czas trwania i lokalizację</li>   
      </ul>
    </td>
  </tr>
</table>
<br>
<b>Wymagania funkcjonalne</b>
<ul>
  <li>użytkownik będzie mógł przeszukać plan zajęć na uczelni dla wybranej grupy</li>
  <li>strona internetowa udostępni plan zajęć w postaci statycznego pliku CSV</li>
</ul>
<br>
<b>Wymagania niefunkcjonalne</b>
<ul>
  <li>dostępność/niezawodność - strona powinna być dostępna cały czas</li>
  <li>wydajność - strona powinna w szybkim czasie zwracać tabelę planu zajęć</li>
  <li>użyteczność - dzięki użyciu komend w konsoli możliwe jest ograniczenie </li>
</ul>

## <p align="center">Architektura systemu</p>
<p align="center"><b>Stos technologiczny - architektura rozwojowa</b></p>
<ul>
<li>Emacs (IDE)</li>
<li>Ekosystem Python 3.10</li>
</ul>

                                     
<p align="center">Stos technologiczny - architektura uruchomieniowa</p>
<ul>
                    <li>Python 3.10</li>
                    <li>biblioteki `requests` wraz z `requests-cache` do realizowania połączeń HTTP</li>
                    <li>biblioteka `click` do tworzenia komend (Command Line Interface)</li>
                    <li>biblioteka `rich` do TUI (Terminal User Interface)</li>
                    <li>Git</li>
</ul>
                 
## <p align="center">Testy</p>               
                 
Testy sprawdzają, czy przetwarzanie planu wedle podanych przez użytkownika komend działają. Testy są także stworzone w sposób, który pozwala na sprawdzenie, czy plan jest pobierany z cache (pamięci podręcznej), czy działa bez interetu lub czy poprawnie wyświetla się najbliższy weekend.

## Pylan API

### `-h, --help`

Pokaż komunikat `help` z dostępnymi komendami.

### `-s SUBJECT, --subject SUBJECT`

Pokaż plan dla wybranego przedmiotu. Możliwe podanie jest wyłącznie części nazwy przedmiotu.

```console
λ python pylan.py -s rachunkowo
```
```console
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┓
┃ Subject           ┃ Date       ┃ Start Time ┃ End Time ┃ Location ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━┩
│ Rachunkowość      │ 28/05/2022 │ 15.15      │ 16.45    │   C-20   │
│ Rachunkowość [ćw] │ 28/05/2022 │ 17.00      │ 18.30    │   C-20   │
│ Rachunkowość      │ 03/07/2022 │ 11.30      │ 13.00    │  WZ-310  │
└───────────────────┴────────────┴────────────┴──────────┴──────────┘
```


### `-d REQUESTED_DATE, --date REQUESTED_DATE`

Pokaż plan dla wybranej daty przekazanej w formacie `dd/mm/yyyy`.

```console
λ python pylan.py -d 28/05/2022
```
```console
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┓
┃ Subject                             ┃ Date       ┃ Start Time ┃ End Time ┃ Location ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━┩
│ Testowanie aplikacji                │ 28/05/2022 │ 08.00      │ 09.30    │   C-2    │
│ Warsztaty z przedsiębiorczości [ćw] │ 28/05/2022 │ 09.45      │ 11.15    │   C-4    │
│ Testowanie aplikacji                │ 28/05/2022 │ 11.30      │ 15.00    │   C-25   │
│ Rachunkowość                        │ 28/05/2022 │ 15.15      │ 16.45    │   C-20   │
│ Rachunkowość [ćw]                   │ 28/05/2022 │ 17.00      │ 18.30    │   C-20   │
└─────────────────────────────────────┴────────────┴────────────┴──────────┴──────────┘
```

### `-n, --next`

Pokaż plan na najbliższy weekend.

```console
λ python pylan.py -n
```
```console
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┓
┃ Subject                                     ┃ Date       ┃ Start Time ┃ End Time ┃ Location ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━┩
│ Testowanie aplikacji                        │ 28/05/2022 │ 08.00      │ 09.30    │   C-2    │
│ Warsztaty z przedsiębiorczości [ćw]         │ 28/05/2022 │ 09.45      │ 11.15    │   C-4    │
│ Testowanie aplikacji                        │ 28/05/2022 │ 11.30      │ 15.00    │   C-25   │
│ Rachunkowość                                │ 28/05/2022 │ 15.15      │ 16.45    │   C-20   │
│ Rachunkowość [ćw]                           │ 28/05/2022 │ 17.00      │ 18.30    │   C-20   │
│ Serwisy e-learningowe 2.0                   │ 29/05/2022 │ 08.00      │ 11.15    │   C-36   │
│ Programowanie aplikacji wieloplatformowych  │ 29/05/2022 │ 11.30      │ 15.00    │   C-36   │
│ Programowanie aplikacji rozproszonych w C#  │ 29/05/2022 │ 15.15      │ 18.30    │   C-36   │
└─────────────────────────────────────────────┴────────────┴────────────┴──────────┴──────────┘
```

## Użyty Link do planu:
https://wzr.ug.edu.pl/.csv/plan_st.php?f1=N22-32&f2=4&jp=cf4f962e1fd3c99dd511843f647d568fb7957663

Możliwe jest użycie innego planu, wystarczy zmienić link do planu w pliku `link_plan.txt`.
