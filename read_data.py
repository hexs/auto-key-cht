import requests

payload = {
  '__VIEWSTATE': 'CldEs0UlTl%2BE%2F1DqYukYM3M%2BHZdTJw3pKhXPYkrbEZublFvOa9cuwt0m%2BWxkj1KyMk%2B9s9Z8K8kiim6FU7MTZr36kTYd4TpSEPMRWUV8TwJ5Wq8olf90F2BRxeQm%2BMtovGzdWFSE6w7xZHy2AbnZIwog%2BLNdq%2BT8SQuczqKNYOoXGuaUAMAXAWJulyndH0rTeiW%2Balqtup7JtXh9QgiZ3zDpYu97hqdWPCXWegWtk9hpCdd3Tvip5VAvY7zHR3itBSBB563i2DHAa18pNTTyYJXj5PwmaiPgaP4a%2FpZHpfVX9o1CIs%2ByqdnZOE1Sl%2B2Tn1xo9FfpX%2FaHw4lEYKe3cxdBEhJwm8aNCOKTtH5Wewy2RYhywLWYxBctMfvr%2BNdmco4cEfYwXH9ZMuuo6xjVhgFrH1fbmCAyzh1c4YXwhoK6KDO3l6SFFqB6FBH3p09CVIZWz0q%2FYl83pJxlVnYZVoJV0RTtNFduuudhKTAdb1fQtVXtdgCjw6%2BAoMLPNemhL%2Be4yFnnxjJPaQVIiB4Lr3Mn7ssGOcK4TQTJKbceaAeW14V75l4qCgSgGsbNuDwFLdHy4FkLKMCSB2h8NgOCGL1SFr%2FJQE5KoKp8qt2pjpEHA5rHG0Ixy5lsWqRXOtAz1p3vlff6mgWBd4r%2FqHeZ%2Bdcllnp3Y2Mi%2BeFSzaau5QMx2DXlqDt8qBpAl5F57XQI3eR8GrT72YTJw93JNtxAQN3T257fkU7%2BMPRmxbQ21nrWZmr%2FIYkMhLkkugUqVXVGaz3qDzPyvgIeBIIHDaA3LQ0KaL0%2F3a3Sr692Aafg3cCWTBIwCKsyf5Ih8iM8S2SCx57qD1IOl%2BPNJsC57VQaoWVNKzvzxYSsv%2F%2FivyS64TMFe6g%2F0vxknmJn%2FFiLjRgwGTtjYszryx1NShs9NI7ym5pcYJApeJipZqzAWCe2U4yMdADxwUGyruDMlvRnToa5AtLp1ZJxQftelNuUPOC666SGDq9vBjxrxY2KVSXlTmzzHrRQC2fpZ%2BDeIGAts9mE1pgKqLdIhO%2BdhiTlpyrUj5dG8ylvR%2FH%2FDA1xOi3lyeWdbddSm7ms9t3x1%2F2qyy2PkzDoZVwTKHtIKuWwLwVzIXb3Hg3Ttg%2FX4l3FZTJETaDN4FvNzchWZTcVbJpXMt7fOtRnAMHR6QyjDWVKG9OZ6TWyt4AX%2F5yvOnghAnlA7VYskB%2ByoZgCUuSmbPmiC4MdNIRhS10JYKuYI972T8OhuEB8Xzpyg%2FQeKSGfhmSRVsC0gKzHjMmtjWgNdN3IWiXihsuTUZMZFTKc%2B1hMItE7yyVIYH%2FI7bXZjbKEVMg29b2IC1RJkr0gWaLA45T5BzqtSOwGfpMx5ijfCimQPgcPvw%3D%3D',
  '__VIEWSTATEGENERATOR': 'F892CD2F',
  '__VIEWSTATEENCRYPTED': '',
  'ctl00%24ContentPlaceHolder1%24txtEmpNo': 'C026730',
  'ctl00%24ContentPlaceHolder1%24txtDate': '14-Mar-24',
  'ctl00%24ContentPlaceHolder1%24btnSearch': 'Search',
  'ctl00%24ContentPlaceHolder1%24hdnRowIndex': '',
  'ctl00%24ContentPlaceHolder1%24txtJobDate': '',
  'ctl00%24ContentPlaceHolder1%24txtTimeStart': '',
  'ctl00%24ContentPlaceHolder1%24txtTimeEnd': '',
  'ctl00%24ContentPlaceHolder1%24txtTimeUse': '',
  'ctl00%24ContentPlaceHolder1%24txtForEmpNo': 'C026730',
  'ctl00%24ContentPlaceHolder1%24txtJobDetail': '',
  'ctl00%24ContentPlaceHolder1%24hdnUserId': 'C026730',
  'ctl00%24ContentPlaceHolder1%24hdnDept': '5603',
  'ctl00%24ContentPlaceHolder1%24hdnJobNo': '',
  'ctl00%24ContentPlaceHolder1%24hdnJobType': 'J2',
  'ctl00%24ContentPlaceHolder1%24hdnEmpNo': '',
  'ctl00%24ContentPlaceHolder1%24hdnJobDate': ''
}
with requests.Session() as session:
    login_url = f'http://it-web-sv:1511/General_HR_Online/Default.aspx?UserName=C026730'
    session.get(login_url)
    url = 'http://it-web-sv:1511/General_HR_Online/GHR_S002_Work_load_Input.aspx?SystemName=WORKLOAD+SYSTEM&FormName=WORKLOAD+DATA+ENTRY+SCREEN'
    response = session.post(url, json=payload)
    print(response.text)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(response.text)
