import sys
import PaymentReminder.Controller.MainController as prcontroller
import PaymentReminder.Utils.Excelator as excelator
import PaymentReminder.Content.Talent as talent
import PaymentReminder.Content.Manager as manager
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

Talents = dict()
{
    "Santi": talent.Talent("Santiago Conde Mendoza", "santiago.conde@ejemplo.com", "LaCocinaDeSantiaguini"),
    "Pilu": talent.Talent("Pilar Cuenca González", "pilu@ejemplo.com", "pilumchef11")
}

Managers = dict()
{
    "Maria": manager.Manager("Maria Perez Ribes", "", "MP")
}

if __name__ == "__main__":
    print("hola")
    # 2. Inicializa la aplicación Qt
    app = prview.QApplication(sys.argv)

    # 3. Crea y muestra la ventana
    model = model.Model()
    view = prview.MainWindow()
    controller = prcontroller.MainController(view, model)
    view.show()

    # 4. Inicia el bucle de eventos de la aplicación
    #sys.exit(app.exec())
    app.exec()
    #excelator.ExcelManager.generateExcel()