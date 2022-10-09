
# NOKflex math solver ( cheat )

This script allows users to automatically solve math questions to earn points. 
## Installation process


```bash
  # Clone Repo
  git clone https://github.com/ismail424/nokflex_automatic_solver
  cd nokflex_automatic_solver
  
  # Install requirements
  pip3 install -r requirements.txt

  # Add token and course_id inside app.py
  token = "your token"
  course_id  = "your course_id"

  #Run script for one assignment
  python3 bot.py --id {assignment_id} 

  #Run script for all assignments 
  python3 bot.py --id {assignment_id} --all True
```
## Arguments for the script.
![Arguments for the program](https://i.imgur.com/3VWRyTt.png)



## FAQ

#### How to get token and group_id?

Get it from inpect element tool. You will find the token under the requests headers. 

Under requests headers copy the text beside Authorization: Bearer "YOUR TOKEN" and paste it inside app.py

You can find course id also in request!

![Inspect element ](https://i.imgur.com/LRisFsY.png)

## DEMO
This is a demo of me solving assignment (144035 ) by the script!

![Running script](https://i.imgur.com/CIjzb3g.gif) 

I got the +10 points!
![Screenshoot of the problem solved](https://i.imgur.com/uvmcDOL.png)
