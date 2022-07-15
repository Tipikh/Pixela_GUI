import requests
import json
import webbrowser

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
COLOR_NAMES = {
    "Green": "shibafu",
    "Red": "momiji",
    "Blue": "sora",
    "Yellow": "ichou",
    "Purple": "ajisai",
    "Black": "kuro"
}


def format_user_params(password, username):
    """Function that get a password and a username and
    return as a dict the params for the pixela API"""

    user_params = {
        'token': password,
        'username': username,
        'agreeTermsOfService': 'yes',
        'notMinor': 'yes'
    }

    return user_params


def create_account_request(params):
    """Send a request to the Pixela API to create an account"""
    response = requests.post(url=PIXELA_ENDPOINT, json=params)
    print(response.text)
    return response.json()


def format_graph_params(my_id, graph_name, unit, color):
    """Function that take a graph id, name, unit and color
    and return as a dict the params for the pixela API"""

    graph_params = {
        "id": my_id,
        "name": graph_name,
        "unit": unit,
        "type": 'float',
        "color": color
    }

    return graph_params


def create_graph_request(params, username, header):
    """Send a request to the Pixela API to create a graph
    with the given parameters"""

    graph_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs"
    response = requests.post(url=graph_endpoint, json=params, headers=header)
    print(response.text)
    return response.json()


def get_user_data(username, password):
    """
    Function that return a dict that contains all the graphs of a given user
    """

    url = f"https://pixe.la/v1/users/{username}/graphs"
    header = {"X-USER-TOKEN": password}
    response = requests.get(url=url, headers=header)

    if response.status_code == 404 or response.status_code == 400:
        return False

    else:
        keys_to_extract = ['id', 'name', 'unit', 'type', 'color']
        graph_list = response.json()['graphs']
        graphs_dict = {}

        for graph in graph_list:
            final_graph = {key: graph[key] for key in keys_to_extract}
            graphs_dict[final_graph['id']] = final_graph

        return graphs_dict


def delete_account(user, password):
    """ Delete the user account from pixela's servers """

    url = f'{PIXELA_ENDPOINT}/{user}'
    header = {"X-USER-TOKEN": password}
    response = requests.delete(url=url, headers=header)
    print(response.text)
    if response.status_code == 404:
        return False
    return response.json()


def request_update_graph(username, password, graph, quantity, my_date):
    """ Send a PUT request to update the graph """
    
    url = f'{PIXELA_ENDPOINT}/{username}/graphs/{graph}/{my_date}'
    header = {"X-USER-TOKEN": password}
    params = {'quantity': quantity}
    response = requests.put(url=url, headers=header, json=params)
    print(response.text)


def get_graph_id_from_name(graph_name, data):
    """
    Input : name of a graph
    Output : id of the graph
    """
    for graph in data:
        if data[graph]['name'] == graph_name:
            return data[graph]['id']


def get_unit_from_name(graph_name, data):
    """
    Input : name of a graph
    Output : unit of the graph
    """
    for graph in data:
        if data[graph]['name'] == graph_name:
            return data[graph]['unit']


def create_graph_id(data):
    """Generate a graph id"""

    my_id = 'graph'
    graph_number = len(data) + 1
    my_graph_id = f"{my_id}{graph_number}"
    return my_graph_id


def delete_graph(username, password, graph_id):
    url = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}"
    header = {"X-USER-TOKEN": password}
    response = requests.delete(url=url, headers=header)
    return response.json()


def callback(url):
    """ Open the url link in a web browser"""
    webbrowser.open_new(url)


def callback_unit(event, variable, value):
    """ Set the var value when the event is triggered """
    variable.set(value)


def check_entry(entry):
    forbidden_char = ['&', '<', '>']
    for char in forbidden_char:
        if char in entry:
            return False
        else:
            return True




def check_username_password(username, password):
    """ Check if the username and password are not 
    empty and does not inclue a space """
    if len(username) > 0 and len(password) > 0 and username.isspace() is False and password.isspace() is False:
        return True
    return False
