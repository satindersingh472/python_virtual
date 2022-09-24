import wikipedia
import webbrowser
def ask_user():
    user_input = input("Enter any city name of Canada:  ")
    try:
        wikipedia.set_lang('en')
        user_input = wikipedia.page(user_input)
        print(user_input.title)
        print(user_input.content)
        webbrowser.open(user_input.url)
    except wikipedia.exceptions.PageError:
        print('This page does not exists')
    except:
        print('Sorry, something went wrong')
    finally:
        print('thanks for using wikipedia')

ask_user()