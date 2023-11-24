import csv
import random
import statistics
import webbrowser

# Funkcja do wczytania danych z pliku CSV
def read_lego_data(file_path):
    lego_data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lego_data.append(row)
    return lego_data

# Funkcja do przetwarzania danych i wyświetlania wyników
def analyze_lego_data(lego_data, year):
    sets_by_year = [set_data for set_data in lego_data if int(set_data['year']) == year]

    if not sets_by_year:
        print(f'Brak danych dla roku {year}.')
        return

    # Ilość zestawów
    num_sets = len(sets_by_year)

    # Lista ilości elementów w zestawach
    num_pieces_list = [int(set_data['num_parts']) for set_data in sets_by_year]

    # Średnia ilość elementów
    average_num_pieces = statistics.mean(num_pieces_list)

    # Mediana ilości elementów
    median_num_pieces = statistics.median(num_pieces_list)

    print(f'\nDane dla roku {year}:')
    print(f'Ilość zestawów: {num_sets}')
    print(f'Średnia ilość elementów: {average_num_pieces:.2f}')
    print(f'Mediana ilości elementów: {median_num_pieces}')

    # Losowanie i wyświetlanie losowego zdjęcia
    try:
        random_set = random.choice(sets_by_year)
        if 'img_url' in random_set:
            random_set_image_url = random_set['img_url']
            print(f'\nLosowe zdjęcie zestawu z roku {year}: {random_set_image_url}')
            webbrowser.open(random_set_image_url)
        else:
            print(f'Brak informacji o URL obrazu dla wybranego zestawu.')
    except IndexError:
        print(f'Brak zestawów dla roku {year}.')
    except Exception as e:
        print(f'Wystąpił nieoczekiwany błąd: {str(e)}')

if __name__ == "__main__":
    # Podaj ścieżkę do pobranego pliku CSV
    file_path = 'lego/sets.csv'

    # Podaj rok (od 1949 do 2024)
    selected_year = int(input('Podaj rok (od 1949 do 2024): '))

    # Wczytaj dane
    lego_data = read_lego_data(file_path)

    # Analizuj i wyświetl wyniki
    analyze_lego_data(lego_data, selected_year)
