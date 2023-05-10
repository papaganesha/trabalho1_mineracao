import uuid

def generate_surrogate():
    # Generate a UUID (Universally Unique Identifier)
    uuidValue = uuid.uuid1()

    # Convert UUID to an integer
    intValue = int(uuidValue.int)

    # Create a surrogate key
    surrogateKey = abs(hash(intValue))

    # Return surrogate key
    return surrogateKey

