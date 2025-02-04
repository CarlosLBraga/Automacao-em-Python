import xlsxwriter
import os

caminho_excel = "C:\\Users\\recepcao\\Desktop\\Cadu\\caminho_excel\\teste.xlsx"
planilha_teste = xlsxwriter.Workbook(caminho_excel)
planilha1 = planilha_teste.add_worksheet()

planilha1.write("A1", "Nome")
planilha1.write("A2", "Cadu")
planilha1.write("A3", "AnA")

planilha1.write("B1", "Idade")
planilha1.write("B2", "23")

planilha1.write("B3", "21")





planilha_teste.close()
os.startfile(caminho_excel)