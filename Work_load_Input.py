import requests

'''
payload = {
    "pJobNo": "",
    "pEmpNo": "C026730",
    "pDept": "5603",
    "pJobDate": "01-Apr-24",
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
'''


def input_workload(EmpNo, JobDate, StartTime, FinishTime, TimeUse, JobGroup, JobTitle, JobProcess, Cate, JobDetail):
    payload = {
        "pJobNo": "",
        "pEmpNo": EmpNo,
        "pDept": "5603",
        "pJobDate": JobDate,
        "pStartTime": StartTime,
        "pFinishTime": FinishTime,
        "pTimeUse": TimeUse,
        "pJobGroup": JobGroup,
        "pJobTitle": JobTitle,
        "pJobProcess": JobProcess,
        "pCate": Cate,
        "pJobDetail": JobDetail,
        "pUserId": EmpNo,
        "pJobType": "J2",
        "pEvent": "Add"
    }

    with requests.Session() as session:
        login_url = f'http://it-web-sv:1511/General_HR_Online/Default.aspx?UserName={EmpNo}'
        session.get(login_url)

        url = 'http://it-web-sv:1511/General_HR_Online/GHR_S002_Work_load_Input.aspx/updateRecord'
        response = session.post(url, json=payload)
        return response.text


def i_meeting(JobDate):
    res = input_workload(
        EmpNo="C026730",
        JobDate=JobDate,
        StartTime='08:00',
        FinishTime='09:00',
        TimeUse='60',
        JobGroup='01.MEETING',
        JobTitle='01.MORNING MEETING',
        JobProcess='02.MORNING JOB FOLLOW UP',
        Cate='ROUTINE',
        JobDetail='meeting'
    )
    print(JobDate, 'input meeting >', res)


def i_coding_auto_inspection(JobDate):
    res = input_workload(
        EmpNo="C026730",
        JobDate=JobDate,
        StartTime='09:00',
        FinishTime='17:00',
        TimeUse='420',
        JobGroup='04.DEBUG',
        JobTitle='03.DX PROJECT',
        JobProcess='02.DEBUG',
        Cate='ROUTINE',
        JobDetail='coding auto inspection'
    )
    print(JobDate, 'input coding auto inspection >', res)
