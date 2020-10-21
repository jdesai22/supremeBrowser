import json


def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def createProfile():
    with open('profiles/test.json') as json_file:
        data = json.load(json_file)

        profiles = data['profiles']

        profileName = input("Profile Name: ")
        name = input("Name: ")
        email = input("Email: ")
        phone_number = input("Phone Number: ")
        street_address = input("Street Address: ")
        city = input("City: ")
        zip_code = input("Zip Code: ")
        card_cvv = input("Card CVV: ")
        card_number = input("Card Number: ")
        month_exp = input("Month Expiration: ")
        year_exp = input("Year Expiration: ")

        newProfile = {
            "profileName": profileName,
            "name": name,
            "email": email,
            "phone_number": phone_number,
            "street_address": street_address,
            "city": city,
            "zip_code": zip_code,
            "card_cvv": card_cvv,
            "card_number": card_number,
            "month_exp": int(month_exp),
            "year_exp": int(year_exp)
             }

        profiles.append(newProfile)

    return data


def removeProfile():
    with open('profiles/test.json') as json_file:
        data = json.load(json_file)

        profileOpts = []

        profiles = data['profiles']

        for i in range(0, len(profiles)):
            profileOpts.append(profiles[i]["profileName"])
            print(profiles[i]["profileName"] + "    [{}]".format(i))

        delete = int(input("Which profile would you like to remove? (1, 2, etc.): "))

        for i in range(0, len(profiles)):
            if i == delete:
                profiles.pop(delete)
                print("Profile removed")

        newProfileSet = {
            "profiles":
                profiles

        }

    return newProfileSet

        # profiles.append(newProfile)

    # return data

# write_json(createProfile(), 'profiles/test.json')

write_json(removeProfile(), 'profiles/test.json')

