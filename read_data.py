import requests
from bs4 import BeautifulSoup

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
        'ctl00$ContentPlaceHolder1$txtEmpNo': 'C026730',
        'ctl00$ContentPlaceHolder1$txtDate': '20-May-24',
        'ctl00$ContentPlaceHolder1$btnSearch': 'Search',
    }
    response = session.post(url, data=form_data)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")

    emp_no_label = soup.find("span", {"id": "ContentPlaceHolder1_lblEmpNo"})
    emp_no_value = emp_no_label.text if emp_no_label else None
    emp_name_label = soup.find("span", {"id": "ContentPlaceHolder1_lblEmpName"})
    emp_name_value = emp_name_label.text if emp_name_label else None
    print(f"Emp No: {emp_no_value}")
    print(f"Emp Name: {emp_name_value}")
    print()

    # Get job details
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

            print(f"Job Date: {job_date}")
            print(f"Start Time: {start_time}")
            print(f"End Time: {end_time}")
            print(f"Job Group: {job_group}")
            print(f"Job Title: {job_title}")
            print(f"Job Process: {job_process}")
            print(f"Categories: {categories}")
            print(f"Job Detail: {job_detail}")
            print(f"Time Use: {time_use}")
            print(f"Record Date: {record_date}")
            print("-" * 20)
    else:
        print('job_table', job_table)
