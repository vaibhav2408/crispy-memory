import logging

from jira.apis import ApisHelper
from jira.apis.BaseApiCaller import BaseApiCaller
from jira.utils.jira.payload import PayloadBuilder
from jira.utils.reader.ExcelFileParser import ExcelFileParser
from jira.utils.reader.config_utils import ConfigUtils

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
    jira_beans = _excel_file_parser.read_jira_excel_sheet()

    _api_caller = BaseApiCaller(configs)

    create_issue_uri = ApisHelper.Apis.create_issue
    for jira_bean in jira_beans:
        if jira_bean.sprint is None or jira_bean.sprint == "":
            formatted_payload = PayloadBuilder.get_payload_without_sprint(configs, jira_bean)
        else:
            formatted_payload = PayloadBuilder.get_payload_with_sprint(configs, jira_bean)
        response = _api_caller.post(create_issue_uri, formatted_payload)

        logger.info('Ticket created in project {} '.format(jira_bean.project_name))
        logger.info('Ticket ID : {}'.format(response['key']))
        logger.info('Ticket Link : {}'.format(configs['browse_jira_url'] + response['key']))
