import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from prettytable import PrettyTable
import pandas as pd
from constant import *


class WorkLoad:
    def __init__(self, year, holiday, EmpNo):
        '''
        :param year: 2024
        :param holiday: datetime list
        :param EmpNo: "C026730"
        '''
        self.year = year
        self.holiday = holiday
        self.EmpNo = EmpNo
        self.df = None
        self.JobDate = None
        self.data = {}

    def read_work_load(self, JobDate):
        '''
        :param JobDate: 02-May-24
        :return:
        '''

        with requests.Session() as session:
            # log in
            login_url = f'http://it-web-sv:1511/General_HR_Online/Default.aspx?UserName=C026730'
            session.get(login_url)

            # Get view state
            url = 'http://it-web-sv:1511/General_HR_Online/GHR_S002_Work_load_Input.aspx?SystemName=WORKLOAD+SYSTEM&FormName=WORKLOAD+DATA+ENTRY+SCREEN'
            response = session.get(url)
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(response.text)
            soup = BeautifulSoup(response.content, "html.parser")
            view_state = soup.select_one("#__VIEWSTATE")["value"]

            # Get data
            form_data = {
                "__VIEWSTATE": view_state,
                'ctl00$ContentPlaceHolder1$txtEmpNo': self.EmpNo,
                'ctl00$ContentPlaceHolder1$txtDate': JobDate,
                'ctl00$ContentPlaceHolder1$btnSearch': 'Search',
            }
            response = session.post(url, data=form_data)
            html_content = response.content
            soup = BeautifulSoup(html_content, "html.parser")

            emp_no_label = soup.find("span", {"id": "ContentPlaceHolder1_lblEmpNo"})
            emp_no_value = emp_no_label.text if emp_no_label else None
            emp_name_label = soup.find("span", {"id": "ContentPlaceHolder1_lblEmpName"})
            emp_name_value = emp_name_label.text if emp_name_label else None

            # Get job details
            data_frame = {
                "job_date": [],
                "start_time": [],
                "end_time": [],
                "job_group": [],
                "job_title": [],
                "job_process": [],
                "categories": [],
                "job_detail": [],
                "time_use": [],
                "record_date": []
            }

            job_table = soup.find("table", {"id": "ContentPlaceHolder1_gvShowData"})
            if job_table:
                job_rows = job_table.find_all("tr")[1:]  # Skip the header row
                for row in job_rows:
                    cells = row.find_all("td")
                    job_date = cells[2].text.strip()
                    start_time = cells[3].text.strip()
                    end_time = cells[4].text.strip()
                    job_group = cells[5].text.strip()
                    job_title = cells[6].text.strip()
                    job_process = cells[7].text.strip()
                    categories = cells[8].text.strip()
                    job_detail = cells[9].text.strip()
                    time_use = cells[10].text.strip()
                    record_date = cells[11].text.strip()

                    data_frame["job_date"].append(job_date)
                    data_frame["start_time"].append(start_time)
                    data_frame["end_time"].append(end_time)
                    data_frame["job_group"].append(job_group)
                    data_frame["job_title"].append(job_title)
                    data_frame["job_process"].append(job_process)
                    data_frame["categories"].append(categories)
                    data_frame["job_detail"].append(job_detail)
                    data_frame["time_use"].append(int(time_use))
                    data_frame["record_date"].append(record_date)

            self.df = pd.DataFrame(data_frame)
            self.data[JobDate] = self.df


    def show_work_load_table(self, JobDate):
        df = self.data[JobDate]
        table = PrettyTable()
        table.field_names = df.columns
        table.align['job_group'] = 'l'
        table.align['job_title'] = 'l'
        table.align['job_process'] = 'l'
        table.align['job_detail'] = 'l'
        for row in df.itertuples(index=False):
            table.add_row(row)
        print(table)

    def show_work_load_time_use(self, JobDate):
        df = self.data[JobDate]
        total_time_use = df['time_use'].sum()
        if total_time_use < 480:
            print(f'{JobDate}: time use is {YELLOW}{total_time_use}{ENDC} min')
        elif total_time_use == 480:
            print(f'{JobDate}: time use is {GREEN}{total_time_use}{ENDC} min')
        elif 480 < total_time_use < 600:
            print(f'{JobDate}: time use is {YELLOW}{total_time_use}{ENDC} min')
        elif total_time_use > 600:
            print(f'{JobDate}: time use is {RED}{total_time_use}{ENDC} min')
        return total_time_use

    def input_workload(self, JobDate, StartTime, FinishTime, TimeUse,
                       JobGroup, JobTitle, JobProcess, Cate, JobDetail):
        '''
        :param JobDate: "01-Apr-24"
        :param StartTime: "08:00"
        :param FinishTime: "09:00"
        :param TimeUse: "60"
        :param JobGroup: "01.MEETING"
        :param JobTitle: "01.MORNING MEETING"
        :param JobProcess: "02.MORNING JOB FOLLOW UP"
        :param Cate: "ROUTINE"
        :param JobDetail: "meeting"
        :return: response.text
        '''

        payload = {
            "pJobNo": "",
            "pEmpNo": self.EmpNo,
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
            "pUserId": self.EmpNo,
            "pJobType": "J2",
            "pEvent": "Add"
        }

        with requests.Session() as session:
            login_url = f'http://it-web-sv:1511/General_HR_Online/Default.aspx?UserName={self.EmpNo}'
            session.get(login_url)

            url = 'http://it-web-sv:1511/General_HR_Online/GHR_S002_Work_load_Input.aspx/updateRecord'
            response = session.post(url, json=payload)
            return response.text

    def i_meeting(self, JobDate):
        res = self.input_workload(
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

    def i_coding_auto_inspection(self, JobDate):
        res = self.input_workload(
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
