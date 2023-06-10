# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WtyczkaProjektDialog
                                 A QGIS plugin
 1. Liczene przewyższeń  2. Liczenie pola powierzchni metodą Gaussa
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-02
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Nina Janczak Jan Sychowiec
        email                : nina.janczak.stud@pw.edu.pl jan.sychowiec.stud@pw.edu.pl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
import numpy as np

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'wtyczka_projekt_dialog_base.ui'))


class WtyczkaProjektDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(WtyczkaProjektDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.klik_przewyzszenie.clicked.connect(self.wysokosc)
        self.klik_pole.clicked.connect(self.pole)
        


    def wysokosc(self): 
        warstwa = self.wybor_warstwy.currentLayer()
        liczba_elementów = len(warstwa.selectedFeatures())
        if liczba_elementów == 2: 
            Nr = []
            X = []
            Y = []
            Z = []
            wybrane_elementy = warstwa.selectedFeatures() 
            for elementy in  wybrane_elementy:
                pnr = elementy["Nr"]
                px = elementy["X"]
                py = elementy["Y"]
                pz = elementy["Z"]
                Nr.append(pnr)
                X.append(px)
                Y.append(py)
                Z.append(pz)
            H = Z[1] - Z[0]
            self.label_wynik_przewyzszenie.setText(f'Przewyższenie między punktem {Nr[0]} a {Nr[1]} wynosi {H:.3f} m')
        elif liczba_elementów < 2:
            self.label_wynik_przewyzszenie.setText("Wybrano za mało punktów")
        elif liczba_elementów > 2:
            self.label_wynik_przewyzszenie.setText("Wybrano za dużo punktów")
    def pole(self):
        warstwa = self.wybor_warstwy.currentLayer()
        liczba_elementów = len(warstwa.selectedFeatures())
        if liczba_elementów == 3 or liczba_elementów == 4: 
            wspolrzedne = []
            Nr = []
            wybrane_elementy = warstwa.selectedFeatures() 
            for elementy in  wybrane_elementy:
                pnr = elementy["Nr"]
                px = elementy["X"]
                py = elementy["Y"]
                Nr.append(pnr)
                wspolrzedne.append((px,py))
            wspolrzedne = np.array(wspolrzedne)
            x = wspolrzedne[:, 0]
            y = wspolrzedne[:, 1]
            idx = np.argsort(x)
            x = x[idx]
            y = y[idx]
            if y[-2] > y[-1]:
                x[-2], x[-1] = x[-1], x[-2]
                y[-2], y[-1] = y[-1], y[-2]
            P = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
            NR = ' '.join(str(numer) for numer in Nr)
            self.label_wyni_pole.setText(f'Pole powierzchni dla punktów {NR} wynosi \n {P:.3f} m^2')
        elif liczba_elementów < 3:
            self.label_wyni_pole.setText("Wybrano za mało punktów")
        elif liczba_elementów > 4:
            self.label_wyni_pole.setText("Wybrano za dużo punktów")
        