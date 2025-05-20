# 1. Wprowadzenie

## 1.1. Cel dokumentu

Celem dokumentu "Strategia testów automatycznych" jest dostarczenie kompleksowych wytycznych dotyczących planowania,
implementacji, wykonania i analizy testów automatycznych w organizacji, ze szczególnym uwzględnieniem testów frontendu
przy użyciu Selenium/Selenide oraz testów API z wykorzystaniem Rest Assured. Dokument ten służy jako:

* Formalne określenie metodyki prowadzenia testów automatycznych w projekcie/organizacji
* Ustanowienie jednolitych standardów i praktyk dla wszystkich zespołów zaangażowanych w automatyzację testów UI i API
* Jasne zdefiniowanie metryk, KPI i kryteriów akceptacji dla oceny skuteczności testów automatycznych
* Zapewnienie spójnego podejścia do identyfikacji, analizy i rozwiązywania problemów związanych z testami automatycznymi
* Przedstawienie procesu integracji testów automatycznych z cyklem wytwarzania oprogramowania i pipeline'ami CI/CD
  zgodnie z podejściem Shift-Left
* Określenie ról i odpowiedzialności w procesie automatyzacji testów
* Zapewnienie zgodności z wymaganiami biznesowymi dotyczącymi jakości i szybkości dostarczania oprogramowania

Dokument ten stanowi punkt odniesienia dla zespołów projektowych, deweloperskich, testerskich, operacyjnych oraz
zarządzających, zapewniając wspólne zrozumienie celów i metod automatyzacji testów UI i API w systemach IT.

## 1.2. Zakres testów automatycznych

Zakres testów automatycznych określa granice i obszary systemu poddawane weryfikacji poprzez zautomatyzowane narzędzia i
skrypty, koncentrując się na testach interfejsu użytkownika (UI) oraz interfejsów programistycznych aplikacji (API).
Kompleksowa strategia testów automatycznych obejmuje:

### Testy UI z wykorzystaniem Selenium/Selenide

* **Funkcjonalne testy interfejsu użytkownika** - weryfikacja poprawności działania elementów interfejsu, przepływów
  użytkownika oraz interakcji między komponentami
* **Testy regresyjne UI** - automatyczne sprawdzanie, czy zmiany w jednym obszarze nie wpłynęły negatywnie na
  funkcjonalność w innych obszarach aplikacji
* **Testy cross-browser** - weryfikacja działania aplikacji w różnych przeglądarkach (Chrome, Firefox, Edge, Safari)
* **Testy responsywności** - sprawdzanie zachowania interfejsu na różnych rozmiarach ekranu
* **Walidacja formularzy** - automatyczna weryfikacja mechanizmów walidacji danych wprowadzanych przez użytkownika
* **Weryfikacja elementów wizualnych** - sprawdzanie obecności, widoczności i stanu elementów interfejsu

### Testy API z wykorzystaniem Rest Assured

* **Testy funkcjonalne API** - weryfikacja poprawności działania endpointów zgodnie ze specyfikacją
* **Testy kontraktów API** - sprawdzanie zgodności interfejsów ze zdefiniowanymi kontraktami (np. Swagger/OpenAPI)
* **Testy integracyjne** - weryfikacja poprawności komunikacji między różnymi komponentami systemu poprzez API
* **Testy bezpieczeństwa API** - podstawowa weryfikacja mechanizmów autoryzacji i uwierzytelniania
* **Testy obsługi błędów** - sprawdzanie poprawności obsługi nieprawidłowych żądań i danych wejściowych
* **Testy wydajnościowe API** - podstawowe testy wydajności kluczowych endpointów

### Podejście Shift-Left

Zakres testów automatycznych obejmuje również aspekty związane z podejściem Shift-Left, takie jak:

* Wczesna integracja testów automatycznych w cyklu wytwarzania oprogramowania
* Automatyzacja testów równolegle z rozwojem funkcjonalności
* Współpraca między deweloperami a testerami przy tworzeniu testów automatycznych
* Automatyzacja testów jednostkowych komponentów UI i API
* Integracja testów automatycznych w pipeline'ach CI/CD od najwcześniejszych etapów rozwoju

### Wyłączenia

Zakres testów automatycznych świadomie nie obejmuje:

* Testów wydajnościowych pełnego systemu
* Kompleksowych testów bezpieczeństwa
* Testów eksploracyjnych i testów użyteczności, które wymagają oceny człowieka
* Testów kompatybilności ze starszymi wersjami przeglądarek lub systemów operacyjnych, jeśli nie są wspierane przez
  specyfikację projektu

Zakres testów automatycznych jest dostosowany do specyfiki testowanego systemu, jego architektury oraz wymagań
biznesowych.
Strategia jasno definiuje, które komponenty, interfejsy i funkcjonalności podlegają automatyzacji testów,
a które wymagają manualnego podejścia, zapewniając tym samym optymalne wykorzystanie zasobów
i maksymalizację pokrycia testowego w kluczowych obszarach.

# 2. Metodyka testów automatycznych

## 2.1. Podejście do testów

Podejście do testów automatycznych definiuje fundamentalną filozofię i zasady, którymi kierujemy się podczas planowania
i realizacji automatyzacji. Nasze podejście opiera się na kilku kluczowych filarach:

### Strategiczna automatyzacja

Stosujemy świadome i celowe podejście do wyboru funkcjonalności do automatyzacji, koncentrując się na obszarach o:

1. Największej wartości biznesowej
2. Wysokim ryzyku defektów
3. Częstej modyfikacji
4. Powtarzalności w testach regresyjnych

Zamiast dążyć do automatyzacji wszystkiego, identyfikujemy te części systemu, gdzie automatyzacja przyniesie największy
zwrot z inwestycji. Analiza kosztów i korzyści pomaga w priorytetyzacji obszarów do automatyzacji.

### Piramida testów automatycznych

Nasze podejście opiera się na zmodyfikowanej piramidzie testów dla UI i API:

* **Podstawa piramidy**: Testy API jako fundament automatyzacji (szybkie, stabilne, łatwe w utrzymaniu)
* **Środkowa warstwa**: Testy komponentowe UI (testowanie izolowanych fragmentów interfejsu)
* **Wierzchołek piramidy**: End-to-end testy UI (pokrywające kluczowe ścieżki biznesowe)

Ta struktura zapewnia optymalne pokrycie przy jednoczesnym utrzymaniu szybkości wykonania i stabilności testów.

### Utrzymywalność i skalowalność

Projektujemy testy z myślą o ich długoterminowej utrzymywalności:

* Stosowanie wzorca Page Object Model dla testów UI
* Tworzenie abstrakcji dla endpointów API
* Separacja kodu testowego od danych testowych
* Modularność i możliwość wielokrotnego wykorzystania komponentów

### Szybka informacja zwrotna

Testy są projektowane tak, aby dostarczać szybkiej informacji zwrotnej o jakości kodu:

* Integracja z pipeline'ami CI/CD
* Priorytetyzacja krytycznych testów do wczesnego wykonania
* Paralelizacja wykonania testów
* Raportowanie wyników w czasie rzeczywistym

### Podejście iteracyjne i przyrostowe

Rozwijamy framework testowy i zestaw testów automatycznych iteracyjnie:

* Rozpoczynamy od podstawowych przypadków testowych
* Stopniowo zwiększamy pokrycie testowe
* Regularnie refaktoryzujemy kod testowy
* Dostosowujemy strategie testowe na podstawie zdobytych doświadczeń

## 2.2. Typy testów automatycznych

### 2.2.1. Testy UI z wykorzystaniem Selenium/Selenide

Testy UI z wykorzystaniem Selenium/Selenide koncentrują się na weryfikacji aplikacji z perspektywy użytkownika
końcowego, symulując interakcje z przeglądarką internetową.

#### Charakterystyka testów UI:

1. **Poziomy testów UI**: 
    * **Testy komponentowe** - testowanie izolowanych elementów UI (formularze, tabele, wykresy)
    * **Testy funkcjonalne** - weryfikacja konkretnych funkcjonalności interfejsu
    * **Testy end-to-end** - odzwierciedlenie pełnych ścieżek biznesowych użytkownika
    * **Testy cross-browser** - weryfikacja działania w różnych przeglądarkach
2. **Struktura testów UI**:
    * Wykorzystanie Page Object Pattern do reprezentacji stron i komponentów
    * Tworzenie abstrakcji dla powtarzalnych działań (np. logowanie, nawigacja)
    * Separacja logiki testowej od szczegółów technicznych lokalizacji elementów
    * Implementacja mechanizmów poczekania i synchronizacji dla operacji asynchronicznych
3. **Strategie stabilizacji**:
    * Dodanie inteligentnych warunków oczekiwania (wait conditions)
    * Mechanizmy ponownych prób dla niestabilnych operacji
    * Zrzuty ekranu i logi dla diagnostyki
    * Izolacja testów (czyszczenie stanu między testami)
4. **Przykładowa implementacja testu UI**:


```java
@Test
public void userShouldBeAbleToLogin() {
    LoginPage loginPage = new LoginPage();
    loginPage.open();
    
    DashboardPage dashboardPage = loginPage.login("user@example.com", "password");
    
    dashboardPage.isUserLoggedIn()
        .shouldBe(visible)
        .shouldHave(text("Welcome, User"));
}

```

Przyjmuje się testowanie UI w celu weryfikacji funkcjonalności aplikacji z perspektywy użytkownika końcowego.
Zatem testy UI odzwierciedlają pełne ścieżki biznesowe, w tym logowanie, nawigacja, edycje danych, itd.

___W tym przypadku bierze się pod uwagę jedynie **Testy End-to-End** jako kandydatów do automatyzacji.___

### 2.2.2. Testy API z wykorzystaniem Rest Assured

Testy API z wykorzystaniem Rest Assured weryfikują działanie interfejsów programistycznych aplikacji, koncentrując się
na poprawności, spójności i niezawodności komunikacji między komponentami systemu.

#### Charakterystyka testów API:

1. **Poziomy testów API**:
    * **Testy podstawowe (smoke)** - sprawdzenie dostępności i podstawowej funkcjonalności
    * **Testy funkcjonalne** - weryfikacja logiki biznesowej zaimplementowanej w API
    * **Testy kontraktowe** - sprawdzenie zgodności API ze specyfikacją
    * **Testy negatywne** - weryfikacja obsługi błędów i nieprawidłowych danych wejściowych
    * **Testy sekwencyjne** - weryfikacja przepływów wieloetapowych (np. tworzenie, aktualizacja, usunięcie)
2. **Struktura testów API**:
    * Organizacja testów według endpointów lub zasobów
    * Modelowanie danych wejściowych i wyjściowych za pomocą POJO
    * Centralizacja konfiguracji i wspólnych elementów (autentykacja, nagłówki)
    * Struktura given-when-then dla przejrzystości testów
3. **Strategie weryfikacji**:
    * Walidacja statusów odpowiedzi
    * Weryfikacja schematu JSON/XML
    * Sprawdzanie wartości biznesowych
    * Walidacja nagłówków i metadanych
    * Weryfikacja czasu odpowiedzi
4. **Przykładowa implementacja testu API**:


```java
@Test
public void shouldCreateNewUser() {
    UserDTO newUser = new UserDTO("Jan", "Kowalski", "john.kowalski@example.com");
    
    UserDTO createdUser = RestAssured
        .given()
            .contentType(ContentType.JSON)
            .body(newUser)
            .log().ifValidationFails()
        .when()
            .post("/api/users")
        .then()
            .statusCode(201)
            .extract().as(UserDTO.class);
    
    assertThat(createdUser.getId()).isNotNull();
    assertThat(createdUser.getEmail()).isEqualTo("john.kowalski@example.com");
}

```

## 2.3. Shift-Left Testing

Shift-Left Testing to podejście, w którym aktywności testowe są przesunięte do wcześniejszych faz cyklu wytwarzania
oprogramowania. W kontekście testów automatycznych oznacza to integrację automatyzacji od najwcześniejszych etapów
projektu.

### Kluczowe elementy Shift-Left w automatyzacji testów:

1. **Testowanie równoległe z rozwojem**:
    * Tworzenie testów automatycznych jednocześnie z rozwojem funkcjonalności
    * Współpraca deweloperów i testerów przy definiowaniu przypadków testowych
    * Wczesna identyfikacja problemów z testowalnością
2. **Automatyzacja od początku projektu**:
    * Budowanie frameworka testowego od pierwszych sprintów
    * Automatyzacja bazowych funkcjonalności zaraz po ich implementacji
    * Tworzenie podstawowych komponentów Page Object Model przed pełną implementacją UI
3. **Integracja z procesem deweloperskim**:
    * Deweloperzy uruchamiają testy automatyczne przed commit'em
    * Testy automatyczne jako część definicji ukończenia (DoD) dla user stories
    * Code review obejmujące również kod testów automatycznych
4. **Prewencja defektów**:
    * Wczesne wykrywanie problemów z testowalnością i designem
    * Definiowanie testów przed implementacją (Test First)
    * Wykorzystanie testów API do weryfikacji backendu przed pełną implementacją frontendu
5. **Praktyczne zastosowanie podejścia Shift-Left**:
    * Testerzy uczestniczą w planowaniu i analizie wymagań
    * Projektowanie testów już na etapie specyfikacji wymagań
    * Identyfikacja przypadków testowych do automatyzacji przed rozpoczęciem implementacji
    * Przygotowanie szkieletów testów automatycznych równolegle z projektowaniem architektury

## 2.4. Metryki i KPI w testach automatycznych

Metryki i KPI (Key Performance Indicators) stanowią fundament do obiektywnej oceny efektywności testów automatycznych i
umożliwiają podejmowanie decyzji opartych na danych.

### Kluczowe metryki dla testów UI i API:

1. **Metryki pokrycia**:
    * **Pokrycie funkcjonalne** - procent zautomatyzowanych przypadków testowych w stosunku do wszystkich
      zidentyfikowanych
    * **Pokrycie kodu** - procent kodu frontendowego pokryty testami UI i procent kodu backendowego pokryty testami API
    * **Pokrycie ryzyka** - procent obszarów wysokiego ryzyka objęty testami automatycznymi
2. **Metryki jakościowe**:
    * **Defect Detection Efficiency (DDE)** - procent defektów wykrytych przez testy automatyczne
    * **Defect Leakage** - liczba defektów, które przedostały się na produkcję mimo istniejących testów automatycznych
    * **False Positives** - liczba fałszywych alarmów zgłaszanych przez testy automatyczne
3. **Metryki wydajnościowe**:
    * **Czas wykonania** - średni czas potrzebny na wykonanie pełnego zestawu testów
    * **Czas do informacji zwrotnej** - jak szybko testy dostarczają informacji o wprowadzonych zmianach
    * **Narzut czasu na uruchomienie testów** w pipeline'ie CI/CD
4. **Metryki stabilności**:
    * **Test Flakiness Rate** - procent testów, które dają niespójne wyniki przy tych samych warunkach
    * **Mean Time Between Failures (MTBF)** - średni czas między awariami zestawu testów
    * **Test Pass Rate** - stosunek testów zakończonych sukcesem do wszystkich uruchomionych testów
5. **Metryki utrzymaniowe**:
    * **Effort Distribution** - proporcja czasu spędzonego na tworzenie vs. utrzymanie testów automatycznych
    * **Test Maintenance Index** - wskaźnik wysiłku potrzebnego do utrzymania testów po zmianach w aplikacji
    * **Test Update Frequency** - jak często testy muszą być aktualizowane

### KPI dla oceny efektywności strategii automatyzacji:

1. **Redukcja czasu testów**:
    * Średni czas zaoszczędzony dzięki automatyzacji w porównaniu do testów manualnych
    * Skrócenie czasu potrzebnego na weryfikację regresji
2. **Zwrot z inwestycji (ROI)**:
    * Koszt tworzenia i utrzymania testów automatycznych vs. korzyści z wykrytych defektów
    * Oszczędności wynikające z wcześniejszego wykrywania defektów
3. **Wskaźniki biznesowe**:
    * Redukcja Time-to-Market nowych funkcjonalności
    * Obniżenie kosztu jakości (Cost of Quality)
    * Zwiększenie częstotliwości wdrożeń na produkcję
4. **Cele dla metryk**:

| Metryka | Cel                             | Priorytet | Pokrycie funkcjonalne                         |
|---------|---------------------------------|-----------|-----------------------------------------------|
| \> 80%  | dla krytycznych funkcjonalności | Wysoki    | Procent pokrycia funkcjonalności w testach UI |
| \> 80%  | dla krytycznych funkcjonalności | Wysoki    | Procent pokrycia funkcjonalności w testach UI |
| \> 95%  | dla krytycznych funkcjonalności | Wysoki    | Test Pass Rate w ostatnich 10 runach          |
| \< 5%   | dla krytycznych funkcjonalności | Wysoki    | Test Flakiness Rate w ostatnich 10 runach     |
| \< 20%  | ogólny czas pracy               | Wysoki    | Utrzymanie testów                             |
| \< 60   | minut dla pełnego zestawu       | Średni    | Czas wykonania testów UI                      |
| \< 20   | minut dla pełnego zestawu       | Średni    | Czas wykonania testów API                     |

Regularne monitorowanie tych metryk pozwala na ciągłe doskonalenie strategii automatyzacji testów oraz podejmowanie
świadomych decyzji dotyczących inwestycji w rozwój testów automatycznych.

# 3. Narzędzia i frameworki

## 3.1. Selenium WebDriver

Selenium WebDriver jest fundamentalną technologią wykorzystywaną do automatyzacji testów interfejsu użytkownika w
aplikacjach webowych. Umożliwia programistyczną kontrolę przeglądarek internetowych, co pozwala na symulowanie
interakcji użytkownika z aplikacją.

### Główne cechy Selenium WebDriver:

1. **Wieloplatformowość**:
    * Wsparcie dla wszystkich głównych przeglądarek (Chrome, Firefox, Edge, Safari)
    * Kompatybilność z różnymi systemami operacyjnymi
    * Możliwość uruchamiania testów w trybie headless (bez interfejsu graficznego)
2. **API WebDriver**:
    * Standardowe, stabilne API do kontrolowania przeglądarek
    * Wsparcie dla różnych języków programowania (Java, C#, Python, JavaScript)
    * Bogaty zestaw metod do interakcji z elementami stron
3. **Lokalizatory elementów**:
    * Wyszukiwanie elementów za pomocą różnych strategii (ID, klasa, nazwa, XPath, CSS selektory)
    * Możliwość tworzenia złożonych selektorów dla dynamicznych elementów
    * Hierarchiczne wyszukiwanie elementów w strukturze DOM
4. **Możliwości akcji**:
    * Klikanie, wprowadzanie tekstu, zaznaczanie opcji
    * Obsługa akcji przesuwania, przeciągania i upuszczania (drag & drop)
    * Wykonywanie skryptów JavaScript w kontekście strony
    * Symulacja zdarzeń klawiatury i myszy
5. **Wykorzystanie w projekcie**:
    * Podstawowy silnik do automatyzacji interfejsu użytkownika
    * Bazowa technologia dla Selenide
    * Integracja z Selenium Grid do równoległego wykonywania testów
    * Wykonywanie testów cross-browser

### Przykładowa implementacja testu z wykorzystaniem Selenium WebDriver:


```java
public void testLoginFunctionality() {
    WebDriver driver = new ChromeDriver();
    try {
        // Otwarcie strony logowania
        driver.get("https://application-url.com/login");
        
        // Wprowadzenie danych logowania
        WebElement usernameField = driver.findElement(By.id("username"));
        WebElement passwordField = driver.findElement(By.id("password"));
        WebElement loginButton = driver.findElement(By.id("login-button"));
        
        usernameField.sendKeys("testuser");
        passwordField.sendKeys("password123");
        loginButton.click();
        
        // Oczekiwanie na załadowanie dashboard
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("dashboard")));
        
        // Weryfikacja pomyślnego logowania
        WebElement welcomeMessage = driver.findElement(By.id("welcome-message"));
        assertTrue(welcomeMessage.getText().contains("Welcome, TestUser"));
    } finally {
        driver.quit();
    }
}

```

### Wyzwania i ograniczenia:

* Wymaga zarządzania cyklem życia WebDrivera (inicjalizacja, czyszczenie)
* Bezpośrednie użycie wymaga implementacji jawnych mechanizmów oczekiwania
* Kod testowy może stać się obszerny i trudny w utrzymaniu bez odpowiedniej abstrakcji
* Testy mogą być niestabilne przy nieprawidłowym podejściu do synchronizacji

## 3.2. Selenide

Selenide to wrapper na Selenium WebDriver, zaprojektowany,
aby rozwiązać typowe problemy związane z automatyzacją UI i uprościć tworzenie testów.
Dzięki jego deklaratywnemu API, testy stają się bardziej zwięzłe, czytelne i stabilne.

### Główne cechy Selenide:

1. **Uproszczona składnia**:
    * Fluent API ułatwiające łańcuchowanie operacji
    * Krótszy i czytelniejszy kod testowy
    * Wbudowana inicjalizacja i zamykanie WebDrivera
2. **Automatyczne oczekiwanie**:
    * Inteligentne mechanizmy oczekiwania na elementy
    * Automatyczne ponowne próby w przypadku StaleElementReferenceException
    * Konfigurowalne timeouty dla różnych operacji
3. **Zaawansowane walidacje**:
    * Bogaty zestaw asercji dla elementów UI
    * Możliwość weryfikacji wielu właściwości naraz
    * Czytelne komunikaty błędów z załączonymi zrzutami ekranu
4. **Obsługa AJAX i JavaScript**:
    * Efektywna obsługa aplikacji wykorzystujących AJAX
    * Automatyczne oczekiwanie na zakończenie animacji i operacji asynchronicznych
    * Uproszczona praca z dynamicznie zmieniającym się DOM
5. **Wykorzystanie w projekcie**:
    * Podstawowy framework do implementacji testów UI
    * Integracja z Page Object Pattern
    * Obsługa złożonych interakcji użytkownika
    * Automatyczne tworzenie zrzutów ekranu dla nieudanych testów

### Przykładowa implementacja testu z wykorzystaniem Selenide:

java


```java
@Test
public void userCanLoginToSystem() {
    // Otwórz stronę logowania
    open("https://application-url.com/login");
    
    // Wprowadź dane logowania i kliknij przycisk
    $("#username").setValue("testuser");
    $("#password").setValue("password123");
    $("#login-button").click();
    
    // Weryfikacja pomyślnego logowania
    $("#dashboard").should(appear);
    $("#welcome-message").shouldHave(text("Welcome, TestUser"));
}

```

### Porównanie z czystym Selenium WebDriver:

| Aspekt             | Zarządzanie WebDriverem        | Obsługa oczekiwania         | Asercje                             | Obsługa AJAX i JavaScript            | Kod                           |
|--------------------|--------------------------------|-----------------------------|-------------------------------------|--------------------------------------|-------------------------------|
| Selenium WebDriver | Ręczne inicjowanie i zamykanie | Wymaga jawnej implementacji | Konieczność zewnętrznych bibliotek  | Konieczność dodatkowej implementacji | Rozwlekły, wymaga boilerplate |
| Selenide           | Automatyczne                   | Wbudowana automatycznie     | Wbudowane z inteligentnym czekaniem | Wbudowana                            | Zwięzły, deklaratywny         |

## 3.3. Rest Assured

Rest Assured to biblioteka Java zaprojektowana do testowania i walidacji REST API. Oferuje DSL (Domain Specific
Language) pozwalający na pisanie czytelnych, zwięzłych testów dla interfejsów programistycznych.

### Główne cechy Rest Assured:

1. **Deklaratywna składnia BDD**:
    * Struktura given-when-then odzwierciedlająca metodologię BDD
    * Czytelne, samodokumentujące się testy
    * Łańcuchowanie metod dla kompaktowej składni
2. **Wszechstronna walidacja odpowiedzi**:
    * Weryfikacja statusów HTTP, nagłówków, treści odpowiedzi
    * Zaawansowana ekstrakcja danych z odpowiedzi JSON/XML
    * Path expressions dla złożonych weryfikacji danych
3. **Elastyczna serializacja/deserializacja**:
    * Automatyczne mapowanie obiektów Java na JSON/XML i odwrotnie
    * Wsparcie dla różnych serializatorów (Jackson, Gson, JAXB)
    * Obsługa różnych formatów danych (JSON, XML, HTML, Text)
4. **Zaawansowana konfiguracja**:
    * Konfigurowalne proxy, timeouty, autentykacja
    * Reużywalne specyfikacje dla powtarzalnych elementów
    * Wsparcie dla SSL/TLS, cookies, sesji
5. **Wykorzystanie w projekcie**:
    * Podstawowy framework do testowania API
    * Weryfikacja kontraktów między front-endem a back-endem
    * Przygotowanie i czyszczenie danych testowych
    * Testy integracyjne komponentów back-endowych

### Przykładowa implementacja testu z wykorzystaniem Rest Assured:


```java
@Test
public void canRetrieveUserById() {
    // Przygotowanie i wykonanie żądania
    RestAssured.given()
        .header("Authorization", "Bearer " + getAuthToken())
        .contentType(ContentType.JSON)
        .pathParam("id", "12345")
        .log().ifValidationFails()
    .when()
        .get("/api/users/{id}")
    .then()
        .statusCode(200)
        .contentType(ContentType.JSON)
        .body("id", equalTo("12345"))
        .body("name", equalTo("Jan Kowalski"))
        .body("email", matchesPattern("[a-z]+@[a-z]+\\.[a-z]+"))
        .body("roles", hasSize(2))
        .body("roles", hasItems("USER", "ADMIN"))
        .time(lessThan(1000L)); // Czas odpowiedzi poniżej 1 sekundy
}

```

### Zaawansowane scenariusze z Rest Assured:

1. **Testowanie sekwencji API**:


```java
// Krok 1: Utworzenie użytkownika
String userId = given()
    .contentType(ContentType.JSON)
    .body(new UserDTO("Jan", "Kowalski", "john@example.com"))
.when()
    .post("/api/users")
.then()
    .statusCode(201)
    .extract().path("id");

// Krok 2: Pobranie utworzonego użytkownika
given()
    .pathParam("id", userId)
.when()
    .get("/api/users/{id}")
.then()
    .statusCode(200)
    .body("email", equalTo("john@example.com"));

// Krok 3: Usunięcie użytkownika
given()
    .pathParam("id", userId)
.when()
    .delete("/api/users/{id}")
.then()
    .statusCode(204);

```

2. **Walidacja schematu JSON**:


```java
given()
    .get("/api/products")
.then()
    .assertThat()
    .body(matchesJsonSchemaInClasspath("schemas/products-schema.json"));

```

## 3.4. Biblioteki wspierające

Poza głównymi frameworkami, w testach automatycznych wykorzystujemy szereg bibliotek wspierających, które rozszerzają
możliwości testowe i ułatwiają implementację rozwiązań.

### JUnit 5 / TestNG

**Rola**:

Podstawowe frameworki do uruchamiania testów

**Funkcjonalności**:

* Definiowanie i organizacja testów
* Parametryzacja testów
* Mechanizmy asercji
* Hooks do zarządzania cyklem życia testów (setup, teardown)
* Równoległe wykonanie testów
* Grupowanie i filtrowanie testów do uruchomienia

### AssertJ

**Rola**:

Biblioteka do asercji w stylu fluent API

**Funkcjonalności**:

* Czytelne, opisowe asercje dla różnych typów danych
* Łańcuchowanie asercji
* Szczegółowe komunikaty błędów
* Rozszerzalne asercje dla własnych typów
* Wykorzystanie Wyrażeń Lambda, Stream i Optional

### Jackson / Gson

**Rola**:

Biblioteki do serializacji/deserializacji JSON

**Funkcjonalności**:

* Konwersja między obiektami Java a JSON
* Obsługa złożonych struktur danych
* Konfigurowalny proces serializacji/deserializacji
* Wsparcie dla adnotacji do kontrolowania procesu mapowania

### Awaitility

**Rola**:

Biblioteka do asynchronicznego oczekiwania na dany efekt w systemie

**Funkcjonalności**:

* Deklaratywne oczekiwanie na spełnienie warunków
* Obsługa operacji asynchronicznych
* Definiowalne timeout'y i interwały
* Integracja z wyrażeniami lambda

### Lombok

**Rola**:

Redukcja boilerplate kodu Java

**Funkcjonalności**:

* Automatyczne generowanie getterów/setterów
* Uproszczone definiowanie klas DTO
* Wzorce Builder, toString, equals/hashCode
* Usprawnienie zarządzania zasobami (try-with-resources)

### Allure Report

**Rola**:

Generowanie raportów z testów

**Funkcjonalności**:

* Atrakcyjne wizualnie raporty HTML
* Szczegółowe statystyki wykonania testów
* Załączniki (zrzuty ekranu, logi, dane wejściowe/wyjściowe)
* Kategoryzacja błędów i trendów
* Integracja z CI/CD i narzędziami zarządzania testami

### Faker

**Rola**:

Generowanie realistycznych danych testowych

**Funkcjonalności**:

Różnorodne typy danych (imiona, adresy, numery telefonów, itp.)

* Wielojęzyczne wsparcie
* Spójne generowanie danych
* Konfigurowalne generatory

### Log4j / SLF4J

**Rola**:

Zarządzanie logowaniem

**Funkcjonalności**:

* Elastyczna konfiguracja logowania
* Różne poziomy logów
* Rotacja plików logów
* Formatowanie komunikatów
* Integracja z narzędziami monitoringu

### JsonPath / XmlPath

**Rola**:

Zaawansowane przetwarzanie odpowiedzi JSON/XML

**Funkcjonalności**:

* Ekstrakcja danych za pomocą wyrażeń ścieżkowych
* Przetwarzanie złożonych hierarchii
* Filtrowanie i transformacja danych
* Integracja z Rest Assured do weryfikacji odpowiedzi

### Integracja bibliotek w frameworku testowym:


```java
@Slf4j // Lombok dla logowania
public class UserApiTest {
    private static final Faker faker = new Faker(); // Generator danych
    
    @Test
    public void shouldCreateAndRetrieveUser() {
        // Przygotowanie danych testowych z Faker
        String email = faker.internet().emailAddress();
        UserDTO newUser = new UserDTO(
            faker.name().firstName(),
            faker.name().lastName(),
            email
        );
        
        // Wykonanie testu z Rest Assured
        String userId = RestAssured.given()
            .contentType(ContentType.JSON)
            .body(newUser) // Jackson/Gson serializacja
            .log().ifValidationFails()
        .when()
            .post("/api/users")
        .then()
            .statusCode(201)
            .extract().path("id");
        
        // Asynchroniczna weryfikacja z Awaitility
        Awaitility.await()
            .atMost(5, TimeUnit.SECONDS)
            .pollInterval(1, TimeUnit.SECONDS)
            .until(() -> isUserAvailableInSystem(userId));
        
        // Asercje z AssertJ
        UserDTO retrievedUser = getUserById(userId);
        assertThat(retrievedUser)
            .isNotNull()
            .extracting(UserDTO::getEmail)
            .isEqualTo(email);
        
        // Logowanie z SLF4J
        log.info("Successfully verified user creation: {}", userId);
    }
    
    // Metody pomocnicze...
}

```

Ta kombinacja narzędzi i bibliotek zapewnia kompleksowe rozwiązanie do testowania aplikacji webowych na wszystkich
poziomach, od API po interfejs użytkownika, z zachowaniem czytelności, utrzymywalności i efektywności testów.

# 4. Proces tworzenia testów automatycznych

## 4.1. Identyfikacja przypadków testowych do automatyzacji

Identyfikacja odpowiednich przypadków testowych do automatyzacji jest kluczowym etapem, który determinuje skuteczność
całego procesu testów automatycznych. Wymaga ona strategicznego podejścia, aby zmaksymalizować zwrot z inwestycji (ROI)
i skoncentrować wysiłki na obszarach o największej wartości.

### Kryteria wyboru przypadków do automatyzacji:

1. **Wartość biznesowa**:
    * Krytyczne funkcjonalności, których awaria ma znaczący wpływ na biznes
    * Główne ścieżki biznesowe wykorzystywane przez większość użytkowników
    * Procesy generujące przychód (np. ścieżka zakupowa, płatności)
    * Funkcjonalności wymagane przez regulacje prawne lub zgodność
2. **Częstotliwość wykonania**:
    *
        * Testy wykonywane regularnie w cyklach regresyjnych
    * Scenariusze walidowane przy każdym wdrożeniu
    * Funkcje wymagające częstego retestingu po zmianach w kodzie
3. **Podatność na błędy**:
    * Obszary z historią częstych defektów
    * Funkcjonalności złożone lub o wysokim ryzyku technicznym
    * Komponenty z wieloma zależnościami
    * Moduły podlegające częstym zmianom
4. **Techniczna wykonalność**:
    * Stabilność interfejsu użytkownika lub API
    * Determinizm wyników (te same dane wejściowe zawsze dają te same wyniki)
    * Możliwość izolacji komponentu do testów
      *Dostępność elementów UI do automatyzacji (identyfikatory, selektory)
5. **Nakład pracy vs. korzyści**:
    * Czas potrzebny na implementację testu automatycznego
    * Częstotliwość ręcznego wykonania testu
    * Złożoność utrzymania testu w czasie
    * Oczekiwana długość życia testowanej funkcjonalności

### Metodologia identyfikacji przypadków testowych:

1. **Analiza ryzyka**:
    * Ocena wpływu potencjalnej awarii (skala 1-5)
    * Ocena prawdopodobieństwa wystąpienia błędu (skala 1-5)
    * Obliczenie indeksu ryzyka (wpływ × prawdopodobieństwo)
    * Priorytetyzacja funkcjonalności o najwyższym indeksie ryzyka
2. **Analiza wymagań**:
    * Przeglądanie dokumentacji biznesowej i technicznej
    * Identyfikacja scenariuszy z User Stories
    * Analiza przypadków użycia
    * Wyodrębnienie testów funkcjonalnych bazujących na specyfikacji
3. **Analiza kodu i pokrycia**:
    * Przegląd struktury aplikacji
    * Identyfikacja obszarów o niskim pokryciu testami
    * Analiza złożoności cyklomatycznej kodu
    * Identyfikacja wspólnych komponentów używanych w wielu miejscach
4. **Analiza historyczna**:
    * Przegląd wcześniejszych incydentów i defektów
    * Identyfikacja częstych obszarów problemowych
    * Analiza raportów z testów manualnych
    * Przegląd logów i metryk produkcyjnych

### Proces decyzyjny i dokumentacja:

1. **Matryca decyzyjna automatyzacji**:

| Kryterium               | Waga | Ocena (1-5) | Wynik ważony |
|-------------------------|------|-------------|--------------|
| Wartość biznesowa       | 3    | ?           | ?            |    
| Częstotliwość wykonania | 2    | ?           | ?            |     
| Podatność na błędy      | 2    | ?           | ?            |     
| Techniczna wykonalność  | 1    | ?           | ?            |     
| Łatwość utrzymania      | 1    | ?           | ?            |     
| **Suma**                |      |             | **?**        |

_Przypadki testowe z sumą powyżej określonego progu są kwalifikowane do automatyzacji._

2. **Dokumentacja wybranych przypadków**:
    * Unikalne ID przypadku testowego
    * Opis funkcjonalności do testowania
    * Kryteria akceptacji
    * Priorytet automatyzacji
    * Szacowany nakład pracy
    * Powiązane wymagania biznesowe
    * Typ testu (UI/API)

3. **Przegląd i zatwierdzenie**:
    * Zespołowy przegląd wybranych przypadków
    * Weryfikacja przez interesariuszy biznesowych
    * Walidacja technicznej wykonalności
    * Finalne zatwierdzenie listy do automatyzacji

### Przykładowa lista kryteriów oceny dla testów UI vs. API:

| Funkcjonalność                       | Lepiej testować przez UI      | Lepiej testować przez API          |
|--------------------------------------|-------------------------------|------------------------------------|
| Logowanie i bezpieczeństwo           | ✓ (pełna ścieżka użytkownika) | ✓ (weryfikacja tokenów, uprawnień) |
| Walidacja formularzy                 | ✓ (interakcje wizualne)       | ✗                                  |
| Przepływy biznesowe (np. zamówienia) | ✓ (end-to-end)                | ✓ (pojedyncze kroki)               |
| CRUD                                 | ✗                             | ✓ (wydajność, spójność)            | 
| Wygląd i układy                      | ✓                             | ✗                                  | 
| Integracja z systemami zewnętrznymi  | ✗                             | ✓ (szybkość, niezawodność)         |
| Weryfikacja integracji z API         | ✗                             | ✓ (skuteczność, szybkość)          |
| Weryfikacja integracji z UI          | ✓                             | ✗                                  |


## 4.2. Projektowanie testów UI

Projektowanie testów UI jest procesem twórczym, wymagającym zrozumienia zarówno aspektów biznesowych, jak i technicznych
aplikacji. Dobrze zaprojektowane testy UI są czytelne, utrzymywalne i skutecznie wykrywają defekty.

### Podejście do projektowania testów UI:

1. **Definiowanie zakresu testu**:
   * Określenie dokładnego celu testu (co konkretnie ma być zweryfikowane)
   * Identyfikacja warunków wstępnych (np. stan aplikacji, dane testowe)
   * Zdefiniowanie oczekiwanych rezultatów
   * Ustalenie granic testu (co należy, a czego nie należy testować)

2. **Dekompozycja scenariusza na kroki**:
   * Podział testu na logiczne, atomowe kroki
   * Identyfikacja punktów kontrolnych i weryfikacyjnych
   * Określenie kolejności działań użytkownika
   * Identyfikacja potencjalnych punktów synchronizacji (oczekiwania)

3. **Identyfikacja elementów UI**:
   * Analiza struktury DOM aplikacji
   * Wybór optymalnych lokalizatorów (preferowane ID, następnie CSS selektory)
   * Dokumentacja lokalizatorów dla wielokrotnego użycia
   * Identyfikacja dynamicznych elementów wymagających specjalnego podejścia

4. **Planowanie walidacji i asercji**:
   * Określenie co dokładnie powinno być weryfikowane
   * Wybór typów asercji (widoczność, tekst, atrybuty, stan)
   * Dokumentacja oczekiwanych wyników
   * Planowanie alternatywnych ścieżek (przypadki błędów)

5. **Identyfikacja potencjalnych wyzwań**:
   * Potencjalne problemy z synchronizacją (AJAX, animacje)
   * Dynamicznie generowane elementy
   * Elementy zależne od stanu (np. widoczne tylko przy określonych warunkach)
   * Cross-browser kompatybilność

### Przykładowy proces projektowania testu UI:

Scenariusz biznesowy: "Użytkownik powinien móc zalogować się do aplikacji, dodać produkt do koszyka i przejść do
płatności"

1. **Dekompozycja scenariusza**:


```
1. Logowanie do aplikacji
   a. Otwarcie strony logowania
   b. Wprowadzenie poprawnych danych
   c. Weryfikacja pomyślnego logowania
2. Wyszukiwanie i dodawanie produktu
   a. Wyszukanie produktu po nazwie
   b. Weryfikacja wyników wyszukiwania
   c. Wybór produktu i dodanie do koszyka
   d. Weryfikacja powiadomienia o dodaniu do koszyka
3. Przejście do procesu płatności
   a. Otwarcie koszyka
   b. Weryfikacja dodanego produktu
   c. Przejście do płątności
   d. Weryfikacja strony checkout

```

3. **Identyfikacja elementów UI i lokalizatorów**:

```
Strona logowania:
- Pole username: #username
- Pole password: #password
- Przycisk login: #login-button
- Komunikat powodzenia: .success-message
1.
Strona główna:
- Pole wyszukiwania: #search-input
- Przycisk wyszukiwania: button[type="submit"]
- Lista wyników: .search-results .product-item
- Przycisk "Dodaj do koszyka": .add-to-cart-button
- Powiadomienie o dodaniu: #cart-notification
1.
Koszyk i checkout:
- Link do koszyka: #cart-link
- Pozycje w koszyku: .cart-items .item
- Przycisk checkout: #checkout-button
- Nagłówek strony checkout: .checkout-page h1

```

4. **Procedury walidacji**:

```
Walidacja logowania:
- Dashboard jest widoczny
- Nazwa użytkownika jest wyświetlona w nagłówku
1.
Walidacja wyszukiwania:
- Lista produktów zawiera przynajmniej jeden element
- Nazwa pierwszego produktu zawiera szukaną frazę
1.
Walidacja dodania do koszyka:
- Powiadomienie jest wyświetlone
- Licznik produktów w koszyku zwiększył się
1.
Walidacja checkout:
- Strona checkout jest załadowana
- Produkt jest widoczny na liście zamówienia
- Cena jest zgodna z oczekiwaną

```

4. **Identyfikacja potencjalnych wyzwań**:

```
- Dynamiczne generowanie ID produktów - konieczne użycie relatywnych lokalizatorów
- Asynchroniczne ładowanie wyników wyszukiwania - potrzebne mechanizmy oczekiwania
- Animacja powiadomienia o dodaniu do koszyka - synchronizacja czasowa
- Sesja użytkownika - może wymagać ponownego logowania przy dłuższych testach

```

### Projektowanie modelu Page Object:

Przy projektowaniu testów UI kluczowe jest zastosowanie wzorca Page Object Model (POM), który oddziela logikę testową od
reprezentacji interfejsu użytkownika.

1. **Identyfikacja stron i komponentów**:
   * Wyodrębnienie głównych stron aplikacji (np. LoginPage, ProductPage,
         CartPage)
   * Identyfikacja współdzielonych komponentów (np. Header, Footer, SearchBox)
   * Abstrakcja skomplikowanych elementów i ich zachowań (UsersTable, AccountTransfersTable)
   * Określenie relacji między stronami (nawigacja)
   * Decyzja zwracania innych page objectów przez page object lub zwracanie przez metody publiczne this/void

2. **Definiowanie metod w Page Objects**:
   * Metody reprezentujące akcje użytkownika (loginAs(User user), searchForProduct(ProductType productType)) - jako abstrakce zachowań
   * Metody weryfikujące stan strony (isLoggedIn()) - jako abstrakcje weryfikacji
   * Metody pobierające stan elementów, które ___muszą___ być wykorzystane w testach (w dalszej części procesu)  (getCartItemCount())


3. **Przykładowa struktura klas Page Object**:


```java
// Bazowa klasa dla wszystkich stron
public abstract class BasePage {
    protected SelenideElement pageContainer;
    
    public void isAt() {
        pageContainer.shoulddBe(displayed);
    }
    
    // Wspólne metody nawigacyjne
    public HomePage navigateToHome() {
        $("#home-link").click();
        return new HomePage();
    }
    
    // Inne wspólne metody...
}

// Konkretna implementacja strony
public class LoginPage extends BasePage {
    private SelenideElement usernameField = $("#username");
    private SelenideElement passwordField = $("#password");
    private SelenideElement loginButton = $("#login-button");
    
    public LoginPage() {
        pageContainer = $(".login-container");
    }
    
    public HomePage loginAs(String username, String password) {
        usernameField.setValue(username);
        passwordField.setValue(password);
        loginButton.click();
        return new HomePage();
    }
    
    public LoginPage loginExpectingError(String username, String password) {
        usernameField.setValue(username);
        passwordField.setValue(password);
        loginButton.click();
        return this;
    }
    
    public boolean isErrorMessageDisplayed() {
        return $(".error-message").isDisplayed();
    }
}

```

## 4.3. Projektowanie testów API

Projektowanie testów API koncentruje się na weryfikacji poprawności działania interfejsów programistycznych aplikacji,
które stanowią fundament komunikacji między komponentami systemu. Dobrze zaprojektowane testy API zapewniają szybką i
niezawodną weryfikację logiki biznesowej.

### Podejście do projektowania testów API:

1. **Analiza dokumentacji API**:
   * Przegląd specyfikacji API (Swagger/OpenAPI, RAML, dokumentacja tekstowa)
   * Zrozumienie dostępnych endpointów, parametrów i odpowiedzi
   * Identyfikacja kodów statusów i ich znaczenia
   * Analiza schematów danych JSON/XML

2. **Identyfikacja scenariuszy testowych**:
   * Testy pozytywne (happy path) dla głównych operacji CRUD
   * Testy negatywne weryfikujące obsługę błędów i walidację
   * Testy graniczne sprawdzające limity parametrów
   * Testy wydajnościowe dla kluczowych endpointów i procesów

3. **Dekompozycja na przypadki testowe**:
   * Grupowanie testów według zasobów/endpointów
   * Identyfikacja testów powiązanych (np. sekwencje create-read-update-delete)
   * Określenie zależności między testami
   * Ustalenie priorytetów testów

4. **Planowanie walidacji i asercji**:
   * Weryfikacja statusu odpowiedzi HTTP
   * Walidacja struktury i schematu odpowiedzi
   * Sprawdzenie konkretnych wartości w odpowiedzi
   * Weryfikacja nagłówków (Content-Type, authorization)
   * Pomiar czasu odpowiedzi (SLA)

5. **Zarządzanie danymi testowymi**:
   * Identyfikacja danych wejściowych wymaganych dla testów
   * Strategia tworzenia/usuwania danych testowych
   * Podejście do izolacji danych między testami
   * Obsługa zależności danych

### Przykładowy proces projektowania testu API:

Scenariusz biznesowy: "Weryfikacja pełnego cyklu życia użytkownika (tworzenie, odczyt, aktualizacja, usuwanie)"

1. **Dekompozycja scenariusza**:

```
1. Tworzenie użytkownika (POST /api/users)
   a. Pozytywne: utworzenie z poprawnymi danymi
   b. Negatywne: próba utworzenia z brakującymi polami
   c. Negatywne: próba utworzenia z niepoprawnym formatem danych

2. Odczyt użytkownika (GET /api/users/{id})
   a. Pozytywne: pobranie istniejącego użytkownika
   b. Negatywne: próba pobrania nieistniejącego użytkownika
   c. Weryfikacja wszystkich zwracanych pól

3. Aktualizacja użytkownika (PUT /api/users/{id})
   a. Pozytywne: pełna aktualizacja danych
   b. Pozytywne: częściowa aktualizacja danych (PATCH)
   c. Negatywne: próba aktualizacji nieistniejącego użytkownika

4. Usuwanie użytkownika (DELETE /api/users/{id})
   a. Pozytywne: usunięcie istniejącego użytkownika
   b. Negatywne: próba usunięcia nieistniejącego użytkownika
   c. Weryfikacja, że usunięty użytkownik jest niedostępny

```

2. **Identyfikacja danych testowych**:

```
Dane użytkownika:
- Poprawny użytkownik: {
    "firstName": "Jan",
    "lastName": "Kowalski",
    "email": "john.kowalski@example.com",
    "roles": ["USER"]
}

- Niepełne dane: {
    "firstName": "Jan",
    "email": "john.incomplete@example.com"
}

- Niepoprawny format: {
    "firstName": "Jan",
    "lastName": "Kowalski",
    "email": "invalid-email"
}

- Dane do aktualizacji: {
    "firstName": "Jan",
    "lastName": "Updated",
    "email": "jan.updated@example.com"
}

```

3**Procedury walidacji**:

```
1. Walidacja tworzenia:
- Status 201 Created
- Odpowiedź zawiera ID utworzonego użytkownika
- Lokalizacja (header Location) wskazuje na nowy zasób

2, Walidacja odczytu:
- Status 200 OK
- Wszystkie pola zgodne z oczekiwanymi
- Content-Type: application/json

3. Walidacja aktualizacji:
- Status 200 OK
- Pola zaktualizowane zgodnie z żądaniem

4. Walidacja usunięcia:
- Status 204 No Content
- Próba odczytu usuniętego użytkownika zwraca 404

```
4. **Potencjalne wyzwania**:


```
- Zależności danych źródłowych
- Zarządzanie identyfikatorami między testami
- Kolejność wykonania testów (zależności pomiędzy procesami)
- Idempotentność testów (możliwość wielokrotnego uruchomienia)
- Zarządzanie danymi testowymi (czyszczenie)

```

### Projektowanie abstrakcji dla testów API:

Przy projektowaniu testów API kluczowe jest stworzenie odpowiednich abstrakcji, które uczynią testy czytelnymi i
utrzymywalnymi.

1. **Modele danych (DTOs)**:
   * Klasy reprezentujące struktury danych używane w API
   * Adnotacje dla serializacji/deserializacji
   * Pola zgodne ze schematem API
   * Metody pomocnicze (np. factory methods, builders)

2. **Klasy klienckie API**:
   * Metody odpowiadające operacjom API
   * Enkapsulacja szczegółów technicznych (nagłówki, serializacja)
   * Obsługa autentykacji
   * Obsługa rutynowych walidacji

4. **Przykładowa implementacja abstrakcji**:


```java
// Model danych
@Data
@Builder
public class UserDTO {
    private String id;
    private String firstName;
    private String lastName;
    private String email;
    private List<String> roles;
    
    // Factory method dla typowych przypadków
    public static UserDTO createDefault() {
        return UserDTO.builder()
            .firstName("jan")
            .lastName("Kowalski")
            .email("jan.kowalski@example.com")
            .roles(List.of("USER"))
            .build();
    }
}

// Klient API
public class UserApiClient {
    private static final String BASE_PATH = "/api/users";
    
    public UserDTO createUser(UserDTO user) {
        return RestAssured
            .given()
                .contentType(ContentType.JSON)
                .body(user)
            .when()
                .post(BASE_PATH)
            .then()
                .statusCode(201)
                .extract().as(UserDTO.class);
    }
    
    public UserDTO getUserById(String id) {
        return RestAssured
            .given()
                .pathParam("id", id)
            .when()
                .get(BASE_PATH + "/{id}")
            .then()
                .statusCode(200)
                .extract().as(UserDTO.class);
    }
    
    public UserDTO updateUser(String id, UserDTO user) {
        return RestAssured
            .given()
                .pathParam("id", id)
                .contentType(ContentType.JSON)
                .body(user)
            .when()
                .put(BASE_PATH + "/{id}")
            .then()
                .statusCode(200)
                .extract().as(UserDTO.class);
    }
    
    public void deleteUser(String id) {
        RestAssured
            .given()
                .pathParam("id", id)
            .when()
                .delete(BASE_PATH + "/{id}")
            .then()
                .statusCode(204);
    }
}

```

## 4.4. Implementacja testów

Implementacja testów to proces przekształcania zaprojektowanych przypadków testowych w faktyczny kod testowy. Ten etap
wymaga zastosowania dobrych praktyk programistycznych, aby zapewnić, że testy będą skuteczne, niezawodne i łatwe w
utrzymaniu.

### Zasady implementacji testów:

1. **Struktura i organizacja kodu**:
   *Logiczny podział kodu testowego na pakiety/moduły
   * Konsekwentne nazewnictwo klas i metod testowych
   * Grupowanie powiązanych testów
   * Hierarchia dziedziczenia dla wspólnej konfiguracji
2. **Standardy kodowania**:
   * Zgodność z konwencjami języka i frameworka
   * Konsekwentne formatowanie kodu
   * Czytelny i samodokumentujący się kod
   * Odpowiednie komentarze dla złożonych scenariuszy
3. **Zasada AAA (Arrange-Act-Assert)**:
   * **Arrange**: przygotowanie stanu początkowego i danych testowych
   * **Act**: wykonanie testowanej operacji
   * **Assert**: weryfikacja wyników i stanu
4. **Separacja odpowiedzialności**:
   * Oddzielenie logiki testowej od konfiguracji
   * Oddzielenie danych testowych od kodu testowego
   * Wykorzystanie wcześniej zaprojektowanych abstrakcji (Page Objects, klasy klienckie API)

### Implementacja testów UI z Selenide:


```java
@DisplayName("Login functionality tests")
public class LoginTests extends BaseTest {
    
    private LoginPage loginPage;
    private HomePage homePage;
    
    @BeforeEach
    public void setUp() {
        // Arrange
        loginPage = new LoginPage();
        loginPage.open();
    }
    
    @Test
    @DisplayName("User can login with valid credentials")
    public void userCanLoginWithValidCredentials() {
        // Act
        homePage = loginPage.loginAs("validuser", "validpassword");
        
        // Assert
        homePage.getUserInfoPanel().shouldHave(text("Welcome, Valid User"));
        homePage.getNavigationMenu().shouldBe(visible);
    }
    
    @Test
    @DisplayName("System shows error message for invalid credentials")
    public void systemShowsErrorForInvalidCredentials() {
        // Act
        loginPage.loginExpectingError("invaliduser", "invalidpassword");
        
        // Assert
        loginPage.getErrorMessage()
            .shouldBe(visible)
            .shouldHave(text("Invalid username or password"));
        loginPage.getUsernameField().shouldHave(cssClass("input-error"));
    }
    
    @Test
    @DisplayName("Password field masks user input")
    public void passwordFieldMasksUserInput() {
        // Act
        loginPage.getPasswordField().setValue("testpassword");
        
        // Assert
        loginPage.getPasswordField().shouldHave(attribute("type", "password"));
    }
    
    @Test
    @DisplayName("User can reset password")
    public void userCanResetPassword() {
        // Act
        PasswordResetPage resetPage = loginPage.clickForgotPassword();
        
        // Assert
        resetPage.getPageTitle().shouldHave(text("Reset Your Password"));
        resetPage.getEmailField().shouldBe(visible);
    }
}

```

### Implementacja testów API z Rest Assured:



```java
@DisplayName("User API integration tests")
public class UserApiTests extends BaseApiTest {
    
    private UserApiClient userApiClient;
    private String testUserId;
    
    @BeforeEach
    public void setUp() {
        // Arrange
        userApiClient = new UserApiClient();
        // Przygotowanie danych testowych lub czyste środowisko
        cleanupTestUsers();
    }
    
    @AfterEach
    public void tearDown() {
        // Cleanup
        if (testUserId != null) {
            try {
                userApiClient.deleteUser(testUserId);
            } catch (Exception e) {
                // Ignoruj błędy podczas czyszczenia
                logger.warn("Error during test cleanup: " + e.getMessage());
            }
        }
    }
    
    @Test
    @DisplayName("Can create a new user")
    public void canCreateNewUser() {
        // Arrange
        UserDTO newUser = UserDTO.createDefault();
        
        // Act
        UserDTO createdUser = userApiClient.createUser(newUser);
        testUserId = createdUser.getId();
        
        // Assert
        assertThat(createdUser.getId()).isNotNull();
        assertThat(createdUser.getEmail()).isEqualTo(newUser.getEmail());
        assertThat(createdUser.getRoles()).containsExactlyElementsOf(newUser.getRoles());
    }
    
    @Test
    @DisplayName("Can retrieve user by ID")
    public void canRetrieveUserById() {
        // Arrange
        UserDTO newUser = UserDTO.createDefault();
        UserDTO createdUser = userApiClient.createUser(newUser);
        testUserId = createdUser.getId();
        
        // Act
        UserDTO retrievedUser = userApiClient.getUserById(testUserId);
        
        // Assert
        assertThat(retrievedUser).isNotNull();
        assertThat(retrievedUser.getId()).isEqualTo(testUserId);
        assertThat(retrievedUser.getFirstName()).isEqualTo(newUser.getFirstName());
    }
    
    @Test
    @DisplayName("Cannot create user with invalid email")
    public void cannotCreateUserWithInvalidEmail() {
        // Arrange
        UserDTO invalidUser = UserDTO.builder()
            .firstName("Jan")
            .lastName("Kowalski")
            .email("invalid-email")
            .roles(List.of("USER"))
            .build();
        
        // Act & Assert
        ValidationErrorResponse errorResponse = RestAssured
            .given()
                .contentType(ContentType.JSON)
                .body(invalidUser)
            .when()
                .post("/api/users")
            .then()
                .statusCode(400)
                .extract().as(ValidationErrorResponse.class);
        
        assertThat(errorResponse.getErrors())
            .anyMatch(error -> error.getField().equals("email") && 
                     error.getMessage().contains("valid email"));
    }
    
    @Test
    @DisplayName("Can update existing user")
    public void canUpdateExistingUser() {
        // Arrange
        UserDTO newUser = UserDTO.createDefault();
        UserDTO createdUser = userApiClient.createUser(newUser);
        testUserId = createdUser.getId();
        
        UserDTO updatedData = UserDTO.builder()
            .firstName("Updated")
            .lastName("User")
            .email("updated.user@example.com")
            .roles(List.of("USER", "ADMIN"))
            .build();
        
        // Act
        UserDTO updatedUser = userApiClient.updateUser(testUserId, updatedData);
        
        // Assert
        assertThat(updatedUser.getFirstName()).isEqualTo("Updated");
        assertThat(updatedUser.getLastName()).isEqualTo("User");
        assertThat(updatedUser.getEmail()).isEqualTo("updated.user@example.com");
        assertThat(updatedUser.getRoles()).contains("ADMIN");
    }
}

```

### Zaawansowane techniki implementacji:

1. **Parametryzacja testów**:

```java
@ParameterizedTest
@CsvSource({
    "Chrome, 1920x1080",
    "Firefox, 1366x768",
    "Edge, 1600x900"
})
public void loginShouldWorkOnDifferentBrowsers(String browser, String resolution) {
    // Konfiguracja specyficzna dla przeglądarki
    configureTest(browser, resolution);

    // Test logowania
    loginPage.open();
    homePage = loginPage.loginAs("validuser", "validpassword");

    // Asercje
    homePage.getUserInfoPanel().shouldBe(visible);
}

```

2. **Obsługa danych zależnych od środowiska**:


```java
@Test
public void canCreateUserInDifferentEnvironments() {
    // Odczyt konfiguracji środowiska
    String environment = getEnvironmentConfig();
    UserDTO userData = TestDataFactory.createUserForEnvironment(environment);

    // Wykonanie testu
    UserDTO createdUser = userApiClient.createUser(userData);

    // Asercje specyficzne dla środowiska
    if ("prod".equals(environment)) {
        // Dodatkowe weryfikacje dla produkcji
        assertThat(createdUser.getVerificationStatus()).isEqualTo("PENDING");
    } else {
        // Weryfikacje dla środowisk testowych
        assertThat(createdUser.getVerificationStatus()).isEqualTo("AUTO_VERIFIED");
    }
}

```

3. **Obsługa asynchroniczności**:


```java
@Test
public void orderShouldBeProcessedAsynchronously() {
    // Utworzenie zamówienia
    OrderDTO order = orderApiClient.createOrder(TestDataFactory.createOrder());

    // Oczekiwanie na przetworzenie asynchroniczne
    Awaitility.await()
        .atMost(30, TimeUnit.SECONDS)
        .pollInterval(2, TimeUnit.SECONDS)
        .until(() -> {
            OrderDTO currentStatus = orderApiClient.getOrderById(order.getId());
            return "PROCESSED".equals(currentStatus.getStatus());
        });

    // Weryfikacja finalnego stanu
    OrderDTO processedOrder = orderApiClient.getOrderById(order.getId());
    assertThat(processedOrder.getStatus()).isEqualTo("PROCESSED");
    assertThat(processedOrder.getProcessingTime()).isGreaterThan(0);
}

```

4. **Obsługa testów wymagających specjalnych uprawnień**:


```java
@Test
@WithMockUser(roles = {"ADMIN"})
public void adminCanAccessRestrictedContent() {
    // Wykonanie akcji wymagającej uprawnień administratora
    AdminDashboardPage adminPage = new AdminDashboardPage();
    adminPage.open();

    // Weryfikacja dostępu
    adminPage.getUserManagementPanel().shouldBe(visible);
    adminPage.getSystemConfigurationPanel().shouldBe(visible);
}

```

## 4.5. Weryfikacja i utrzymanie testów

Weryfikacja i utrzymanie testów to ciągły proces zapewniający, że zautomatyzowane testy pozostają efektywne, niezawodne
i aktualne w miarę ewolucji testowanej aplikacji. Jest to krytyczny aspekt automatyzacji testów, często pochłaniający
znaczącą część całkowitego nakładu pracy.

### Weryfikacja testów automatycznych:

1. **Podstawowe kryteria weryfikacji**:
   * **Dokładność**: Test powinien prawidłowo weryfikować implementowaną funkcjonalność
   * **Niezawodność**: Test powinien dawać spójne wyniki przy tych samych warunkach
   * **Wydajność**: Test powinien wykonywać się w rozsądnym czasie
   * **Czytelność**: Kod testu powinien być zrozumiały dla innych członków zespołu
   * **Utrzymywalność**: Test powinien być łatwy do aktualizacji po zmianach w aplikacji

2. **Proces weryfikacji testów**:
   * **Code review**: Przegląd kodu testowego przez innych członków zespołu
   * **Test testów**: Weryfikacja, że test wykrywa błędy, gdy są wprowadzane (np. negative testing)
   * **Kontrolowane uruchomienia**: Sprawdzanie zachowania testów w różnych środowiskach
   * **Analiza stabilności**: Wielokrotne uruchamianie testów w celu wykrycia flakiness
   * **Peer validation**: Weryfikacja przez drugiego testera, czy test pokrywa wszystkie wymagania
 
3. **Weryfikacja testów UI**:
   * Sprawdzenie, czy testy Selenium/Selenide poprawnie odzwierciedlają interakcje użytkownika
   * Weryfikacja mechanizmów synchronizacji i oczekiwania
   * Kontrola nad stanem przeglądarki i sesji użytkownika
   * Walidacja asercji i punktów weryfikacji

4. **Weryfikacja testów API**:
   * Sprawdzenie pokrycia wszystkich ważnych ścieżek i parametrów
   * Weryfikacja poprawności schematów walidacji
   * Kontrola nad przygotowaniem i czyszczeniem danych testowych
   * Walidacja obsługi błędów i przypadków granicznych

### Utrzymanie testów automatycznych:

1. **Monitorowanie zdrowia testów**:
   * Śledzenie wskaźnika przechodzenia testów (pass rate)
   * Identyfikacja niestabilnych testów (flaky tests)
   * Monitorowanie czasu wykonania
   * Analiza trendów porażek testów
 
2. **Proces refaktoryzacji testów**:
   * Regularne przeglądy i udoskonalanie kodu testowego
   * Eliminacja duplikacji w testach
   * Aktualizacja lokalizatorów elementów UI
   * Optymalizacja wydajności testów
   * Aplikowanie najnowszych wzorców i dobrych praktyk
   
3. **Aktualizacja testów po zmianach w aplikacji**:
   * Systematyczny przegląd i aktualizacja testów po każdej znaczącej zmianie
   * Utrzymanie synchronizacji między specyfikacją, dokumentacją a testami
   * Weryfikacja aktualności danych testowych
   * Dostosowanie testów do nowych funkcji i przepływów

4. **Zarządzanie problemami z testami**:
   * Procesy zgłaszania i śledzenia problemów z testami
   * Priorytetyzacja napraw testów
   * Analiza głównych przyczyn niestabilności
   * Dokumentacja znanych problemów i obejść

### Strategie obsługi niestabilnych testów (flaky tests):

1. **Identyfikacja i klasyfikacja**:
   * Systematyczne gromadzenie danych o niestabilnych testach
   * Analiza wzorców niestabilności (sporadyczna, cykliczna, środowiskowa)
   * Klasyfikacja według przyczyn niestabilności
   * Ocena wpływu na ogólną wiarygodność zestawu testów

2. **Techniki stabilizacji testów UI**:

* Implementacja inteligentnych mechanizmów oczekiwania

```java
// Zamiast:
Thread.sleep(2000);

// użyj::
$("#loadingIndicator").shouldBe(disappear, Duration.ofSeconds(10));
$("#content").shouldBe(visible);

```

* Stosowanie bardziej niezawodnych lokalizatorów


```java
// Zamiast:
$("div.user-list div:nth-child(3)");

// Lepsze rozwiązanie:
$("div.user-list").find(byText("John Kowalski"));

```

* Implementacja mechanizmów retry


```java
@Test
@Retries(3) // Ponów test do 3 razy w przypadku awarii
public void flakySynchronizationTest() {
    // Test code
}

```

* Izolacja stanu testowego


```java
@BeforeEach
public void ensureCleanState() {
    // Czyszczenie stanu, resetowanie danych, itp.
    clearBrowserState();
    loginWithFreshUser();
}

```

3. **Techniki stabilizacji testów API**:

* Implementacja mechanizmów idempotentności


```java
@BeforeEach
public void ensureTestEntityExists() {
    // Sprawdź, czy encja już istnieje, w przeciwnym razie utwórz
    if (!entityExists(TEST_ENTITY_ID)) {
        createEntity(TEST_ENTITY_ID);
    }
}

```
  
* Obsługa Race Condition

```java
// Zamiast oczekiwać natychmiastowych wyników
OrderDTO order = orderApiClient.createOrder(newOrder);
assertThat(order.getStatus()).isEqualTo("PROCESSED"); // Może zawieść!

// Lepsze rozwiązanie z oczekiwaniem
OrderDTO createdOrder = orderApiClient.createOrder(newOrder);
await().atMost(10, SECONDS).until(() -> {
    OrderDTO current = orderApiClient.getOrderById(createdOrder.getId());
    return "PROCESSED".equals(current.getStatus());
});

```

* Izolacja od zależności zewnętrznych

```java
// Użycie mocków dla niepewnych zewnętrznych zależności
@Test
public void testWithMockedExternalDependency() {
    // Skonfiguruj mock zewnętrznego API
    wireMockServer.stubFor(post(urlEqualTo("/external/api"))
        .willReturn(aResponse()
            .withStatus(200)
            .withBody("{\"result\": \"success\"}")));

    // Test używający zamockowanego API
    assertThat(ourService.processWithExternalDependency()).isSuccessful();
}

```

4. **Zarządzanie nienaprawialnymi testami**:

* Kwarantanna dla niestabilnych testów

```java
@Tag("flaky") // Oznaczenie testu jako niestabilnego
@Test
public void knownFlakyTest() {
    // Test code
}
// W konfiguracji uruchomienia:
// mvn test -Dgroups=!flaky // Wykluczenie niestabilnych testów z głównego przebiegu

```

* Dokumentacja znanych problemów

```java
/**
 * This test may fail intermittently due to network latency issues with the third-party API.
 * Issue tracked in JIRA-1234.
 * Workaround: Retry the test up to 3 times with 5-second intervals.
 */
@Test
@Retries(3)
public void testWithKnownNetworkIssues() {
    // Test code
}

```

* Priorytetyzacja napraw

```
Kategorie priorytetów napraw:
P0: Krytyczne testy mające wpływ na główne funkcjonalności - naprawić natychmiast
P1: Ważne testy biznesowe - naprawić w bieżącym sprincie
P2: Testy pomocnicze - naprawić w ciągu 2 sprintów
P3: Testy niekrytyczne - rozważyć refaktoryzację lub usunięcie

```

### Dokumentacja i dzielenie się wiedzą:

1. **Dokumentacja frameworka testowego**:
   * Opis architektury i głównych komponentów
   * Przewodniki dla nowych członków zespołu
   * Standardy i konwencje kodowania
   * Rozwiązania typowych problemów
2. **Dokumentacja konkretnych testów**:
   * Mapowanie testów do wymagań biznesowych
   * Opis scenariuszy testowych i ich celów
   * Dokumentacja znanych ograniczeń i założeń
   * Instrukcje uruchamiania i interpretacji wyników
3. **Rozpowszechnianie dobrych praktyk**:
   * Wewnętrzne warsztaty i szkolenia
   * Biblioteki przykładów i wzorców
   * Regularne spotkania przeglądowe
   * Współpraca między zespołami automatyzacji

### Strategie ciągłego doskonalenia:

1. **Regularne przeglądy jakości testów**:
   * Sesje analizy metryk testowych
   * Weryfikacja skuteczności testów w wykrywaniu defektów
   * Ocena utrzymywalności i stabilności testów
   * Identyfikacja możliwości optymalizacji
2. **Wprowadzanie nowych technologii i podejść**:
   * Ewaluacja nowych narzędzi i frameworków
   * Testowanie pilotażowe nowych rozwiązań
   * Zbieranie informacji zwrotnej i analiza korzyści
   * Planowanie migracji i aktualizacji
3. **Dostosowanie strategii do ewolucji aplikacji**:
   * Dostosowanie zakresu automatyzacji do zmieniających się priorytetów
   * Rewaluacja ryzyka biznesowego i technicznego
   * Równoważenie wysiłków między tworzeniem nowych testów a utrzymaniem istniejących
   * Dostosowanie metodyki do nowych wzorców architektonicznych

Skuteczna weryfikacja i utrzymanie testów automatycznych wymaga systematycznego podejścia, odpowiednich procesów i
narzędzi, a także stałego zaangażowania zespołu. Jest to inwestycja, która zwraca się w postaci bardziej niezawodnych
testów, szybszej identyfikacji defektów i zwiększonej efektywności procesu testowania.

# 5. Architektura frameworka testowego

## 5.1. Page Object Model dla testów UI

Page Object Model (POM) to wzorzec projektowy stosowany w automatyzacji testów UI, który tworzy warstwę abstrakcji
oddzielającą logikę testową od szczegółów implementacji interfejsu użytkownika. Jest to kluczowy element architektury
frameworka testowego, zapewniający utrzymywalność, czytelność i skalowalność testów UI.

### Główne zasady Page Object Model:

1. **Enkapsulacja elementów strony**:
   * Każda strona lub komponent UI reprezentowany jest przez oddzielną klasę
   * Selektory i lokalizatory elementów są zdefiniowane tylko w jednym miejscu
   * Szczegóły techniczne implementacji UI są ukryte przed testami

2. **Rozdzielenie odpowiedzialności**:
   * Klasy Page Object reprezentują strukturę UI i dostępne akcje
   * Testy wykorzystują Page Objects do interakcji z UI
   * Logika weryfikacji jest oddzielona od manipulacji elementami

3. **Reprezentacja przepływów biznesowych**:
   *  Metody w Page Objects odzwierciedlają akcje użytkownika
   *  Nawigacja między stronami zwraca obiekty reprezentujące docelowe strony
   *  Interfejs Page Object powinien używać terminologii biznesowej (języka domeny)

### Implementacja POM z wykorzystaniem Selenide:

#### Struktura hierarchiczna Page Objects:


```
src/test/java/com/company/pageobjects/
├── base/
│   ├── BasePage.java             // Abstrakcyjna klasa bazowa dla wszystkich stron
│   ├── BaseComponent.java        // Abstrakcyjna klasa bazowa dla komponentów
│   └── PageFactory.java          // Fabryka tworząca instancje Page Objects
├── pages/
│   ├── LoginPage.java            // Konkretna strona logowania
│   ├── DashboardPage.java        // Strona głównego panelu
│   ├── ProductPage.java          // Strona produktu
│   └── CheckoutPage.java         // Strona koszyka/zamówienia
└── components/
    ├── NavigationMenu.java       // Komponent menu nawigacyjnego
    ├── SearchBar.java            // Komponent wyszukiwarki
    ├── UserInfoPanel.java        // Panel informacji o użytkowniku
    └── ProductTile.java          // Pojedynczy kafelek produktu

```

#### Przykładowa implementacja klasy bazowej:


```java
/**
 * Abstrakcyjna klasa bazowa dla wszystkich Page Objects.
 * Zawiera wspólną funkcjonalność i właściwości wszystkich stron aplikacji.
 */
public abstract class BasePage {
    
    protected SelenideElement pageRoot; // Główny element identyfikujący stronę
    
    /**
     * Weryfikuje, czy strona jest załadowana i gotowa do interakcji.
     * Każda konkretna strona implementuje własną logikę weryfikacji.
     */
    public abstract boolean isPageLoaded();
    
    /**
     * Metoda do oczekiwania na załadowanie strony.
     * @param timeout Maksymalny czas oczekiwania w sekundach
     * @return Ten sam obiekt strony (fluent interface)
     */
    public BasePage waitForPageToLoad(int timeout) {
        // Implementacja oczekiwania specyficzna dla projektu
        try {
            await().atMost(timeout, TimeUnit.SECONDS)
                   .pollInterval(200, TimeUnit.MILLISECONDS)
                   .until(this::isPageLoaded);
        } catch (Exception e) {
            fail("Page did not load within " + timeout + " seconds: " + e.getMessage());
        }
        return this;
    }
    
    /**
     * Wykonuje zrzut ekranu aktualnej strony.
     * @param fileName Nazwa pliku zrzutu ekranu
     * @return Ten sam obiekt strony (fluent interface)
     */
    public BasePage takeScreenshot(String fileName) {
        Selenide.screenshot(fileName);
        return this;
    }
    
    /**
     * Metoda do nawigacji do strony głównej, dostępna dla wszystkich stron.
     * @return Nowy obiekt reprezentujący stronę główną
     */
    public DashboardPage navigateToHome() {
        $(".home-link").click();
        return new DashboardPage().waitForPageToLoad(5);
    }
    
    // Wspólne metody nawigacyjne i pomocnicze...
}

```

#### Przykładowa implementacja konkretnej strony:


```java
/**
 * Page Object reprezentujący stronę logowania.
 * Zawiera wszystkie elementy i akcje specyficzne dla tej strony.
 */
public class LoginPage extends BasePage {
    
    // Lokalizatory elementów
    private final SelenideElement usernameField = $("#username");
    private final SelenideElement passwordField = $("#password");
    private final SelenideElement loginButton = $("#login-button");
    private final SelenideElement errorMessage = $(".error-message");
    private final SelenideElement forgotPasswordLink = $("#forgot-password");
    
    /**
     * Konstruktor inicjalizujący stronę.
     */
    public LoginPage() {
        this.pageRoot = $(".login-container");
    }
    
    /**
     * Otwiera stronę logowania.
     * @return Ten sam obiekt LoginPage (fluent interface)
     */
    public LoginPage open() {
        Selenide.open("/login");
        return this;
    }
    
    /**
     * Sprawdza, czy strona logowania jest załadowana.
     * @return true jeśli strona jest załadowana, false w przeciwnym razie
     */
    @Override
    public boolean isPageLoaded() {
        return pageRoot.isDisplayed() && 
               usernameField.isDisplayed() && 
               loginButton.isDisplayed();
    }
    
    /**
     * Wykonuje logowanie z podanymi danymi.
     * @param username Nazwa użytkownika
     * @param password Hasło
     * @return Obiekt DashboardPage jeśli logowanie się powiodło
     */
    public DashboardPage loginAs(String username, String password) {
        usernameField.setValue(username);
        passwordField.setValue(password);
        loginButton.click();
        return new DashboardPage().waitForPageToLoad(5);
    }
    
    /**
     * Wykonuje próbę logowania oczekując błędu.
     * @param username Nazwa użytkownika
     * @param password Hasło
     * @return Ten sam obiekt LoginPage (fluent interface)
     */
    public LoginPage loginExpectingError(String username, String password) {
        usernameField.setValue(username);
        passwordField.setValue(password);
        loginButton.click();
        errorMessage.shouldBe(visible, Duration.ofSeconds(2));
        return this;
    }
    
    /**
     * Przechodzi do strony resetowania hasła.
     * @return Obiekt PasswordResetPage
     */
    public PasswordResetPage clickForgotPassword() {
        forgotPasswordLink.click();
        return new PasswordResetPage().waitForPageToLoad(5);
    }
    
    // Gettery dla elementów, które mogą być używane w asercjach
    public SelenideElement getUsernameField() {
        return usernameField;
    }
    
    public SelenideElement getPasswordField() {
        return passwordField;
    }
    
    public SelenideElement getErrorMessage() {
        return errorMessage;
    }
}

```

#### Przykładowa implementacja komponentu wielokrotnego użytku:


```java
/**
 * Komponent reprezentujący panel nawigacyjny dostępny na wielu stronach.
 */
public class NavigationMenu extends BaseComponent {
    
    private final SelenideElement rootElement;
    
    private final SelenideElement productsLink;
    private final SelenideElement ordersLink;
    private final SelenideElement accountLink;
    private final SelenideElement logoutButton;
    
    /**
     * Konstruktor przyjmujący element nadrzędny komponentu.
     * @param rootElement Element nadrzędny dla komponentu
     */
    public NavigationMenu(SelenideElement rootElement) {
        this.rootElement = rootElement;
        
        // Inicjalizacja elementów w kontekście
        this.productsLink = rootElement.$("[data-test='products-link']");
        this.ordersLink = rootElement.$("[data-test='orders-link']");
        this.accountLink = rootElement.$("[data-test='account-link']");
        this.logoutButton = rootElement.$("[data-test='logout-button']");
    }
    
    /**
     * Alternatywny konstruktor tworzący komponent od globalnego selektora.
     */
    public NavigationMenu() {
        this($(".main-navigation"));
    }
    
    /**
     * Przejście do strony produktów.
     * @return Obiekt ProductsPage
     */
    public ProductsPage navigateToProducts() {
        productsLink.click();
        return new ProductsPage().waitForPageToLoad(5);
    }
    
    /**
     * Przejście do strony zamówień.
     * @return Obiekt OrdersPage
     */
    public OrdersPage navigateToOrders() {
        ordersLink.click();
        return new OrdersPage().waitForPageToLoad(5);
    }
    
    /**
     * Przejście do strony konta użytkownika.
     * @return Obiekt AccountPage
     */
    public AccountPage navigateToAccount() {
        accountLink.click();
        return new AccountPage().waitForPageToLoad(5);
    }
    
    /**
     * Wylogowanie użytkownika.
     * @return Obiekt LoginPage
     */
    public LoginPage logout() {
        logoutButton.click();
        return new LoginPage().waitForPageToLoad(5);
    }
    
    /**
     * Sprawdza, czy nawigacja jest widoczna.
     * @return true jeśli nawigacja jest widoczna
     */
    public boolean isVisible() {
        return rootElement.isDisplayed();
    }
}

```

#### Organizacja testów korzystających z POM:


```java
@DisplayName("Testy funkcjonalności koszyka zakupowego")
public class ShoppingCartTests extends BaseTest {
    
    private LoginPage loginPage;
    private DashboardPage dashboardPage;
    private ProductsPage productsPage;
    private CartPage cartPage;
    
    @BeforeEach
    public void setUp() {
        // Inicjalizacja stron
        loginPage = new LoginPage();
        
        // Przygotowanie stanu - zalogowany użytkownik
        loginPage.open();
        dashboardPage = loginPage.loginAs("testuser", "testpassword");
    }
    
    @Test
    @DisplayName("Użytkownik może dodać produkt do koszyka")
    public void userCanAddProductToCart() {
        // Nawigacja do produktów
        productsPage = dashboardPage.getNavigationMenu().navigateToProducts();
        
        // Dodanie produktu do koszyka
        String productName = "Test Product";
        productsPage.addProductToCart(productName);
        
        // Weryfikacja powiadomienia
        productsPage.getNotification().shouldHave(text("Added to cart"));
        
        // Przejście do koszyka
        cartPage = productsPage.openCart();
        
        // Weryfikacja zawartości koszyka
        cartPage.getCartItems().shouldHave(size(1));
        cartPage.getCartItem(0).shouldHave(text(productName));
    }
    
    @Test
    @DisplayName("Użytkownik może usunąć produkt z koszyka")
    public void userCanRemoveProductFromCart() {
        // Nawigacja do produktów
        productsPage = dashboardPage.getNavigationMenu().navigateToProducts();
        
        // Dodanie produktu
        productsPage.addProductToCart("Test Product");
        
        // Przejście do koszyka
        cartPage = productsPage.openCart();
        
        // Weryfikacja początkowej zawartości
        cartPage.getCartItems().shouldHave(size(1));
        
        // Usunięcie produktu
        cartPage.removeItemFromCart(0);
        
        // Weryfikacja pustego koszyka
        cartPage.getEmptyCartMessage().shouldBe(visible)
                .shouldHave(text("Your cart is empty"));
    }
}

```

### Korzyści z zastosowania Page Object Model:

1. **Utrzymywalność**:
   * Zmiany w UI wymagają aktualizacji tylko w jednym miejscu
   * Modularna struktura ułatwia dodawanie nowych funkcjonalności
   * Jasna separacja odpowiedzialności między warstwami
2. **Czytelność i zrozumiałość**:
   * Testy odzwierciedlają działania użytkownika, a nie techniczne szczegóły
   * Kod jest samodokumentujący się, używając terminologii biznesowej
   * Łatwiejsza onboarding nowych członków zespołu
3. **Wielokrotne wykorzystanie kodu**:
   * Komponenty UI mogą być używane w wielu testach
   * Wspólne wzorce interakcji są zaimplementowane tylko raz
   * Reużywalność powoduje szybsze tworzenie nowych testów
4. **Łatwiejsza adaptacja do zmian**:
   * Zmiany w UI mają minimalny wpływ na testy
   * Możliwość łatwej integracji z nowymi technologiami lub frameworkami
   * Elastyczność w konfiguracji testów dla różnych środowisk

## 5.2. Struktura testów API

Struktura testów API jest kluczowym elementem architektury frameworka testowego, zapewniającym organizację,
utrzymywalność i efektywność testów interfejsów programistycznych. Dobrze zaprojektowana struktura umożliwia szybkie
tworzenie nowych testów, ułatwia utrzymanie istniejących oraz zapewnia przejrzystość i zrozumiałość dla całego zespołu.

### Główne komponenty struktury testów API:

1. **Modele danych (DTOs)**:
   * Obiekty reprezentujące struktury danych używane w API
   * Mapowanie JSON/XML na obiekty Javy
   * Walidatory i konwertery formatów

2. **Klienty API**:
   * Abstrakcja nad Rest Assured dla poszczególnych zasobów/endpointów 
   * Enkapsulacja szczegółów technicznych komunikacji 
   * Metody odzwierciedlające operacje biznesowe

3. **Specyfikacje API**:
   * Definicje wspólnych elementów żądań (headers, auth)
   * Konfiguracja bazowa dla różnych typów zapytań 
   * Szablony dla często używanych wzorców

4. **Warstwa testów**:
   * Konkretne przypadki testowe korzystające z klientów API 
   * Konfiguracja środowiska i danych testowych 
   * Asercje i weryfikacje biznesowe

### Przykładowa struktura katalogów dla testów API:


```
src/test/java/com/company/api/
├── config/
│   ├── ApiConfig.java               // Konfiguracja API (URL, timeout)
│   ├── AuthConfig.java              // Konfiguracja autentykacji
│   └── EnvironmentConfig.java       // Konfiguracja dla różnych środowisk
├── model/
│   ├── request/
│   │   ├── UserCreateRequest.java   // DTO dla żądania utworzenia użytkownika
│   │   └── ProductSearchRequest.java // DTO dla wyszukiwania produktów
│   ├── response/
│   │   ├── UserResponse.java        // DTO dla odpowiedzi z danymi użytkownika
│   │   └── ErrorResponse.java       // DTO dla odpowiedzi błędów
│   └── common/
│       ├── Address.java             // Współdzielone modele danych
│       └── PaymentDetails.java      // Współdzielone modele danych
├── client/
│   ├── BaseApiClient.java           // Abstrakcyjna klasa bazowa dla klientów
│   ├── UserApiClient.java           // Klient API dla zasobu użytkowników
│   ├── ProductApiClient.java        // Klient API dla zasobu produktów
│   └── OrderApiClient.java          // Klient API dla zasobu zamówień
├── spec/
│   ├── CommonRequestSpecs.java      // Wspólne specyfikacje żądań
│   ├── CommonResponseSpecs.java     // Wspólne specyfikacje odpowiedzi
│   └── AuthenticationSpecs.java     // Specyfikacje związane z autentykacją
├── test/
│   ├── user/
│   │   ├── UserCreationTests.java   // Testy tworzenia użytkowników
│   │   └── UserAuthenticationTests.java // Testy logowania/autoryzacji
│   ├── product/
│   │   ├── ProductSearchTests.java  // Testy wyszukiwania produktów
│   │   └── ProductCatalogTests.java // Testy katalogu produktów
│   └── order/
│       ├── OrderCreationTests.java  // Testy tworzenia zamówień
│       └── OrderProcessingTests.java // Testy przetwarzania zamówień
└── util/
    ├── JsonSchemaValidator.java     // Narzędzia do walidacji schematów
    ├── ApiTestDataGenerator.java    // Generator danych testowych
    └── ResponseExtractor.java       // Narzędzia do ekstrakcji danych z odpowiedzi

```

### Implementacja poszczególnych komponentów:

#### Klasa konfiguracyjna API:


```java
/**
 * Centralna konfiguracja dla testów API.
 * Dostarcza parametry zależne od środowiska i wspólne ustawienia.
 */
public class ApiConfig {
    
    private static final String DEFAULT_BASE_URL = "https://api.example.com";
    private static final int DEFAULT_TIMEOUT = 10000; // ms
    
    /**
     * Zwraca bazowy URL API dla aktualnego środowiska.
     * @return String z bazowym URL
     */
    public static String getBaseUrl() {
        return System.getProperty("api.baseUrl", DEFAULT_BASE_URL);
    }
    
    /**
     * Zwraca timeout dla żądań HTTP.
     * @return Timeout w milisekundach
     */
    public static int getTimeout() {
        return Integer.parseInt(System.getProperty("api.timeout", 
                                String.valueOf(DEFAULT_TIMEOUT)));
    }
    
    /**
     * Inicjalizuje konfigurację RestAssured.
     * Powinno być wywołane przed uruchomieniem testów.
     */
    public static void initRestAssured() {
        RestAssured.baseURI = getBaseUrl();
        RestAssured.config = RestAssuredConfig.config()
            .httpClient(HttpClientConfig.httpClientConfig()
                .setParam("http.socket.timeout", getTimeout())
                .setParam("http.connection.timeout", getTimeout()));
        
        // Konfiguracja logowania (ostrożnie z danymi wrażliwymi!)
        if (isDebugMode()) {
            RestAssured.filters(new RequestLoggingFilter(), new ResponseLoggingFilter());
        }
    }
    
    /**
     * Sprawdza, czy włączony jest tryb debug.
     * @return true jeśli tryb debug jest włączony
     */
    public static boolean isDebugMode() {
        return Boolean.parseBoolean(System.getProperty("api.debug", "false"));
    }
}

```

#### Przykładowy model danych (DTO):


```java
/**
 * Data Transfer Object reprezentujący żądanie utworzenia użytkownika.
 */
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class UserCreateRequest {
    
    @NotNull(message = "First name is required")
    private String firstName;
    
    @NotNull(message = "Last name is required")
    private String lastName;
    
    @Email(message = "Must be a valid email address")
    private String email;
    
    @NotNull(message = "Password is required")
    @Size(min = 8, message = "Password must be at least 8 characters")
    private String password;
    
    private List<String> roles;
    
    /**
     * Factory method tworzący przykładowego użytkownika.
     * @return Przykładowy obiekt żądania
     */
    public static UserCreateRequest createDefault() {
        return UserCreateRequest.builder()
            .firstName("John")
            .lastName("Kowalski")
            .email("john.Kowalski@example.com")
            .password("Password123!")
            .roles(List.of("USER"))
            .build();
    }
}

/**
 * DTO reprezentujący odpowiedź z danymi użytkownika.
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
public class UserResponse {
    private String id;
    private String firstName;
    private String lastName;
    private String email;
    private List<String> roles;
    private Date createdAt;
    private Date updatedAt;
}

```

#### Bazowy klient API:


```java
/**
 * Bazowa klasa dla wszystkich klientów API.
 * Dostarcza wspólną funkcjonalność i konfigurację.
 */
public abstract class BaseApiClient {
    
    protected final RequestSpecification baseSpec;
    
    /**
     * Konstruktor inicjalizujący bazową specyfikację.
     */
    public BaseApiClient() {
        this.baseSpec = RestAssured.given()
            .contentType(ContentType.JSON)
            .accept(ContentType.JSON)
            .config(RestAssuredConfig.config()
                .objectMapperConfig(new ObjectMapperConfig()
                    .jackson2ObjectMapperFactory((cls, charset) -> {
                        ObjectMapper mapper = new ObjectMapper();
                        mapper.registerModule(new JavaTimeModule());
                        mapper.disable(SerializationFeature.WRITE_DATES_AS_TIMESTAMPS);
                        mapper.setSerializationInclusion(JsonInclude.Include.NON_NULL);
                        return mapper;
                    })))
            .log().ifValidationFails();
    }
    
    /**
     * Dodaje autentykację do specyfikacji.
     * @param token Token autentykacji
     * @return RequestSpecification z dodaną autentykacją
     */
    protected RequestSpecification withAuth(String token) {
        return baseSpec.header("Authorization", "Bearer " + token);
    }
    
    /**
     * Loguje błąd odpowiedzi HTTP dla lepszej diagnostyki.
     * @param response Odpowiedź do zalogowania
     */
    protected void logErrorResponse(Response response) {
        if (response.statusCode() >= 400) {
            log.error("API Error: Status {}, Body: {}", 
                     response.statusCode(), response.body().asString());
        }
    }
    
    /**
     * Przetwarza odpowiedź na określony typ.
     * @param response Odpowiedź HTTP
     * @param clazz Klasa docelowa
     * @param <T> Typ docelowy
     * @return Obiekt określonego typu
     */
    protected <T> T processResponse(Response response, Class<T> clazz) {
        if (response.statusCode() >= 400) {
            logErrorResponse(response);
            throw new ApiException("API request failed with status: " + response.statusCode());
        }
        return response.as(clazz);
    }
}

```

#### Konkretna implementacja klienta API:


```java
/**
 * Klient API dla zasobu użytkowników.
 * Enkapsuluje operacje CRUD i inne akcje związane z użytkownikami.
 */
@Slf4j
public class UserApiClient extends BaseApiClient {
    
    private static final String USERS_PATH = "/api/users";
    
    /**
     * Tworzy nowego użytkownika.
     * @param request Dane nowego użytkownika
     * @return Utworzony użytkownik
     */
    public UserResponse createUser(UserCreateRequest request) {
        log.info("Creating user with email: {}", request.getEmail());
        
        Response response = baseSpec
            .body(request)
            .when()
            .post(USERS_PATH);
        
        return processResponse(response, UserResponse.class);
    }
    
    /**
     * Pobiera użytkownika po ID.
     * @param userId ID użytkownika
     * @return Dane użytkownika
     */
    public UserResponse getUserById(String userId) {
        log.info("Fetching user with ID: {}", userId);
        
        Response response = baseSpec
            .pathParam("id", userId)
            .when()
            .get(USERS_PATH + "/{id}");
        
        return processResponse(response, UserResponse.class);
    }
    
    /**
     * Aktualizuje dane użytkownika.
     * @param userId ID użytkownika
     * @param request Dane do aktualizacji
     * @return Zaktualizowany użytkownik
     */
    public UserResponse updateUser(String userId, UserCreateRequest request) {
        log.info("Updating user with ID: {}", userId);
        
        Response response = baseSpec
            .pathParam("id", userId)
            .body(request)
            .when()
            .put(USERS_PATH + "/{id}");
        
        return processResponse(response, UserResponse.class);
    }
    
    /**
     * Usuwa użytkownika.
     * @param userId ID użytkownika do usunięcia
     */
    public void deleteUser(String userId) {
        log.info("Deleting user with ID: {}", userId);
        
        Response response = baseSpec
            .pathParam("id", userId)
            .when()
            .delete(USERS_PATH + "/{id}");
        
        if (response.statusCode() != 204) {
            logErrorResponse(response);
            throw new ApiException("Failed to delete user: " + userId);
        }
    }
    
    /**
     * Wyszukuje użytkowników według kryteriów.
     * @param searchParams Parametry wyszukiwania
     * @return Lista znalezionych użytkowników
     */
    public List<UserResponse> searchUsers(Map<String, String> searchParams) {
        log.info("Searching users with criteria: {}", searchParams);
        
        Response response = baseSpec
            .queryParams(searchParams)
            .when()
            .get(USERS_PATH);
        
        return Arrays.asList(processResponse(response, UserResponse[].class));
    }
    
    /**
     * Autentykuje użytkownika i zwraca token.
     * @param email Email użytkownika
     * @param password Hasło
     * @return Token autentykacji
     */
    public String authenticateUser(String email, String password) {
        log.info("Authenticating user: {}", email);
        
        AuthRequest authRequest = new AuthRequest(email, password);
        
        Response response = baseSpec
            .body(authRequest)
            .when()
            .post("/api/auth/login");
        
        AuthResponse authResponse = processResponse(response, AuthResponse.class);
        return authResponse.getToken();
    }
}

```

#### Przykład specyfikacji wspólnych:


```java
/**
 * Wspólne specyfikacje żądań używane w testach API.
 */
public class CommonRequestSpecs {
    
    /**
     * Podstawowa specyfikacja dla żądań JSON.
     * @return RequestSpecification z typowymi ustawieniami
     */
    public static RequestSpecification jsonRequestSpec() {
        return new RequestSpecBuilder()
            .setContentType(ContentType.JSON)
            .setAccept(ContentType.JSON)
            .log(LogDetail.ALL)
            .build();
    }
    
    /**
     * Specyfikacja z podstawową autentykacją.
     * @param username Nazwa użytkownika
     * @param password Hasło
     * @return RequestSpecification z autentykacją
     */
    public static RequestSpecification basicAuthSpec(String username, String password) {
        return new RequestSpecBuilder()
            .addRequestSpecification(jsonRequestSpec())
            .setAuth(RestAssured.basic(username, password))
            .build();
    }
    
    /**
     * Specyfikacja z autentykacją OAuth2/Bearer.
     * @param token Token autoryzacyjny
     * @return RequestSpecification z autentykacją
     */
    public static RequestSpecification oauthSpec(String token) {
        return new RequestSpecBuilder()
            .addRequestSpecification(jsonRequestSpec())
            .addHeader("Authorization", "Bearer " + token)
            .build();
    }
    
    /**
     * Specyfikacja dla żądań z paginacją.
     * @param page Numer strony
     * @param size Rozmiar strony
     * @return RequestSpecification z parametrami paginacji
     */
    public static RequestSpecification paginationSpec(int page, int size) {
        return new RequestSpecBuilder()
            .addRequestSpecification(jsonRequestSpec())
            .addQueryParam("page", page)
            .addQueryParam("size", size)
            .build();
    }
}

/**
 * Wspólne specyfikacje odpowiedzi używane w testach API.
 */
public class CommonResponseSpecs {
    
    /**
     * Specyfikacja dla pomyślnych odpowiedzi.
     * @return ResponseSpecification weryfikujące sukces
     */
    public static ResponseSpecification successResponse() {
        return new ResponseSpecBuilder()
            .expectStatusCode(anyOf(is(200), is(201), is(204)))
            .log(LogDetail.ALL)
            .build();
    }
    
    /**
     * Specyfikacja dla odpowiedzi z błędem walidacji.
     * @return ResponseSpecification weryfikujące błąd walidacji
     */
    public static ResponseSpecification validationErrorResponse() {
        return new ResponseSpecBuilder()
            .expectStatusCode(400)
            .expectContentType(ContentType.JSON)
            .log(LogDetail.ALL)
            .build();
    }
    
    /**
     * Specyfikacja dla odpowiedzi o nieautoryzowanym dostępie.
     * @return ResponseSpecification weryfikujące błąd autoryzacji
     */
    public static ResponseSpecification unauthorizedResponse() {
        return new ResponseSpecBuilder()
            .expectStatusCode(anyOf(is(401), is(403)))
            .log(LogDetail.ALL)
            .build();
    }
    
    /**
     * Specyfikacja dla odpow

```


```java
    /**
     * Specyfikacja dla odpowiedzi o nieautoryzowanym dostępie.
     * @return ResponseSpecification weryfikujące błąd autoryzacji
     */
    public static ResponseSpecification unauthorizedResponse() {
        return new ResponseSpecBuilder()
            .expectStatusCode(anyOf(is(401), is(403)))
            .log(LogDetail.ALL)
            .build();
    }
    
    /**
     * Specyfikacja dla odpowiedzi "nie znaleziono".
     * @return ResponseSpecification weryfikujące 404
     */
    public static ResponseSpecification notFoundResponse() {
        return new ResponseSpecBuilder()
            .expectStatusCode(404)
            .log(LogDetail.ALL)
            .build();
    }
    
    /**
     * Specyfikacja weryfikująca zgodność ze schematem JSON.
     * @param schemaPath Ścieżka do pliku schematu JSON
     * @return ResponseSpecification weryfikujące schemat JSON
     */
    public static ResponseSpecification matchesJsonSchema(String schemaPath) {
        return new ResponseSpecBuilder()
            .expectBody(matchesJsonSchemaInClasspath(schemaPath))
            .log(LogDetail.ALL)
            .build();
    }
}

```

#### Przykładowa implementacja testu API:


```java
/**
 * Testy funkcjonalności zarządzania użytkownikami.
 */
@DisplayName("User Management API Tests")
public class UserManagementTests extends BaseApiTest {
    
    private UserApiClient userApiClient;
    private String testUserId;
    private final List<String> userIdsToCleanup = new ArrayList<>();
    
    @BeforeEach
    public void setUp() {
        userApiClient = new UserApiClient();
    }
    
    @AfterEach
    public void cleanup() {
        // Usunięcie testowych użytkowników po teście
        userIdsToCleanup.forEach(id -> {
            try {
                userApiClient.deleteUser(id);
            } catch (Exception e) {
                log.warn("Could not delete test user {}: {}", id, e.getMessage());
            }
        });
    }
    
    @Test
    @DisplayName("Should create a new user with valid data")
    public void shouldCreateNewUserWithValidData() {
        // Arrange
        UserCreateRequest newUser = UserCreateRequest.builder()
            .firstName("John")
            .lastName("Kowalski")
            .email("john.Kowalski." + UUID.randomUUID().toString() + "@example.com")
            .password("SecurePass123!")
            .roles(List.of("USER"))
            .build();
        
        // Act
        UserResponse createdUser = userApiClient.createUser(newUser);
        userIdsToCleanup.add(createdUser.getId());
        
        // Assert
        assertThat(createdUser).isNotNull();
        assertThat(createdUser.getId()).isNotEmpty();
        assertThat(createdUser.getEmail()).isEqualTo(newUser.getEmail());
        assertThat(createdUser.getFirstName()).isEqualTo(newUser.getFirstName());
        assertThat(createdUser.getLastName()).isEqualTo(newUser.getLastName());
        assertThat(createdUser.getRoles()).containsExactlyElementsOf(newUser.getRoles());
    }
    
    @Test
    @DisplayName("Should return 400 when creating user with invalid email")
    public void shouldReturn400WhenCreatingUserWithInvalidEmail() {
        // Arrange
        UserCreateRequest invalidUser = UserCreateRequest.builder()
            .firstName("John")
            .lastName("Kowalski")
            .email("invalid-email") // Niepoprawny format email
            .password("SecurePass123!")
            .roles(List.of("USER"))
            .build();
        
        // Act & Assert
        try {
            userApiClient.createUser(invalidUser);
            fail("Expected an ApiException to be thrown");
        } catch (ApiException e) {
            assertThat(e.getMessage()).contains("400");
        }
    }
    
    @Test
    @DisplayName("Should update existing user")
    public void shouldUpdateExistingUser() {
        // Arrange - create a user first
        UserCreateRequest initialUser = UserCreateRequest.createDefault();
        UserResponse createdUser = userApiClient.createUser(initialUser);
        userIdsToCleanup.add(createdUser.getId());
        
        // Define update data
        UserCreateRequest updateData = UserCreateRequest.builder()
            .firstName("Updated")
            .lastName("User")
            .email("updated." + UUID.randomUUID().toString() + "@example.com")
            .password("NewPassword123!")
            .roles(List.of("USER", "ADMIN"))
            .build();
        
        // Act
        UserResponse updatedUser = userApiClient.updateUser(createdUser.getId(), updateData);
        
        // Assert
        assertThat(updatedUser).isNotNull();
        assertThat(updatedUser.getId()).isEqualTo(createdUser.getId());
        assertThat(updatedUser.getFirstName()).isEqualTo(updateData.getFirstName());
        assertThat(updatedUser.getLastName()).isEqualTo(updateData.getLastName());
        assertThat(updatedUser.getEmail()).isEqualTo(updateData.getEmail());
        assertThat(updatedUser.getRoles()).containsExactlyInAnyOrderElementsOf(updateData.getRoles());
    }
    
    @Test
    @DisplayName("Should delete user")
    public void shouldDeleteUser() {
        // Arrange - create a user first
        UserCreateRequest user = UserCreateRequest.createDefault();
        UserResponse createdUser = userApiClient.createUser(user);
        String userId = createdUser.getId();
        
        // Act
        userApiClient.deleteUser(userId);
        
        // Assert - verify the user is not found
        try {
            userApiClient.getUserById(userId);
            fail("Expected an ApiException as user should be deleted");
        } catch (ApiException e) {
            assertThat(e.getMessage()).contains("404");
        }
    }
    
    @Test
    @DisplayName("Should find users by search criteria")
    public void shouldFindUsersBySearchCriteria() {
        // Arrange - create users with specific data
        String uniqueLastName = "Searcher" + UUID.randomUUID().toString().substring(0, 8);
        
        UserCreateRequest user1 = UserCreateRequest.builder()
            .firstName("John")
            .lastName(uniqueLastName)
            .email("john." + UUID.randomUUID().toString() + "@example.com")
            .password("Password123!")
            .roles(List.of("USER"))
            .build();
        
        UserCreateRequest user2 = UserCreateRequest.builder()
            .firstName("Jane")
            .lastName(uniqueLastName)
            .email("jane." + UUID.randomUUID().toString() + "@example.com")
            .password("Password123!")
            .roles(List.of("USER"))
            .build();
        
        UserResponse createdUser1 = userApiClient.createUser(user1);
        UserResponse createdUser2 = userApiClient.createUser(user2);
        userIdsToCleanup.add(createdUser1.getId());
        userIdsToCleanup.add(createdUser2.getId());
        
        // Act
        Map<String, String> searchParams = new HashMap<>();
        searchParams.put("lastName", uniqueLastName);
        List<UserResponse> foundUsers = userApiClient.searchUsers(searchParams);
        
        // Assert
        assertThat(foundUsers).isNotNull().hasSize(2);
        assertThat(foundUsers.stream().map(UserResponse::getLastName))
            .allMatch(lastName -> lastName.equals(uniqueLastName));
    }
}

```

### Korzyści struktury testów API:

1. **Abstrakcja i enkapsulacja**:
   * Ukrycie szczegółów technicznych komunikacji HTTP
   * Centralizacja logiki interakcji z API
   * Spójna obsługa błędów i wyjątków

2. **Utrzymywalność i skalowalność**:
   * Modułowa struktura ułatwiająca rozbudowę
   * Wielokrotne wykorzystanie komponentów
   * Centralizacja konfiguracji i wspólnych elementów

3. **Przejrzystość i czytelność**:
   * Testy odzwierciedlające operacje biznesowe, a nie techniczne
   * Spójna terminologia i nazewnictwo
   * Czytelna organizacja kodu odpowiadająca strukturze API

4. **Elastyczność i adaptowalność**:
   * Łatwa aktualizacja przy zmianach w API
   * Możliwość rozszerzenia o nowe funkcjonalności
   * Konfiguracja dla różnych środowisk testowych

## 5.3. Separacja kodu testowego od danych testowych

Separacja kodu testowego od danych testowych to fundamentalna zasada projektowania frameworka testowego, która znacząco
zwiększa utrzymywalność, czytelność i efektywność testów automatycznych. Podejście to polega na wyraźnym oddzieleniu
logiki testów od danych wejściowych i oczekiwanych wyników.

### Kluczowe aspekty separacji kodu od danych:


1. **Centralizacja danych testowych**:

   * Dane testowe przechowywane w dedykowanych repozytoriach
   * Oddzielenie danych od implementacji testów
   * Możliwość wielokrotnego wykorzystania tych samych danych

2. **Zewnętrzne źródła danych**:

   * Pliki JSON/XML/CSV zawierające dane testowe
   * Bazy danych testowych
   * Usługi dostarczające dane testowe

3. **Parametryzacja testów**:

   * Uruchamianie tych samych testów z różnymi zestawami danych
   * Dynamiczne pobieranie danych w czasie wykonania
   * Czytelne raportowanie z informacją o wykorzystanych danych

4. **Generatory danych testowych**:

   * Programowe tworzenie danych syntetycznych
   * Fabryki obiektów testowych
   * Randomizacja danych dla zwiększenia pokrycia testowego

### Implementacja separacji danych dla testów UI:

#### Podejście z wykorzystaniem plików zewnętrznych:


```java
/**
 * Klasa odpowiedzialna za ładowanie i zarządzanie danymi testowymi z plików JSON.
 */
public class TestDataLoader {
    
    private static final ObjectMapper objectMapper = new ObjectMapper();
    
    /**
     * Ładuje dane testowe z pliku JSON.
     * @param filePath Ścieżka do pliku z danymi
     * @param clazz Klasa docelowa
     * @param <T> Typ danych
     * @return Obiekt zawierający dane testowe
     */
    public static <T> T loadFromJson(String filePath, Class<T> clazz) {
        try {
            InputStream is = TestDataLoader.class.getResourceAsStream(filePath);
            if (is == null) {
                throw new IllegalArgumentException("File not found: " + filePath);
            }
            return objectMapper.readValue(is, clazz);
        } catch (IOException e) {
            throw new RuntimeException("Failed to load test data from " + filePath, e);
        }
    }
    
    /**
     * Ładuje kolekcję danych testowych z pliku JSON.
     * @param filePath Ścieżka do pliku z danymi
     * @param elementClass Klasa elementów kolekcji
     * @param <T> Typ elementów
     * @return Lista obiektów danych testowych
     */
    public static <T> List<T> loadListFromJson(String filePath, Class<T> elementClass) {
        try {
            InputStream is = TestDataLoader.class.getResourceAsStream(filePath);
            if (is == null) {
                throw new IllegalArgumentException("File not found: " + filePath);
            }
            JavaType type = objectMapper.getTypeFactory()
                .constructCollectionType(List.class, elementClass);
            return objectMapper.readValue(is, type);
        } catch (IOException e) {
            throw new RuntimeException("Failed to load test data list from " + filePath, e);
        }
    }
    
    /**
     * Ładuje dane testowe z pliku CSV.
     * @param filePath Ścieżka do pliku CSV
     * @return Lista map reprezentujących wiersze CSV
     */
    public static List<Map<String, String>> loadFromCsv(String filePath) {
        try {
            InputStream is = TestDataLoader.class.getResourceAsStream(filePath);
            if (is == null) {
                throw new IllegalArgumentException("File not found: " + filePath);
            }
            
            CsvReader reader = new CsvReader();
            reader.setContainsHeader(true);
            return reader.read(is);
        } catch (Exception e) {
            throw new RuntimeException("Failed to load CSV data from " + filePath, e);
        }
    }
}

```

#### Organizacja danych testowych w plikach:


```
src/test/resources/test-data/
├── ui/
│   ├── login/
│   │   ├── valid-users.json
│   │   └── invalid-users.json
│   ├── products/
│   │   ├── product-catalog.json
│   │   └── product-details.json
│   └── checkout/
│       ├── payment-methods.json
│       └── shipping-options.json
└── api/
    ├── user/
    │   ├── create-user-requests.json
    │   └── user-responses.json
    ├── product/
    │   ├── product-requests.json
    │   └── product-responses.json
    └── order/
        ├── order-requests.json
        └── order-responses.json

```

#### Przykładowy plik JSON z danymi testowymi:


```json
// valid-users.json
[
  {
    "username": "standard_user",
    "password": "secret_sauce",
    "firstName": "John",
    "lastName": "Kowalski",
    "expectedRole": "STANDARD"
  },
  {
    "username": "admin_user",
    "password": "admin123",
    "firstName": "Admin",
    "lastName": "User",
    "expectedRole": "ADMIN"
  },
  {
    "username": "locked_out_user",
    "password": "secret_sauce",
    "firstName": "Locked",
    "lastName": "User",
    "expectedRole": "LOCKED",
    "expectError": true,
    "errorMessage": "This user has been locked out."
  }
]

```

#### Wykorzystanie zewnętrznych danych w testach UI:


```java
/**
 * Testy funkcjonalności logowania z wykorzystaniem zewnętrznych danych testowych.
 */
@DisplayName("Login Functionality Tests")
public class LoginTests extends BaseTest {
    
    private LoginPage loginPage;
    
    @BeforeEach
    public void setUp() {
        loginPage = new LoginPage();
        loginPage.open();
    }
    
    /**
     * Test z parametrami z pliku JSON.
     * Każdy rekord w pliku JSON generuje oddzielny przypadek testowy.
     */
    @ParameterizedTest(name = "User login: {0}")
    @DisplayName("User can log in with valid credentials")
    @MethodSource("provideValidUsers")
    public void userCanLoginWithValidCredentials(UserTestData userData) {
        // Test tylko dla użytkowników bez oczekiwanego błędu
        assumeFalse(userData.isExpectError());
        
        // Wykonanie logowania
        DashboardPage dashboardPage = loginPage.loginAs(
            userData.getUsername(), 
            userData.getPassword()
        );
        
        // Weryfikacja
        dashboardPage.getUserInfoPanel()
            .shouldBe(visible)
            .shouldHave(text(userData.getFirstName()));
        
        // Dodatkowa weryfikacja roli jeśli określona
        if (userData.getExpectedRole() != null) {
            if ("ADMIN".equals(userData.getExpectedRole())) {
                dashboardPage.getAdminPanel().shouldBe(visible);
            } else {
                dashboardPage.getAdminPanel().shouldNotBe(visible);
            }
        }
    }
    
    /**
     * Test dla przypadków błędnego logowania.
     */
    @ParameterizedTest(name = "Error login: {0}")
    @DisplayName("System shows error for invalid login attempts")
    @MethodSource("provideInvalidUsers")
    public void systemShowsErrorForInvalidLogin(UserTestData userData) {
        // Test tylko dla użytkowników z oczekiwanym błędem
        assumeTrue(userData.isExpectError());
        
        // Próba logowania
        loginPage.loginExpectingError(
            userData.getUsername(), 
            userData.getPassword()
        );
        
        // Weryfikacja komunikatu błędu
        loginPage.getErrorMessage()
            .shouldBe(visible);
        
        // Weryfikacja szczegółowego komunikatu jeśli określony
        if (userData.getErrorMessage() != null) {
            loginPage.getErrorMessage()
                .shouldHave(text(userData.getErrorMessage()));
        }
    }
    
    /**
     * Dostawca danych dla testów poprawnego logowania.
     * @return Strumień danych testowych
     */
    static Stream<UserTestData> provideValidUsers() {
        List<UserTestData> users = TestDataLoader.loadListFromJson(
            "/test-data/ui/login/valid-users.json", 
            UserTestData.class
        );
        return users.stream()
            .filter(user -> !user.isExpectError());
    }
    
    /**
     * Dostawca danych dla testów niepoprawnego logowania.
     * @return Strumień danych testowych
     */
    static Stream<UserTestData> provideInvalidUsers() {
        List<UserTestData> allUsers = new ArrayList<>();
        
        // Załaduj użytkowników z pliku valid-users.json którzy mają flagę expectError
        List<UserTestData> validUsersWithErrors = TestDataLoader.loadListFromJson(
            "/test-data/ui/login/valid-users.json", 
            UserTestData.class
        ).stream()
        .filter(UserTestData::isExpectError)
        .collect(Collectors.toList());
        
        // Załaduj użytkowników z pliku invalid-users.json
        List<UserTestData> invalidUsers = TestDataLoader.loadListFromJson(
            "/test-data/ui/login/invalid-users.json", 
            UserTestData.class
        );
        
        allUsers.addAll(validUsersWithErrors);
        allUsers.addAll(invalidUsers);
        
        return allUsers.stream();
    }
    
    /**
     * Klasa reprezentująca dane testowe użytkownika.
     */
    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    public static class UserTestData {
        private String username;
        private String password;
        private String firstName;
        private String lastName;
        private String expectedRole;
        private boolean expectError;
        private String errorMessage;
        
        @Override
        public String toString() {
            return username + (expectError ? " (error expected)" : "");
        }
    }
}

```

### Implementacja separacji danych dla testów API:

#### Fabryki danych testowych:


```java
/**
 * Fabryka generująca dane testowe dla testów API.
 * Centralizuje logikę tworzenia obiektów testowych.
 */
public class ApiTestDataFactory {
    
    private static final Faker faker = new Faker();
    
    /**
     * Generuje dane dla utworzenia nowego użytkownika.
     * @return Obiekt żądania utworzenia użytkownika
     */
    public static UserCreateRequest createRandomUser() {
        return UserCreateRequest.builder()
            .firstName(faker.name().firstName())
            .lastName(faker.name().lastName())
            .email(faker.internet().emailAddress())
            .password(faker.internet().password(8, 12, true, true))
            .roles(List.of("USER"))
            .build();
    }
    
    /**
     * Generuje dane dla użytkownika z określoną rolą.
     * @param role Rola użytkownika
     * @return Obiekt żądania utworzenia użytkownika
     */
    public static UserCreateRequest createUserWithRole(String role) {
        UserCreateRequest user = createRandomUser();
        user.setRoles(List.of(role));
        return user;
    }
    
    /**
     * Generuje dane dla zamówienia.
     * @return Obiekt żądania utworzenia zamówienia
     */
    public static OrderCreateRequest createRandomOrder() {
        List<OrderItem> items = new ArrayList<>();
        
        // Dodaj 1-5 losowych produktów
        int itemCount = faker.number().numberBetween(1, 6);
        for (int i = 0; i < itemCount; i++) {
            items.add(OrderItem.builder()
                .productId(UUID.randomUUID().toString())
                .quantity(faker.number().numberBetween(1, 10))
                .unitPrice(BigDecimal.valueOf(faker.number().randomDouble(2, 10, 1000)))
                .build());
        }
        
        return OrderCreateRequest.builder()
            .customerName(faker.name().fullName())
            .customerEmail(faker.internet().emailAddress())
            .shippingAddress(createRandomAddress())
            .billingAddress(createRandomAddress())
            .paymentMethod("CREDIT_CARD")
            .items(items)
            .build();
    }
    
    /**
     * Generuje losowy adres.
     * @return Obiekt adresu
     */
    public static Address createRandomAddress() {
        return Address.builder()
            .street(faker.address().streetAddress())
            .city(faker.address().city())
            .state(faker.address().state())
            .postalCode(faker.address().zipCode())
            .country(faker.address().country())
            .build();
    }
    
    /**
     * Ładuje dane testowe z pliku JSON i modyfikuje pola w celu zapewnienia unikalności.
     * @param filePath Ścieżka do pliku
     * @return Zmodyfikowany obiekt żądania
     */
    public static UserCreateRequest loadAndModifyUserData(String filePath) {
        UserCreateRequest template = TestDataLoader.loadFromJson(filePath, UserCreateRequest.class);
        
        // Modyfikacja pól zapewniająca unikalność
        String uniqueSuffix = UUID.randomUUID().toString().substring(0, 8);
        template.setEmail(template.getEmail().replace("@", "." + uniqueSuffix + "@"));
        
        return template;
    }
}

```

#### Parametryzacja testów API:


```java
/**
 * Przykład testów API z separacją kodu i danych.
 */
@DisplayName("Product API Tests")
public class ProductApiTests extends BaseApiTest {
    
    private ProductApiClient productApiClient;
    
    @BeforeEach
    public void setUp() {
        productApiClient = new ProductApiClient();
    }
    
    /**
     * Test parametryzowany z danymi z pliku CSV.
     */
    @ParameterizedTest(name = "Product search with category: {0}, minPrice: {1}, maxPrice: {2}")
    @CsvFileSource(resources = "/test-data/api/product/search-criteria.csv", 
                  numLinesToSkip = 1) // Pomiń nagłówek
    public void shouldFilterProductsBySearchCriteria(String category, 
                                                   BigDecimal minPrice, 
                                                   BigDecimal maxPrice,
                                                   int expectedMinResults) {
        // Arrange
        Map<String, Object> searchParams = new HashMap<>();
        searchParams.put("category", category);
        
        if (minPrice != null) {
            searchParams.put("minPrice", minPrice);
        }
        
        if (maxPrice != null) {
            searchParams.put("maxPrice", maxPrice);
        }
        
        // Act
        List<ProductResponse> results = productApiClient.searchProducts(searchParams);
        
        // Assert
        assertThat(results).isNotNull();
        assertThat(results.size()).isGreaterThanOrEqualTo(expectedMinResults);
        
        for (ProductResponse product : results) {
            // Verify category filter
            assertThat(product.getCategory()).isEqualTo(category);
            
            // Verify price range if specified
            if (minPrice != null) {
                assertThat(product.getPrice()).isGreaterThanOrEqualTo(minPrice);
            }
            
            if (maxPrice != null) {
                assertThat(product.getPrice()).isLessThanOrEqualTo(maxPrice);
            }
        }
    }
    
    /**
     * Test wykorzystujący dane z pliku JSON.
     */
    @Test
    @DisplayName("Should create product with valid data")
    public void shouldCreateProductWithValidData() {
        // Arrange - load base data from JSON
        ProductCreateRequest productData = TestDataLoader.loadFromJson(
            "/test-data/api/product/valid-product.json", 
            ProductCreateRequest.class
        );
        
        // Modify to ensure uniqueness
        String uniqueSuffix = UUID.randomUUID().toString().substring(0, 8);
        productData.setName(productData.getName() + " " + uniqueSuffix);
        productData.setSku("SKU-" + uniqueSuffix);
        
        // Act
        ProductResponse createdProduct = productApiClient.createProduct(productData);
        
        // Assert
        assertThat(createdProduct).isNotNull();
        assertThat(createdProduct.getId()).isNotEmpty();
        assertThat(createdProduct.getName()).isEqualTo(productData.getName());
        assertThat(createdProduct.getSku()).isEqualTo(productData.getSku());
        assertThat(createdProduct.getPrice()).isEqualByComparingTo(productData.getPrice());
        
        // Cleanup
        productApiClient.deleteProduct(createdProduct.getId());
    }
    
    /**
     * Test wykorzystujący generator danych.
     */
    @Test
    @DisplayName("Should update product fields")
    public void shouldUpdateProductFields() {
        // Arrange - create a product using generator
        ProductCreateRequest initialProduct = ProductTestDataFactory.createRandomProduct();
        ProductResponse createdProduct = productApiClient.createProduct(initialProduct);
        
        // Prepare update data
        ProductUpdateRequest updateData = ProductUpdateRequest.builder()
            .name("Updated " + initialProduct.getName())
            .description("Updated description")
            .price(initialProduct.getPrice().multiply(BigDecimal.valueOf(1.1))) // 10% increase
            .build();
        
        // Act
        ProductResponse updatedProduct = productApiClient.updateProduct(
            createdProduct.getId(), 
            updateData
        );
        
        // Assert
        assertThat(updatedProduct).isNotNull();
        assertThat(updatedProduct.getId()).isEqualTo(createdProduct.getId());
        assertThat(updatedProduct.getName()).isEqualTo(updateData.getName());
        assertThat(updatedProduct.getDescription()).isEqualTo(updateData.getDescription());
        assertThat(updatedProduct.getPrice()).isEqualByComparingTo(updateData.getPrice());
        
        // Verify that unmodified fields remain the same
        assertThat(updatedProduct.getSku()).isEqualTo(createdProduct.getSku());
        assertThat(updatedProduct.getCategory()).isEqualTo(createdProduct.getCategory());
        
        // Cleanup
        productApiClient.deleteProduct(updatedProduct.getId());
    }
}

```

### Korzyści separacji kodu od danych:

1. **Zwiększona utrzymywalność**:

   * Zmiany w danych testowych nie wymagają modyfikacji kodu
   * Łatwiejsze zarządzanie różnymi zestawami danych dla różnych środowisk
   * Mniej duplikacji kodu przez wielokrotne wykorzystanie logiki testowej

2. **Lepsza czytelność i organizacja**:
   
   * Przejrzysta struktura z wyraźnym podziałem odpowiedzialności
   * Łatwiejsza nawigacja i zrozumienie testów
   * Bardziej deklaratywny charakter testów

3. **Większe pokrycie testowe**:

   * Łatwe rozszerzanie pokrycia przez dodawanie nowych zestawów danych
   * Parametryzacja testów zwiększająca różnorodność scenariuszy
   * Efektywne testowanie przypadków brzegowych

4. **Efektywność procesu testowego**:

   * Szybsze tworzenie nowych testów
   * Łatwiejsza adaptacja do zmian w testowanej aplikacji
   * Możliwość równoległej pracy nad kodem i danymi testowymi

5. **Elastyczność i skalowalność**:

   * Łatwe dostosowanie testów do różnych środowisk
   * Mniejsze bariery wejścia dla nowych członków zespołu
   * Możliwość zarządzania dużymi zbiorami danych testowych

## 5.4. Projektowanie pod kątem utrzymywalności

Projektowanie frameworka testowego pod kątem utrzymywalności to strategiczne podejście zapewniające, że testy
automatyczne pozostaną efektywne, niezawodne i łatwe do aktualizacji w miarę ewolucji aplikacji. Jest to kluczowy aspekt
architektury, który bezpośrednio wpływa na długoterminową wartość inwestycji w automatyzację.

### Kluczowe zasady projektowania pod kątem utrzymywalności:


1. **Abstrakcja i enkapsulacja**:

     * Ukrywanie szczegółów implementacyjnych za odpowiednimi interfejsami
     * Ograniczenie zależności między komponentami
     * Izolacja zmian w jednym miejscu

2. **Modularność i kompozycja**:

    * Podział frameworka na niezależne, współpracujące moduły
    * Unikanie monolitycznych struktur
    * Możliwość wymiany komponentów bez wpływu na resztę systemu

3. **Separacja odpowiedzialności**:

    * Każdy komponent ma jasno zdefiniowany zakres działań
    * Unikanie klas/metod o wielu różnych funkcjach
    * Stosowanie wzorców projektowych odpowiednich dla domeny testów

4. **Spójne standardy i konwencje**:

    * Jednolite nazewnictwo klas, metod, zmiennych
    * Konsekwentna struktura projektów i pakietów
    * Dokumentacja kodu i komponentów
    * Wspólne podejście do obsługi błędów i wyjątków

5. **Adaptacyjność do zmian**:

    * Elastyczne struktury danych i interfejsy
    * Minimalizacja "sztywnych" zależności
    * Strategie radzenia sobie ze zmianami w testowanej aplikacji

### Praktyczne techniki zwiększania utrzymywalności:

#### 1. Wielowarstwowa architektura


```
Framework Testowy
├── Core Layer (Core)
│   ├── Konfiguracja
│   ├── Zarządzanie sterownikami
│   └── Mechanizmy raportowania
├── Service Layer (Warstwa usług)
│   ├── Abstrakcje dla UI (Page Objects)
│   ├── Klienty API
│   └── Zarządzanie danymi
└── Test Layer (Warstwa testów)
    ├── Testy UI
    ├── Testy API
    └── Testy integracyjne

```

Ta struktura zapewnia, że:
    * Zmiany w Core Layer nie wpływają na testy
    * Aktualizacje UI wymagają zmian tylko w Service Layer
    * Warstwy komunikują się przez dobrze zdefiniowane interfejsy

#### 2. Implementacja wzorców projektowych

**Wzorzec Factory (Fabryka)**:


```java
/**
 * Fabryka użytkowników odpowiedzialna za tworzenie różnych typów użytkowników
 * z odpowiednimi uprawnieniami w systemie.
 */
public class UserFactory {
    
    /**
     * Typ użytkownika określający poziom uprawnień.
     */
    public enum UserType {
        GUEST,
        REGULAR,
        MODERATOR,
        ADMIN
    }
    
    /**
     * Tworzy użytkownika określonego typu z podanymi danymi.
     * 
     * @param type typ użytkownika do utworzenia
     * @param username nazwa użytkownika
     * @param email adres email
     * @param password hasło
     * @return utworzony obiekt użytkownika z odpowiednimi uprawnieniami
     * @throws IllegalArgumentException jeśli podany typ użytkownika nie istnieje
     */
    public static User createUser(UserType type, String username, String email, String password) {
        switch (type) {
            case GUEST:
                return new GuestUser(username, email, password);
            case REGULAR:
                return new RegularUser(username, email, password);
            case MODERATOR:
                return new ModeratorUser(username, email, password);
            case ADMIN:
                return new AdminUser(username, email, password);
            default:
                throw new IllegalArgumentException("Nieznany typ użytkownika: " + type);
        }
    }
    
    /**
     * Tworzy użytkownika gościa z domyślnymi uprawnieniami.
     * 
     * @param username nazwa użytkownika
     * @param email adres email
     * @return utworzony obiekt użytkownika gościa
     */
    public static User createGuestUser(String username, String email) {
        return createUser(UserType.GUEST, username, email, "guest" + System.currentTimeMillis());
    }
    
    /**
     * Tworzy administratora systemu z pełnymi uprawnieniami.
     * 
     * @param username nazwa użytkownika
     * @param email adres email
     * @param password silne hasło
     * @return utworzony obiekt administratora
     */
    public static User createAdminUser(String username, String email, String password) {
        return createUser(UserType.ADMIN, username, email, password);
    }
    
    /**
     * Tworzy użytkownika na podstawie roli w systemie.
     * 
     * @param role nazwa roli w systemie
     * @param username nazwa użytkownika
     * @param email adres email
     * @param password hasło
     * @return utworzony obiekt użytkownika o odpowiednim typie
     * @throws IllegalArgumentException jeśli podana rola nie jest obsługiwana
     */
    public static User createUserByRole(String role, String username, String email, String password) {
        try {
            UserType type = UserType.valueOf(role.toUpperCase());
            return createUser(type, username, email, password);
        } catch (IllegalArgumentException e) {
            throw new IllegalArgumentException("Nieobsługiwana rola: " + role);
        }
    }
}


```

```java
/**
 * Przykładowy test sprawdzający uprawnienia różnych typów użytkowników.
 */
@Test
public void testUserPermissionsForDifferentRoles() {
    // Utworzenie użytkowników różnych typów za pomocą fabryki
    User guestUser = UserFactory.createUser(UserFactory.UserType.GUEST, "guest", "guest@example.com", "pass123");
    User regularUser = UserFactory.createUser(UserFactory.UserType.REGULAR, "user", "user@example.com", "pass123");
    User moderatorUser = UserFactory.createUser(UserFactory.UserType.MODERATOR, "mod", "mod@example.com", "pass123");
    User adminUser = UserFactory.createUser(UserFactory.UserType.ADMIN, "admin", "admin@example.com", "pass123");
    
    // Skrócony sposób tworzenia gościa
    User anotherGuest = UserFactory.createGuestUser("visitor", "visitor@example.com");
    
    // Tworzenie użytkownika na podstawie nazwy roli
    User superAdmin = UserFactory.createUserByRole("ADMIN", "superadmin", "super@example.com", "strongPass!");
    
    // Test funkcjonalności systemu z różnymi użytkownikami
    LoginPage loginPage = new LoginPage();
    
    // Test jako gość
    loginPage.loginAs(guestUser.getUsername(), "pass123");
    assertFalse("Gość nie powinien mieć dostępu do panelu administratora", dashboardPage.isAdminPanelVisible());
    
    // Test jako admin
    loginPage.loginAs(adminUser.getUsername(), "pass123");
    assertTrue("Administrator powinien mieć dostęp do panelu administratora", dashboardPage.isAdminPanelVisible());
    
    // Test dynamicznego tworzenia użytkowników podczas testów
    for (UserFactory.UserType type : UserFactory.UserType.values()) {
        User testUser = UserFactory.createUser(type, "test_" + type, "test_" + type + "@example.com", "testPass");
        // Wykonanie testów z użyciem wygenerowanego użytkownika...
    }
}

```

**Wzorzec Builder (Budowniczy)**:


```java
/**
 * Builder do tworzenia złożonych obiektów testowych.
 * Umożliwia czytelne i elastyczne definiowanie danych testowych.
 */
public class OrderBuilder {
    private final OrderRequest order = new OrderRequest();
    
    public OrderBuilder withCustomer(String name, String email) {
        order.setCustomerName(name);
        order.setCustomerEmail(email);
        return this;
    }
    
    public OrderBuilder withShippingAddress(Address address) {
        order.setShippingAddress(address);
        return this;
    }
    
    public OrderBuilder withItem(String productId, int quantity, BigDecimal price) {
        if (order.getItems() == null) {
            order.setItems(new ArrayList<>());
        }
        
        OrderItem item = new OrderItem();
        item.setProductId(productId);
        item.setQuantity(quantity);
        item.setUnitPrice(price);
        
        order.getItems().add(item);
        return this;
    }
    
    public OrderBuilder withPaymentMethod(String method) {
        order.setPaymentMethod(method);
        return this;
    }
    
    public OrderRequest build() {
        // Walidacja kompletności zamówienia
        if (order.getCustomerName() == null || order.getCustomerEmail() == null) {
            throw new IllegalStateException("Customer information is required");
        }
        
        if (order.getItems() == null || order.getItems().isEmpty()) {
            throw new IllegalStateException("Order must contain at least one item");
        }
        
        return order;
    }
}

// Wykorzystanie w teście
OrderRequest testOrder = new OrderBuilder()
    .withCustomer("John Kowalski", "john.Kowalski@example.com")
    .withShippingAddress(TestDataFactory.createAddress())
    .withItem("PROD-123", 2, BigDecimal.valueOf(29.99))
    .withItem("PROD-456", 1, BigDecimal.valueOf(49.99))
    .withPaymentMethod("CREDIT_CARD")
    .build();

```

**Wzorzec Strategy (Strategia)**:


```java
/**
 * Interfejs strategii testowania przepływu biznesowego.
 * Definiuje sposób testowania różnych ścieżek dla różnych ról.
 */
public interface BusinessFlowStrategy {
    /**
     * Wykonuje test flow biznesowego dla określonej roli.
     * 
     * @param testData dane testowe
     * @return wynik testu
     */
    FlowResult executeFlow(FlowTestData testData);
    
    /**
     * Zwraca nazwę roli dla której jest implementowana strategia.
     * 
     * @return nazwa roli
     */
    String getRole();
}

/**
 * Kontekst wykonywania testów flow biznesowego.
 */
public class BusinessFlowContext {
    private BusinessFlowStrategy strategy;
    
    /**
     * Ustawia strategię testowania przepływu biznesowego.
     * 
     * @param strategy strategia do zastosowania
     */
    public void setStrategy(BusinessFlowStrategy strategy) {
        this.strategy = strategy;
    }
    
    /**
     * Wykonuje test przepływu biznesowego używając bieżącej strategii.
     * 
     * @param testData dane testowe
     * @return wynik testu
     */
    public FlowResult testFlow(FlowTestData testData) {
        return strategy.executeFlow(testData);
    }
}

/**
 * Strategia testowania przepływu biznesowego dla podatnika.
 */
public class TaxpayerFlowStrategy implements BusinessFlowStrategy {
    /**
     * Wykonuje test przepływu biznesowego z perspektywy podatnika.
     * 
     * @param testData dane testowe
     * @return wynik testu
     */
    @Override
    public FlowResult executeFlow(FlowTestData testData) {
        // Implementacja testu dla podatnika składającego deklarację podatkową online
        return new FlowResult("Podatnik złożył deklarację", true);
    }
    
    /**
     * Zwraca nazwę roli.
     * 
     * @return "podatnik"
     */
    @Override
    public String getRole() {
        return "podatnik";
    }
}

/**
 * Strategia testowania przepływu biznesowego dla urzędnika.
 */
public class TaxOfficerFlowStrategy implements BusinessFlowStrategy {
    /**
     * Wykonuje test przepływu biznesowego z perspektywy urzędnika skarbowego.
     * 
     * @param testData dane testowe
     * @return wynik testu
     */
    @Override
    public FlowResult executeFlow(FlowTestData testData) {
        // Implementacja testu dla urzędnika przetwarzającego deklarację
        return new FlowResult("Urzędnik zweryfikował deklarację", true);
    }
    
    /**
     * Zwraca nazwę roli.
     * 
     * @return "urzędnik"
     */
    @Override
    public String getRole() {
        return "urzędnik";
    }
}

/**
 * Strategia testowania przepływu biznesowego dla kontrolera skarbowego.
 */
public class TaxAuditorFlowStrategy implements BusinessFlowStrategy {
    /**
     * Wykonuje test przepływu biznesowego z perspektywy kontrolera skarbowego.
     * 
     * @param testData dane testowe
     * @return wynik testu
     */
    @Override
    public FlowResult executeFlow(FlowTestData testData) {
        // Implementacja testu dla kontrolera przeprowadzającego dodatkową weryfikację
        return new FlowResult("Kontroler przeprowadził audyt", true);
    }
    
    /**
     * Zwraca nazwę roli.
     * 
     * @return "kontroler"
     */
    @Override
    public String getRole() {
        return "kontroler";
    }
}

```


```java
/**
 * Test sprawdzający przepływ biznesowy dla różnych ról w systemie podatkowym.
 */
@Test
public void testTaxDeclarationFlow() {
    // Przygotowanie danych testowych
    FlowTestData testData = new FlowTestData("PIT-37", Map.of(
        "taxId", "123-456-78-90",
        "year", "2025",
        "income", "120000",
        "expenses", "45000"
    ));
    
    // Utworzenie kontekstu testowego
    BusinessFlowContext context = new BusinessFlowContext();
    
    // Test przepływu z perspektywy podatnika
    context.setStrategy(new TaxpayerFlowStrategy());
    FlowResult taxpayerResult = context.testFlow(testData);
    
    assertThat(taxpayerResult)
        .as("Wynik testu dla podatnika")
        .isNotNull()
        .extracting(FlowResult::isSuccessful, FlowResult::getMessage, FlowResult::getReference)
        .containsExactly(true, "Podatnik złożył deklarację", "PIT-37-12345");
    
    // Test przepływu z perspektywy urzędnika weryfikującego deklarację
    context.setStrategy(new TaxOfficerFlowStrategy());
    FlowResult officerResult = context.testFlow(testData);
    
    assertThat(officerResult.isSuccessful())
        .as("Weryfikacja deklaracji przez urzędnika")
        .isTrue();
    
    assertThat(officerResult.getMessage())
        .as("Komunikat z weryfikacji")
        .contains("zweryfikował")
        .doesNotContain("odrzucił");
    
    assertThat(officerResult.getReference())
        .as("Identyfikator weryfikacji")
        .startsWith("VERIFIED-")
        .hasSize(VERIFICATION_IDENTIFIER_SIZE);
    
    // Test przepływu z perspektywy kontrolera skarbowego
    context.setStrategy(new TaxAuditorFlowStrategy());
    FlowResult auditorResult = context.testFlow(testData);
    
    assertThat(auditorResult)
        .as("Wynik testu dla kontrolera")
        .satisfies(result -> {
            assertThat(result.isSuccessful()).isTrue();
            assertThat(result.getMessage()).contains("audyt");
            assertThat(result.getReference()).matches("AUDIT-\\d+");
        });
    
    // Przykład dynamicznego wyboru strategii na podstawie roli
    String userRole = System.getProperty("test.role", "podatnik");
    
    BusinessFlowStrategy roleStrategy = switch (userRole) {
        case "urzędnik" -> new TaxOfficerFlowStrategy();
        case "kontroler" -> new TaxAuditorFlowStrategy();
        default -> new TaxpayerFlowStrategy();
    };
    
    context.setStrategy(roleStrategy);
    FlowResult dynamicResult = context.testFlow(testData);
    
    // Asercje dla dynamicznie wybranej strategii
    assertThat(roleStrategy.getRole())
        .as("Wybrana rola dla testu")
        .isIn("podatnik", "urzędnik", "kontroler");
    
    assertThat(dynamicResult)
        .as("Wynik dla roli %s", roleStrategy.getRole())
        .hasFieldOrProperty("successful")
        .hasFieldOrProperty("message")
        .hasFieldOrProperty("reference");
}

/**
 * Test pełnego procesu biznesowego od złożenia do audytu deklaracji.
 */
@Test
public void testEndToEndTaxProcess() {
    // Przygotowanie danych testowych dla scenariusza end-to-end
    FlowTestData testData = new FlowTestData("PIT-37", Map.of(
        "taxId", "123-456-78-90",
        "year", "2025",
        "income", "120000",
        "expenses", "45000",
        "attachments", "invoice_1.pdf,invoice_2.pdf"
    ));
    
    BusinessFlowContext context = new BusinessFlowContext();
    List<FlowResult> allResults = new ArrayList<>();
    
    // Krok 1: Podatnik składa deklarację
    context.setStrategy(new TaxpayerFlowStrategy());
    FlowResult submitResult = context.testFlow(testData);
    allResults.add(submitResult);
    
    // Krok 2: Urzędnik weryfikuje deklarację
    context.setStrategy(new TaxOfficerFlowStrategy());
    FlowResult verifyResult = context.testFlow(testData);
    allResults.add(verifyResult);
    
    // Krok 3: Kontroler przeprowadza audyt (tylko dla wybranych przypadków)
    if (Double.parseDouble(testData.getProperty("income")) > 100000) {
        context.setStrategy(new TaxAuditorFlowStrategy());
        FlowResult auditResult = context.testFlow(testData);
        allResults.add(auditResult);
    }
    
    // Asercje dla całego procesu z użyciem AssertJ
    assertThat(allResults)
        .as("Wyniki dla całego procesu podatkowego")
        .hasSize(3)
        .extracting(FlowResult::isSuccessful)
        .containsOnly(true);
    
    // Sprawdzenie sekwencji kroków
    assertThat(allResults)
        .extracting(FlowResult::getMessage)
        .containsExactly(
            "Podatnik złożył deklarację",
            "Urzędnik zweryfikował deklarację",
            "Kontroler przeprowadził audyt"
        );
    
    // Sprawdzenie referencji
    assertThat(allResults)
        .extracting(FlowResult::getReference)
        .satisfies(references -> {
            assertThat(references.get(0)).startsWith("PIT-37-");
            assertThat(references.get(1)).startsWith("VERIFIED-");
            assertThat(references.get(2)).startsWith("AUDIT-");
        });
    
    // Sprawdzenie danych testowych
    assertThat(testData.getProperty("income"))
        .as("Dochód do opodatkowania")
        .isNotEmpty()
        .satisfies(income -> {
            double incomeVal = Double.parseDouble(income);
            assertThat(incomeVal)
                .as("Wartość dochodu")
                .isGreaterThan(0)
                .isGreaterThan(Double.parseDouble(testData.getProperty("expenses")));
        });
    
    // Sprawdzenie załączników
    assertThat(testData.getProperty("attachments"))
        .as("Załączone dokumenty")
        .contains("invoice_1.pdf")
        .contains("invoice_2.pdf")
        .doesNotContain("virus.exe");
}

```


#### 3. Dokumentacja kodu i komponentów


```java
/**
 * Reprezentuje stronę logowania do aplikacji.
 * <p>
 * Ta klasa implementuje Page Object Model dla strony logowania, 
 * zapewniając enkapsulację elementów UI i operacji logowania.
 * </p>
 * <p>
 * Typowy przepływ użycia:
 * <pre>
 * LoginPage loginPage = new LoginPage();
 * loginPage.open();
 * DashboardPage dashboard = loginPage.loginAs("username", "password");
 * </pre>
 * </p>
 * 
 * @author Test Automation Team
 * @see BasePage
 * @see DashboardPage
 * @since 0
 */
public class LoginPage {
    
    /**
     * Wykonuje operację logowania z podanymi danymi.
     * 
     * @param username Nazwa użytkownika
     * @param password Hasło użytkownika
     * @return Obiekt DashboardPage, jeśli logowanie się powiodło
     * @throws ElementException jeśli elementy strony nie są dostępne
     */
    public DashboardPage loginAs(String username, String password) {
        try {
            logger.info("Logging in as user: {}", username);
            
            usernameField.shouldBe(visible).setValue(username);
            passwordField.shouldBe(visible).setValue(password);
            loginButton.shouldBe(visible, enabled).click();
            
            return new DashboardPage();
        } catch (ElementNotFound e) {
            throw new ElementException("Failed to interact with login elements", 
                                    e.toString(), e);
        }
    }
    
    /**
     * Wykonuje operację logowania oczekując błędu.
     * Używane do testowania negatywnych scenariuszy.
     * 
     * @param username Nazwa użytkownika
     * @param password Hasło użytkownika
     * @return Ten sam obiekt LoginPage (fluent interface)
     */
    public LoginPage loginExpectingError(String username, String password) {
        usernameField.setValue(username);
        passwordField.setValue(password);
        loginButton.click();
        
        // Oczekiwanie na komunikat błędu
        errorMessage.shouldBe(visible);
        return this;
    }
}

```

### Długoterminowe korzyści z projektowania pod kątem utrzymywalności:


1. **Redukcja długu technicznego**:

   * Mniejsza potrzeba refaktoryzacji w przyszłości
   * Łatwiejsza adaptacja do zmieniających się wymagań
   * Spójna jakość kodu w całym frameworku

2. **Skrócenie czasu wprowadzania zmian**:

   * Szybsza lokalizacja miejsc wymagających aktualizacji
   * Mniejsze ryzyko błędów regresyjnych
   * Krótszy czas onboardingu nowych członków zespołu

3. **Obniżenie kosztów utrzymania**:

   * Mniejszy nakład pracy na aktualizacje po zmianach w aplikacji
   * Redukcja liczby niestabilnych testów wymagających ciągłej naprawy
   * Lepszy zwrot z inwestycji w automatyzację w długim okresie

4. **Zwiększenie zaufania do testów**:

   * Bardziej niezawodne wyniki testów
   * Łatwiejsza interpretacja raportów
   * Wyższa akceptacja testów automatycznych przez interesariuszy

Projektowanie frameworka testowego pod kątem utrzymywalności jest inwestycją, która zwraca się wielokrotnie w całym
cyklu życia projektu. Wymaga świadomego planowania architektury, dyscypliny w implementacji oraz ciągłego doskonalenia,
ale prowadzi do znaczącego obniżenia kosztów i zwiększenia efektywności procesu testowego w długim okresie.

# 6. Integracja z CI/CD

## 6.1. Automatyzacja wykonania testów

Integracja testów automatycznych z procesem Continuous Integration i Continuous Delivery (CI/CD) stanowi kluczowy
element nowoczesnego podejścia do zapewnienia jakości oprogramowania. Efektywna automatyzacja wykonania testów wymaga
systematycznego i przemyślanego podejścia, które umożliwi płynne włączenie ich w pipeline deweloperski.

### Struktura i organizacja skryptów uruchomieniowych

W środowisku opartym na Javie, podstawą automatyzacji testów jest właściwe skonfigurowanie narzędzi budowania, takich
jak Maven czy Gradle. Skrypty te powinny umożliwiać:

- **Modułową strukturę testów** - podział na moduły odpowiadające różnym warstwom aplikacji (front-end, back-end,
  integracje z systemami zewnętrznymi)
- **Parametryzację uruchomień** - możliwość dynamicznego wyboru zestawów testów, środowisk i konfiguracji bez
  konieczności modyfikacji kodu
- **Profile testowe** - dedykowane profile dla różnych typów testów (np. `-Psmoke`, `-Pregression`, `-Pperformance`)
- **Zarządzanie zależnościami** - automatyczne pobieranie i aktualizacja bibliotek testowych (Selenium, Selenide,
  RestAssured, frameworki asercji)

Przykład konfiguracji Maven do uruchamiania różnych zestawów testów:


```xml

<profiles>
    <profile>
        <id>smoke</id>
        <properties>
            <groups>smoke</groups>
            <skip.integration.tests>true</skip.integration.tests>
            <skip.ui.tests>true</skip.ui.tests>
        </properties>
    </profile>
    <profile>
        <id>regression</id>
        <properties>
            <groups>regression</groups>
            <skip.integration.tests>false</skip.integration.tests>
            <skip.ui.tests>false</skip.ui.tests>
        </properties>
    </profile>
</profiles>

```

Przykład konfiguracji Gradle do uruchamiania różnych zestawów testów:

```gradle
task apiTests(type: Test) {
    useJUnitPlatform {
        includeTags 'api'
    }
    
    // Właściwości systemowe do konfiguracji środowiska testowego
    systemProperty 'test.api.baseUrl', project.findProperty('apiUrl') ?: 'http://localhost:8080'
    systemProperty 'test.api.timeout', '30000'
    
    testLogging {
        events "passed", "skipped", "failed"
    }
}

// Testy UI z Selenide - uruchamiane w dedykowanym środowisku
task uiTests(type: Test) {
    useJUnitPlatform {
        includeTags 'ui'
    }
    
    // Właściwości dla testów UI
    systemProperty 'selenide.browser', project.findProperty('browser') ?: 'chrome'
    systemProperty 'selenide.headless', project.findProperty('headless') ?: 'true'
    systemProperty 'selenide.baseUrl', project.findProperty('baseUrl') ?: 'http://localhost:8080'
    
    // Zwiększ timeout dla testów UI
    systemProperty 'junit.jupiter.execution.timeout.default', '2m'
    
    testLogging {
        events "passed", "skipped", "failed"
        exceptionFormat "full"
    }
}


```

### Kategoryzacja i selekcja testów

Efektywna automatyzacja wymaga przemyślanego systemu kategoryzacji testów, który umożliwi ich selektywne uruchamianie w
zależności od kontekstu:

- **Tagowanie testów** - wykorzystanie adnotacji w JUnit czy TestNG do oznaczania testów według:
    - Krytyczności (P0, P1, P2)
    - Komponentu funkcjonalnego (np. `@Tag("payment")`, `@Tag("registration")`)
    - Rodzaju testu (integracyjny, UI)
    - Czasu wykonania (szybkie, średnie, długie)
    - Zależności środowiskowych (np. `@RequiresExternalApi`)

- **Filtrowanie zestawów testów** - mechanizmy do dynamicznego wyboru testów do uruchomienia:
    - Selektywne uruchamianie testów na podstawie wyników poprzednich uruchomień (Test Impact Analysis)
    - Inteligentny wybór testów na podstawie zmian w kodzie
    - Priorytetyzacja testów według historii ich niestabilności i efektywności w wykrywaniu błędów

### Zarządzanie środowiskiem testowym

Kluczowym aspektem automatyzacji jest zapewnienie powtarzalności i izolacji środowiska testowego:

- **Konteneryzacja środowiska** - wykorzystanie Dockera do tworzenia izolowanych i przenośnych środowisk testowych:
    - Dedykowane obrazy Docker dla aplikacji testowanej
    - Kontenery Selenium Grid do współbieżnego uruchamiania testów UI
    - Zestawy kontenerów dla systemów zewnętrznych (bazy danych, usługi REST, kolejki)
    - Orkiestracja przy użyciu Docker Compose lub Kubernetes dla złożonych środowisk

- **Zarządzanie danymi testowymi**:
    - Automatyczne generowanie danych testowych z wykorzystaniem bibliotek (np. Java Faker, DataFactory)
    - Snapshot izolowanych baz danych przywracanych przed każdym uruchomieniem
    - Mechanizmy czyszczenia danych po wykonaniu testów
    - Wersjonowanie danych testowych wraz z kodem

- **Symulacja usług zewnętrznych**:
    - Implementacja mocków i stubów dla interfejsów zewnętrznych (WireMock, MockServer)
    - Nagrywanie i odtwarzanie rzeczywistych interakcji z systemami zewnętrznymi
    - Symulacja różnych scenariuszy odpowiedzi (sukces, błędy, opóźnienia)

### Mechanizmy odporności i stabilności

Testy automatyczne, szczególnie te na poziomie UI, mogą być podatne na niestabilność. Skuteczna automatyzacja wymaga
implementacji:

- **Strategii powtarzania (retry)** - mechanizmy ponownych prób dla niestabilnych testów:
    - Retry na poziomie pojedynczych asercji z wykorzystaniem bibliotek jak Awaitility
    - Powtarzanie całych metod testowych z progresywnymi opóźnieniami (exponential backoff)
    - Inteligentne mechanizmy powtórzeń dla specyficznych rodzajów błędów


```java
@Test
@RetryingTest(maxRetries = 3)
public void testPaymentProcessing() {
    // Test logic that might be flaky due to external dependencies
}

```

- **Zarządzanie timeoutami**:
    - Dynamiczne dostosowanie timeoutów w zależności od środowiska i typu testu
    - Progresywne strategie oczekiwania na elementy UI (explicit wait, fluent wait)
    - Monitoring czasów wykonania dla wykrywania degradacji wydajności

- **Obsługa równoległości**:
    - Konfiguracja ThreadPoolSize w TestNG lub JUnit5 Parallel
    - Identyfikacja i izolacja testów z współdzielonymi zasobami
    - Mechanizmy synchronizacji dla testów wymagających sekwencyjnego wykonania

### Automatyzacja przygotowania i wdrażania testów

Pełna automatyzacja obejmuje również:

- **Automatyczną aktualizację sterowników przeglądarek** - wykorzystanie WebDriverManager lub dedykowanych skryptów
- **Wersjonowanie artefaktów testowych** wraz z kodem aplikacji
- **Automatyczną kompilację i wdrażanie testów** jako część pipeline
- **Automatyczną walidację samych testów** przed ich włączeniem do głównego zestawu (testy dla testów)

### Strategie dla różnych typów testów

#### Testy API z RestAssured

Dla efektywnej automatyzacji testów API należy wdrożyć:

- Biblioteki specyfikacji (RestAssured RequestSpecification) do centralizacji konfiguracji
- Serializację/deserializację JSON/XML z wykorzystaniem Jackson lub JAXB
- Walidację schematów API (JSON Schema, Swagger/OpenAPI)
- Łańcuchy testów API symulujących przepływy użytkownika

#### Testy UI z Selenium/Selenide

Automatyzacja testów UI wymaga:

- Implementacji wzorca Page Object Model (POM) z bazowymi klasami
- Mechanizmów identyfikacji elementów odpornych na zmiany (np. data-testid zamiast XPath)
- Strategii obsługi dynamicznych elementów AJAX
- Zarządzania stanami przeglądarek i sesji

#### Testy wydajnościowe

Włączenie testów wydajnościowych do pipeline wymaga:

- Integracji narzędzi jak JMeter, Gatling z procesem CI/CD
- Automatycznej analizy metryk wydajnościowych
- Progów akceptacji dla czasów odpowiedzi i przepustowości
- Porównywania wyników z poprzednimi wersjami aplikacji

Kompleksowa automatyzacja wykonania testów stanowi fundament efektywnego procesu CI/CD, umożliwiając szybkie i
wiarygodne dostarczanie informacji zwrotnej dotyczącej jakości oprogramowania na każdym etapie procesu wytwórczego.

## 6.2. Strategie wykonywania testów w pipeline

Integracja testów automatycznych z pipeline CI/CD wymaga starannego zaprojektowania strategii ich wykonywania, aby
zrównoważyć szybkość dostarczania informacji zwrotnej z kompleksowością weryfikacji. Efektywna strategia musi
uwzględniać specyfikę różnych etapów cyklu wytwarzania oprogramowania, minimalizując czas potrzebny na wykrycie
problemów, jednocześnie optymalizując wykorzystanie zasobów.

### Wielowarstwowa piramida testów w pipeline

Nowoczesne podejście do wykonywania testów w pipeline opiera się na koncepcji piramidy testów, gdzie różne typy testów
są wykonywane na odpowiednich etapach:

- **Warstwa podstawowa (commit stage)** - najszybsze testy wykonywane natychmiast po każdej zmianie:
    - Testy jednostkowe weryfikujące logikę biznesową
    - Szybkie testy integracyjne (z wykorzystaniem in-memory databases)
    - Analiza statyczna kodu (SonarQube, SpotBugs, CheckStyle)
    - Testy architektury (ArchUnit) weryfikujące zgodność z ustalonymi wzorcami

- **Warstwa środkowa (build acceptance stage)** - uruchamiana po pomyślnym przejściu etapu commit:
    - Testy integracyjne z rzeczywistymi bazami danych
    - Testy API dla kluczowych ścieżek biznesowych
    - Podstawowe testy UI (smoke tests) dla krytycznych funkcjonalności
    - Testy zgodności (compatibility tests) dla różnych konfiguracji

- **Warstwa wyższa (comprehensive testing stage)** - wykonywana przed wdrożeniem na środowiska pre-produkcyjne:
    - Pełne zestawy testów UI dla wszystkich głównych funkcjonalności
    - Testy end-to-end symulujące rzeczywiste przepływy użytkownika
    - Testy wydajnościowe i skalowania
    - Testy bezpieczeństwa (SAST/DAST)

- **Warstwa wierzchołkowa (release stage)** - wykonywana przed wdrożeniem na produkcję:
    - Testy akceptacyjne w środowisku produkcyjnym lub jego wiernej replice
    - Testy zgodności z regulacjami i standardami (GDPR, WCAG, PCI-DSS itp.)
    - Testy smoke po wdrożeniu na produkcję (canary tests)

### Strategie uruchamiania testów w zależności od etapu pipeline

#### Strategia Fast Feedback

Celem tej strategii jest zapewnienie natychmiastowej informacji zwrotnej deweloperom:

- **Trigger**: Każdy commit lub pull request
- **Zakres testów**:
    - Testy jednostkowe (< 1-2 minuty)
    - Lekkie testy integracyjne (< 5 minut)
    - Weryfikacja stylu kodu i podstawowych reguł jakościowych
- **Implementacja**:
    - Uruchamianie tylko testów dla zmienionych komponentów (Test Impact Analysis)
    - Wykorzystanie cache dla zależności i kompilacji
    - Możliwość przerwania wykonania po pierwszym błędzie
- **Cel czasowy**: < 10 minut dla pełnego cyklu


```yaml
# Przykład konfiguracji GitLab CI dla fast feedback
fast_feedback:
  stage: test
  script:
    - ./mvnw test -Dtest="UnitTests,*FastIntegrationTest" -DfailIfNoTests=false
  rules:
    - if: $CI_PIPELINE_SOURCE == 'merge_request_event'
  artifacts:
    reports:
      junit: target/surefire-reports/TEST-*.xml

```

#### Strategia Smoke Testing

Ta strategia koncentruje się na weryfikacji kluczowych funkcjonalności:

- **Trigger**: Pomyślny wynik etapu Fast Feedback
- **Zakres testów**:
    - Krytyczne testy API (20-30 testów)
    - Podstawowe testy UI (5-10 scenariuszy)
    - Weryfikacja głównych przepływów biznesowych
- **Implementacja**:
    - Równoległe uruchamianie niezależnych scenariuszy
    - Priorytetyzacja testów według krytyczności biznesowej
    - Retry dla niestabilnych testów
- **Cel czasowy**: < 30 minut

#### Strategia testów pełnych (Comprehensive Testing)

Strategia zapewniająca kompleksową weryfikację przed wdrożeniem na staging:

- **Trigger**: Zaplanowane lub manualne po pomyślnych smoke testach
- **Zakres testów**:
    - Pełen zakres testów funkcjonalnych (UI, API)
    - Testy integracyjne z systemami zewnętrznymi
    - Podstawowe testy wydajnościowe
    - Testy bezpieczeństwa
- **Implementacja**:
    - Uruchamianie w dedykowanych środowiskach testowych
    - Pełna dystrybucja równoległa na wielu węzłach
    - Kompleksowe raportowanie wyników
- **Cel czasowy**: < 2-3 godziny

#### Strategia nocnej regresji (Nightly Regression)

Strategia zapewniająca kompleksową weryfikację całego systemu:

- **Trigger**: Harmonogram (np. codziennie o północy)
- **Zakres testów**:
    - Pełny zestaw wszystkich testów (regresja)
    - Długotrwałe testy stabilności
    - Testy wydajnościowe pod obciążeniem
    - Testy penetracyjne i bezpieczeństwa
- **Implementacja**:
    - Automatyczne przygotowanie środowisk testowych
    - Maksymalne wykorzystanie równoległości
    - Szczegółowa analiza wyników i trendów
- **Cel czasowy**: 6-8 godzin (wykonywane poza godzinami pracy)

### Optymalizacja wykonania testów

#### Równoległe wykonanie testów

Efektywna strategia równoległego wykonania testów jest kluczem do optymalizacji czasu trwania pipeline:

- **Poziomy równoległości**:
    - Równoległość na poziomie metod testowych (TestNG/JUnit5)
    - Równoległość na poziomie klas testowych
    - Równoległość na poziomie zestawów testów (test suites)
    - Równoległość na poziomie środowisk (różne wersje przeglądarek, systemy operacyjne)

- **Techniki dystrybucji obciążenia**:
    - Dynamiczny podział testów na podstawie historycznego czasu wykonania
    - Grupowanie testów współdzielących dane wejściowe
    - Izolacja testów z potencjalnymi konfliktami zasobów


```java
// Przykład konfiguracji równoległości w TestNG
@Test(threadPoolSize = 3, invocationCount = 10, timeOut = 10000)
public void testPaymentProcessingConcurrently() {
    // Test logic that can be executed in parallel
}

```

- **Infrastruktura dla testów równoległych**:
    - Selenium Grid do zarządzania pulą przeglądarek
    - Dynamiczne skalowanie zasobów w środowiskach chmurowych
    - Dedykowane pule zasobów dla różnych typów testów

#### Priorytetyzacja testów

Strategia priorytetyzacji testów umożliwia wcześniejsze wykrywanie krytycznych problemów:

- **Kryteria priorytetyzacji**:
    - Historyczna efektywność testów w wykrywaniu błędów
    - Pokrycie krytycznych ścieżek biznesowych
    - Czas wykonania testu (krótsze testy pierwsze)
    - Zależność od zmodyfikowanego kodu (Test Impact Analysis)

- **Dynamiczna priorytetyzacja**:
    - Uczenie maszynowe do przewidywania prawdopodobieństwa wystąpienia błędu
    - Adaptacyjne dostosowanie priorytetów na podstawie bieżących wyników
    - Automatyczna reklasyfikacja testów na podstawie historii ich niestabilności

#### Strategie dla testów długotrwałych

Testy wymagające dłuższego czasu wykonania wymagają specjalnych strategii:

- **Wykonanie asynchroniczne** - oddzielenie testów długotrwałych od głównego pipeline
- **Wczesne informowanie o wynikach częściowych** - raportowanie wyników testów na bieżąco
- **Profilowanie i identyfikacja "wąskich gardeł"** w zestawach testów
- **Automatyczna optymalizacja** długotrwałych testów

### Strategie dla różnych branży i przepływów pracy

#### Strategia dla modelu GitFlow

Dla zespołów pracujących z GitFlow, strategia wykonywania testów powinna być dostosowana do specyfiki branchy:

- **Feature branches**: Fast Feedback + Smoke Tests
- **Develop branch**: Fast Feedback + Smoke Tests + wybrane testy regresyjne
- **Release branches**: Pełna regresja + testy wydajnościowe
- **Hotfix branches**: Fast Feedback + ukierunkowane testy regresyjne

#### Strategia dla modelu Trunk-based Development

Dla zespołów pracujących z trunk-based development:

- **Przed push do trunk**: Fast Feedback (lokalnie)
- **Po push do trunk**: Fast Feedback + Smoke Tests (serwer CI)
- **Przed wdrożeniem**: Pełne testy funkcjonalne i regresyjne

### Strategie odzyskiwania i obsługi niestabilności

Efektywna strategia musi uwzględniać mechanizmy radzenia sobie z niestabilnością testów:

- **Automatyczne powtarzanie niestabilnych testów** z progresywnym opóźnieniem
- **Izolacja niestabilnych testów** do osobnych zestawów z mniejszym wpływem na pipeline
- **Mechanizmy graceful degradation** - umożliwiające kontynuację pipeline mimo nieistotnych błędów
- **Procedury eskalsji** dla krytycznych problemów wymagających natychmiastowej uwagi

Wdrożenie kompleksowej strategii wykonywania testów w pipeline CI/CD wymaga starannego planowania i ciągłego
doskonalenia. Kluczowym wskaźnikiem sukcesu jest zrównoważenie szybkości dostarczania informacji zwrotnej z
kompleksowością weryfikacji, przy jednoczesnej optymalizacji wykorzystania zasobów i minimalizacji kosztów utrzymania
infrastruktury testowej.

## 6.3. Raportowanie wyników

Efektywne raportowanie wyników testów automatycznych stanowi kluczowy element procesu CI/CD, umożliwiający szybką
identyfikację problemów, analizę trendów jakościowych oraz podejmowanie świadomych decyzji dotyczących wdrożeń. System
raportowania powinien dostarczać przejrzystych, użytecznych informacji wszystkim interesariuszom, od deweloperów po
zarząd, dostosowując zakres i formę prezentacji do specyficznych potrzeb każdej grupy odbiorców.

### Wielopoziomowe raportowanie wyników

Kompleksowy system raportowania powinien obejmować kilka poziomów szczegółowości:

- **Raportowanie na poziomie pojedynczego testu**:
    - Szczegółowy log wykonania z krokami testowymi
    - Przechwycone zrzuty ekranu dla testów UI (przed/po akcji, w momencie błędu)
    - Zapisy ruchu sieciowego (pliki HAR, logi API)
    - Stack trace błędów z kontekstem
    - Metryki wydajnościowe (czas wykonania, zużycie zasobów)

- **Raportowanie na poziomie zestawu testów (test suite)**:
    - Podsumowanie wykonania (liczba testów: udanych, nieudanych, pominiętych)
    - Trendy stabilności w czasie
    - Analiza przyczyn niepowodzeń (klasyfikacja błędów)
    - Metryki pokrycia (funkcjonalnego, kodu)
    - Czas wykonania z identyfikacją "wąskich gardeł"

- **Raportowanie na poziomie pipeline**:
    - Status całego pipeline z podziałem na etapy
    - Kluczowe metryki jakościowe (odsetek udanych testów, stabilność)
    - Porównanie z poprzednimi wykonaniami
    - Podkreślenie nowych/powtarzających się błędów

- **Raportowanie na poziomie projektu/organizacji**:
    - Trendy jakościowe w czasie
    - Benchmarki między zespołami/projektami
    - Analiza ROI z automatyzacji testów
    - Identyfikacja obszarów najwyższego ryzyka

### Narzędzia i technologie raportowania

#### Podstawowe narzędzia raportowania

Wybór odpowiednich narzędzi raportowania jest kluczowy dla efektywnej komunikacji wyników:

- **Allure Framework** - kompleksowe narzędzie do generowania raportów:
    - Wizualizacja kroków testowych z załącznikami (zrzuty ekranu, logi)
    - Kategoryzacja błędów i analiza trendów
    - Interaktywne dashboardy z filtrowaniem
    - Integracja z popularnymi frameworkami testowymi (JUnit, TestNG)


```java
@Test
@DisplayName("Weryfikacja procesu płatności kartą")
@Severity(SeverityLevel.CRITICAL)
@Feature("Płatności")
@Story("Płatność kartą kredytową")
public void testPaymentProcessing() {
    AllureLifecycle lifecycle = Allure.getLifecycle();
    
    lifecycle.updateStep(step -> step.setName("Wybierz produkt"));
    productPage.selectProduct("Premium Plan");
    
    lifecycle.updateStep(step -> step.setName("Przejdź do koszyka"));
    productPage.proceedToCheckout();
    
    // Załącznik z przechwyconym żądaniem API
    Allure.addAttachment("Payment API Request", "application/json", paymentRequestJson);
    
    // Dodanie zrzutu ekranu
    Allure.addAttachment("Ekran potwierdzenia", new ByteArrayInputStream(
        ((TakesScreenshot) driver).getScreenshotAs(OutputType.BYTES)));
}

```

- **Extent Reports** - elastyczna biblioteka do tworzenia raportów HTML:
    - Konfigurowalne dashboardy i wykresy
    - Kategoryzacja testów i filtrowanie wyników
    - Systemie etykiet i tagów
    - Integracja multimedialna (zrzuty ekranu, wideo, logi)

- **TestNG Reports / JUnit Reports** - natywne raportowanie w frameworkach testowych:
    - Podstawowe podsumowania wykonania testów
    - Integracja z narzędziami CI/CD (Jenkins, GitLab CI)
    - Możliwość eksportu wyników w formacie XML/HTML

#### Zaawansowane platformy raportowania

Dla kompleksowych potrzeb raportowania warto rozważyć dedykowane platformy:

- **Xray for Jira** - integracja raportowania z systemem zarządzania projektami:
    - Łączenie wyników testów z wymaganiami i historiami użytkownika
    - Śledzenie pokrycia wymagań testami
    - Zarządzanie cyklami testowymi
    - Generowanie raportów dla interesariuszy biznesowych

- **Dashboardy Grafana/Kibana** - wizualizacja metryk i trendów:
    - Agregacja danych z różnych źródeł
    - Tworzenie customizowanych dashboardów
    - Alerty oparte na progach
    - Analiza historyczna i prognozowanie

### Automatyzacja raportowania w pipeline CI/CD

Proces raportowania powinien być w pełni zautomatyzowany jako część pipeline:

- **Generowanie raportów jako krok pipeline**:
    - Automatyczne zbieranie wyników testów z różnych etapów
    - Konsolidacja raportów z różnych typów testów (jednostkowe, integracyjne, UI)
    - Archiwizacja artefaktów (logi, zrzuty ekranu) jako załączników do raportów


```groovy
# Przykład konfiguracji Jenkins Pipeline dla generowania raportów
stage('Generate Reports') {
   steps {
      script {
         // Wykonanie testów
         sh './gradlew clean test'

         // Generowanie raportu Allure
         allure([
         includeProperties: false,
         jdk: '',
         properties: [ ],
         reportBuildPolicy: 'ALWAYS',
         results: [ [ path: 'target/allure-results' ] ]
         ])

        // Publikacja raportów JUnit
        junit 'target/surefire-reports/*.xml'

        // Publikacja raportów pokrycia kodu
        jacoco()
      }
   }
}

```

- **Powiadomienia i dystrybucja raportów**:
    - Automatyczne powiadomienia email dla zespołu w przypadku błędów
    - Integracja z komunikatorami
    - Automatyczna publikacja raportów na portalach wewnętrznych

### Strategie dla różnych odbiorców

Efektywne raportowanie powinno być dostosowane do potrzeb różnych grup odbiorców:

- **Dla deweloperów i testerów automatyzujących**:
    - Szczegółowe informacje techniczne (stack trace, logi)
    - Szybki dostęp do konkretnych przypadków testowych
    - Integracja z IDE i systemami kontroli wersji
    - Łatwa reprodukcja błędów

- **Dla kierowników projektów/Scrum Masterów**:
    - Podsumowania statusu na poziomie sprintów/wydań
    - Trendy jakościowe w czasie
    - Identyfikacja ryzyk i "wąskich gardeł"
    - KPI związane z jakością (stabilność testów, czas wykrywania błędów)

- **Dla interesariuszy biznesowych**:
    - Wysokopoziomowe dashboardy z kluczowymi metrykami
    - Raportowanie oparte na wymaganiach biznesowych
    - Wizualizacja postępu i ryzyk
    - ROI z automatyzacji testów

### Integracja z systemami zarządzania defektami

Skuteczne raportowanie powinno być zintegrowane z systemami zarządzania defektami:

- **Automatyczne tworzenie zgłoszeń**:
    - Generowanie zgłoszeń w Jira dla nowych błędów
    - Przypisywanie zgłoszeń do właściwych osób na podstawie analizy kodu
    - Dołączanie kontekstu testowego (logi, zrzuty ekranu)

- **Śledzenie cyklu życia defektów**:
    - Aktualizacja statusu defektów
    - Weryfikacja rozwiązania poprzez ponowne uruchomienie testów
    - Agregacja statystyk związanych z defektami

- **Automatyczna weryfikacja poprawek**:
    - Automatyczne uruchamianie testów związanych z poprawkami
    - Weryfikacja regresji związanej z wprowadzonymi zmianami
    - Generowanie raportów walidacyjnych po naprawie

### Pomiar efektywności i optymalizacja raportowania

Proces raportowania powinien podlegać ciągłej optymalizacji:

- **Metryki efektywności raportowania**:
    - Czas identyfikacji problemów przez zespół
    - Odsetek błędów poprawnie sklasyfikowanych automatycznie
    - Stopień wykorzystania raportów przez różne grupy odbiorców

- **Ciągłe doskonalenie**:
    - Regularne przeglądy i aktualizacje szablonów raportowania
    - Zbieranie opinii od użytkowników raportów
    - Wdrażanie nowych technologii i metodologii raportowania

Efektywne raportowanie jest nieodłącznym elementem dojrzałego procesu automatyzacji testów, umożliwiającym
maksymalizację wartości uzyskiwanej z automatyzacji oraz podejmowanie świadomych decyzji dotyczących jakości
oprogramowania na każdym etapie procesu wytwórczego.

## 6.4. Bramki jakościowe

Bramki jakościowe (quality gates) stanowią kluczowy element procesu CI/CD, definiując mierzalne kryteria, które muszą
zostać spełnione, aby oprogramowanie mogło przejść do kolejnego etapu pipeline. Właściwie skonfigurowane bramki
jakościowe zapewniają, że tylko kod spełniający określone standardy jakości jest wdrażany na środowiska testowe i
produkcyjne, minimalizując ryzyko wprowadzania defektów i problemów wydajnościowych.

### Koncepcja i znaczenie bramek jakościowych

Bramki jakościowe pełnią rolę punktów kontrolnych w procesie CI/CD, gdzie automatycznie weryfikowane są określone
metryki i kryteria jakościowe. Ich główne cele to:

- Zapewnienie minimalnego akceptowalnego poziomu jakości na każdym etapie
- Wczesne wykrywanie problemów i zapobieganie ich propagacji
- Obiektywizacja decyzji o gotowości oprogramowania do wdrożenia
- Wymuszanie przestrzegania standardów i praktyk jakościowych
- Budowanie kultury jakości w organizacji

Bramki jakościowe powinny być:

- **Mierzalne** - oparte na konkretnych, liczbowych wskaźnikach
- **Automatyczne** - weryfikowane bez interwencji manualnej
- **Powtarzalne** - dające te same wyniki przy tych samych warunkach
- **Istotne biznesowo** - powiązane z realnymi ryzykami i potrzebami biznesowymi
- **Ewoluujące** - dostosowywane do rosnącej dojrzałości procesu

### Typy bramek jakościowych

#### Bramki oparte na wynikach testów

Najbardziej podstawowym typem bramek jakościowych są te oparte na wynikach testów automatycznych:

- **Wskaźnik sukcesu testów** (test pass rate):
    - Ogólny wskaźnik testów zakończonych sukcesem (np. minimum 95%)
    - Zróżnicowane progi dla różnych typów testów (np. 100% dla testów krytycznych, 90% dla pozostałych)
    - Progresywne progi w zależności od etapu projektu (niższe na początku, wyższe w miarę dojrzewania)

- **Stabilność testów**:
    - Maksymalny dopuszczalny odsetek niestabilnych testów (np. < 5%)
    - Trend stabilności w czasie (brak pogorszenia względem poprzednich wykonań)
    - Maksymalna liczba kolejnych nieudanych wykonań dla tego samego testu


```groovy
# Przykład definicji bramki jakościowej w Jenkins
stage('Quality Gate: Test Results') {
  steps {
    script {
      def testResults = readJSON file: 'target/test-results-summary.json'
      
      // Weryfikacja ogólnego wskaźnika sukcesu
      if (testResults.passRate < 95) {
        error "Test pass rate below threshold: ${testResults.passRate}% < 95%"
      }
      
      // Weryfikacja wskaźnika sukcesu dla testów krytycznych
      if (testResults.criticalTestsPassRate < 100) {
        error "Critical tests pass rate below threshold: ${testResults.criticalTestsPassRate}% < 100%"
      }
      
      // Weryfikacja stabilności testów
      if (testResults.flakyTestsRate > 5) {
        error "Too many flaky tests: ${testResults.flakyTestsRate}% > 5%"
      }
    }
  }
}

```

#### Bramki oparte na pokryciu kodu

Pokrycie kodu testami jest istotnym wskaźnikiem jakości zestawu testów:

- **Ogólne pokrycie kodu**:
    - Minimalny procent pokrycia linii kodu (np. 80%)
    - Minimalny procent pokrycia gałęzi (np. 70%)
    - Minimalny procent pokrycia ścieżek

- **Pokrycie dla kodu krytycznego**:
    - Wyższe progi dla modułów krytycznych biznesowo (np. 90-95%)
    - Specjalne wymagania dla kodu odpowiedzialnego za bezpieczeństwo i integralność danych
    - Śledzenie trendów pokrycia w czasie (zakaz regresji)

- **Różnicowe pokrycie kodu** (differential coverage):
    - Wymagane 100% pokrycie dla nowo dodanego lub zmodyfikowanego kodu
    - Automatyczna identyfikacja zmian niepokrytych testami
    - Blokowanie merga zmian bez odpowiedniego pokrycia


```xml
// Przykład konfiguracji JaCoCo w Maven do weryfikacji pokrycia
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.8</version>
    <executions>
        <execution>
            <id>jacoco-check</id>
            <goals>
                <goal>check</goal>
            </goals>
            <configuration>
                <rules>
                    <rule>
                        <element>BUNDLE</element>
                        <limits>
                            <limit>
                                <counter>LINE</counter>
                                <value>COVEREDRATIO</value>
                                <minimum>0.80</minimum>
                            </limit>
                            <limit>
                                <counter>BRANCH</counter>
                                <value>COVEREDRATIO</value>
                                <minimum>0.70</minimum>
                            </limit>
                        </limits>
                    </rule>
                    <!-- Wyższe pokrycie dla krytycznych pakietów -->
                    <rule>
                        <element>PACKAGE</element>
                        <includes>
                            <include>com.company.app.security.*</include>
                            <include>com.company.app.payment.*</include>
                        </includes>
                        <limits>
                            <limit>
                                <counter>LINE</counter>
                                <value>COVEREDRATIO</value>
                                <minimum>0.90</minimum>
                            </limit>
                        </limits>
                    </rule>
                </rules>
            </configuration>
        </execution>
    </executions>
</plugin>

```

#### Bramki oparte na jakości kodu

Statyczna analiza kodu dostarcza cennych wskaźników dotyczących jakości i utrzymywalności:

- **Metryki jakości kodu**:
    - Złożoność cyklomatyczna (np. maksimum 10 per metoda)
    - Dublowanie kodu (np. < 5%)
    - Długość metod i klas (np. maksimum 30 linii per metoda)
    - Liczba parametrów metod (np. maksimum 5)

- **Zgodność ze standardami kodowania**:
    - Zero błędów krytycznych
    - Ograniczona liczba błędów o wysokim priorytecie (np. < 10)
    - Trend w liczbie problemów (zakaz wzrostu)

- **Dług techniczny**:
    - Maksymalny akceptowalny poziom długu technicznego
    - Maksymalny przyrost długu technicznego w jednej zmianie
    - Współczynnik spłaty długu technicznego


```groovy
# Przykład definicji bramki jakościowej opartej na SonarQube
stage('Quality Gate: Code Quality') {
  steps {
    script {
      withSonarQubeEnv('SonarQube') {
        sh './mvnw sonar:sonar'
      }
      
      timeout(time: 10, unit: 'MINUTES') {
        def qg = waitForQualityGate()
        if (qg.status != 'OK') {
          error "SonarQube Quality Gate failed: ${qg.status}"
        }
      }
    }
  }
}

```

#### Bramki oparte na wydajności

Dla aplikacji z wymaganiami wydajnościowymi kluczowe są bramki oparte na metrykach wydajnościowych:

- **Czasy odpowiedzi**:
    - Maksymalny czas odpowiedzi dla krytycznych funkcji (np. < 1s dla 95 percentyla)
    - Średni czas odpowiedzi dla wszystkich operacji (np. < 500ms)
    - Maksymalny spadek wydajności względem poprzedniej wersji (np. < 10%)

- **Przepustowość**:
    - Minimalna obsługiwana liczba transakcji na sekundę
    - Minimalna liczba równoczesnych użytkowników
    - Stabilność pod obciążeniem (brak błędów przy zwiększonym ruchu)

- **Wykorzystanie zasobów**:
    - Maksymalne zużycie pamięci
    - Maksymalne wykorzystanie CPU
    - Maksymalna liczba zapytań do bazy danych per transakcja


```java
// Przykład definicji bramki wydajnościowej w JMeter z wykorzystaniem Assert
<jp:JSR223Assertion guiclass="TestBeanGUI" testclass="JSR223Assertion" testname="Performance Quality Gate" enabled="true">
  <stringProp name="scriptLanguage">groovy</stringProp>
  <stringProp name="parameters"></stringProp>
  <stringProp name="filename"></stringProp>
  <stringProp name="cacheKey">true</stringProp>
  <stringProp name="script">
    def response = prev.getResponseDataAsString();
    def responseTime = prev.getTime();
    def maxAllowedTime = 1000; // 1 second
    
    if (responseTime > maxAllowedTime) {
        AssertionResult.setFailure(true);
        AssertionResult.setFailureMessage("Response time exceeded threshold: " + responseTime + "ms > " + maxAllowedTime + "ms");
    }
    
    // Weryfikacja trendu wydajności
    def previousResults = props.get("previousResponseTime");
    if (previousResults != null) {
        def previousTime = previousResults.toInteger();
        def degradation = ((responseTime - previousTime) / previousTime) * 100;
        def maxDegradation = 10; // 10%
        
        if (degradation > maxDegradation) {
            AssertionResult.setFailure(true);
            AssertionResult.setFailureMessage("Performance degradation exceeded threshold: " + degradation.round(2) + "% > " + maxDegradation + "%");
        }
    }
  </stringProp>
</jp:JSR223Assertion>

```

#### Bramki oparte na bezpieczeństwie

W dobie rosnących zagrożeń cyberbezpieczeństwa, bramki bezpieczeństwa stają się niezbędne:

- **Wyniki skanów bezpieczeństwa**:
    - Zero podatności krytycznych i wysokich
    - Ograniczona liczba podatności średnich (np. < 5)
    - Brak znanych exploitów dla wykrytych podatności

- **Bezpieczeństwo komponentów**:
    - Brak przestarzałych bibliotek z znanymi podatnościami
    - Weryfikacja licencji używanych bibliotek
    - Skanowanie kontenerów pod kątem podatności

- **Zgodność z zasadami bezpieczeństwa**:
    - Spełnienie wymagań OWASP Top 10
    - Zgodność z regulacjami branżowymi (PCI DSS, HIPAA itp.)
    - Brak wrażliwych danych w kodzie (hasła, klucze API)


```yaml
# Przykład definicji bramki bezpieczeństwa w GitLab CI
security_gate:
  stage: test
  script:
    - ./run-security-scan.sh
    - |
      CRITICAL_VULNS=$(cat security-report.json | jq '.vulnerabilities | map(select(.severity == "Critical")) | length')
      HIGH_VULNS=$(cat security-report.json | jq '.vulnerabilities | map(select(.severity == "High")) | length')

      if [ $CRITICAL_VULNS -gt 0 ]; then
        echo "Security gate failed: $CRITICAL_VULNS critical vulnerabilities found"
        exit 1
      fi

      if [ $HIGH_VULNS -gt 0 ]; then
        echo "Security gate failed: $HIGH_VULNS high vulnerabilities found"
        exit 1
      fi
  artifacts:
    paths:
      - security-report.json

```

### Implementacja bramek jakościowych w pipeline

#### Strategiczne rozmieszczenie bramek

Bramki jakościowe powinny być strategicznie rozmieszczone w pipeline, aby zapewnić wczesne wykrywanie problemów:

- **Bramki deweloperskie** (commit stage):
    - Podstawowe testy jednostkowe
    - Statyczna analiza kodu
    - Weryfikacja stylu kodowania

- **Bramki przed integracją** (merge stage):
    - Rozszerzone testy jednostkowe i integracyjne
    - Weryfikacja pokrycia kodu
    - Skanowanie bezpieczeństwa kodu

- **Bramki przed wdrożeniem na staging** (release stage):
    - Pełne testy funkcjonalne
    - Testy wydajnościowe
    - Kompleksowe skanowanie bezpieczeństwa

- **Bramki przed wdrożeniem na produkcję** (deployment stage):
    - Weryfikacja krytycznych scenariuszy biznesowych
    - Testy akceptacyjne
    - Weryfikacja zgodności ze standardami i regulacjami

#### Zarządzanie wyjątkami i eskalacjami

Nawet najlepiej zaprojektowane bramki jakościowe mogą wymagać wyjątków w określonych sytuacjach:

- **Proces zatwierdzania wyjątków**:
    - Jasno zdefiniowane kryteria dopuszczalności wyjątków
    - Proces formalnej aprobaty przez właściwe osoby
    - Czasowe ograniczenie wyjątków z planem naprawczym
    - Audyt i monitorowanie wyjątków

- **Mechanizmy eskalacji**:
    - Automatyczne powiadomienia dla odpowiednich osób
    - Definiowanie ścieżek eskalacyjnych dla różnych typów bramek
    - Mechanizmy priorytetyzacji problemów


```java
// Przykład implementacji mechanizmu wyjątków w Jenkins Pipeline
stage('Quality Gate: Test Results') {
  steps {
    script {
      def testResults = readJSON file: 'target/test-results-summary.json'
      
      // Weryfikacja wskaźnika sukcesu
      if (testResults.passRate < 95) {
        // Sprawdzenie, czy istnieje zatwierdzony wyjątek
        def exceptions = readJSON file: 'quality-gate-exceptions.json'
        def hasValidException = exceptions.find { 
          it.type == 'test-pass-rate' && 
          it.value <= testResults.passRate && 
          it.expiryDate > currentDate
        }
        
        if (hasValidException) {
          echo "WARNING: Quality gate bypassed due to approved exception: ${hasValidException.reason}"
          echo "Exception expires on ${hasValidException.expiryDate}, approved by: ${hasValidException.approver}"
        } else {
          error "Test pass rate below threshold: ${testResults.passRate}% < 95%"
        }
      }
    }
  }
}

```

### Ewolucja bramek jakościowych

Bramki jakościowe nie powinny być statyczne, lecz ewoluować wraz z rozwojem organizacji i projektu:

- **Progresywne zaostrzanie kryteriów**:
    - Rozpoczęcie od podstawowych, łatwych do spełnienia progów
    - Stopniowe zaostrzanie wymagań w miarę dojrzewania procesu
    - Regularne przeglądy i aktualizacje progów

- **Adaptacja do specyfiki projektu**:
    - Dostosowanie bramek do charakterystyki technologicznej projektu
    - Uwzględnienie specyficznych ryzyk biznesowych
    - Balansowanie rygorystyczności bramek z potrzebą szybkiego dostarczania

- **Mierzenie skuteczności**:
    - Analiza korelacji między bramkami a defektami produkcyjnymi
    - Optymalizacja bramek na podstawie empirycznych danych
    - Eliminacja nieefektywnych bramek

### Kultura jakości i bramki jakościowe

Bramki jakościowe powinny wspierać budowanie kultury jakości w organizacji:

- **Transparentność i widoczność**:
    - Jasna komunikacja celów i znaczenia bramek jakościowych
    - Widoczne dashboardy pokazujące status bramek
    - Regularne przeglądy wyników i trendów

- **Odpowiedzialność zespołowa**:
    - Współodpowiedzialność całego zespołu za przechodzenie przez bramki
    - Angażowanie deweloperów w definiowanie i ewolucję bramek
    - Promowanie praktyk shift-left (wczesne wykrywanie problemów)

- **Ciągłe doskonalenie**:
    - Regularne retrospektywy dotyczące procesu jakościowego
    - Analiza przyczyn źródłowych naruszeń bramek
    - Wdrażanie usprawnień na podstawie zebranych doświadczeń

Efektywne bramki jakościowe stanowią kluczowy element dojrzałego procesu CI/CD, zapewniając obiektywne kryteria oceny
gotowości oprogramowania do wdrożenia oraz wspierając budowanie kultury odpowiedzialności za jakość w całej organizacji.
Odpowiednio zaimplementowane, nie tylko minimalizują ryzyko wdrażania wadliwego oprogramowania, ale także przyczyniają
się do zwiększenia efektywności całego procesu wytwarzania poprzez wczesne wykrywanie i naprawianie problemów.

# 7. Dane testowe

## 7.1. Strategie zarządzania danymi testowymi

Efektywne zarządzanie danymi testowymi stanowi fundament wiarygodnych i powtarzalnych testów automatycznych. Zgodnie z
zasadami ISTQB, dane testowe powinny zapewniać odpowiednie pokrycie wymagań funkcjonalnych i niefunkcjonalnych, a
jednocześnie być łatwe w utrzymaniu i aktualizacji. W praktyce oznacza to opracowanie spójnej strategii, która odpowiada
na specyficzne potrzeby projektu oraz wykorzystywane narzędzia (Java, Selenium, Selenide, RestAssured).

Jednym z kluczowych podejść jest wdrożenie czterowarstwowej strategii zarządzania danymi testowymi, która pozwala na
elastyczne dostosowanie się do różnych scenariuszy testowych:

1. **Dane statyczne wbudowane w kod** - Najprostsze podejście, odpowiednie dla małych, niezmiennych zbiorów danych. W
   Javie implementujemy je jako stałe (np. `public static final`) lub umieszczamy w plikach zasobów (resources). Dla
   testów z wykorzystaniem Selenium/Selenide, mogą to być selektory CSS/XPath, natomiast w przypadku RestAssured -
   podstawowe parametry zapytań HTTP.

2. **Zewnętrzne pliki danych** - Rozdzielenie danych od kodu testowego. Najczęściej wykorzystujemy formaty takie jak
   CSV, JSON, XML czy YAML, które są łatwe w utrzymaniu i mogą być modyfikowane przez osoby nietechniczne. W Javie
   odczytujemy je za pomocą bibliotek takich jak Jackson (JSON), JAXB (XML) czy SnakeYAML. Zastosowanie wzorca Page
   Object Model w połączeniu z zewnętrznymi danymi znacząco zwiększa czytelność testów.

3. **Bazy danych testowych** - Dla złożonych systemów wykorzystujemy dedykowane bazy danych testowych, które są
   replikami lub uproszczonymi wersjami baz produkcyjnych. Podejście to pozwala na testowanie skomplikowanych
   scenariuszy, ale wymaga odpowiedniego zarządzania stanem bazy. W Javie wykorzystujemy JDBC, JPA lub specjalizowane
   narzędzia jak Flyway czy Liquibase do kontroli stanu bazy.

4. **Dane generowane w locie** - Tworzenie danych testowych w trakcie wykonywania testów. Podejście szczególnie
   przydatne w testach API z wykorzystaniem RestAssured, gdzie możemy dynamicznie generować payloady zapytań w oparciu o
   bieżący kontekst testu.

Kluczowym aspektem strategii zarządzania danymi jest podejście do **kontroli wersji danych testowych**. Zgodnie z
dobrymi praktykami, dane testowe powinny być wersjonowane razem z kodem testów, co zapewnia spójność i powtarzalność
wykonania. W praktyce oznacza to przechowywanie plików z danymi w tym samym repozytorium co kod testów lub wykorzystanie
dedykowanych repozytoriów z odpowiednim powiązaniem wersji.

Istotnym elementem strategii jest też **zarządzanie danymi wrażliwymi**. Zgodnie z zasadami ISTQB, dane produkcyjne
zawierające informacje osobowe nie powinny być używane w środowiskach testowych bez odpowiedniej anonimizacji. W
praktyce implementujemy to poprzez:

- Maskowanie danych (np. zastępowanie prawdziwych nazwisk losowymi ciągami znaków)
- Pseudonimizację (zastępowanie rzeczywistych danych realistycznymi, ale fikcyjnymi)
- Tokenizację (zamiana wrażliwych danych na tokeny bez znaczenia biznesowego)

Efektywna strategia musi również uwzględniać **zarządzanie stanem danych**. W testach z wykorzystaniem Selenium/Selenide
często musimy zapewnić, że system znajduje się w określonym stanie przed wykonaniem testu. Realizujemy to poprzez:

- Tworzenie prekondycji za pomocą API (szybsze niż przez UI)
- Wykorzystanie zrzutów bazy danych dla określonych stanów aplikacji
- Bezpośrednie manipulowanie bazą danych przed rozpoczęciem testu

Nieodzownym elementem strategii zarządzania danymi testowymi jest **monitoring i konserwacja**. Dane testowe z czasem
stają się nieaktualne lub niekompletne. Regularne przeglądy i aktualizacje zbioru danych testowych są kluczowe dla
utrzymania efektywności testów. W praktyce implementujemy to poprzez:

- Automatyczne audyty pokrycia danych testowych
- Synchronizację struktury danych testowych ze zmianami w systemie
- Cykliczne odświeżanie danych testowych w oparciu o (zanonimizowane) dane produkcyjne

Wybór odpowiedniej strategii zarządzania danymi testowymi powinien być oparty na analizie czynników takich jak złożoność
systemu, częstotliwość zmian w danych, wymagania dotyczące wydajności testów oraz dostępne zasoby. Dobrze zaprojektowana
strategia znacząco przyczynia się do zwiększenia efektywności procesu testowego, redukcji kosztów utrzymania oraz
poprawy jakości testów automatycznych.

## 7.2. Generowanie danych testowych

Generowanie danych testowych to kluczowy element efektywnej automatyzacji testów, który bezpośrednio wpływa na jakość i
wiarygodność wyników. Zgodnie z wytycznymi ISTQB, dane testowe powinny odzwierciedlać rzeczywiste scenariusze użycia, a
jednocześnie pokrywać przypadki brzegowe i wyjątkowe. W kontekście automatyzacji z wykorzystaniem Javy,
Selenium/Selenide i RestAssured, mamy do dyspozycji szereg metod i narzędzi usprawniających ten proces.

**Biblioteki do generowania danych testowych w Javie** stanowią podstawowe narzędzie każdego testera automatyzującego.
Najpopularniejsze z nich to:

1. **Java Faker** - biblioteka umożliwiająca generowanie realistycznych, losowych danych dla różnych kategorii (dane
   osobowe, adresy, numery telefonów). Szczególnie przydatna w testach formularzy z wykorzystaniem Selenium/Selenide.
   
```java
   Faker faker = new Faker(new Locale("pl"));
   String name = faker.name().fullName();
   String email = faker.internet().emailAddress();
   
```

2. **JUnit Params / TestNG DataProvider** - mechanizmy parametryzacji testów, które umożliwiają łatwe dostarczanie
   różnych zestawów danych do tych samych metod testowych.
   
```java
   @ParameterizedTest
   @CsvSource({"jan.kowalski@example.com, JanKowalski123", "anna.nowak@example.com, Anna!2023"})
   void testLogin(String username, String password) {
       loginPage.login(username, password);
       assertThat(homePage.isDisplayed()).isTrue();
   }
   
```

3. **Apache Commons Lang** - zawiera narzędzia do generowania losowych ciągów znaków, liczb i innych podstawowych typów
   danych.

4. **RandomizedTesting** - rozszerzenie dla JUnit, które wprowadza deterministyczne, ale losowe dane do testów.

5. **jOOR** - biblioteka do refleksji, pomocna przy generowaniu kompletnych obiektów testowych.

**Techniki generowania danych testowych** można podzielić na kilka głównych kategorii:

1. **Generowanie przypadków brzegowych** - automatyczne tworzenie wartości na granicach dozwolonych zakresów, co jest
   kluczowe dla testowania walidacji. Dla interfejsów REST testowanych przy użyciu RestAssured, oznacza to generowanie
   payloadów z wartościami na granicach dozwolonych zakresów.
   
```java
   // Testowanie walidacji długości pola
   String exactlyMaxLength = RandomStringUtils.random(255);
   String tooLongString = RandomStringUtils.random(256);
   
```

2. **Generowanie danych strukturalnych** - tworzenie złożonych struktur danych odpowiadających modelowi domenowemu
   aplikacji. W przypadku testów REST API z wykorzystaniem RestAssured, często generujemy całe drzewa obiektów JSON.
   
```java
   User user = User.builder()
       .firstName(faker.name().firstName())
       .lastName(faker.name().lastName())
       .address(Address.builder()
           .street(faker.address().streetAddress())
           .city(faker.address().city())
           .zipCode(faker.address().zipCode())
           .build())
       .build();
   
```

3. **Generowanie danych warunkowych** - tworzenie danych, które spełniają określone warunki biznesowe lub zależności.
   
```java
   // Generowanie wieku odpowiedniego dla emeryta
   int retirementAge = faker.number().numberBetween(65, 100);
   
```

4. **Generowanie danych zależnych od czasu** - tworzenie danych uwzględniających aspekty czasowe, co jest szczególnie
   istotne w systemach z logiką biznesową opartą na datach.
   
```java
   // Data urodzenia osoby pełnoletniej
   LocalDate adultBirthDate = LocalDate.now().minusYears(
       faker.number().numberBetween(18, 90));
   
```

**Projektowanie generatorów danych testowych** zgodnie z dobrymi praktykami wymaga:

1. **Enkapsulacji logiki generowania** - tworzenie dedykowanych fabryk danych, które ukrywają szczegóły implementacyjne
   i oferują czytelny interfejs.
   
```java
   public class UserTestDataFactory {
       public static User createValidUser() { /* ... */ }
       public static User createUserWithInvalidEmail() { /* ... */ }
   }
   
```

2. **Separacji mechanizmu generowania od logiki testowej** - zgodnie z zasadą SRP (Single Responsibility Principle), kod
   odpowiedzialny za generowanie danych powinien być oddzielony od kodu testowego.

3. **Powtarzalności** - zapewnienie, że przy tych samych parametrach wejściowych generator zawsze produkuje te same
   dane, co jest kluczowe dla debugowania testów.
   
```java
   // Używanie ziarna (seed) dla powtarzalnych wyników
   Random random = new Random(42);
   
```

4. **Elastyczności** - możliwość łatwego dostosowania generatorów do zmieniających się wymagań i struktur danych.
   
```java
   public User createUser(UserTemplate template) {
       User user = createBaseUser();
       if (template.hasCustomEmail()) {
           user.setEmail(template.getEmail());
       }
       return user;
   }
   
```

**Integracja z zewnętrznymi źródłami danych** może znacząco zwiększyć realizm i pokrycie testów:

1. **API do generowania danych** - wykorzystanie zewnętrznych usług dostarczających realistyczne dane (np. Random User
   API).

2. **Zanonimizowane dane produkcyjne** - wykorzystanie rzeczywistych, ale zanonimizowanych danych z systemów
   produkcyjnych.

3. **Crowdsourcing danych testowych** - wykorzystanie platform typu Mechanical Turk do pozyskiwania danych testowych od
   rzeczywistych użytkowników.

Efektywne generowanie danych testowych nie tylko zwiększa pokrycie testowe, ale także przyspiesza proces tworzenia
testów i zmniejsza ryzyko przeoczenia istotnych scenariuszy. W kontekście narzędzi takich jak Selenium/Selenide czy
RestAssured, dobrze zaprojektowane generatory danych testowych stanowią niezbędny element infrastruktury testowej.

## 7.3. Izolacja danych między testami

Izolacja danych testowych to fundamentalny aspekt tworzenia niezawodnych i powtarzalnych testów automatycznych. Zgodnie
z zasadami ISTQB, każdy test powinien być niezależny od innych i wykonywać się w przewidywalnym środowisku. W praktyce
oznacza to, że dane używane lub modyfikowane przez jeden test nie powinny wpływać na wykonanie innych testów.
Implementacja tej zasady w środowisku Java z wykorzystaniem narzędzi takich jak Selenium, Selenide i RestAssured wymaga
zastosowania odpowiednich technik i wzorców.

**Główne problemy związane z brakiem izolacji danych** to:

1. **Testy zależne od kolejności wykonania** - gdy jeden test tworzy dane, które są następnie używane przez inny test,
   co prowadzi do niestabilności i trudności w debugowaniu.

2. **Efekty uboczne** - gdy jeden test modyfikuje dane w sposób, który wpływa na inne testy, powodując nieprzewidywalne
   wyniki.

3. **Wyścigi (race conditions)** - gdy testy wykonywane równolegle konkurują o te same dane, co może prowadzić do
   nieprzewidywalnych wyników i fałszywych błędów.

**Techniki izolacji danych w testach** można podzielić na kilka głównych kategorii:

1. **Izolacja na poziomie środowiska** - zapewnienie każdemu testowi lub zestawowi testów dedykowanego środowiska.
   

```java
   @BeforeEach
   void setupTestDatabase() {
       databaseManager.createTemporarySchema();
       databaseManager.applyMigrations();
   }
   
   @AfterEach
   void cleanupTestDatabase() {
       databaseManager.dropTemporarySchema();
   }
   
```

2. **Izolacja na poziomie transakcji** - wykorzystanie transakcji bazodanowych do izolowania zmian wprowadzanych przez
   testy.
   
```java
   @Test
   @Transactional
   void testUserCreation() {
       // Zmiany zostaną wycofane po zakończeniu testu
       userRepository.save(new User("jan", "kowalski"));
       assertThat(userRepository.findByUsername("jan")).isPresent();
   }
   
```

3. **Izolacja przez unikalność danych** - zapewnienie, że każdy test operuje na unikalnych danych, które nie kolidują z
   danymi innych testów.
   
```java
   @Test
   void testUserRegistration() {
       String uniqueEmail = "user_" + UUID.randomUUID() + "@example.com";
       registrationPage.registerUser(uniqueEmail, "password123");
       assertThat(dashboardPage.isLoggedIn()).isTrue();
   }
   
```

4. **Izolacja przez czyszczenie danych** - systematyczne czyszczenie danych przed lub po każdym teście.
   
```java
   @AfterEach
   void cleanupCreatedUsers() {
       userRepository.deleteByEmailContaining(testIdentifier);
   }
   
```

**Wzorce projektowe wspierające izolację danych** obejmują:

1. **Test Fixture** - przygotowanie znanego, stałego środowiska dla każdego testu, co eliminuje zależności między
   testami.
   
```java
   @BeforeEach
   void setupFixture() {
       // Przygotowanie danych dla testu
       testUser = userTestDataFactory.createTestUser();
       testProduct = productTestDataFactory.createTestProduct();
       
       // Dodanie danych do systemu
       given().contentType(ContentType.JSON)
           .body(testUser)
           .when().post("/api/users")
           .then().statusCode(201);
   }
   
```

2. **Object Mother** - wzorzec dostarczający metody fabrykujące obiekty testowe o określonych właściwościach.
   
```java
   public class OrderMother {
       public static Order createPendingOrder() { /* ... */ }
       public static Order createCompletedOrder() { /* ... */ }
   }
   
```

3. **Test Data Builder** - wzorzec umożliwiający fluent API do tworzenia obiektów testowych.
   
```java
   User user = new UserBuilder()
       .withUsername("testuser_" + System.currentTimeMillis())
       .withEmail("test_" + UUID.randomUUID() + "@example.com")
       .withActivatedAccount()
       .build();
   
```

**Praktyczne strategie izolacji danych w różnych warstwach testów**:

1. **Testy UI (Selenium/Selenide)**:
    - Używanie unikalnych identyfikatorów w testach (np. dodawanie timestampów do nazw użytkowników)
    - Czyszczenie stanu aplikacji poprzez API przed uruchomieniem testu UI
    - Wykorzystanie cookies lub localStorage do izolacji sesji między testami

2. **Testy API (RestAssured)**:
    - Tworzenie unikalnych zasobów dla każdego testu
    - Wykorzystanie dedykowanych nagłówków HTTP do identyfikacji zasobów utworzonych przez testy
    - Implementacja mechanizmu śledzenia i czyszczenia zasobów po testach
   
```java
   String resourceId = given().contentType(ContentType.JSON)
       .header("X-Test-Identifier", testRunId)
       .body(newResource)
       .when().post("/api/resources")
       .then().extract().path("id");
       
   // Po teście
   given().header("X-Test-Identifier", testRunId)
       .when().delete("/api/resources/cleanup");
   
```

3. **Testy integracyjne z bazą danych**:
    - Wykorzystanie wbudowanych mechanizmów izolacji w bazach danych (np. schematy w PostgreSQL)
    - Implementacja testów z wykorzystaniem kontenerów Docker (np. Testcontainers)
    - Stosowanie migracji bazodanowych dla każdego uruchomienia testu

**Narzędzia wspierające izolację danych** w ekosystemie Java:

1. **DBUnit** - umożliwia przygotowanie danych testowych w bazie danych i przywracanie stanu początkowego.

2. **Flyway/Liquibase** - narzędzia do migracji baz danych, które można wykorzystać do przygotowania schematu i danych
   początkowych.

3. **Testcontainers** - biblioteka umożliwiająca uruchamianie kontenerów Docker na potrzeby testów, co zapewnia izolację
   na poziomie infrastruktury.
   
```java
   @Container
   static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:13")
       .withDatabaseName("testdb")
       .withUsername("test")
       .withPassword("test");
   
```

4. **Spring Test** - dla aplikacji Spring, oferuje narzędzia do izolacji testów, takie jak `@DirtiesContext` czy
   `@Transactional`.

Efektywna izolacja danych testowych wymaga starannego planowania i konsekwentnego stosowania wybranych technik. Choć
może wymagać dodatkowego nakładu pracy na etapie implementacji testów, znacząco zwiększa niezawodność i powtarzalność
testów automatycznych, co ostatecznie prowadzi do wyższej jakości oprogramowania i szybszego wykrywania defektów.

# Strategia Shift-Left w praktyce

Strategia Shift-Left to podejście, które polega na przesunięciu aktywności testowych na wcześniejsze etapy cyklu
wytwarzania oprogramowania. Zamiast koncentrować się na testowaniu pod koniec cyklu rozwoju, Shift-Left promuje
testowanie od samego początku procesu. Celem jest wcześniejsze wykrywanie defektów, co znacząco redukuje koszty naprawy
błędów i skraca czas wprowadzania produktu na rynek.

W kontekście testów automatycznych strategia Shift-Left nabiera szczególnego znaczenia. Automatyzacja testów już na
wczesnych etapach rozwoju oprogramowania pozwala na szybkie wykrywanie błędów, uzyskiwanie natychmiastowej informacji
zwrotnej i zapewnianie wysokiej jakości produktu końcowego. Implementując podejście Shift-Left, organizacje mogą tworzyć
bardziej niezawodne oprogramowanie przy jednoczesnym skróceniu cyklu wytwarzania.

Kluczowe korzyści strategii Shift-Left:

- Wcześniejsze wykrywanie defektów, gdy koszt ich naprawy jest niższy
- Skrócenie czasu wprowadzania produktu na rynek
- Zwiększenie współpracy między zespołami deweloperskimi i testowymi
- Poprawa jakości oprogramowania
- Zmniejszenie długu technicznego
- Redukcja kosztów związanych z naprawą błędów

Przejdźmy teraz do szczegółowego omówienia implementacji strategii Shift-Left w praktyce, ze szczególnym uwzględnieniem
testów automatycznych realizowanych przy użyciu Javy, Selenium, Selenide i Rest Assured.

## 11.1. Integracja testów automatycznych w procesie wytwarzania

Skuteczna integracja testów automatycznych w procesie wytwarzania oprogramowania stanowi fundament strategii Shift-Left.
Wymaga to przemyślanego podejścia, które łączy narzędzia, procesy i ludzi w spójny ekosystem.

### Wybór odpowiednich narzędzi i frameworków

W kontekście Javy, ekosystem testów automatycznych oferuje wiele dojrzałych rozwiązań. Dla testów interfejsu
użytkownika, Selenium WebDriver wraz z Selenide stanowią potężną kombinację. Selenide, jako warstwa abstrakcji nad
Selenium, upraszcza pisanie i utrzymywanie testów UI poprzez elegantny API i wbudowane mechanizmy oczekiwania na
elementy.


```java
// Przykład testu UI z wykorzystaniem Selenide
@Test
public void userCanLoginSuccessfully() {
    open("https://example.com/login");
    $(By.id("username")).setValue("testuser");
    $(By.id("password")).setValue("password");
    $(By.id("loginButton")).click();
    $(By.id("welcomeMessage")).shouldHave(text("Welcome, Test User!"));
}

```

Dla testów API, Rest Assured oferuje czytelny, fluent interfejs, który ułatwia weryfikację odpowiedzi i zachowań usług
RESTful:


```java
// Przykład testu API z wykorzystaniem Rest Assured
@Test
public void canRetrieveUserDetails() {
    given()
        .header("Authorization", "Bearer " + authToken)
    .when()
        .get("/api/users/1")
    .then()
        .statusCode(200)
        .body("name", equalTo("John Kowalski"))
        .body("email", equalTo("john.Kowalski@example.com"));
}

```

### Integracja z CI/CD

Kluczowym elementem strategii Shift-Left jest integracja testów automatycznych z CI/CD (Continuous
Integration/Continuous Delivery).
Testy powinny być uruchamiane automatycznie przy każdej zmianie kodu, dostarczając natychmiastową informację zwrotną.
Wykonywany poziom testów powinien być wykonywany przy każdym pushu (unit testy), czy pull requeście (testy integracyjne) 
a nawet akceptacyjne przy mołżiwościu deploya zmiany na środowisko tworzone ad-hoc.

### Strategia zarządzania danymi testowymi

Efektywne zarządzanie danymi testowymi jest krytyczne dla strategii Shift-Left. Testy automatyczne wymagają
przewidywalnego i kontrolowanego środowiska, aby zapewnić powtarzalność i niezawodność.

W praktyce najlepiej sprawdzają się następujące podejścia:

- Izolacja testów - każdy test powinien być niezależny i samodzielnie przygotowywać swoje dane
- Wykorzystanie baz testowych - dedykowane bazy danych dla środowisk testowych
- Test Data Builders - wzorzec projektowy ułatwiający tworzenie obiektów testowych
- Wykorzystanie rozwiązań typu "database versioning" (np. Flyway, Liquibase)

### Automatyzacja na różnych poziomach

Strategia Shift-Left wymaga automatyzacji testów na różnych poziomach:

- Testy jednostkowe
- Testy integracyjne (Testcontainers)
- Testy API (Rest Assured)
- Testy UI (Selenium, Selenide)
- Testy wydajnościowe (JMeter/Locut/k6)
- Testy bezpieczeństwa (OWASP ZAP, Burp Suite)

Kluczem jest utrzymanie właściwych proporcji między różnymi typami testów, zgodnie z Piramidą Testów.

## 11.2. Współpraca między deweloperami a testerami

Skuteczna implementacja strategii Shift-Left wymaga fundamentalnej zmiany w tradycyjnej relacji między deweloperami a
testerami. Zamiast działać jako oddzielne, często konkurujące ze sobą zespoły, deweloperzy i testerzy muszą funkcjonować
jako zintegrowana jednostka, dążąca do wspólnego celu - dostarczania wysokiej jakości oprogramowania.

### Wspólna odpowiedzialność za jakość

W podejściu Shift-Left, jakość nie jest wyłączną domeną testerów - staje się odpowiedzialnością całego zespołu.
Deweloperzy nie mogą już po prostu "przerzucać kodu przez mur" do zespołu testowego; muszą aktywnie uczestniczyć w
procesie zapewniania jakości.

Praktyczne sposoby implementacji wspólnej odpowiedzialności:

- **Testy jednostkowe pisane przez deweloperów** - Każda funkcjonalność powinna być pokryta testami jednostkowymi
  jeszcze przed przekazaniem kodu do testów wyższego poziomu.
- **Code review z uwzględnieniem testowalności** - Podczas przeglądów kodu należy zwracać uwagę na aspekty związane z
  testowalnością, takie jak modularność, rozdzielenie zależności czy odpowiednie abstrakcje.
- **Pair programming deweloper-tester** - Wspólne sesje programowania, podczas których deweloper i tester razem pracują
  nad kodem i testami, prowadzą do lepszego zrozumienia perspektyw obu stron.

### Transfer wiedzy i budowanie kompetencji

Skuteczna współpraca wymaga wzajemnego zrozumienia i szacunku dla różnych umiejętności i perspektyw. Testerzy powinni
rozumieć podstawy programowania, a deweloperzy - zasady testowania.

Efektywne mechanizmy transferu wiedzy obejmują:

- **Wewnętrzne warsztaty i szkolenia** - Regularne sesje, podczas których deweloperzy i testerzy dzielą się wiedzą i
  najlepszymi praktykami.
- **Communities of Practice** - Grupy tematyczne skupiające osoby zainteresowane konkretnymi aspektami testowania
  automatycznego.
- **Rotacja ról** - Czasowe przejmowanie obowiązków innych członków zespołu, co sprzyja lepszemu zrozumieniu ich
  perspektywy.

### Projektowanie testów z myślą o automatyzacji

W strategii Shift-Left, testy automatyczne nie są tworzone po fakcie - są projektowane równolegle z funkcjonalnościami.
Wymaga to ścisłej współpracy między deweloperami a testerami już na etapie projektowania - najlepiej w formie ATDD.


```java
// Przykład kodu zaprojektowanego z myślą o testowalności
public class UserService {
    private final UserRepository userRepository;
    private final EmailService emailService;
    
    // Wstrzykiwanie zależności zamiast tworzenia ich wewnątrz klasy
    public UserService(UserRepository userRepository, EmailService emailService) {
        this.userRepository = userRepository;
        this.emailService = emailService;
    }
    
    public User registerUser(String username, String email, String password) {
        // Walidacja wejścia
        validateRegistrationData(username, email, password);
        
        // Tworzenie użytkownika
        User user = new User(username, email, password);
        userRepository.save(user);
        
        // Wysyłanie powiadomienia
        emailService.sendWelcomeEmail(user);
        
        return user;
    }
    
    // Metoda publiczna dla ułatwienia testowania
    public void validateRegistrationData(String username, String email, String password) {
        // Implementacja walidacji
    }
}

// Odpowiadający test jednostkowy
@Test
public void shouldRegisterUserSuccessfully() {
    // Arrange
    UserRepository mockRepository = mock(UserRepository.class);
    EmailService mockEmailService = mock(EmailService.class);
    UserService userService = new UserService(mockRepository, mockEmailService);
    
    String username = "testuser";
    String email = "test@example.com";
    String password = "password123";
    
    // Act
    User result = userService.registerUser(username, email, password);
    
    // Assert
    assertThat(result).isNotNull();
    assertThat(username).isEquatlTo(result.getUsername());
    assertThat(email).isEquatlTo(result.getEmail());
    
    verify(mockRepository).save(any(User.class));
    verify(mockEmailService).sendWelcomeEmail(any(User.class));
}

```

### Wspólne narzędzia i infrastruktura

Efektywna współpraca wymaga wspólnego zestawu narzędzi i infrastruktury, które umożliwiają płynną komunikację i
integrację pracy deweloperów i testerów:

- **Wspólne systemy zarządzania kodem** - Zarówno kod produkcyjny, jak i testy powinny być przechowywane w tym samym
  repozytorium, ułatwiając jednoczesną pracę nad oboma aspektami.
- **Zintegrowane środowiska deweloperskie** - IDE z rozszerzeniami wspierającymi testowanie, takimi jak wsparcie dla
  JUnit, TestNG czy Cucumber.
- **Narzędzia komunikacji i współpracy** - Wspólne platformy do zarządzania zadaniami (Jira), komunikacji (Microsoft Teams) i dokumentacji (Confluence, Wiki).

### Metryki i ich analiza

Współpraca powinna być wspierana przez odpowiednie metryki, które pozwalają ocenić skuteczność strategii Shift-Left:

- **Pokrycie kodu testami** - Mierzy, jaka część kodu jest testowana automatycznie. 
  - Testy jednostkowe
  - Testy integracyjne w izolacji (najlepiej oparte o testy kontraktowe)
  - Testy Funkcjonalne - Functional QA - pokrycie funkcjonalności testami automatycznymi od strony API i UI
  - Testy Produktowe - pokrycie kryteriów akceptacji odbioru produktu testami UI
- **Czas naprawy defektów** - Mierzy, jak szybko wykryte defekty są naprawiane.
- **Defect Escape Rate** - Mierzy, jaki procent defektów "ucieka" do produkcji (liczba defektów zgłoszonych podczas testowania kontra liczba defektów zgłoszonych na produkcji).
- **Czas wprowadzenia na rynek** - Mierzy, jak szybko nowe funkcjonalności są dostarczane do klientów.

Wspólna analiza tych metryk pozwala zidentyfikować obszary wymagające poprawy i zoptymalizować proces współpracy między
deweloperami a testerami.

## 11.3. Testowanie w fazie analizy wymagań

Tradycyjnie testowanie rozpoczyna się po zakończeniu fazy implementacji, gdy kod jest już gotowy. Strategia Shift-Left
fundamentalnie zmienia to podejście, przesuwając aktywności testowe do najwcześniejszych etapów cyklu wytwarzania
oprogramowania - fazy analizy wymagań. Testowanie na tym etapie pomaga wcześnie identyfikować potencjalne problemy,
niejasności i luki w wymaganiach, co znacząco redukuje koszty późniejszych zmian.

### Weryfikacja jakości wymagań

Pierwszym krokiem w testowaniu wymagań jest ocena ich jakości. Wysokiej jakości wymagania powinny być:

- **Jednoznaczne** - niepozostawiające miejsca na różne interpretacje
- **Testowalne** - możliwe do zweryfikowania poprzez testy
- **Kompletne** - obejmujące wszystkie aspekty funkcjonalności
- **Spójne** - niewprowadzające sprzeczności
- **Realistyczne** - możliwe do zrealizowania w ramach ograniczeń projektu

Testerzy, dzięki swojemu doświadczeniu w znajdowaniu "dziur" w systemach, są idealnie przygotowani do oceny wymagań pod
tymi względami.

### Definiowanie kryteriów akceptacji

Kluczowym elementem testowania w fazie analizy jest definiowanie kryteriów akceptacji dla wymagań. Kryteria te stają się
podstawą do późniejszego tworzenia testów automatycznych.

Skutecznym podejściem jest wykorzystanie notacji Gherkin (Given-When-Then), która jest czytelna zarówno dla biznesu, jak
i dla zespołu technicznego:


```gherkin
Potrzeba biznesowa: Rejestracja Użytkownika
  Jako nowy klient serwisu
  Potrzebuję możliwości utworzenia własnego konta
  Aby móc korzystać z pełnej funkcjonalności platformy

  Scenariusz: Pomyślna rejestracja z poprawnymi danymi
    Zakładając, że Użytkownik chce założyć nowe konto
    Kiedy Użytkownik podaje następujące dane rejestracyjne
      | nazwa      | email                  | hasło          |
      | kowalski87 | jan.kowalski@poczta.pl | Bezpieczne123! |
    Oraz Użytkownik akceptuje warunki korzystania z serwisu
    Oraz Użytkownik zatwierdza proces rejestracji
    Wtedy System potwierdza utworzenie konta
    Oraz System wysyła wiadomość aktywacyjną na podany adres email
    
  Scenariusz: Rejestracja nie powodzi się z powodu zajętej nazwy użytkownika
    Zakładając, że Użytkownik chce założyć nowe konto
    Kiedy Użytkownik podaje następujące dane rejestracyjne
      | nazwa    | email           | hasło          |
      | nowak22  | nowy@poczta.pl  | MocneHasło45!  |
    Oraz Użytkownik akceptuje warunki korzystania z serwisu
    Oraz Użytkownik zatwierdza proces rejestracji
    Wtedy System informuje o niemożności utworzenia konta
    Oraz System wyświetla komunikat o zajętej nazwie użytkownika

```

### Prototypowanie testów

Już na etapie analizy wymagań można tworzyć "szkielety" testów automatycznych, nawet jeśli implementacja nie jest
jeszcze gotowa. Te prototypy testów pozwalają wcześnie wykryć potencjalne problemy z testowalnością i projektowaniem
interfejsów API.


```java
// Prototyp testu API - implementacja jeszcze nie istnieje
@Test
public void userRegistrationAPITest() {
    // Przygotowanie danych testowych
    RegistrationRequest request = new RegistrationRequest(
        "newuser",
        "newuser@example.com",
        "securePassword123"
    );
    
    // Wywołanie API (które jeszcze nie istnieje)
    Response response = given()
        .contentType(ContentType.JSON)
        .body(request)
    .when()
        .post("/api/users/register");
    
    // Oczekiwane rezultaty
    response.then()
        .statusCode(201)
        .body("id", notNullValue())
        .body("username", equalTo("newuser"))
        .body("email", equalTo("newuser@example.com"));
}

```

Pozwala to na wdrożenie procesu ATDD - gdzie testy tworzymy przed implementacją kodu produkcyjnego.
Co zwiększa pokrycie testami akceptacyjnymi i umożliwia wdrożenie checków w CI/CD przez testy automatyczne.
Dzięki czemu zespół developerski może efektywniej przeprowadzać wdrożenia.

### Testowanie modeli i makiet

W wielu projektach, przed pełną implementacją, tworzone są modele, prototypy lub makiety interfejsu użytkownika. Te
elementy można i należy testować.

Dla makiet interfejsu użytkownika można wykorzystać narzędzia jak Selenium czy Selenide do weryfikacji podstawowych
interakcji i przepływów:


```java
// Test makiety UI
@Test
public void registrationFlowInMockupTest() {
    open("https://mockup.example.com/register");
    
    // Weryfikacja obecności wszystkich wymaganych pól
    $(By.id("username")).should(exist);
    $(By.id("email")).should(exist);
    $(By.id("password")).should(exist);
    $(By.id("confirmPassword")).should(exist);
    $(By.id("termsCheckbox")).should(exist);
    $(By.id("registerButton")).should(exist);
    
    // Weryfikacja podstawowego przepływu
    $(By.id("username")).setValue("testuser");
    $(By.id("email")).setValue("test@example.com");
    $(By.id("password")).setValue("password123");
    $(By.id("confirmPassword")).setValue("password123");
    $(By.id("termsCheckbox")).click();
    
    // Na makiecie przycisk może nie działać, ale możemy sprawdzić jego dostępność
    $(By.id("registerButton")).shouldBe(enabled);
}

```

Należy zaznaczyć, że do efektywnego testowania makiet interfejsu użytkownika należy wykorzystać narzędzia takie jak Cypress czy Playwright
ponieważ umożliwiaja one mockowanie danych i interakcje z elementami interfejsu.
Dodatkowo wspierają natywnie JavaScript i TypeScript - mogą być wykorzystywane na etapie Functional QA a nie Product QA,
a zatem ___powinny być przygotowywane przez developerów frontendu.___


### Identyfikacja przypadków brzegowych

Testerzy są szczególnie dobrzy w identyfikacji przypadków brzegowych i sytuacji nietypowych. Wczesna identyfikacja
takich przypadków pozwala uwzględnić je w projekcie, zamiast dodawać obsługę po fakcie.

Przykładowa lista przypadków brzegowych dla funkcji rejestracji użytkownika:

- Użytkownik z bardzo długim username (np. 100 znaków)
- Email w niestandarowym, ale poprawnym formacie (np. z podwójnym TLD jak .co.uk)
- Użytkownik próbujący wykorzystać znaki specjalne w nazwie użytkownika
- Hasło zawierające emotikony lub znaki z różnych alfabetów
- Próba rejestracji w trakcie prac konserwacyjnych lub awarii systemu

Dla każdego zidentyfikowanego przypadku brzegowego można zaprojektować odpowiedni test automatyczny.
Należy jednak zwrócić uwagę na proliferację testów automatycznych i ich odpowiednią priorytetyzację i grupowanie
tak aby dawały największy współczynnik ROI.

### Wczesne planowanie strategii testowej dla danego projektu

Faza analizy wymagań to idealny moment na opracowanie strategii testowej dla projektu, obejmującej:

- Poziomy testowania (jednostkowe, integracyjne, systemowe, akceptacyjne)
- Podejście do automatyzacji (co automatyzować, kiedy, jakimi narzędziami)
- Zarządzanie środowiskami testowymi
- Zarządzanie danymi testowymi
- Strategię raportowania i monitorowania

Dokument strategii testowej staje się przewodnikiem dla całego zespołu, zapewniającym spójne podejście do testowania na
wszystkich etapach projektu.

## 11.4. Testowanie równoległe z wytwarzaniem

Strategia Shift-Left osiąga swoją kulminację w koncepcji testowania równoległego z wytwarzaniem. W tym podejściu testy
nie są tworzone po implementacji funkcjonalności, ale równolegle z nią. Takie podejście zapewnia natychmiastową
informację zwrotną, skraca cykl rozwoju i podnosi jakość oprogramowania.

### Test-Driven Development (TDD)

TDD to metodyka, w której testy są pisane przed implementacją. Proces składa się z trzech kroków:

1. Red - napisanie testu, który nie przechodzi, ponieważ funkcjonalność jeszcze nie istnieje
2. Green - implementacja minimalnej ilości kodu, aby test przeszedł
3. Refactor - przeorganizowanie kodu bez zmiany jego zachowania


```java
// TDD dla funkcji walidacji adresu email
@Test
public void validateEmailShouldRejectInvalidFormats() {
    EmailValidator validator = new EmailValidator();
    
    assertFalse(validator.isValid("notanemail"));
    assertFalse(validator.isValid("missing@domain"));
    assertFalse(validator.isValid("@missingusername.com"));
    assertFalse(validator.isValid("spaces in@email.com"));
}

@Test
public void validateEmailShouldAcceptValidFormats() {
    EmailValidator validator = new EmailValidator();
    
    assertTrue(validator.isValid("valid@example.com"));
    assertTrue(validator.isValid("valid+tag@example.com"));
    assertTrue(validator.isValid("valid.name@example.co.uk"));
    assertTrue(validator.isValid("valid123@example-domain.com"));
}

// Implementacja tylko na tyle, aby testy przechodziły
public class EmailValidator {
    public boolean isValid(String email) {
        if (email == null || email.isEmpty()) {
            return false;
        }
        
        if (!email.contains("@")) {
            return false;
        }
        
        String[] parts = email.split("@");
        if (parts.length != 2 || parts[0].isEmpty() || parts[1].isEmpty()) {
            return false;
        }
        
        if (parts[0].contains(" ") || parts[1].contains(" ")) {
            return false;
        }
        
        if (!parts[1].contains(".")) {
            return false;
        }
        
        return true;
    }
}

```

### Behavior-Driven Development (BDD)

BDD to rozszerzenie TDD, które kładzie nacisk na współpracę między deweloperami, testerami i interesariuszami
biznesowymi. Wykorzystuje język naturalny do opisu oczekiwanego zachowania systemu, co ułatwia komunikację między
różnymi rolami w projekcie.

Framework Cucumber pozwala na implementację BDD w Javie:


```gherkin
Feature: Shopping Cart

  Scenario: Adding a product to an empty cart
    Given I am a logged-in user
    And my shopping cart is empty
    When I add a product "Smartphone" with price $599.99 to the cart
    Then my shopping cart should contain 1 item
    And the total cost should be $599.99

```


```java
// Implementacja kroków BDD
@Given("I am a logged-in user")
public void iAmALoggedInUser() {
    // Kod logowania lub symulacji zalogowanego użytkownika
    user = userService.loginUser("testuser", "password");
    assertNotNull(user);
}

@Given("my shopping cart is empty")
public void myShoppingCartIsEmpty() {
    // Upewnienie się, że koszyk jest pusty
    shoppingCart = shoppingCartService.getCartForUser(user.getId());
    shoppingCartService.clearCart(shoppingCart.getId());
    assertEquals(0, shoppingCart.getItems().size());
}

@When("I add a product {string} with price ${double} to the cart")
public void iAddAProductToTheCart(String productName, double price) {
    // Dodanie produktu do koszyka
    Product product = new Product(productName, new BigDecimal(price));
    shoppingCartService.addToCart(shoppingCart.getId(), product, 1);
}

@Then("my shopping cart should contain {int} item")
public void myShoppingCartShouldContainItems(int expectedItemCount) {
    // Weryfikacja liczby przedmiotów w koszyku
    shoppingCart = shoppingCartService.getCartForUser(user.getId());
    assertEquals(expectedItemCount, shoppingCart.getItems().size());
}

@Then("the total cost should be ${double}")
public void theTotalCostShouldBe(double expectedTotal) {
    // Weryfikacja łącznej wartości koszyka
    shoppingCart = shoppingCartService.getCartForUser(user.getId());
    assertEquals(new BigDecimal(expectedTotal), shoppingCart.getTotalCost());
}

```

### Continuous Testing

Continuous Testing to praktyka automatycznego uruchamiania testów przy każdej zmianie kodu. Jest to kluczowy element
potoku CI/CD i strategii Shift-Left.

Konfiguracja testów w Jenkins:


```groovy
pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                sh 'mvn clean compile'
            }
        }
        
        stage('Unit Tests') {
            steps {
                sh 'mvn test'
            }
            post {
                always {
                    junit '**/target/surefire-reports/TEST-*.xml'
                }
            }
        }
        
        stage('Integration Tests') {
            steps {
                sh 'mvn verify -DskipUnitTests'
            }
            post {
                always {
                    junit '**/target/failsafe-reports/TEST-*.xml'
                }
            }
        }
        
        stage('UI Tests') {
            steps {
                sh 'mvn test -Dtest=ui.**'
            }
            post {
                always {
                    publishHTML(target: [
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'target/surefire-reports',
                        reportFiles: 'index.html',
                        reportName: 'UI Test Report'
                    ])
                }
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
        }
    }
}

```

### Feature Toggles

Feature Toggles (lub Feature Flags) to technika, która umożliwia włączanie i wyłączanie funkcjonalności bez konieczności
wdrażania nowego kodu. Jest to szczególnie przydatne w kontekście testowania równoległego z wytwarzaniem, ponieważ
pozwala na testowanie funkcjonalności jeszcze niedostępnych dla użytkowników końcowych.


```java
public class FeatureToggleService {
    private Map<String, Boolean> toggles;
    
    public FeatureToggleService() {
        // Inicjalizacja z konfiguracji, bazy danych lub zewnętrznego serwisu
        toggles = new HashMap<>();
        toggles.put("NEW_REGISTRATION_FLOW", false);
        toggles.put("ENHANCED_SEARCH", true);
        toggles.put("DARK_MODE", false);
    }
    
    public boolean isEnabled(String featureName) {
        return toggles.getOrDefault(featureName, false);
    }
}

// Użycie Feature Toggle w kodzie
@Controller
public class RegistrationController {
    private final FeatureToggleService featureToggleService;
    private final RegistrationService registrationService;
    
    public RegistrationController(
            FeatureToggleService featureToggleService,
            RegistrationService registrationService) {
        this.featureToggleService = featureToggleService;
        this.registrationService = registrationService;
    }
    
    @GetMapping("/register")
    public String showRegistrationPage(Model model) {
        // Wybór widoku w zależności od togglea
        if (featureToggleService.isEnabled("NEW_REGISTRATION_FLOW")) {
            model.addAttribute("useNewFlow", true);
            return "registration-new";
        } else {
            return "registration";
        }
    }
}

// Testowanie z Feature Toggle
@Test
public void testNewRegistrationFlow() {
    // Przygotowanie mocka FeatureToggleService, który zawsze zwraca true dla NEW_REGISTRATION_FLOW
    FeatureToggleService mockToggleService = mock(FeatureToggleService.class);
    when(mockToggleService.isEnabled("NEW_REGISTRATION_FLOW")).thenReturn(true);
    
    RegistrationService mockRegistrationService = mock(RegistrationService.class);
    RegistrationController controller = new RegistrationController(
            mockToggleService, mockRegistrationService);
    
    Model model = new ExtendedModelMap();
    String viewName = controller.showRegistrationPage(model);
    
    assertEquals("registration-new", viewName);
    assertTrue((Boolean) model.getAttribute("useNewFlow"));
}

```

# 9. Definition of Ready i Definition of Done

## 9.1. Definition of Ready (DoR)

Definition of Ready (DoR) to kompleksowy zestaw kryteriów określających gotowość zadania automatyzacyjnego do
implementacji. W kontekście profesjonalnej automatyzacji testów z wykorzystaniem stosu technologicznego Java, Selenium,
Selenide i REST Assured, DoR musi łączyć aspekty techniczne z biznesowymi, zapewniając optymalne wykorzystanie zasobów i
maksymalizację zwrotu z inwestycji (ROI).

**Analiza biznesowej wartości automatyzacji** - Każde zadanie automatyzacyjne powinno mieć jasno określoną wartość
biznesową, wyrażoną jako wskaźnik ROI. Należy zdefiniować, ile ręcznych cykli testowych zostanie zastąpionych przez
automatyzację oraz jaki jest szacowany czas życia testu. Zgodnie z rekomendacjami ISTQB Advanced Test Automation
Engineer, automatyzować należy tylko te przypadki, które będą wykonywane wielokrotnie i nie podlegają częstym zmianom.
Kalkulator ROI powinien uwzględniać: czas implementacji automatyzacji, czas wykonania testu ręcznego, częstotliwość
wykonywania i szacowany okres użytkowania testu.

**Szczegółowa specyfikacja techniczna** - Oprócz ogólnych wymagań funkcjonalnych, DoR powinno zawierać szczegółową
specyfikację techniczną dla każdego przypadku testowego, w tym:

* Selektory XPath/CSS dla elementów webowych (dla Selenium/Selenide) z uwzględnieniem ich stabilności
*Szczegółowe schematy JSON/XML dla żądań i odpowiedzi API (dla REST Assured)
* Specyfikację nagłówków HTTP, parametrów zapytań i kodów statusu
* Definicje JSON Schema do walidacji odpowiedzi API

**Mapowanie przypadków testowych do wymagań** - Każdy automatyzowany przypadek testowy powinien być powiązany z
konkretnym wymaganiem biznesowym w systemie zarządzania wymaganiami (np. JIRA). Zgodnie z praktykami TMap NEXT, należy
stosować macierz traceability, która dokumentuje pokrycie wymagań przez testy i umożliwia analizę wpływu zmian.

**Szczegółowa analiza ryzyka technicznego** - DoR powinno zawierać analizę potencjalnych wyzwań technicznych, takich
jak:

* Dynamicznie generowane identyfikatory elementów w DOM
* Skomplikowane mechanizmy AJAX i SPA (Single Page Applications)
* Kwestie synchronizacji i timeoutów
* Obsługa scenariuszy cross-browser z uwzględnieniem specyficznych zachowań przeglądarek
* Mechanizmy zabezpieczeń API (OAuth 2.0, JWT, CSRF tokens)

**Aspekty infrastrukturalne** - Szczegółowe wymagania dotyczące infrastruktury testowej:

* Konfiguracja Selenium Grid lub alternatywnych rozwiązań (Selenoid, Zalenium)
* Specyfikacja kontenerów Docker z określonymi wersjami przeglądarek
* Wymagania dotyczące wydajności maszyn testowych (CPU, RAM)
* Konfiguracja proxy dla przechwytywania ruchu HTTP/HTTPS (np. BrowserMob Proxy)
* Parametry profilów przeglądarek (chrome options, firefox profile)

**Strategia zarządzania danymi testowymi** - Kompletna specyfikacja wymaganych danych testowych:

* Schemat automatycznej generacji danych (np. z wykorzystaniem biblioteki JavaFaker)
* Strategia izolacji danych dla równoległego wykonywania testów
* Model dostępu do zewnętrznych źródeł danych (JDBC, MongoDB, REST API)
* Mechanizmy anonymizacji danych produkcyjnych do celów testowych zgodne z RODO/GDPR

**Integracja z ekosystemem DevOps** - Określenie, jak testy będą współpracować z:

* Systemem kontroli wersji (Git branching strategy)
* Pipeline'ami CI/CD (Jenkins, GitLab CI, GitHub Actions)
* Systemami raportowania (Allure, ExtentReports)
* Narzędziami monitoringu jakości kodu (SonarQube, CodeClimate)

**Wymagania niefunkcjonalne** - Zdefiniowanie aspektów niefunkcjonalnych testów:

* Maksymalny akceptowalny czas wykonania pojedynczego testu (np. <2 minuty)
* Limity czasu odpowiedzi API przy różnych warunkach sieciowych
* Wymagania dotyczące lokalizacji i obsługi wielu języków
* Dostępność (WCAG) i zgodność z czytnikami ekranu

**Uzgodniona architektura techniczna** - Szczegółowy opis architektury frameworka testowego:

* Hierarchia abstrakcji dla POM (Page Object Model)
* Strategia implementacji wzorców projektowych (Factory, Builder, Chain of Responsibility)
* Model kompozycji dla komponentów wielokrotnego użytku
* Mechanizm zarządzania stanem (state management) między krokami testowymi
* Strategia wykorzystania adnotacji i metaprogramowania w JUnit/TestNG

**Gotowość biznesowa** - Aspekty organizacyjne gotowości:

* Zatwierdzenie przez Product Ownera i Stakeholderów
* Potwierdzenie finansowania i przydzielenia zasobów
* Zgodność z regulacjami branżowymi (np. HIPAA dla aplikacji medycznych, PCI DSS dla aplikacji płatniczych)
* Priorytetyzacja względem innych inicjatyw testowych

Zgodnie z filozofią Scaled Agile Framework (SAFe), DoR powinno także uwzględniać potrzeby różnych poziomów organizacji,
od zespołu testowego po zarząd, zapewniając, że automatyzacja testów jest zgodna ze strategicznymi celami biznesowymi i
technicznymi. Dokument DoR powinien być wersjonowany i przechowywany w systemie zarządzania konfiguracją, z jasno
określonym procesem zatwierdzania zmian.

## 9.2. Definition of Done (DoD)

Definition of Done (DoD) w kontekście automatyzacji testów z wykorzystaniem Javy, Selenium, Selenide i REST Assured to
wielowymiarowy zbiór kryteriów, łączący rygorystyczne aspekty techniczne z kluczowymi wskaźnikami biznesowymi.
Kompleksowy DoD stanowi gwarancję jakości, utrzymywalności i wartości biznesowej zautomatyzowanych testów.

**Jakość i czystość kodu** - Kod testów automatycznych musi spełniać ściśle zdefiniowane metryki jakości:

* Pokrycie testami jednostkowymi na poziomie min. 85% dla samego kodu automatyzacyjnego (zgodnie z wytycznymi TMMi
      poziom 4)
* Zgodność ze standardem kodowania określonym przez SonarQube (zero "blocker issues", max 5 "critical issues")
* Złożoność cyklomatyczna metod < 10 (dla lepszej czytelności i utrzymywalności)
* Brak duplikacji kodu > 5 linii (DRY principle)
* Zastosowanie adnotacji `@API` (stability markers) z frameworka Guava dla publicznych interfejsów
* Poprawna implementacja wzorców GoF (Gang of Four) zgodnie z zasadami SOLID

**Aspekty techniczne wykonania testów** - Szczegółowe kryteria techniczne:

* Efektywność lokatorów Selenium (preferencja dla CSS, XPath tylko w uzasadnionych przypadkach)
* Wykorzystanie explicit wait zamiast implicit wait, z timeout'ami skonfigurowanymi w pliku properties
* Implementacja wzorca PageFactory z wykorzystaniem adnotacji `@FindBy` dla elementów UI
* Zastosowanie `ExpectedConditions` dla zaawansowanych warunków oczekiwania
* Konfiguracja timeout'ów dla REST Assured z wykorzystaniem RequestSpecBuilder
* Walidacja schematów odpowiedzi API z użyciem JSON Schema lub XMLUnit
* Obsługa serializacji/deserializacji z wykorzystaniem Jackson/GSON
* Implementacja custom assertion'ów dla złożonych walidacji biznesowych

**Zaawansowane aspekty architektury testów** - Standardy architektoniczne:

* Implementacja architektury screenplay/journey/BDD zgodna z ATDD (Acceptance Test-Driven Development)
* Zastosowanie wzorca Chain of Responsibility dla elastycznej obsługi prekondycji testowych
* Wykorzystanie rzutowania typu z Proxy Pattern dla dynamicznych interfejsów Page Object
* Implementacja mechanizmu lazy loading dla heavy page objects
* Zastosowanie kompozycji zamiast dziedziczenia dla współdzielonych funkcjonalności
* Implementacja custom ExpectedConditions dla złożonych stanów UI
* Zastosowanie wzorca Decorator dla rozszerzania funkcjonalności bazowych klas testowych

**Obsługa równoległego wykonania i skalowalności** - Kryteria wydajnościowe:

* Testy skonfigurowane do wykonania równoległego z parametrem thread-count w TestNG/JUnit5
* Zaimplementowana izolacja danych testowych dla wykonania współbieżnego
* Testy zoptymalizowane pod kątem wydajności (benchmark: kompletna suita <30 minut)
* Poprawne zarządzanie zasobami (zamykanie WebDriver, czyszczenie połączeń HTTP)
* Mechanizm ponownych prób (retry mechanism) dla niestabilnych testów z exponential backoff
* Konfiguracja dla dynamic thread allocation w środowisku CI

**Integracja biznesowa** - Aspekty biznesowe zdefiniowane według ISTQB Business Analyst:

* Test Coverage Report powiązany z ryzykiem biznesowym w formacie RCRCM (Risk & Control Risk Coverage Matrix)
* Zrealizowane cele KPI dla automatyzacji (np. redukcja czasu cyklu testowego o X%)
* Udokumentowany zwrot z inwestycji (ROI) zgodny z przedwdrożeniowymi kalkulacjami
* Raport z analizy trendów defektów wykrywanych przez zautomatyzowane testy
* Metryki efektywności testów (Defect Detection Percentage, Test Design Efficiency, Test Execution Efficiency)

**Zaawansowane raportowanie** - Wymagania dotyczące raportowania:

* Integracja Allure ReportPortal z dashboardami zarządczymi
* Wdrożona graficzna wizualizacja trendów wykonania testów
* Automatyczna kategoryzacja defektów według wzorców błędów
* Integracja z systemem śledzenia defektów (JIRA) z automatycznym tworzeniem zgłoszeń
* Raportowanie metryk flaky tests z analizą przyczyn źródłowych
* Wdrożony mechanizm notification (Slack, email, MS Teams) dla krytycznych błędów

**Standardy dokumentacji technicznej** - Dokumentacja kodu i procedur:

* Dokumentacja JavaDoc zgodna ze standardem Oracle dla wszystkich publicznych API
* Diagram architektury frameworka testowego w notacji UML/C4
* Dokumentacja warstwy abstrakcji z opisem wzorców projektowych
* Instrukcja konfiguracji środowiska lokalnego w formacie asciidoc/markdown
* Słownik Domain-Specific Language dla słów kluczowych BDD
* Wiki z troubleshooting guide dla najczęstszych problemów

**Aspekty bezpieczeństwa i zgodności** - Kryteria bezpieczeństwa:

* Audyt kodu pod kątem wrażliwych danych (hasła, tokeny)
* Implementacja szyfrowania dla wrażliwych danych testowych zgodnie z OWASP
* Zgodność z polityką bezpieczeństwa organizacji (Security Compliance Report)
* Odseparowanie danych testowych z różnych środowisk (dev, stage, prod)
* Implementacja bezpiecznego zarządzania sekretami (np. HashiCorp Vault integration)

**Maintainability i knowledge transfer** - Aspekty utrzymaniowe:

* Code walkthrough przeprowadzony z zespołem deweloperskim i QA
* Sesja knowledge sharing z dokumentacją video
* Identyfikacja key-person risk i plan mitygacji
* Stworzenie "decision log" dokumentującego kluczowe decyzje architektoniczne
* Wdrożenie Test Maintenance Plan zgodnego z IEEE 829

Zgodnie z metodyką TMap NEXT, DoD powinno być wielopoziomowe, z oddzielnymi kryteriami dla poziomu komponentu,
integracji i systemu. Każdy poziom DoD powinien być zweryfikowany przez odpowiednie role (developer, technical lead,
business analyst, product owner), co zapewnia kompleksowe podejście do jakości zautomatyzowanych testów.

Proces weryfikacji DoD powinien być sformalizowany z wykorzystaniem checklist i zintegrowany z procesem continuous
improvement, umożliwiając regularne przeglądy i aktualizacje kryteriów w oparciu o retrospektywy sprintów i analizę
metryk jakości.
