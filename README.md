# daftacademy-python_levelup-spring2020

## Ważne linki
Informacje organizacyjne:
[https://www.facebook.com/events/205462480547356/](https://www.facebook.com/events/205462480547356/)

Materiały z zajęć:
[https://github.com/daftcode/daftacademy-python_levelup-spring2020](https://github.com/daftcode/daftacademy-python_levelup-spring2020)
## Kontakt
[python@daftacademy.pl](python@daftacademy.pl)
## Przygotowanie środowiska pracy przed zajęciami
### Instalacja Python 3.8
Żeby nie tracić czasu w trakcie warsztatu, zależałoby nam żebyście przyszli na zajęcia z zainstalowaną odpowiednią wersją Pythona. Poniżej opisana jest krótka instrukcja instalacji dla najpopularniejszych systemów operacyjnych. 

Prosimy o nie używanie menadżera pakietów takich jak Conda czy Anaconda itp.
#### Windows
Wejdź na stronę [https://www.python.org/downloads/release/python-382/](https://www.python.org/downloads/release/python-382/) i pobierz odpowiedni instalator z sekcji `Files` - `Windows x86-64 executable installer` dla systemu 64-bitowego lub `Windows x86 executable installer` dla systemu 32-bitowego.

Uruchom pobrany instalator. Zaznacz opcję `Add Python 3.8 to PATH`, a następnie kliknij `Install Now`.
#### macOS
Wejdź na stronę [https://www.python.org/downloads/release/python-382/](https://www.python.org/downloads/release/python-382/) i pobierz odpowiedni instalator z sekcji `Files` - `Mac OS X 64-bit/32-bit installer`. Uruchom pobrany plik i dokończ instalację.
#### Linux
Istnieje duża szansa, że masz już zainstalowanego pythona na swoim komputerze. W celu sprawdzenia jaka wersja jest zainstalowana, wpisz w terminalu:
```
python3 --version
```
Jeżeli uzyskasz wynik `Python 3.8.x` - jesteś gotowy na zajęcia. W przypadku, gdy nie zostanie odnaleziona komenda `python3` lub zainstalowana będzie niższa wersja niż `Python 3.8`, należy podążać za kolejnymi krokami, zależnymi od systemu, który posiadasz.
##### Debian lub Ubuntu
Użyj w terminalu następującej komendy:
```
sudo apt install python3.8
```
Dla wersji Ubuntu starszych niż 16.10 powyższa komenda może nie zadziałać. W takiej sytuacji należy skorzystać z deadsnakes PPA:
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8
sudo apt install python3.8-distutils python3.8-dev python3.8-venv wget
sudo wget https://bootstrap.pypa.io/get-pip.py
python3.8 get-pip.py
```
##### Fedora (29+)

```
sudo dnf -y install python38 python3-pip python3-virtualenv
```
Dla starszych wersji Fedory powyższa komenda może nie zadziałać. W takiej sytuacji należy wykonać następującej komendy:
```
sudo dnf -y install gcc gcc-c++ zlib zlib-devel libffi-devel openssl-devel openssl-static wget tar make
cd /tmp/;
wget https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz;
tar xzf Python-3.8.2.tgz;
cd Python-3.8.2;
sudo ./configure --prefix=/opt/python38 --enable-optimizations --with-lto --with-system-ffi --with-computed-gotos --enable-loadable-sqlite-extensions;
sudo make -j $(nproc);
sudo make altinstall;
sudo rm /tmp/Python-3.8.2.tgz;
sudo ln -s /opt/python38/bin/python3.8 /opt/python38/bin/python3;
sudo ln -s /opt/python38/bin/python3.8 /opt/python38/bin/python;
sudo ln -s /opt/python38/bin/python3.8-config /opt/python38/bin/python-config;
sudo ln -s /opt/python38/bin/pydoc3.8 /opt/python38/bin/pydoc;
sudo ln -s /opt/python38/bin/idle3.8 /opt/python38/bin/idle;
sudo ln -s /opt/python38/bin/python3.8 /usr/bin/python38;
sudo ln -s /opt/python38/bin/pip3.8 /opt/python38/bin/pip3;
sudo ln -s /opt/python38/bin/pip3.8 /opt/python38/bin/pip;
```
Dla starszych wersji Fedory możesz dostać błąd mówiący o tym, że komenda `dnf` nie została znaleziona. W takiej sytuacji należy skorzystać z komendy `yum`.
##### openSUSE
Użyj w terminalu następujące komendy:
```
sudo zypper in python3 python3-pip python3-virtualenv
```
Dla starszych wersji openSUSE powyższa komenda może nie zadziałać. W takiej sytuacji należy wykonać następującej komendy:
```
sudo zypper in gcc gcc-c++ zlib-devel bzip2 libbz2-devel libffi-devel libopenssl-devel readline-devel sqlite3 sqlite3-devel xz xz-devel wget tar make;
cd /tmp/;
sudo wget https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tar.xz;
tar xf Python-3.8.2.tar.xz;
cd Python-3.8.2;
sudo ./configure --prefix=/opt/python38 --enable-optimizations --with-lto --with-system-ffi --with-computed-gotos --enable-loadable-sqlite-extensions;
sudo make -j $(nproc);
sudo make altinstall;
sudo rm /tmp/Python-3.8.2.tgz;
sudo ln -s /opt/python38/bin/python3.8 /opt/python38/bin/python3;
sudo ln -s /opt/python38/bin/python3.8 /opt/python38/bin/python;
sudo ln -s /opt/python38/bin/python3.8-config /opt/python38/bin/python-config;
sudo ln -s /opt/python38/bin/pydoc3.8 /opt/python38/bin/pydoc;
sudo ln -s /opt/python38/bin/idle3.8 /opt/python38/bin/idle;
sudo ln -s /opt/python38/bin/python3.8 /usr/bin/python38;
sudo ln -s /opt/python38/bin/pip3.8 /opt/python38/bin/pip3;
sudo ln -s /opt/python38/bin/pip3.8 /opt/python38/bin/pip;
```
### Sprawdzenie, czy Python 3.8 jest zainstalowany
Wpisz w terminalu następującą komendę:
```
python3.8 --version
```
Jeżeli powyższa komenda zwróci wynik `Python 3.8.x` oznacza to, że masz zainstalowaną odpowiednią wersję Pythona.

Na Windowsie powyższa komenda może nie zadziałać. Wtedy należy użyć w `Wierszu polecenia`:
```
python --version
```
Powinno ono zwrócić wynik `Python 3.8.x`.
### Wybór edytora tekstu
Programowanie w Pythonie nie wymaga żadnych specjalistycznych narzędzi - wystarczy korzystać z edytora tekstu. Na zajęciach możesz korzystać z dowolnego edytora. Jeżeli nie wiesz co wybrać, polecamy Sublime Text [https://www.sublimetext.com/](https://www.sublimetext.com/).

### Punktacja prac domowych
Punktacja za prace domowe:
Praca domowa 1:max 15 punktów (poprawne/max * 15)
Praca domowa 2:max 25 punktów (poprawne/max * 25)
Praca domowa 3:max 30 punktów (poprawne/max * 30)
Praca domowa 4:max 30 punktów (poprawne/max * 30)

Sumarycznie max 100 punktów
Minimalnie wymaganych na zaliczenie jest 70 punktów.