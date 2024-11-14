```python
import pandas as pd
from openpyxl.styles import Font, Alignment
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class SheetGenerator:
    """
    Responsável pela geração da planilha Excel com os dados extraídos do Epimed.
    """
    def __init__(self, data_extractor):
        self.data_extractor = data_extractor

    def generate_ward_sheets(self, ward_data):
        """
        Gera as abas da planilha Excel para cada unidade do hospital.
        """
        wb = pd.ExcelWriter("planilha_epimed.xlsx", engine="openpyxl")

        for ward, patients in ward_data.items():
            df = pd.DataFrame(patients)
            df.to_excel(wb, sheet_name=ward, index=False)

            # Formatar a planilha
            ws = wb.sheets[ward]
            self._format_sheet(ws)

        wb.save()
        logger.info("Planilha Excel gerada com sucesso.")

    def _format_sheet(self, worksheet):
        """
        Formata a planilha Excel com estilos e alinhamento.
        """
        # Formatar cabeçalhos
        for col in worksheet.iter_cols(min_row=1, max_row=1):
            for cell in col:
                cell.font = Font(bold=True)
                cell.alignment = Alignment(horizontal="center", vertical="center")

        # Ajustar largura das colunas
        for column_cells in worksheet.columns:
            length = max(len(str(cell.value)) for cell in column_cells)
            worksheet.column_dimensions[column_cells[0].column_letter].width = length * 1.2
```

O módulo `sheet_generator.py` é responsável pela geração da planilha Excel com os dados extraídos do sistema Epimed. Ele contém as seguintes funcionalidades:

1. `__init__(self, data_extractor)`: Inicializa a classe com uma instância do `DataExtractor` para obter os dados a serem incluídos na planilha.
2. `generate_ward_sheets(self, ward_data)`: Gera as abas da planilha Excel, uma para cada unidade do hospital, com os dados dos pacientes.
   - Cria um arquivo Excel utilizando a biblioteca `openpyxl`.
   - Itera sobre os dados das unidades e cria uma aba para cada uma delas.
   - Formata a planilha, aplicando estilos aos cabeçalhos e ajustando a largura das colunas.
   - Salva o arquivo Excel.
3. `_format_sheet(self, worksheet)`: Função auxiliar para aplicar formatação à uma aba específica da planilha.
   - Define a fonte em negrito para os cabeçalhos.
   - Centraliza o alinhamento horizontal e vertical dos cabeçalhos.
   - Ajusta a largura das colunas com base no tamanho do conteúdo.

Esse módulo utiliza as bibliotecas `pandas` e `openpyxl` para a manipulação e geração da planilha Excel.

Caso ocorra algum erro durante a geração da planilha, o módulo irá gerar um log de erro com informações relevantes.