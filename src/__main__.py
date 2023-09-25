import dotenv

from view.connection_view import ConnectionView

# This script is the entry point of your application

if __name__ == "__main__":
    dotenv.load_dotenv(override=True)

    # run the Connection View
    current_view = ConnectionView()

    # while current_view is not none, the application is still running
    while current_view:
        # a border between view
        with open("src/graphical_assets/border.txt", "r", encoding="utf-8") as asset:
            print(asset.read())
        # Display the info of the view
        current_view.display_info()
        # ask user for a choice
        current_view = current_view.make_choice()

    with open(
        "src/graphical_assets/suprised_pikachu.txt", "r", encoding="utf-8"
    ) as asset:
        print(asset.read())
