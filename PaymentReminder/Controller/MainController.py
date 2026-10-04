class MainController:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.configureCRUDBTNs()

    def configureCRUDBTNs(self):
        # Conecta los botones de la vista con los métodos del controlador
        brand_tab = self.view.module_tabs["Brands"]
        brand_tab.create_btn.clicked.connect(lambda: self.model.createBrand("", "", ""))

        #self.view.edit_btn.clicked.connect(self.editRecord)
        #self.view.delete_btn.clicked.connect(self.deleteRecord)