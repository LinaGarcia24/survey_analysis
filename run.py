import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('survey_data')


survey_data = []


def get_survey_data():
    """
    Collects survey answers from user.
    """
    print("Where do you live?")
    country = input("Country: \n")
    print("If in the US, which state or territory of the USA do you live in? If not in the US type 'NA'.")
    state = input("State: \n")
    print("If in the UK, which part of the United Kingdom do you live in? If not in the UK type 'NA'.")
    uk_region = input("UK Region: \n")
    print("Which programming, scripting, and markup languages have you done extensive development work in over the past year? Type all that apply and separate each with a semicolon (;).")
    languages = input("Languages: \n")
    print("Which programming, scripting, and markup languages do you want to do extensive development work in the next year? Type all that apply and separate each with a semicolon (;).")
    future_languages = input("Future Languages: \n")
    print("What is your age?")
    age = input("Age: \n")
    print("What is your gender? Enter 'Prefer not to say' if you do not wish to respond.")
    gender = input("Gender: \n")
    print("Do you identify as transgender? Enter 'Prefer not to say' if you do not wish to respond.")
    trans = input("Transgender: \n")
    print("What is your sexuality? Enter 'Prefer not to say' if you do not wish to respond.")
    sexuality = input("Sexuality: \n")
    print("What is your Ethnicity? Enter 'Prefer not to say' if you do not wish to respond.")
    ethnicity = input("Ethnicity: \n")

    survey_data.append(country)
    survey_data.append(state)
    survey_data.append(uk_region)
    survey_data.append(languages)
    survey_data.append(future_languages)
    survey_data.append(age)
    survey_data.append(gender)
    survey_data.append(trans)
    survey_data.append(sexuality)
    survey_data.append(ethnicity)
    
    return survey_data


get_survey_data()
