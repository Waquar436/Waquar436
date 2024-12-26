browser_name = input("Enter the browser in which u want to run automation.")
match browser_name:
    case "firefox":
        print("Starting firefox!!!")
    case "chrome":
        print("Execute the chrome code")
    case "edge":
        print("Execute the edge code")
    case "safari":
        print("Execute the safari code")
    case _:
        print("Browser not found!")

