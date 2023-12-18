#8. You need to write a function that accepts an encoded string as a parameter. This
#string will contain a first name, last name, and an id.
#Values in the string can be separated by any number of zeros. The id is a numeric
#value but will contain no zeros. The function should parse the string and return a
#Python dictionary that contains the first name, last name, and id values.
#An example input would be “Robert000Smith000123”. The function should return the
#following using that input:
#{ “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }

def string_breaker(encoded_string):
    parts = encoded_string.split("000")
    first_name = parts[0]
    last_name = parts[1]    
    user_id = "".join(parts[2:])
    result_dict = {"first_name": first_name, "last_name": last_name, "id": user_id}
    return result_dict
encoded_str = "Robert000Smith000123"
result = string_breaker(encoded_str)

print(result)
