# Thesis Progress

A script that makes progress bar from the number of PDFs.

## Requirement
- PyPDF2
- requests
- requests-oauthlib
```
pip3 install pypdf2 requests requests-oauthlib
```
## USAGE
If you want to tweet or update your profile, edit CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN and ACCESS_TOKEN_SECRET in config.py.
Just print progress bar, you don't need edit config.py.
```
thesis_progress.py [-h] {tweet,print,update_profile} ...
```
### tweet command usage
```
thesis_progress.py tweet [-h] [-c CUSTOMIZE] [-f FILE] [-g GOAL]

optional arguments:
  -h, --help            show this help message and exit
  -c CUSTOMIZE, --customize CUSTOMIZE
                        customize tweet. put `%BAR%` where you want to put the progress bar.
  -f FILE, --file FILE  file name
  -g GOAL, --goal GOAL  goal page
```
### print command usage
```
thesis_progress.py print [-h] [-c CUSTOMIZE] [-f FILE] [-g GOAL]

optional arguments:
  -h, --help            show this help message and exit
  -c CUSTOMIZE, --customize CUSTOMIZE
                        customize text. put `%BAR%` where you want to put the progress bar.
  -f FILE, --file FILE  file name
  -g GOAL, --goal GOAL  goal page
  

```
### update_profile command usage
```
thesis_progress.py update_profile [-h] [-c CUSTOMIZE] [-f FILE] [-g GOAL]

optional arguments:
  -h, --help            show this help message and exit
  -c CUSTOMIZE, --customize CUSTOMIZE
                        customize profile description. put `%BAR%` where you want to put the progress bar.
  -f FILE, --file FILE  file name
  -g GOAL, --goal GOAL  goal page
```

# input example
```
./thesis_progress.py print -f /Users/jau5/Documents/workspace/修論/main.pdf -c "修論進捗 %BAR%" -g 50
```
# output example
```
修論進捗 | ##############------ | 74.0%
```
