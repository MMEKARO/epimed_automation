```python
import pandas as pd
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

class DataExtractor:
    """
    Responsável pela extração de dados do sistema Epimed.
    """
    def __init__(self, epimed_connector):
        self.epimed_connector = epimed_connector

    def extract_patient_data(self, patient_id):
        """
        Extrai os dados de um paciente específico do sistema Epimed.
        """
        try:
            html_content = self.epimed_connector.get_patient_data(patient_id)
            soup = BeautifulSoup(html_content, "html.parser")

            # Extração das informações do paciente
            patient_name = soup.find("span", id="ctl00_ContentPlaceHolder1_lblPatientName").text
            admission_date = soup.find("span", id="ctl00_ContentPlaceHolder1_lblAdmissionDate").text
            discharge_date = soup.find("span", id="ctl00_ContentPlaceHolder1_lblDischargeDate").text
            comorbidities = [item.text for item in soup.find_all("span", id="ctl00_ContentPlaceHolder1_lblComorbidities_0")]
            diagnoses = [item.text for item in soup.find_all("span", id="ctl00_ContentPlaceHolder1_lblDiagnosis_0")]
            devices = [item.text for item in soup.find_all("span", id="ctl00_ContentPlaceHolder1_lblDevices_0")]

            patient_data = {
                "nome": patient_name,
                "data_admissao": admission_date,
                "data_alta": discharge_date,
                "comorbidades": comorbidities,
                "diagnosticos": diagnoses,
                "dispositivos": devices
            }

            logger.info(f"Dados do paciente {patient_id} extraídos com sucesso.")
            return patient_data
        except Exception as e:
            logger.error(f"Erro ao extrair dados do paciente {patient_id}: {e}")
            raise e

    def extract_ward_data(self, ward_id):
        """
        Extrai os dados de todos os pacientes de uma determinada unidade do sistema Epimed.
        """
        try:
            # Implementação para obter os dados dos pacientes de uma unidade específica
            pass
        except Exception as e:
            logger.error(f"Erro ao extrair dados da unidade {ward_id}: {e}")
            raise e
```

O módulo `data_extractor.py` é responsável pela extração dos dados do sistema Epimed. Ele contém as seguintes funcionalidades:

1. `__init__(self, epimed_connector)`: Inicializa a classe com uma instância do `EpimedConnector` para realizar as conexões com o sistema.
2. `extract_patient_data(self, patient_id)`: Extrai os dados de um paciente específico, incluindo informações como nome, datas de admissão e alta, comorbidades, diagnósticos e dispositivos invasivos.
3. `extract_ward_data(self, ward_id)`: Extrai os dados de todos os pacientes de uma determinada unidade do hospital (ainda não implementado neste exemplo).

A extração dos dados é feita através do HTML retornado pelo sistema Epimed, utilizando a biblioteca `BeautifulSoup` para navegar e extrair as informações relevantes.

Caso ocorra algum erro durante a extração dos dados, o módulo irá gerar um log de erro com informações relevantes.