START=$(date +%s.%N)
echo "Skrypt napisany pod systemy debianowate, testowany na Linux Mint"
echo "Ta instalacja wymaga uprawnien administratora. Upewnij sie, ze uruchomiles skrypt przy pomocy sudo"
echo "Proces moze potrwac do kilkunastu minut, cierpliwosci"
read -p "Jestes gotowy na instalacje (y/n)? " choice
case "$choice" in 
  y|Y ) echo "yes";;
  n|N ) exit;;
  * ) exit;;
esac
echo "1/15    Czyszczenie ewentualnych poprzednich instalacji"
yes | rm install.log
yes | rm -r env 2>&1 >>install.log
echo "2/15    Aktualizacja repozytoriow"
yes | apt-get update 2>&1 >>install.log
echo "3/15    Instalacja python-dev w wersji 2.7"
yes | apt-get install python-dev 2>&1 >>install.log
echo "4/15    Instalacja virtualenv"
yes | apt-get install virtualenv 2>&1 >>install.log
echo "5/15    Instalacja wymagan do bibliotek"
yes | apt-get install build-essential gfortran libatlas-base-dev 2>&1 >>install.log
echo "6/15    Instalacja git"
yes | apt-get install git
echo "7/15    Stawianie srodowiska"
virtualenv env 2>&1 >>install.log
echo "8/15    Aktualizacja repozytoriow pythona"
env/bin/pip install --upgrade pip 2>&1 >>install.log
echo "9/15    Instalacja flask"
env/bin/pip install flask 2>&1 >>install.log
echo "10/15   Instalacja numpy"
env/bin/pip install numpy 2>&1 >>install.log
echo "11/15   Instalacja scipy"
env/bin/pip install scipy 2>&1 >>install.log
echo "12/15   Instalacja scikit-learn"
env/bin/pip install -U scikit-learn 2>&1 >>install.log
echo "13/15   Instalacja pybrain"
env/bin/pip install pybrain 2>&1 >>install.log
echo "14/15   Instalacja biblioteki libSVM"
chmod 777 .
git clone https://github.com/cjlin1/libsvm.git
cd libsvm
make
cd ..
echo "15/15   Instalacja fann2 - eksperymentalnie"
wget http://downloads.sourceforge.net/project/fann/fann/2.2.0/FANN-2.2.0-Source.zip 2>&1 >>install.log
unzip FANN-2.2.0-Source.zip 2>&1 >>install.log
cd FANN-2.2.0-Source/
cmake . 2>&1 >>install.log
make install 2>&1 >>install.log
cd examples/
make runtest 2>&1 >>install.log
cd ../..
yes | apt-get install swig 2>&1 >>install.log
env/bin/pip install fann2 2>&1 >>install.log
echo "Tutaj jeszcze msuza byc dodatkowe biblioteki - kohonen, linki do libsvm poprawnie konfigurnac itd"
END=$(date +%s.%N)
DIFF=$(echo "$END - $START" | bc)
echo "Czas wykonywania: $DIFF"
