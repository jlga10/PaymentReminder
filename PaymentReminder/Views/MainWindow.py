import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QCheckBox, QHBoxLayout, QLineEdit, QMainWindow, QPushButton, QSpinBox, QTabWidget, QWidget, 
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
        self.label = QLabel(f"{module_name}")
        self.label.setStyleSheet("font-weight: bold; font-size: 13px; margin-bottom: 5px;")

        # 2. Crear el ComboBox con algunas opciones de ejemplo
        #self.combo = QComboBox()
        #self.combo.addItems([
        #    f"Ejemplo {module_name} 1", 
        #    f"Ejemplo {module_name} 2", 
        #    f"Ejemplo {module_name} 3"
        #])
        

        # 3. Crear los widgets genericos para el CRUD (Agregar, Editar, Eliminar)
        self.name_label = QLabel("Name:")
        self.name_label.setStyleSheet("font-weight: bold; font-size: 12px;")
        self.name_line_edit = QLineEdit()
    
        line_edit_layout = QHBoxLayout()
        line_edit_layout.addWidget(self.name_label)
        line_edit_layout.addWidget(self.name_line_edit)

        self.especific_widgets_layout = QVBoxLayout()

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
        layout.addLayout(line_edit_layout)
        layout.addLayout(self.especific_widgets_layout)
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

        self.createBrandWidgets(self.module_tabs["Brands"])
        self.createManagerWidgets(self.module_tabs["Managers"])
        self.createTalentWidgets(self.module_tabs["Talents"])
        self.createCollaborationWidgets(self.module_tabs["Collaborations"])
        # Establecer el QTabWidget como el componente central de la ventana principal
        self.setCentralWidget(tabs)

    def createBrandWidgets(self, brand_tab):
        # Creamos los widgets específicos para la pestaña de Brands
        brand_tab.brand_email_label = QLabel("Email:")
        brand_tab.brand_email_line_edit = QLineEdit()
        brand_tab.brand_telephone_label = QLabel("Telephone:")
        brand_tab.brand_telephone_line_edit = QLineEdit()

        brand_tab.especific_widgets_layout.addWidget(brand_tab.brand_email_label)
        brand_tab.especific_widgets_layout.addWidget(brand_tab.brand_email_line_edit)
        brand_tab.especific_widgets_layout.addWidget(brand_tab.brand_telephone_label)
        brand_tab.especific_widgets_layout.addWidget(brand_tab.brand_telephone_line_edit)  

    def createManagerWidgets(self, manager_tab):
        manager_tab.manager_email_label = QLabel("Email:")
        manager_tab.manager_email_line_edit = QLineEdit()
        manager_tab.manager_alias_label = QLabel("Alias:")
        manager_tab.manager_alias_line_edit = QLineEdit()

        manager_tab.especific_widgets_layout.addWidget(manager_tab.manager_email_label)
        manager_tab.especific_widgets_layout.addWidget(manager_tab.manager_email_line_edit)
        manager_tab.especific_widgets_layout.addWidget(manager_tab.manager_alias_label)
        manager_tab.especific_widgets_layout.addWidget(manager_tab.manager_alias_line_edit)

    def createTalentWidgets(self, talent_tab):
        talent_tab.talent_email_label = QLabel("Email:")
        talent_tab.talent_email_line_edit = QLineEdit()
        talent_tab.talent_telephone_label = QLabel("Telephone:")
        talent_tab.talent_telephone_line_edit = QLineEdit()

        talent_tab.especific_widgets_layout.addWidget(talent_tab.talent_email_label)
        talent_tab.especific_widgets_layout.addWidget(talent_tab.talent_email_line_edit)
        talent_tab.especific_widgets_layout.addWidget(talent_tab.talent_telephone_label)
        talent_tab.especific_widgets_layout.addWidget(talent_tab.talent_telephone_line_edit)

    def createCollaborationWidgets(self, collaboration_tab):
        collaboration_tab.collaboration_id_label = QLabel("ID:")
        collaboration_tab.collaboration_id_spin_box = QSpinBox()
        collaboration_tab.collaboration_talent_label = QLabel("Talent:")
        collaboration_tab.collaboration_talent_line_edit = QLineEdit()
        collaboration_tab.collaboration_brand_label = QLabel("Brand:")
        collaboration_tab.collaboration_brand_line_edit = QLineEdit()
        collaboration_tab.collaboration_manager_label = QLabel("Manager:")
        collaboration_tab.collaboration_manager_line_edit = QLineEdit()
        collaboration_tab.collaboration_total_amount_label = QLabel("Total Amount:")
        collaboration_tab.collaboration_total_amount_spin_box = QSpinBox()
        collaboration_tab.collaboration_billing_date_label = QLabel("Billing Date:")
        collaboration_tab.collaboration_billing_date_spin_box = QSpinBox()
        collaboration_tab.collaboration_remaining_days_label = QLabel("Remaining Days:")
        collaboration_tab.collaboration_remaining_days_spin_box = QSpinBox()
        collaboration_tab.collaboration_charged_label = QLabel("Charged:")
        collaboration_tab.collaboration_charged_checkBox = QCheckBox()

        collaboration_tab.especific_widgets_layout.addWidget(collaboration_tab.collaboration_id_label)
        collaboration_tab.especific_widgets_layout.addWidget(collaboration_tab.collaboration_id_spin_box)
        collaboration_tab.especific_widgets_layout.addWidget(collaboration_tab.collaboration_talent_label)
        collaboration_tab.especific_widgets_layout.addWidget(collaboration_tab.collaboration_talent_line_edit)
        collaboration_tab.especific_widgets_layout.addWidget(collaboration_tab.collaboration_brand_label)
        collaboration_tab.especific_widgets_layout.addWidget(collaboration_tab.collaboration_brand_line_edit)
        collaboration_tab.especific_widgets_layout.addWidget(collaboration_tab.collaboration_manager_label)
        collaboration_tab.especific_widgets_layout.addWidget(collaboration_tab.collaboration_manager_line_edit)
        collaboration_tab.especific_widgets_layout.addWidget(collaboration_tab.collaboration_total_amount_label)
        collaboration_tab.especific_widgets_layout.addWidget(collaboration_tab.collaboration_total_amount_spin_box)
        collaboration_tab.especific_widgets_layout.addWidget(collaboration_tab.collaboration_billing_date_label)
        collaboration_tab.especific_widgets_layout.addWidget(collaboration_tab.collaboration_billing_date_spin_box)
        collaboration_tab.especific_widgets_layout.addWidget(collaboration_tab.collaboration_remaining_days_label)
        collaboration_tab.especific_widgets_layout.addWidget(collaboration_tab.collaboration_remaining_days_spin_box)
        collaboration_tab.especific_widgets_layout.addWidget(collaboration_tab.collaboration_charged_label)
        collaboration_tab.especific_widgets_layout.addWidget(collaboration_tab.collaboration_charged_checkBox)