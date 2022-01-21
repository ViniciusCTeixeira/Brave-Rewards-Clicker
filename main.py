from Start import Main

if __name__ == "__main__":
    main = Main()
    try:
        main.start()
    except KeyboardInterrupt:
        print("Goodbye!")
