class MainController:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.configureCRUDBTNs()

    def configureCRUDBTNs(self):
        # Conecta los botones de la vista con los métodos del controlador
        #Brands
        brand_tab = self.view.module_tabs["Brands"]
        print(self.model.brands)
        brand_tab.module_combobox.addItems([brand.name for name, brand in self.model.brands.items()])
        brand_tab.create_btn.clicked.connect(lambda: self.createBrand(brand_tab))
        brand_tab.edit_btn.clicked.connect(lambda: self.editBrand(brand_tab))
        brand_tab.delete_btn.clicked.connect(lambda: self.deleteBrand(brand_tab))
        #Managers
        manager_tab = self.view.module_tabs["Managers"]
        manager_tab.module_combobox.addItems([manager.name for name, manager in self.model.managers.items()])
        manager_tab.create_btn.clicked.connect(lambda: self.createManager(manager_tab))
        manager_tab.edit_btn.clicked.connect(lambda: self.editManager(manager_tab))
        manager_tab.delete_btn.clicked.connect(lambda: self.deleteManager(manager_tab))
        #Talents
        talent_tab = self.view.module_tabs["Talents"]
        talent_tab.module_combobox.addItems([talent.name for name, talent in self.model.talents.items()])
        talent_tab.create_btn.clicked.connect(lambda: self.createTalent(talent_tab))
        talent_tab.edit_btn.clicked.connect(lambda: self.editTalent(talent_tab))
        talent_tab.delete_btn.clicked.connect(lambda: self.deleteTalent(talent_tab))
        #Collaborations
        collaboration_tab = self.view.module_tabs["Collaborations"]
        collaboration_tab.module_combobox.addItems([str(collaboration.id) for name, collaboration in self.model.collaborations.items()])
        collaboration_tab.create_btn.clicked.connect(lambda: self.createCollaboration(collaboration_tab))
        collaboration_tab.edit_btn.clicked.connect(lambda: self.editCollaboration(collaboration_tab))
        collaboration_tab.delete_btn.clicked.connect(lambda: self.deleteCollaboration(collaboration_tab))

#region BRAND
    def createBrand(self, brand_tab):
        self.model.createBrand(brand_tab.name_line_edit.text(), brand_tab.brand_email_line_edit.text(), brand_tab.brand_telephone_line_edit.text())
        self.updateViews()
    def editBrand(self, brand_tab):
        self.model.editBrand(brand_tab.name_line_edit.text(), brand_tab.brand_email_line_edit.text(), brand_tab.brand_telephone_line_edit.text())
        self.updateViews()
    def deleteBrand(self, brand_tab):
        self.model.deleteBrand(brand_tab.name_line_edit.text())
        self.updateViews()
#endregion BRAND
#region TALENT
    def createTalent(self, talent_tab):
        self.model.createTalent(talent_tab.name_line_edit.text(), talent_tab.talent_email_line_edit.text(), talent_tab.talent_telephone_line_edit.text())
        self.updateViews()
    def editTalent(self, talent_tab):
        self.model.editTalent(talent_tab.name_line_edit.text(), talent_tab.talent_email_line_edit.text(), talent_tab.talent_telephone_line_edit.text())
        self.updateViews()
    def deleteTalent(self, talent_tab):
        self.model.deleteTalent(talent_tab.name_line_edit.text())
        self.updateViews()
#endregion TALENT
#region MANAGER
    def createManager(self, manager_tab):
        self.model.createManager(manager_tab.name_line_edit.text(), manager_tab.manager_email_line_edit.text(), manager_tab.manager_alias_line_edit.text())
        self.updateViews()
    def editManager(self, manager_tab):
        self.model.editManager(manager_tab.name_line_edit.text(), manager_tab.manager_email_line_edit.text(), manager_tab.manager_alias_line_edit.text())
        self.updateViews()  
    def deleteManager(self, manager_tab):
        self.model.deleteManager(manager_tab.name_line_edit.text())
        self.updateViews()
#endregion MANAGER
#region COLLABORATION
    def createCollaboration(self, collaboration_tab):
        self.model.createCollaboration(
            collaboration_tab.collaboration_id_line_edit.text(),
            collaboration_tab.collaboration_talent_line_edit.text(),
            collaboration_tab.collaboration_brand_line_edit.text(),
            collaboration_tab.collaboration_manager_line_edit.text(),
            collaboration_tab.collaboration_total_amount_spin_box.value(),
            collaboration_tab.collaboration_billing_date_spin_box.value(),
            collaboration_tab.collaboration_remaining_days_spin_box.value(),
            collaboration_tab.collaboration_charged_checkBox.isChecked()
        )
        self.updateViews()
    def editCollaboration(self, collaboration_tab):
        self.model.editCollaboration(
            collaboration_tab.collaboration_id_line_edit.text(),
            collaboration_tab.collaboration_talent_line_edit.text(),
            collaboration_tab.collaboration_brand_line_edit.text(),
            collaboration_tab.collaboration_manager_line_edit.text(),
            collaboration_tab.collaboration_total_amount_spin_box.value(),
            collaboration_tab.collaboration_billing_date_spin_box.value(),
            collaboration_tab.collaboration_remaining_days_spin_box.value(),
            collaboration_tab.collaboration_charged_checkBox.isChecked()
        )
        self.updateViews()
    def deleteCollaboration(self, collaboration_tab):
        self.model.deleteCollaboration(collaboration_tab.collaboration_id_line_edit.text())
        self.updateViews()
#endregion COLLABORATION
#region UPDATE_WIDGETS
    def updateCollaborationWidgets(self):
        collaboration_tab = self.view.module_tabs["Collaborations"]
        collaboration_tab.collaboration_talent_combobox.clear()
        collaboration_tab.collaboration_talent_combobox.addItems([name for name, talent in self.model.talents.items()])
        collaboration_tab.collaboration_brand_combobox.clear()
        collaboration_tab.collaboration_brand_combobox.addItems([name for name, brand in self.model.brands.items()])
        collaboration_tab.collaboration_manager_combobox.clear()
        collaboration_tab.collaboration_manager_combobox.addItems([name for name, manager in self.model.managers.items()])
    def updateBrandWidgets(self):
        brand_tab = self.view.module_tabs["Brands"]
        brand_tab.module_combobox.clear()
        brand_tab.module_combobox.addItems([name for name, brand in self.model.brands.items()])
        brand_tab.module_string_list_model.setStringList(list(self.model.brands.keys()))
    def updateTalentWidgets(self):
        talent_tab = self.view.module_tabs["Talents"]
        talent_tab.module_combobox.clear()
        talent_tab.module_combobox.addItems([name for name, talent in self.model.talents.items()])
        talent_tab.module_string_list_model.setStringList(list(self.model.talents.keys()))
    def updateManagerWidgets(self):
        manager_tab = self.view.module_tabs["Managers"]
        manager_tab.module_combobox.clear()
        manager_tab.module_combobox.addItems([name for name, manager in self.model.managers.items()])
        manager_tab.module_string_list_model.setStringList(list(self.model.managers.keys()))
    def updateViews(self):
        self.updateCollaborationWidgets()
        self.updateBrandWidgets()
        self.updateTalentWidgets()
        self.updateManagerWidgets()
#endregion UPDATE_WIDGETS