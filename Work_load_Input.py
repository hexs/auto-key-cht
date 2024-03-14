import requests

payload = {
    "pJobNo": "",
    "pEmpNo": "C026730",
    "pDept": "5603",
    "pJobDate": "14-Mar-24",
    "pStartTime": "08:00",
    "pFinishTime": "09:00",
    "pTimeUse": "60",
    "pJobGroup": "01.MEETING",
    "pJobTitle": "01.MORNING MEETING",
    "pJobProcess": "02.MORNING JOB FOLLOW UP",
    "pCate": "ROUTINE",
    "pJobDetail": "meeting",
    "pUserId": "C026730",
    "pJobType": "J2",
    "pEvent": "Add"
}

with requests.Session() as session:
    login_url = f'http://it-web-sv:1511/General_HR_Online/Default.aspx?UserName=C026730'
    session.get(login_url)

    url = 'http://it-web-sv:1511/General_HR_Online/GHR_S002_Work_load_Input.aspx/updateRecord'
    response = session.post(url, json=payload)
    print(response.text)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(response.text)
