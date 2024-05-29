import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO


class PD_Attendance:
    def __init__(self):
        self.session = requests.Session()

    def log_in(self):
        home_url = f'http://it-src-sv:1213/HRMS_ViewItYourself/default.aspx'

        response = self.session.get(home_url)
        soup = BeautifulSoup(response.content, "html.parser")
        view_state = soup.select_one("#__VIEWSTATE")["value"]
        event_validation = soup.select_one("#__EVENTVALIDATION")["value"]

        form_data = {
            '__VIEWSTATE': view_state,
            '__EVENTVALIDATION': event_validation,
            'ctl00$txt_Id': '1801300254921',
            'ctl00$txt_Emp': '026730',
            'ctl00$btn_login': 'Login',
        }
        self.session.post(home_url, data=form_data)

    def view_state_to_csv(self):
        def view_state_to_csv_(url):
            response = self.session.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            html_table = soup.find('span', {'id': 'ctl00_ContentPlaceHolder1_Mnth'})
            month_and_year = html_table.text
            soup = BeautifulSoup(response.content, 'html.parser', from_encoding='tis620', exclude_encodings='utf-8')
            html_table = soup.find('table', {'id': 'ctl00_ContentPlaceHolder1_GridView1'})

            df = pd.read_html(StringIO(str(html_table)), header=0)[0]
            pd_attendance_dir = os.path.join(os.path.dirname(__file__), 'PD_Attendance')
            os.makedirs(pd_attendance_dir, exist_ok=True)
            df.to_csv(os.path.join(pd_attendance_dir, f'{month_and_year}.csv'), index=False, encoding='utf-8')

        view_state_to_csv_('http://it-src-sv:1213/HRMS_ViewItYourself/Z_PD/PD_Attendance.aspx')
        view_state_to_csv_('http://it-src-sv:1213/HRMS_ViewItYourself/Z_PD/PD_Attendance_Last.aspx')


attendance = PD_Attendance()
attendance.log_in()
attendance.view_state_to_csv()
