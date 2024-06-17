# Automatyzacja testów API z wykorzystaniem curl

## Opis
Skrypt `test_api.py` automatycznie testuje różne endpointy API przy użyciu narzędzia curl. Wysyła żądania HTTP do wybranej publicznej API (JSONPlaceholder) i sprawdza, czy odpowiedzi są poprawne (statusy HTTP i kluczowe elementy w odpowiedziach JSON).

## Uruchomienie
1. Upewnij się, że masz zainstalowany Python oraz curl.
2. Uruchom skrypt:
   ```bash
   python test_api.py
