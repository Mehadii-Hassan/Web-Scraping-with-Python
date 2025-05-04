from openpyxl import Workbook

def save_to_excel(data):
    wb = Workbook()
    ws = wb.active
    ws.title = "Website Scan Report"

    ws.append(["Website", "Malware Found", "Contact Info"])
    for row in data:
        ws.append(row)

    wb.save("infected_websites.xlsx")
