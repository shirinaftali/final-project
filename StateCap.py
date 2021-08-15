""""
5. Ensure the string you created in 4. is alphabetically sorted by state
7. Now we want to add the reverse look up, given the name of a capital what state
is it in?
Implement the function def get_state(capital): below so it returns the state.
GOTCHAS: What happens if two states have the same capital name, how do you
handle that?"""

def capital_of_Idaho():
    cap_idaho = STATES_CAPITALS["Idaho"]
    print(f"idaho capital is {cap_idaho}")
    return cap_idaho


def all_states():
    print(STATES_CAPITALS.keys())
    pass
2
def all_capitals():
    print(STATES_CAPITALS.values())
    pass

def states_capitals_string():

    NEW_STATES_CAPITALS = str(STATES_CAPITALS)
    print(NEW_STATES_CAPITALS.replace(":", "->"))
    pass

def get_state(capital):

    for key, value in STATES_CAPITALS.items():
        if capital == value:
            return key

    return "key doesn't exist"


def test_state_to_capital():
    assert 'Cheyenne' == STATES_CAPITALS['Wyoming']


def test_state_to_capital_unknown():
    with pytest.raises(KeyError):
        STATES_CAPITALS['']


def test_capital_to_state():
    assert 'Wyoming' == get_state('Cheyenne')


def test_capital_to_state_unknown():
    with pytest.raises(KeyError):
        get_state('')


def main():
    return pytest.main(__file__)



User_choose = str("")
User_choose = input("""please chose from below and press the number that
        1. Print the state capital of Idaho
        2. Print all states
        3. Print all capitals.
        4. Create a single string 
        5. Alphabetically sorted by state
        7. Enter a capital and find the state
        0. Exit  
        """)


STATES_CAPITALS = {
    'Alabama' : 'Montgomery',
    'Alaska' : 'Juneau',
    'Arizona' : 'Phoenix',
    'Arkansas': 'Little Rock',
    'California' : 'Sacramento',
    'Colorado' : 'Denver',
    'Connecticut' : 'Hartford',
    'Delaware' : 'Dover',
    'Florida' : 'Tallahassee',
    'Georgia' : 'Atlanta',
    'Hawaii' : 'Honolulu',
    'Idaho' : 'Boise',
    'Illinois' : 'Springfield',
    'Indiana' : 'Indianapolis',
    'Iowa' : 'Des Moines',
    'Kansas' : 'Topeka',
    'Kentucky' : 'Frankfort',
    'Louisiana' : 'Baton Rouge',
    'Maine' : 'Augusta',
    'Maryland' : 'Annapolis',
    'Massachusetts' : 'Boston',
    'Michigan' : 'Lansing',
    'Minnesota' : 'Saint Paul',
    'Mississippi' : 'Jackson',
    'Missouri' : 'Jefferson City',
    'Montana' : 'Helena',
    'Nebraska' : 'Lincoln',
    'Nevada' : 'Carson City',
    'New Hampshire' : 'Concord',
    'New Jersey' : 'Trenton',
    'New Mexico' : 'Santa Fe',
    'New York' : 'Albany',
    'North Carolina' : 'Raleigh',
    'North Dakota' : 'Bismarck',
    'Ohio' : 'Columbus',
    'Oklahoma' : 'Oklahoma City',
    'Oregon' : 'Salem',
    'Pennsylvania' : 'Harrisburg',
    'Rhode Island' : 'Providence',
    'South Carolina' : 'Columbia',
    'South Dakota' : 'Pierre',
    'Tennessee' : 'Nashville',
    'Texas' : 'Austin',
    'Utah' : 'Salt Lake City',
    'Vermont' : 'Montpelier',
    'Virginia' : 'Richmond',
    'Washington' : 'Olympia',
    'West Virginia' : 'Charleston',
    'Wisconsin' : 'Madison',
    'Wyoming' : 'Cheyenne',
}


if User_choose == "1":
    capital_of_Idaho()
if User_choose == "2":
    all_states()
if User_choose == "3":
    all_capitals()
if User_choose == "4":
    states_capitals_string()
if User_choose == "5":
    print("!")
if User_choose == "7":
    capital = input("for which capital you asking about the state name: ")
    print(get_state(capital))




