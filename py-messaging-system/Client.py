import requests

try:
    # Suppress all warnings
    import warnings
    warnings.filterwarnings("ignore")

    input("Please click enter to get the server time")
    r = requests.get('https://localhost:4657/get-server-time', verify=False)
    print(f"Current server time is{r.text} \n")

    var1 = input("Please enter number: ")
    var2 = input("Please enter another number: ")
    r = requests.post('https://localhost:4657/multiply', data=f"{var1},{var2}", verify=False)
    print(f"The result of multiplying the two numbers is: {r.text} \n")

    input("Please click enter to get server request count: ")
    r = requests.get('https://localhost:4657/get-req-count', verify=False)
    print(f"The current server request count is: {r.text} \n")

except Exception as e:
    print(e)
