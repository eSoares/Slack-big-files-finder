# Find big files in your Slack

This script aims to help users find big files in a slack workspace.


## How to use

Get yourself a token in [https://api.slack.com/custom-integrations/legacy-tokens](https://api.slack.com/custom-integrations/legacy-tokens)

Run the script:
> python script.py YOUR_TOKEN_HERE

It will print the five biggest files on your team and the total size of public files that you have.


## Notes

 - The script takes some time to run if you have a huge number of files.
 - The script will not count files shared between other users, so the total file size that will find will be different 
 from the one [here](https://manfios.slack.com/admin/stats).