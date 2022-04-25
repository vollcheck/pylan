# Studies plan assistant

## Pylan in action:

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

## Pylan API

### `-h, --help`

Show help message and exit.

### `-s SUBJECT, --subject SUBJECT`

Filter by the name of subject. It is possible to give only part of the subject name.

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

Show the plan for requested date.

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

Show the plan for the next weekend.

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

## Link used:
https://wzr.ug.edu.pl/.csv/plan_st.php?f1=N22-32&f2=4&jp=cf4f962e1fd3c99dd511843f647d568fb7957663

Probably you are able to discover more plans from the given link, just tweak with the query parameters.

## Possible room for improvement:

- [ ] validate date that comes with `requested_date` opt
- [ ] allow to show the completed plan
