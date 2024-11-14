```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class ReportGenerator:
    """
    Responsável pela geração de relatórios e gráficos a partir dos dados.
    """
    def __init__(self, sheet_generator):
        self.sheet_generator = sheet_generator

    def generate_ward_reports(self, ward_data):
        """
        Gera relatórios e gráficos para cada unidade do hospital.
        """
        for ward, patients in ward_data.items():
            df = pd.DataFrame(patients)

            # Calcular indicadores da unidade
            occupancy_rate = self._calculate_occupancy_rate(df)
            fugulin_index = self._calculate_fugulin_index(df)
            turnover_rate = self._calculate_turnover_rate(df)

            # Gerar gráficos
            self._generate_device_distribution_plot(df, ward)