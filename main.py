import sys
import PaymentReminder.Controller.MainController as prcontroller
import PaymentReminder.Utils.Excelator as excelator
import PaymentReminder.Content.Talent as talent
import PaymentReminder.Content.Manager as manager
import PaymentReminder.Content.Brand as brand
import PaymentReminder.Content.Collaboration as collaboration
import PaymentReminder.Views.MainWindow as prview
import PaymentReminder.Content.Model as model

registros = [
    {
            "Identificador": 1,
            "Talento": "Nombre del talento",
            "Marca": "Nombre de la marca",
            "Cantidad Total": 2500.00,
            "Fecha de Facturación": "2026-09-30",
            "Días Restantes": 15,
            "Cobrado": False,
        },
]

def create_sample_data(model):
    Talents = {
        "Santi": talent.Talent("Santiago Conde Mendoza", "santiago.conde@ejemplo.com", "telefono", "LaCocinaDeSantiaguini"),
        "Pilu": talent.Talent("Pilar Cuenca González", "pilu@ejemplo.com", "telefono", "pilumchef11")
    }

    Managers = {
        "Maria": manager.Manager("Maria Perez Ribes", "", "telefono", "MP")
    }

    Brands = {
        "Pascual": brand.Brand("Pascual", "pascual@gmail.com", "123456789"),
    }

    Collaborations = {
        "Collab1": collaboration.Collaboration(
            id=1,
            talent=Talents["Santi"],
            brand=Brands["Pascual"],
            manager=Managers["Maria"],
            total_amount=2500.00,
            billing_date="2026-09-30",
            remaining_days=15,
            charged=False
        )
    }
    model.brands = Brands
    model.managers = Managers
    model.talents = Talents
    model.collaborations = Collaborations

if __name__ == "__main__":
    print("hola")
    # 2. Inicializa la aplicación Qt
    app = prview.QApplication(sys.argv)

    # 3. Crea y muestra la ventana
    model = model.Model()

    #Fill data
    create_sample_data(model)

    view = prview.MainWindow()
    controller = prcontroller.MainController(view, model)
    view.show()
    controller.updateViews()

    # 4. Inicia el bucle de eventos de la aplicación
    #sys.exit(app.exec())
    app.exec()
    #excelator.ExcelManager.generateExcel()
    #print("hello")