from PyQt5 import QtGui, QtWidgets


class NotEmptyValidator(QtGui.QValidator):
    def validate(self, text, pos):
        state = QtGui.QIntValidator.Acceptable if bool(text) else QtGui.QIntValidator.Invalid
        return state, text, pos