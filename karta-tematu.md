# Karta zgłoszenia tematu projektu

**Grupa:** L3 (niestacjonarna) **Data zgłoszenia:** 03.10.2026

---

## 1. Skład zespołu

|||
|---|---|
|Imię i nazwisko|Nr albumu|Rola w zespole|
|Michał S|31885|dane, implementacja, ewaluacja, dokumentacja, koordynacja|
|Iza J|31881|dane, implementacja, ewaluacja, dokumentacja, koordynacja|

Rola to nie stanowisko, tylko deklaracja, za co ta osoba odpowiada: dane, implementacja, ewaluacja, dokumentacja, koordynacja.

## 2. Tytuł projektu

**Po polsku:**
eepyAI
**Po angielsku:**
eepyAI
## 3. Problem
System ma za zadanie przewidzieć na podstawie zebranych danych poziom zmęczenia osoby biorącej udział w badaniu. Na podstawie danych bio danej osoby oraz danych z użycia smartfona system przewidzi w zakresie 1-10, jak bardzo dana osoba będzie zmęczona następnego dnia.
_Co system ma robić i dla kogo. Opis sytuacji, nie nazwy technologii. 3–5 zdań._

## 4. Dlaczego zwykły algorytm nie wystarczy

_Wskażcie jeden z trzech powodów omawianych na zajęciach i uzasadnijcie:_

- [x] nie umiemy zapisać reguły krok po kroku
- [ ] przepis istnieje, ale jest obliczeniowo za drogi
- [x] reguł jest za dużo i zmieniają się w czasie

_Uzasadnienie, 2–3 zdania:_
Poziom zmęczenia następnego dnia to wartość na którą wpływ ma wiele czynników w nieokreślony sposób. Na dodatek sposób użycia smartfona oraz jego wpływ na osoby bardzo się różni.

---

> Punkty poniżej wypełniacie do 3.10.

---

## 5. Technologia SI

- [ ] sieć neuronowa
- [ ] system ekspertowy / wnioskowanie regułowe
- [ ] algorytm genetyczny
- [x] klasyczne uczenie maszynowe
- [ ] inne:

_Dlaczego akurat ta technologia pasuje do tego problemu, 2–3 zdania:_
 
Systemy ekspertowe wymagałyby zdefiniowania warunków. Zmęczenie i wpływ stylu życia są jednak zbyt złożone, indywidualne i subtelne, by opisać je statyczną listą warunków.

Sieci neuronowe pasowałyby raczej do dużych danych historycznych o dużej rozdzielczości. Obrany przez nas zbiór danych to pojedyncze zagregowane dane dzienne poszczególnych osób (1 osoba - 1 dzień). Sieci neuronowe są możliwe do zastosowania ale prawdopodobnie nie będą lepsze niż uczenie maszynowe.

Algorytm genetyczny służy do problemów optymalizacyjnych (np. znajdowanie najkrótszej trasy lub układanie grafiku), a nie do predykcji/analizy wzorców w danych.

## 6. Dane

|||
|---|---|
|Źródło|https://www.kaggle.com/datasets/samartalwar/sleep-debt-and-screen-time-late-night-phone-habits|
|Rozmiar i format|8500 rekordów 18 kolumn csv|
|Czy są już dostępne?|tak|
|Jeśli nie — plan pozyskania||

Uzasadnienie (dlaczego takie dane?):
Inne publiczne datasety nie mają wartości next_day_fatigue_score lub ekwiwalentu takiej wartości. W innych badaniach celem nie było zmierzenie zmęczenia lecz wpływu jakości snu na parametry zdrowotne i inne dziedziny życia (edukacja, sport)
Przejrzane datasety:
https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset
https://www.kaggle.com/datasets/aamir28/student-sleep-screen-time-and-academic-performance
https://www.kaggle.com/datasets/amith1707/fitness-and-health-simulation-dataset

## 7. Stos technologiczny
Python3
pandas,numpy,scikit-learn,matplotlib

_Język, biblioteki, środowisko uruchomieniowe. Pamiętajcie: wszystko ma działać na CPU, bez karty graficznej._

## 8. Kryterium sukcesu
Program przewiduje wartość next_day_fatigue_score ze średnim błędem bezwzględnym == 1.5
_Po czym poznamy, że projekt działa. Jaka metryka, jaki próg. Liczba, nie deklaracja._

## 9. Zakres minimalny
Skrypt w Pythonie, który wczyta dane z pliku, wykona na nich pewne operacje (między innymi podzieli dane na treningowe i testowe, może wykluczy pewne kolumny/rekordy). Następnie dane zostaną wykorzystane do nauczenia modelu. Następnie wykorzystamy model do przewidywania na danych testowych
_Co powstanie na pewno. To jest obietnica, z której będziecie rozliczeni._

## 10. Zakres opcjonalny
Wykonanie powyższego na innych modelach 
_Co dorobicie, jeśli starczy czasu. Brak realizacji tej części nie obniża oceny._

## 11. Repozytorium

_Link:_ [https://github.com/Krestal/eepyAI/tree/main](https://github.com/Krestal/eepyAI)

## 12. Główne ryzyko i plan awaryjny
Model może przewidywać ale z błędem większym niż zamierzony. Wtedy postaramy się o lepszy dobór danych testowych lub zmienimy model.
_Co najprawdopodobniej pójdzie nie tak i co wtedy zrobicie._

## 13. Podział pracy w czasie

|Etap|Kto|Szacowany czas|
|---|---|---|
|Dane i przygotowanie|Iza J|5h|
|Implementacja|Michał S, Iza J|10h|
|Eksperymenty i ewaluacja|Michał S, Iza J|24h|
|Dokumentacja PL|Iza J|5h|
|Dokumentacja EN|Iza J|5h|
|Prezentacja|Michał S, Iza J|10h|
|**Razem na osobę**||**28–30 h**|

---

## Decyzja prowadzącego

_Wypełnia prowadzący — nie edytujcie tej sekcji._

- [ ] zatwierdzony
- [ ] do poprawy

**Uwagi:**
