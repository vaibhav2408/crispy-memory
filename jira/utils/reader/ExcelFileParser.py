import logging

import xlrd

from jira.utils.jira.issue_bean.Issuebean import IssueBean

logger = logging.getLogger(__name__)


class ExcelFileParser:
    """
    Excel file reader class
    Pass the excel file path in the constructor args
    """

    file_path = None

    def __init__(self, file_path):
        self.file_path = file_path

    def read_jira_excel_sheet(self):
        """
            The sheet is of format:
            ROW 1 - Guidelines.
            ROW 2 - Headings
            ROW 3 onwards - JIRA Content

            Hence we start parsing from ROW 3
        """

        if self.file_path is None:
            logger.error("File path is null. Returning None")
            return None

        wb = xlrd.open_workbook(self.file_path)
        sheet = wb.sheet_by_index(0)

        jira_beans = list()

        row_index = 0
        logger.info(
            "Reading the rows of the excel. Number of rows : {}. \nNumber of columns {} :".format(sheet.nrows,
                                                                                                  sheet.ncols))
        for row in sheet.get_rows():
            row_index += 1
            if row_index > 2:
                cell_fields = list()
                for cell in row:
                    cell_fields.append(cell.value)
                issue_bean = IssueBean(*cell_fields)
                jira_beans.append(issue_bean)
        logger.info("Done reading the rows of the excel. Returning the values")
        return jira_beans
