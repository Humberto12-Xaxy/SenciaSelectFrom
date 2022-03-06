import re
import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from View.view import Ui_MainWindow

RESERVADAS = {
    'palabraS' : ['SELECT','select'],
    'palabraF' : ['FROM','from'],
    'columna' : '*'
}

apuntador = 0

def sentencia(sql):
    global apuntador

    if sql[apuntador] == RESERVADAS['palabraS'][0] or sql[apuntador] == RESERVADAS['palabraS'][1]:
        apuntador +=1
        if sql[apuntador] == RESERVADAS['columna']:
            apuntador += 1
            if sql[apuntador] == RESERVADAS['palabraF'][0] or sql[apuntador] == RESERVADAS['palabraF'][1]:
                apuntador += 1
                if palabra(sql[apuntador]) == 'Correcto':
                    return 'Correcto'
                else:
                    return 'Error'
            else:
                return 'Error'    
        else:
            return 'Error'    
    else:
        return 'Error'



def palabra(palabra):
    p = re.compile('(\w|\d|_)+')

    if p.fullmatch(palabra) is None:
        return 'Error'
    else:
        return 'Correcto'

class main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.comprobacion)
    
    def comprobacion(self):
        global apuntador
        sql = self.ui.lineEdit.text().strip(' ').split()
        response = sentencia(sql)

        self.ui.message.setText(response)
        apuntador = 0

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())

    # sql = input('Escriba la sentancia sql: ').strip(' ').split()
    # print(sentencia(sql))



