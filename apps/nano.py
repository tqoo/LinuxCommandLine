import PyQt5.QtWidgets as qt

nano = qt.QApplication([])
frame = qt.QWidget(nano)
textbox = qt.QLineEdit(frame)
textbox.move(20, 20)
textbox.resize(280,40)
textbox.show()
frame.show()