from iszlc import app

#Checks if the run.py file has executed directly and not imported
#Sprawdza, czy plik run.py został uruchomiony bezpośrednio i nie został zaimportowany

if __name__ == '__main__':
    app.run(debug=True)