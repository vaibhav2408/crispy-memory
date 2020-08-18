import logging

from bidgely.apis import ApisHelper
from bidgely.apis.BaseBidgelyApi import BaseBidgelyApi
from bidgely.utils.jira.payload import PayloadBuilder
from bidgely.utils.reader.ExcelFileParser import ExcelFileParser
from bidgely.utils.reader.config_utils import ConfigUtils

logger = logging.getLogger(__name__)


def execute(filepath):
    """
    The execute method to trigger the JIRA Issue creator in batch
    :return:
    """
    _config_utils = ConfigUtils()
    configs = _config_utils.read_file('globalConfig.yaml')

    print(configs['clientSecret'])

    _excel_file_parser = ExcelFileParser(filepath)
    jira_beans = _excel_file_parser.read_bidgely_jira_sheet()

    _api_caller = BaseBidgelyApi(configs)

    create_issue_uri = ApisHelper.Apis.create_issue
    for jira_bean in jira_beans:
        if jira_bean.sprint is None or jira_bean.sprint == "":
            formatted_payload = PayloadBuilder.get_payload_without_sprint(configs, jira_bean)
        else:
            formatted_payload = PayloadBuilder.get_payload_with_sprint(configs, jira_bean)
        response = _api_caller.post(create_issue_uri, formatted_payload)
        print('Ticket created in project {} \nTicket ID : {}\nLink : {}'.format(jira_bean.project_name, response['key'],
                                                                                configs['browse_jira_url'] +
                                                                                response['key']))