
def main():
    count=0;
    a=range(1,101);
    print("not executed")
    for i in a:

        if(i%2==0):
            count = count + 1
            print(i)
print(count)
if __name__ == "__main__":
    main()