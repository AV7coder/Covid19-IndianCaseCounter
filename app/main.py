from pyautogui import prompt, alert
from covid_india import states

while True:
    state = prompt("Enter the state you want to get results for:", "State")
    data=(states.getdata(state))
    alert(f'''State: {state} 
Total Cases: {data['Active']+data['Cured']+data['Death']}
Active Cases: {data['Active']}
Cured Cases: {data['Cured']}
Deaths: {data['Death']}''')