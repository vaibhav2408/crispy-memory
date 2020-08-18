class IssueBean:
    """
    The bean class for jira issue fields
    """

    project_name = None
    issue_type = "Task"
    title = None
    description = None
    sprint = ""
    assignee = ""
    components = ""
    labels = ""

    def __init__(self, project_name, issue_type, title, description, sprint, assignee, components, labels):
        self.project_name = project_name
        self.issue_type = issue_type
        self.title = title
        self.description = description
        self.sprint = sprint
        self.assignee = assignee
        self.components = components
        self.labels = labels
