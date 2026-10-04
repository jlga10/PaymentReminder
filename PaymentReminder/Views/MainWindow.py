import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QHBoxLayout, QMainWindow, QPushButton, QTabWidget, QWidget, 
    QVBoxLayout, QLabel, QComboBox
)
from PaymentReminder.Utils import CustomWidgets

class WindowGenericContent(QWidget):
    """
    Clase reutilizable para crear una pestaña que contiene 
    un CRUD de la clase.
    """
    def __init__(self, module_name):
        super().__init__()
        layout = QVBoxLayout()
        # Alinear el contenido en la parte superior para que no flote en el centro
        layout.setAlignment(Qt.AlignTop)
        
        # 1. Crear el Label con el texto correspondiente
        self.name = module_name
        self.label = QLabel(f"Number of {module_name}:")
        self.label.setStyleSheet("font-weight: bold; font-size: 13px; margin-bottom: 5px;")

        # 2. Crear el ComboBox con algunas opciones de ejemplo
        #self.combo = QComboBox()
        #self.combo.addItems([
        #    f"Ejemplo {module_name} 1", 
        #    f"Ejemplo {module_name} 2", 
        #    f"Ejemplo {module_name} 3"
        #])
        

        # 3. Crear los widgets genericos para el CRUD (Agregar, Editar, Eliminar)
        self.create_btn = CustomWidgets.createCustomButton(
            text=f"Create {module_name}",
            style_sheet="background-color: #4CAF50; color: white; font-weight: bold;",
            tool_tip=f"Click to create a new {module_name}",
            click_func=lambda: print(f"Create {module_name} clicked")
        )
        self.edit_btn = CustomWidgets.createCustomButton(
            text=f"Edit {module_name}",
            style_sheet="background-color: #FFC107; color: white; font-weight: bold;",
            tool_tip=f"Click to edit the {module_name}",
            click_func=lambda: print(f"Edit {module_name} clicked")
        )
        self.delete_btn = CustomWidgets.createCustomButton(
            text=f"Delete {module_name}",
            style_sheet="background-color: #F44336; color: white; font-weight: bold;",
            tool_tip=f"Click to delete the {module_name}",
            click_func=lambda: print(f"Delete {module_name} clicked")
        )
        buttonHLayout = QHBoxLayout()
        buttonHLayout.addWidget(self.create_btn)
        buttonHLayout.addWidget(self.edit_btn)
        buttonHLayout.addWidget(self.delete_btn)

        # Añadir los widgets al layout de esta pestaña
        layout.addWidget(self.label)
        layout.addLayout(buttonHLayout)
        #layout.addWidget(self.combo)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Panel de Gestión")
        self.resize(600, 400)

        # Contenedor principal de pestañas
        self.module_tabs = {}
        tabs = QTabWidget()
        # --- 1. Pestaña HOME ---
        tab_home = QWidget()
        # Le ponemos un layout vacío o con un pequeño texto informativo si lo deseas
        layout_home = QVBoxLayout()
        layout_home.addWidget(QLabel("Bienvenido a la página de inicio."), alignment=Qt.AlignCenter)
        tab_home.setLayout(layout_home)
        
        # --- 2. Crear el resto de pestañas dinámicamente ---
        # Definimos los nombres de las pestañas que llevan la misma estructura
        modules = ["Collaborations", "Brands", "Talents", "Managers", "Settings"]
        
        # Añadimos primero la pestaña Home
        tabs.addTab(tab_home, "Home")
        
        # Creamos e insertamos el resto de pestañas usando nuestro componente personalizado
        for module in modules:
            page = WindowGenericContent(module)
            self.module_tabs[module] = page  # Guardamos la referencia a la pestaña
            tabs.addTab(page, module)

        # Establecer el QTabWidget como el componente central de la ventana principal
        self.setCentralWidget(tabs)
