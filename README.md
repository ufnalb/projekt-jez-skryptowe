## Opis projektu: Bot informacyjny do kryptowalut na Discorda

Celem projektu jest stworzenie bota informacyjnego do kryptowalut działającego na platformie Discord, który w czasie rzeczywistym będzie dostarczać dane o kursach wybranych kryptowalut, takich jak Bitcoin (BTC), Ethereum (ETH) i innych. Bot będzie aktualizować dane o kryptowalutach w czasie rzeczywistym przy użyciu WebSocketów oraz udostępniać użytkownikom wykresy obrazujące zmiany cen w zadanym okresie.

### Główne funkcje bota:
- **Aktualizacja cen w czasie rzeczywistym**  
    Bot wykorzysta WebSockety (np. z giełdy Binance) do monitorowania zmian cen wybranych kryptowalut. Ceny będą aktualizowane natychmiastowo, a bot będzie informować użytkowników o bieżącej cenie kryptowaluty.

- **Generowanie wykresów**  
    Bot będzie generować wykresy przedstawiające zmiany ceny kryptowaluty w czasie, np. w ciągu ostatnich 24 godzin, 7 dni itp. Wykresy będą tworzone przy pomocy biblioteki Matplotlib w Pythonie i wysyłane na Discorda.

- **Interakcja z użytkownikami Discorda**  
    Użytkownicy będą mogli zapytać bota o aktualną cenę danej kryptowaluty, a także poprosić o wygenerowanie wykresu pokazującego jej zmiany w określonym okresie czasu. Komendy będą wprowadzane w prosty sposób, np. `!crypto BTC`.

- **Wykorzystanie API**  
    Do pozyskiwania danych historycznych i aktualnych cen kryptowalut wykorzystane zostanie API giełdy, takie jak Binance lub CoinGecko.

### Technologie:
- **Python** – język programowania do implementacji logiki bota.
- **discord.py** – biblioteka do interakcji z Discordem.
- **WebSockety** – do uzyskiwania danych w czasie rzeczywistym z giełdy kryptowalut.
- **Matplotlib** – do generowania wykresów na podstawie danych o cenach kryptowalut.
- **Pandas** – do manipulacji i analizy danych, takich jak historia cen.
- **Requests** – do komunikacji z API i pobierania danych historycznych.

## Zastosowanie:
Projekt ten będzie doskonałą okazją do wykorzystania technologii WebSocketów i REST API w praktyce, a także do zapoznania się z tworzeniem botów na Discordzie. Będzie również świetnym przykładem pracy z danymi finansowymi i ich wizualizowaniem.

### Harmonogram realizacji:
1. **Etap 1**: Stworzenie podstawowej funkcjonalności bota (połączenie z Discordem, obsługa komend, wyciąganie danych z API).
2. **Etap 2**: Integracja z WebSocketami i implementacja funkcji aktualizacji cen w czasie rzeczywistym.
3. **Etap 3**: Tworzenie i wysyłanie wykresów do Discorda.
4. **Etap 4**: Testowanie i optymalizacja bota, dodanie dodatkowych funkcji (np. alerty cenowe).


### Opcjonalne technologie
CoinGecko API / Binance REST API – do pobierania historycznych danych
Docker – jeśli chcesz uruchomić bota w kontenerze
Redis / SQLite – jeśli chcesz przechowywać dane lokalnie
