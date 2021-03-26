from covid_india import states
while True:
    state = str(input("Enter the state:"))
    data=(states.getdata(state))
    print(f'''State:{state}
Total Cases:{data["Active"]+data["Cured"]+data["Death"]}
Active Cases:{data["Active"]}
Cured Cases: {data["Cured"]}
Deaths: {data["Death"]}''')
