import csv

sciezka_do_pliku = input("Podaj ścieżkę do pliku CSV: ")

try:
    
    with open(sciezka_do_pliku, newline='', encoding='utf-8') as csvfile:
        
        csvreader = csv.reader(csvfile)
        
       
        liczba_wierszy = 5  
        for i, row in enumerate(csvreader):
            print(row)
            if i >= liczba_wierszy - 1:
                break
except FileNotFoundError:
    print(f"Plik o ścieżce '{sciezka_do_pliku}' nie został znaleziony.")
except Exception as e:
    print(f"Wystąpił błąd: {e}")