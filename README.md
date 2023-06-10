# Wtyczka do Qgis
Wtyczka służy do liczenia przewyższeń między 2 punktami oraz do liczenia pola powierzchni dla 3 lub 4 punktów używając metody Gaussa.

## Minimalne wymagania sprzętowe :
- Windows 10  
- Qgis: 3.22.16

## Opis pracy wtyczki :
1. Użytkownik wybiera 2 lub 3/4 punkty odpowiednio dla obliczenia przewyższenia lub pola powierzchni.
2. Następnie otwiera wtyczkę i klika przycisk odpowiedni dla danego działania.
```sh
Oblicz przewyższenie
```
lub
```sh
Oblicz pole powierzchni
```
3. Wynik jest wyświetlany po prawej stronie przycisku.

## Możliwe błedy :
Kiedy użytkownik nie wybierze punktu albo wybrane zostanie za mało punktów dla danego obliczenia wyskoczy błąd:
```sh
Wybrano za mało punktów
```
Zaś kiedy wybrana zostanie za duża ilość punktów wtedy użytkownik zobaczy taki komunikat:
```sh
Wybrano za dużo punktów
```

## Uwagi techniczne :
Aby wtyczka działała poprawnie należy albo wgrać do programu Qgis plik .csv podobny do tego co jest podany powyżej lub w inny dowolny sposób tak aby w tabeli atrybutów znajdowały się kolumny o takich nazwach:
```sh
Nr X Y Z
```
oraz żeby wartości w tych kolumnach były liczbami zmiennoprzecinkowymi.
