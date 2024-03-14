import requests

# login
url = 'http://it-web-sv:1919/SSO_LOGIN.aspx'
payload = {
    '__VIEWSTATE': 'uPoOVUFZodM11nGIP0WI5hMXWck4eu4sf/9doNg2bJwAHH+z05Ay5188HtFa8iug1xnuFY2HHlrEcih3eZV2+CTuFNrWGHOjY0nSQrEQiD8NLv2p3daxbGwX8msb6j9uZo9AlpTwNm/Ns1kP41WhFibrul9f1lwDJDdORN5mXxh66jT4xfEFxxrU7Bo7EVD8JuCo8r0FlS6hTIqD0pGHlmgvERQuCYMBJ8Zd+S3b22VpfVLndF7M1ehfj1/JS2YvLg8CE5g881FUN/9cIPiySQ==',
    '__VIEWSTATEGENERATOR': 'A081907C',
    '__PREVIOUSPAGE': 'US7DcyH2p_wUWCCmAZ0nxy01upy8JFrs9mRdhEKCOGakPoejMM5I3-ycHO1EFp1QpTkIkStIiVa9wYhfBNl8RA2',
    '__EVENTVALIDATION': '+nMY93didlHpbIxYQT1pepUbIibOCAbX3w6XbpaC/SZid97LRgtjyTjuUkKerwGGh5i2qvPchX5SzR8jo9anMUtMjeogIJdVL2KQNi97TZq2HMzUOh7IN6HmjoKB7vD5iol2oRK9ROsnVwKO916PlY2y4hWekn4mxy2KL97jZCHAPK4vbm/dC2n5yNmBqungb4c/mQPQdNvwFPknnIH64uaFpZW5I5XEhXVGIoe7h2WpGqj68XrOKnMLTl5FdEEUUbfzL/a4voTq982m+CX3Tze/gBuD4oEin1Vm9Ha0cpuU4rw56Xj/6LDQY5I24xzfk6jcSpi9x3BFs1P/nzhEiFI8tUHj4FvMFuu1T1Zdp7xOdq0urw5oiZwU611xLWpkuN8/7szAj6i4NilG2ajnng==',
    'ctl00$ContentPlaceHolder1$txtUserID': 'C026730',
    'ctl00$ContentPlaceHolder1$txtPassword': 'Uio90-===',
    'ctl00$ContentPlaceHolder1$btnLogin': 'Login'
}
r = requests.post(url, data=payload)

# input data
url2 = 'http://it-web-sv:1511/General_HR_Online/GHR_S002_Work_load_Input.aspx?SystemName=WORKLOAD+SYSTEM&FormName=WORKLOAD+DATA+ENTRY+SCREEN'
r = requests.get(url2)
print(r.text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(r.text)
