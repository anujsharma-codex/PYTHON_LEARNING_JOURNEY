from Solar.Data_Pipeline import*
from pathlib import Path
# helping functions - 

def get_int_input(ch):
   if ch == "" :
       return ""
   else:
       return int(ch)
   
def get_float_input(ch):
    if ch == "":
        return ""
    else:
        return float(ch)
   
# object creation-
def data_handling_obj_creation(ofile, nfile):
    dh_obj = DataHandling(ofile, nfile)
    return dh_obj

def data_quality_obj_creation(dh_obj):
    dq_obj = Data_Quality(dh_obj)
    return dq_obj

def main():
    while True:

        ofile = str((input("Enter the original file name: ")).strip())
        nfile = str((input("Enter the new file location for storing the cleaned file: ")).strip())
        folder_path = Path("data/")
        file_name = ofile
        full_path = folder_path/file_name

        if full_path.exists():
            print("Original File found !!!")
            dh_obj = data_handling_obj_creation(ofile, nfile)
        else:
            print("File Not Found!!! Object not created!!!")
            break        
        
        while True:    
            print("""Menu:
                1. Report Data Quality
                2. Handle Data""")

            ch = get_int_input((input("Enter the choice number: ")).strip())
            if ch == "":
                print("Exiting...")
                break
            elif ch == 1:
                while True:

                    dq_obj = data_quality_obj_creation(dh_obj)
                    
                    print("\n" + "="*50)
                    print("""Options:-
                          1. Get missing value report
                          2. Get Duplicates report
                          3. Get Duplicate rows
                          4. Get Data Type report
                          5. Get Statistical Summary
                          6. Get Zero Count
                          7. Get Negative Count
                          \n""")
                    print("\n" + "="*50)
                    ch = get_int_input((input("Enter your choice or press 'Enter' to cancel: ")).strip())
                    if ch == "":
                        print("Exiting")
                        break

                    elif ch == 1:
                        print("Your missing value report: \n")
                        rep = dq_obj.get_missing_values()
                        print(rep)

                    elif ch == 2:
                        print("Your duplicate calculation report:\n")
                        count = dq_obj.get_duplicate_calculation()
                        print(f"There are {count} duplicate rows in your dataset.")
                        
                    elif ch == 3:
                        print("Your each duplicate rows: \n")
                        rep = dq_obj.get_duplicate_rows()
                        print(rep)

                    elif ch == 4:
                        print("Your Data Type Report: \n")
                        rep = dq_obj.get_datatype_report()
                        print(rep)

                    elif ch == 5:
                        print("Your Statistical Report: \n")
                        rep = dq_obj.get_stat_summary()
                        print(rep)

                    elif ch == 6:
                        print("Your Zero Count Report: \n")
                        rep = dq_obj.get_zero_count()
                        print(rep)

                    elif ch == 7:
                        print("Your Negative Count Report: \n")
                        rep = dq_obj.get_negative_count()
                        print(rep)

                    else:
                        print("Choose from given Options!!!")
                        break

            elif ch == 2:
                print("You chose Data Handling...")
                print("These are the options: \n")
                
                while True:
                    print("\n" + "="*50)
                    print("""
                    1. Filter cols
                    2. Handle Missing Values
                    3. Handle Duplicate Values
                    4. Handle Outliers
                    5. Handle Datatypes
                    6. Assign the clean data to new file
                    """)
                    print("\n" + "="*50)

                    ch = get_int_input(input("Enter the choice or press ENTER to exit: "))
                    if ch == "":
                        print("Exiting !")
                        break

                    elif ch == 1:
                        dh_obj.filter_cols()
                        print("Columns Filtered !!!")

                    elif ch == 2:
                        dh_obj.handle_missing_values()
                        print("Missing Values Handled")

                    elif ch == 3:
                        dh_obj.handle_duplicate_values()
                        print("Duplicate Values Handled !!!")

                    elif ch == 4:
                        dh_obj.handle_outliers()
                        print("Ouliers Handled !!!")

                    elif ch == 5:
                        dh_obj.handle_datatypes()
                        print("Datatypes Handled !!!")

                    elif ch == 6:
                        new_loc = dh_obj.data_feeding()
                        print(f"New Data Saved To the new file location: /n {new_loc}")                       
                    
                    else:
                        print("Invalid input, exiting")
                        break

            else:
                print("Your Choice Does Not Exist (Enter available choice only)")
                break



if __name__ == "__main__":
    main()