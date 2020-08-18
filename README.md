# crispy-memory

## Description ##
This repository can be used to create JIRA tickets in bulk.

### Development Setup ###
1. Import the project, install the dependencies using the requirements.txt file.
1. Add the following fields to the file at path - `jira/configs/globalConfig.yaml`
    1. The company URL for JIRA dashboard
    1. The username(emailID which you use for login)
    1. The auth token generated from JIRA dashboard for your account.

### How To Run###
1. Enter the values in the spreadsheet, present in the root folder, named `Jira-Bulk-Issue-Creator.xlsx`
1. The file `trigger.py` shall be used as the main file.
1. Pass the full path of the file as input parameter.
1. Catch all the logs in the console.
