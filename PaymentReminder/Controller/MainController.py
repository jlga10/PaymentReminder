class MainController:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.configureCRUDBTNs()

    def configureCRUDBTNs(self):
        # Conecta los botones de la vista con los métodos del controlador
        #Brands
        brand_tab = self.view.module_tabs["Brands"]
        brand_tab.create_btn.clicked.connect(lambda: self.model.createBrand(brand_tab.name_line_edit.text(), brand_tab.brand_email_line_edit.text(), brand_tab.brand_telephone_line_edit.text()))
        brand_tab.edit_btn.clicked.connect(lambda: self.model.editBrand(brand_tab.name_line_edit.text(), brand_tab.brand_email_line_edit.text(), brand_tab.brand_telephone_line_edit.text()))
        brand_tab.delete_btn.clicked.connect(lambda: self.model.deleteBrand(brand_tab.name_line_edit.text()))
        #Managers
        manager_tab = self.view.module_tabs["Managers"]
        manager_tab.create_btn.clicked.connect(lambda: self.model.createManager(manager_tab.name_line_edit.text(), manager_tab.manager_email_line_edit.text(), manager_tab.manager_alias_line_edit.text()))
        #Talents
        talent_tab = self.view.module_tabs["Talents"]
        talent_tab.create_btn.clicked.connect(lambda: self.model.createTalent(talent_tab.name_line_edit.text(), talent_tab.talent_email_line_edit.text(), talent_tab.talent_telephone_line_edit.text()))
        talent_tab.edit_btn.clicked.connect(lambda: self.model.editTalent(talent_tab.name_line_edit.text(), talent_tab.talent_email_line_edit.text(), talent_tab.talent_telephone_line_edit.text()))
        talent_tab.delete_btn.clicked.connect(lambda: self.model.deleteTalent(talent_tab.name_line_edit.text()))
        #Collaborations
        collaboration_tab = self.view.module_tabs["Collaborations"]
        collaboration_tab.create_btn.clicked.connect(lambda: self.model.createCollaboration(
            collaboration_tab.collaboration_id_line_edit.text(),
            collaboration_tab.collaboration_talent_line_edit.text(),
            collaboration_tab.collaboration_brand_line_edit.text(),
            collaboration_tab.collaboration_manager_line_edit.text(),
            collaboration_tab.collaboration_total_amount_spin_box.value(),
            collaboration_tab.collaboration_billing_date_spin_box.value(),
            collaboration_tab.collaboration_remaining_days_spin_box.value(),
            collaboration_tab.collaboration_charged_checkBox.isChecked()
        ))
        collaboration_tab.edit_btn.clicked.connect(lambda: self.model.editCollaboration(
            collaboration_tab.collaboration_id_line_edit.text(),
            collaboration_tab.collaboration_talent_line_edit.text(),
            collaboration_tab.collaboration_brand_line_edit.text(),
            collaboration_tab.collaboration_manager_line_edit.text(),
            collaboration_tab.collaboration_total_amount_spin_box.value(),
            collaboration_tab.collaboration_billing_date_spin_box.value(),
            collaboration_tab.collaboration_remaining_days_spin_box.value(),
            collaboration_tab.collaboration_charged_checkBox.isChecked()
        ))
        collaboration_tab.delete_btn.clicked.connect(lambda: self.model.deleteCollaboration(collaboration_tab.collaboration_id_line_edit.text()))