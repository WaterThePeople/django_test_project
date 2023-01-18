Instrukcja dla Windows (kroki instalacji mogą się różnić, zależnie od aktualnych wersji oprogramowania):

1.Zainstaluj pythona:
	1.1.Z strony https://www.python.org/downloads/ pobierz najnowszą wersję pythona.
	1.2.Podążąj za instrukcjami instalatora
	1.3.W opcjach zaawansowanych instalatora, zaznacz opcję 'Add python to environment variables'
	1.4.Pamiętaj aby python był dodany do ścieżki Windowsa, można zaznaczyć tą opcję w instalatorze
	lub ustawić to ręcznie w zmiennych środowiskowych.

2.Zainstaluj pip (Pip jest domyślnie zainstalowany z pythonem, w przypadku 
starszych wersji trzeba zainstalować ręcznie):
	2.1.Otwórz cmd terminal.
	2.2.Użyj komendy 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'.
	2.3.Następnie użyj komendy 'py get-pip.py'.

3.Stwórz wirtualne środowisko w folderze pojektu.
	3.1.Poprzez terminal wejdź to folderu gdzie znajduje się plik 'manage.py'.
	3.2.W terminalu uruchom komende 'py -m venv folder_name_of_env'.
	3.3.Następnie aktywujemy je poprzez komende 'folder_name_of_env\Scripts\activate.bat'.

4.W tym wirutalnym środowisku zainstaluj django.
	4.1.Poprzez terminal wejdź to folderu gdzie znajduje się plik 'manage.py'.
	4.2.Użyj komendy 'py -m pip install Django'.

5.W tym wirtualnym środowisku zainstauj django crispy forms.
	5.1.Poprzez terminal wejdź to folderu gdzie znajduje się plik 'manage.py'.
	5.2.Użyj komendy 'pip install django-crispy-forms'.

6.Uruchom serwer(te kroki są zawsze takie same przy uruchamianiu serwera).
	6.1.Poprzez terminal wejdź to folderu gdzie znajduje się plik 'manage.py'.
	6.2.Użyj komendy 'folder_name_of_env\Scripts\activate.bat', aby uruchomić wirtualne środowisko.
	6.3.Użyj komendy 'py manage.py runserver', aby uruchomić serwer.
	6.4.Teraz możesz już wejść na serwer, za pomocą localhost (http://127.0.0.1:8000/)
