# Dusza Árpád Országos Programozói Emlékverseny

## Projekt Leírása

A projekt a következő főbb funkciókat biztosítja:
- **Csapatok számára**: Jelentkezési lehetőség az összes szükséges adat megadásával, valamint a regisztráció utáni adatmódosítás.
- **Iskolák számára**: Az iskolák jóváhagyhatják saját csapataik jelentkezését.
- **Szervezők számára**: A szervezők ellenőrizhetik és jóváhagyhatják a jelentkezéseket, valamint hiánypótlást kérhetnek a csapatoktól.

## Hogyan kell futtatni?
1. menj a projekt mappájába (`cd ~/dusza_web_2024`)
2. aktiváld a virtuális környezetet (`source dusza_venv/bin/activate`)
3. telepítsd le a szükséges csomagokat, ami a requirements.txt-ben található (`pip install -r reqruirements.txt`)
4. futtasd gunicorn-al (` unicorn --bind 0.0.0.0:8000 dusza_project_django.wsgi`)
5. A szerver a 8000-es porton fut
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

## Továbbfejlesztési ötletek
1. Akadálymentesség (megjelenő szövegbuborékok ikonok felett, )
2. UI továbbfeljesztése (egység színvilág, jobban átláthó felhasználói felület)
3. Jelszó visszaállítás a felhasználók számára
4. Hiánypótlás esetén email küldése a csapat összes tagjának és a felkészítő tanárnak

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

