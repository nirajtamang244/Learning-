# throws an error if the file does not exits and reads the document if the file exists


try:
    with open ("/Users/nirajtamang/Documents/Projects/ Learning Back & ML/Phase 1/Week 2/Lambda Functions, Error Handling, Python Modules/data.txt","r") as folder:
        variable= folder.read()
        print(f"The file is opened and the details are as follows:\n {variable}")

except FileNotFoundError:
    print("The file does not exist.")

finally:
    print("Thank you for using our program.")