# [1]  The finally code block is also a part of the Exception handelinng,

# [2] When we hanndel exception using the try and except block We cann include a finally block at the end 

# [3] The finally block always excuted so it is genrally usedd for doing teh concluding task like , Closing File Rescouses , Closing Database Connection , Or may be ending of program execution with the deihtful massege


#  SYNTAX

# try:
#     # statment which should genrate exceptption
# except:
#     # soution of genrated exception
# finally:
#     # Block of code which is going to execute in any siituation


#  NOTE -->  The finally block iss excuted irrespective of the outcome of try..... expect....else  block
#  ---->> One of the importat use cases of finally block is in a function which return a value



# EXAMPLE 
def func1():
    try:
        list1 = [1, 10, 5, 20, 30]
        i = int(input("Enter the index: "))
        print(list1[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("I'm always executed")

x = func1()
print(x)
