import csv
import os

sciezka_do_pliku = input("Podaj ścieżkę do pliku CSV: ")


if not os.path.isfile(sciezka_do_pliku):
    print(f"Plik o ścieżce '{sciezka_do_pliku}' nie został znaleziony.")
else:
    try:
        with open(sciezka_do_pliku, newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            
            liczba_wierszy = 5 
            for i, row in enumerate(csvreader):
                print(row)
                if i >= liczba_wierszy - 1:
                    break
    except Exception as e:
        print(f"Wystąpił błąd: {e}")