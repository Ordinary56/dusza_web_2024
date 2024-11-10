# Dusza Árpád Országos Programozói Emlékverseny

## Projekt Leírása

A projekt a következő főbb funkciókat biztosítja:
- **Csapatok számára**: Jelentkezési lehetőség az összes szükséges adat megadásával, valamint a regisztráció utáni adatmódosítás.
- **Iskolák számára**: Az iskolák jóváhagyhatják saját csapataik jelentkezését.
- **Szervezők számára**: A szervezők ellenőrizhetik és jóváhagyhatják a jelentkezéseket, valamint hiánypótlást kérhetnek a csapatoktól.

## Csapattagok

- **Balog Tamás**
- **Papp László Levente**
- **Nagy Hunor József**

## Nehézségek

- **A pénteki nap iskolával és haza utazással telt.**
- **Az egyik csapattagunk nem állt a helyzet magaslatán (röviden nem vett részt a munkában minden nyöszögtetés ellenére) ezért rá nem lehetett számítani.**

## Működő Funkciók

A következő funkciók a fejlesztés során megvalósításra kerültek és teljes mértékben működőképesek:
1. **Bejelentkezés**: A felhasználók biztonságosan be tudnak jelentkezni a saját szerepkörük alapján (csapat, iskola, szervező).
2. **Kategória**: Új kategória hozzáadása / törlése.
3. **Iskolai Felület**: Az iskolák felülete lehetővé teszi a csapatok jelentkezésének megtekintése.
4. **Programozási nyelv**: Új programozási nyelv hozzáadása / törlése.
5. **Exportálás**: A szervező képes a csapat adatainak kiexportálására.

## Bejelentkezéshez Szükséges Teszt Adatok
A tesztelés során használható felhasználói adatok a következők:

- **Szerepkör:** csapat  
  **Felhasználónév:** `kovacs.peter`  
  **Jelszó:** `jelszo123`
  
- **Szerepkör:** csapat  
  **Felhasználónév:** `kovacs.adam`  
  **Jelszó:** `jelszo456`

- **Szerepkör:** csapat  
  **Felhasználónév:** `kovacs.ede`  
  **Jelszó:** `jelszo789`

- **Szerepkör:** szervező  
  **Felhasználónév:** `nagy.janos`  
  **Jelszó:** `jelszo101`  

- **Szerepkör:** szervező  
  **Felhasználónév:** `nagy.peter`  
  **Jelszó:** `jelszo112`

- **Szerepkör:** iskola  
  **Felhasználónév:** `kiss.anna`  
  **Jelszó:** `jelszo131`
  
- **Szerepkör:** iskola  
  **Felhasználónév:** `kiss.albert`  
  **Jelszó:** `jelszo141`  

