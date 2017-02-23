echo "Użycie tego skryptu wymaga uprawnień administratorskich"
echo "Zabijanie procesów pythona..."
sudo killall python
echo "$EXIT_SUCCESS"
sudo env/bin/python -B main.py
