START=$(date +%s.%N)
echo "Skrypt napisany pod systemy oparte o dystrybucję Debian, testowany na Linux Mint"
echo "Ta instalacja wymaga uprawnień administratora. Upewnij się, że uruchomiłeś skrypt przy pomocy sudo"
echo "Proces moze potrwać do kilkunastu minut, cierpliwości"
read -p "Jesteś gotowy na instalację (y/n)? " choice
case "$choice" in 
  y|Y ) echo "Rozpoczynanie instalacji";;
  n|N ) exit;;
  * ) exit;;
esac
echo "1/11    Czyszczenie ewentualnych poprzednich instalacji"
yes | rm install.log
yes | rm -r env 2>&1 >>install.log
echo "2/11    Aktualizacja repozytoriów"
yes | apt-get update 2>&1 >>install.log
echo "3/11    Instalacja python-dev w wersji 2.7"
yes | apt-get install python-dev 2>&1 >>install.log
echo "4/11    Instalacja virtualenv"
yes | apt-get install virtualenv 2>&1 >>install.log
echo "5/11    Instalacja wymagan do bibliotek"
yes | apt-get install build-essential gfortran libatlas-base-dev 2>&1 >>install.log
echo "6/11    Stawianie srodowiska"
virtualenv env 2>&1 >>install.log
echo "7/11    Aktualizacja repozytoriow pythona"
env/bin/pip install --upgrade pip 2>&1 >>install.log
echo "8/11    Instalacja flask"
env/bin/pip install flask 2>&1 >>install.log
echo "9/11   Instalacja numpy"
env/bin/pip install numpy 2>&1 >>install.log
echo "10/11   Instalacja scipy"
env/bin/pip install scipy 2>&1 >>install.log
echo "11/11   Instalacja scikit-learn"
env/bin/pip install -U scikit-learn 2>&1 >>install.log
mkdir tmp
END=$(date +%s.%N)
DIFF=$(echo "$END - $START" | bc)
echo "Czas wykonywania: $DIFF"
