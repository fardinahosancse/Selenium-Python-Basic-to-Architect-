import pytest

def get_data():
    # Define an empty list to store the data
    data = []

    # Open the CSV file and read data
    with open('a.csv', 'r') as csv_file:
        for i in csv_file:
            i = i.strip()  # Remove leading/trailing whitespace
            parts = i.split(',')

            if len(parts) == 2:
                username = parts[0]
                password = parts[1]
                data.append((username, password))

    return data


@pytest.mark.parametrize("username, password", get_data())
def test_doLoginUserNAME(username, password):
    print('----')


