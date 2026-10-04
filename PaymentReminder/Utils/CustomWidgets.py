from PySide6.QtWidgets import QPushButton

def createCustomButton(text, style_sheet, tool_tip, click_func):
    button = QPushButton(text)
    button.setStyleSheet(style_sheet)
    button.setToolTip(tool_tip)
    button.clicked.connect(click_func)
    return button