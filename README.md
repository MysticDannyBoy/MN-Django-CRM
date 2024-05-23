# Project Sima Liba
## Összefoglaló
### Leírás
Ez a fork arról szól, hogy személyes módon felhasználhassuk az eredeti projekt fájljait.

### Cél
Egy egyszerű felületet teremteni arra, hogy különféle, listázható adatokat webfelületen létrehozzuk, módosítsuk, töröljük.
Elsősorban a Mintafeldolgozó táblázat kiváltása miatt hoznánk létre, de ezt lehet általánosítani is.

## Lépések
### 0. lépés: felrakni a függőségeket
0. Legyen feltelepítve a Python, és fusson egy MySQL adatbázis, port 3306.
1. `py -m venv .venv` futtatása parancssoron
2. `.venv\Scripts\activate.bat` futtatása parancssoron
3. `pip install -r requirements.txt` futtatása parancssoron

### 1. lépés: Inicializálni az adatbázist.
1. Valami egyedi nevet adni az adatbázisnak a `beallitasok.py` fájlban.
2. Lefuttatni egy `python mydb.py` parancsot, hogy létrehozzuk az adatbázist (a futó mysql szerveren, port: 3306).
3. Lefuttatni egy `python manage.py migrate` parancsot, hogy inicializáljuk a táblákat az adatbázisban.

### 2. lépés: Elindítani a szervert, létrehozni a felhasználót
1. `python manage.py runserver` futtatása parancssoron.
2. Felhasználó regisztrálása a http://127.0.0.1:8000/register/ címen. Ez be is léptet.

### 3. lépés: Személyre szabni a template-et, és az adatbázist
1. Kattintani az `Add Record` gombra (bal fölső sarok).
2. Kitölteni adatokkal. Szemügyre vételezni, hogy mi kell, mi nem.
3. Kattintani az `Add Record` gombra alul. Sikeresen hozzáadtunk egy bejegyzést.
4. Az "ID"-re kattitva megnyitjuk a bejegyzést. `Update record` módosítja a bejegyzést.
5. Termékeket akarunk felvinni: név, ár, kiszerelés, bevezetés dátuma. Ez 4 féle adat.
Ezeket a következő helyeken kell módosítani: 
- `website/models.py` (`Record` class)
- `website/forms.py` (`AddRecordForm` rész)
- `website/templates/record.html`
- `website/templates/home.html`
6. Létrehozni az adatbázison belül (`website_records` táblában) az adatoknak megfelelő mezőket, a megfelelő nevekkel (ugyanaz, mint a `models.py` fájlban.)
7. NotNull-ra átállítani az adatbázisban azokat a mezőket, amikre nincs szükség. És törölni őket

### 4. lépés: Használni!

### Fontos: előkészületek
Ha az elejétől kezdve tudjuk, hogy milyen adatokat akarunk tárolni az adatbázisban, akkor érdemes előre, ugyanazokat a field-eket szinkronba hozva módosítani, már előre, a következő fájlokat:
- `website/migrations/0001_initial.py` (a `migrations.CreateModel` rész)
- `website/models.py` (a `Record` class)
- `website/forms.py` (a `AddRecordForm` rész)
- `website/templates/record.html`
- `website/templates/home.html`
