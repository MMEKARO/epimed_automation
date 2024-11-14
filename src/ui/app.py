import tkinter as tk
from tkinter import ttk
from .components import PatientTable, IndicatorsChart
from epimed_automation.sheet_generator import SheetGenerator
from epimed_automation.report_generator import ReportGenerator

class EpimedApp(tk.Tk):
    def __init__(self, sheet_generator, report_generator):
        super().__init__()
        self.title("Automação da Planilha do Epimed")

        # Instâncias dos geradores de planilha e relatório
        self.sheet_generator = sheet_generator
        self.report_generator = report_generator

        # Criar os principais componentes da interface
        self.patient_table = PatientTable(self)
        self.indicators_chart = IndicatorsChart(self)

        # Organizar os componentes na janela principal
        self.patient_table.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.indicators_chart.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Botões para atualizar, carregar planilha, converter para PDF e imprimir
        self.create_action_buttons()

    def create_action_buttons(self):
        # Implementar a lógica para cada ação
        pass

def run_ui():
    app = EpimedApp(SheetGenerator, ReportGenerator)
    app.mainloop()