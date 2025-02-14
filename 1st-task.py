import json

def kwargsAcceptFun(**kwargs):
    """
    This function accepts an arbitrary number of named arguments and converts to JSON.
    """
    json_output = json.dumps(kwargs, indent=4)
    print(json_output)

kwargsAcceptFun(name="New Uzbekistan University", ranking=999, students_count=1000)
