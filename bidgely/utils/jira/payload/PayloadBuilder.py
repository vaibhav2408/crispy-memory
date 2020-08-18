import json


def get_payload_without_sprint(configs, jira_bean):
    payload = configs['payload']['createIssue']['createIssueWithNoSprint']
    formatted_payload = json.loads(payload % (jira_bean.project_name, jira_bean.title, jira_bean.description,
                                              jira_bean.issue_type))
    return formatted_payload


def get_payload_with_sprint(configs, jira_bean):
    payload = configs['payload']['createIssue']['createIssueWithSprint']
    formatted_payload = json.loads(payload % (jira_bean.project_name, jira_bean.title, jira_bean.description,
                                              jira_bean.issue_type, jira_bean.sprint))
    return formatted_payload
