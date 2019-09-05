import pandas as pd
from collections import Counter


class Awards:
    """Class that contains methods for opening excel sheets, analysis of data and calculate sales of employees
    in order to grant them awards"""

    def __init__(self):
        self.xlsx = None
        self.sheet = None
        self.data_frame = None
        self.sales_per_employee = {}
        self.amount_of_awards = 0
        self.list_of_awards = []
        self.winners = []

    def open_file(self, file_name: str):
        self.xlsx = pd.ExcelFile(r'{}'.format(str(file_name)))

    def open_sheet(self, sheet_name: str):
        self.sheet = pd.read_excel(self.xlsx, str(sheet_name))

    def set_columns_to_read(self, column1: str, column2: str):
        self.data_frame = pd.DataFrame(self.sheet, columns=['{}'.format(str(column1)), '{}'.format(str(column2))])
        self.sheet = self.data_frame.values.tolist()

    def count_each_employee_sales(self):
        # Iterates through opened sheet and fills dictionary with keys - column 1 and values - column2
        for employee in self.sheet:
            try:
                self.sales_per_employee[employee[0]] += int(employee[1])
            except KeyError:
                self.sales_per_employee.setdefault(employee[0], 0)
                self.sales_per_employee[employee[0]] += int(employee[1])

    def count_amount_of_awards(self):
        for award in self.sheet:
            self.amount_of_awards += int(award[1])

    def append_list_of_awards(self):
        for award in self.sheet:
            self.list_of_awards += [award[0]] * int(award[1])

    def find_winners_among_employees(self):
        # Checks sales_per_employee dictionary and fills list of tuples containing best employees and their sales
        best_employees = Counter(self.sales_per_employee)
        self.winners = best_employees.most_common(self.amount_of_awards)

    def awards_ceremony(self):
        i = 0
        for employee in self.winners:
            print('Place {}: {} \n'
                  'Sales : {}\n'
                  'Award : {}\n'
                  '---------------------'
                  .format(i + 1, employee[0], employee[1], self.list_of_awards[i]))
            i += 1


if __name__ == '__main__':
    styczen = Awards()
    styczen.open_file('sda_clients.xlsx')
    styczen.open_sheet('FAKTURY')

    styczen.set_columns_to_read('Pracownik', 'Wartosc [pln]')
    styczen.count_each_employee_sales()

    styczen.open_sheet('NAGRODY')
    styczen.set_columns_to_read('Lista nagrod', 'Liczba nagrod')

    styczen.count_amount_of_awards()
    styczen.append_list_of_awards()

    styczen.find_winners_among_employees()
    styczen.awards_ceremony()