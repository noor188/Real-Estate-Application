def getValidInput(inputString, validOptions):
    inputString += "  ({})  ".format(", ".join(validOptions))
    response = input(inputString)
    while response.lower() not in validOptions:
        response = input(inputString)
    return response