from Start import Main

if __name__ == "__main__":
    main = Main()
    try:
        main.start()
    except KeyboardInterrupt:
        print()
        print("Ads:", main.get_count_ads(), "/", "New Tab Ads:", main.get_count_new_tab_ads())
        print("Goodbye!")
