class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError

class Apis(Enum):
    create_issue = "/rest/api/2/issue/"
    assign_issue = "/rest/api/3/issue/PLATFORM-178/assignee"