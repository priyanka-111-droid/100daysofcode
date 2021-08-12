#__name__ is a special attribute built in python
# A module's __name__ is set equal to '__main__' when file is being directly run by python and NOT being imported.

print(f"First module's name:{__name__}")

if __name__=='__main__':
    print("Run directly")
else:
    print("Run from import")


    