def main():

    try:
        # user input
        user_number = int(input("Enter a whole number: "))
        # negative input catch
        if user_number <= 0:
            print(" {} is not a whole number".format(user_number))
        # loop
        for loop_counter in range(user_number):
            print("{0} time through loop.".format(loop_counter))
            print("")
            power = loop_counter ** 2
            print("{} to the power of 2 = {}".format(loop_counter, power))

    # invalid input catch
    except ValueError:
        print("invalid input")
    finally:
        print("thank you for using this program")


if __name__ == "__main__":
    main()
