import wikipedia

def ask_user():
    user_input = input("Enter any city name of Canada:  ")
    try:
        user_input = wikipedia.page(user_input)
        print(user_input.title)
        print(user_input.content)
    except:
        print('Not a valid entry, page does not exists')
    finally:
        print('thanks for using wikipedia')

ask_user()