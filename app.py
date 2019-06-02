import json
import sys
import requests


def main():

    if sys.version_info[0] != 3:
        print("This script requires Python 3")
        exit()

    while True:
        try:
            try:
                choice = int(input("Enter an album id to view. > "))
                if not isinstance(choice, int):
                    raise ValueError()
            except ValueError:
                print ("That was not a number! Please provide an Album ID which is a number. E.g. 1, 2, 3, 4, ...")
            else:
                photo_list = get_the_json(choice)
                output_photos(photo_list)
        except (KeyboardInterrupt, SystemExit):
            pass


def get_the_json(album_id):
    """
    Load the json data

    :param album_id:int
    :return:
    """
    url = "https://jsonplaceholder.typicode.com/photos?albumId=" + str(album_id)

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print("WHOOOOOOOOOOOO - Response error, lets abort our mission!", e)
        sys.exit()
    else:
        # for this simple example let's assume the json response is aOK
        json_data = json.loads(response.text)
        return json_data


def output_photos(photo_list):
    """
    Print out the list of photos in the album

    :param photo_list:
    """
    if len(photo_list) is 0:
        print("We did not find an album with the ID provided")

    for photos in photo_list:
        print('[', photos['id'], ']  ', photos['title'])


if __name__ == '__main__':
    main()