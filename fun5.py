# Stworzyc funkcje kantor
# ma posiadac dwie funkcje wewnętrzne usd, eur
# w zaleznosci od konfiguracji mamy zwraca jedną z nich
# konfiguracje przekazujemy podczas uruchomienia kantoru
# mozliwosc przekazania dowolnej kwoty
def kantor(waluta):
    print("Uruchomienie kantoru")

    def usd(kwota=0):
        print("Wymieniam dolary", kwota * 4.01)

    def eur(kwota=0):
        print("Wymieniam euro", kwota * 4.40)

    if waluta == 'eur':
        return eur
    else:
        return usd


kantor_usd = kantor('usd')  # Uruchomienie kantoru
kantor_usd()  # Wymieniam dolary
kantor_eur = kantor('eur')
kantor_eur()
kantor_usd()
kantor_eur(1000)  # Wymieniam euro 1000
