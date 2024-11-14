from epimed_connector import EpimedConnector
from data_extractor import DataExtractor
from sheet_generator import SheetGenerator
from report_generator import ReportGenerator
from ui.app import run_ui

def main():
    # Autenticar no Epimed
    epimed_connector = EpimedConnector("seu_usuario", "sua_senha")
    epimed_connector.login()

    # Extrair dados do Epimed
    data_extractor = DataExtractor(epimed_connector)
    ward_data = {
        "UTI": data_extractor.extract_ward_data("UTI"),
        "Enfermaria": data_extractor.extract_ward_data("Enfermaria"),
        # Adicione mais unidades conforme necessário
    }

    # Gerar planilha Excel
    sheet_generator = SheetGenerator(data_extractor)
    sheet_generator.generate_ward_sheets(ward_data)

    # Gerar relatórios e gráficos
    report_generator = ReportGenerator(sheet_generator)
    report_generator.generate_ward_reports(ward_data)

    # Iniciar a interface gráfica do usuário
    run_ui()

if __name__ == "__main__":
    main()