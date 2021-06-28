status_code=500

try:
    if status_code == 200 :
        print("rest call went well")
    elif status_code == 400:
        raise AssertionError("not found!")
    elif status_code == 500:
        raise AssertionError("internal server error")
except AssertionError as e:
    print(e)
