# LT Technical Showcase
Here is a simple (yet verbose) solution to list photos from the [Fake Online REST API](https://jsonplaceholder.typicode.com) 
using python. 

**FYI:** Python is not my strong suit, but I thought it would be fun to try this on this app. 

## Application Requirements 
This application requires Python 3 and the Python Request library. 

*   Download and install [Python 3](https://www.python.org/downloads/)
*   Download and install the [Python Request library](https://3.python-requests.org/user/install/)

### Running this application

After you downloaded the project files, open a terminal and navigate into the project folder 
and run the application. 

```bash
python app.py
```

or if you have not made python 3 your default

``` bash
python3 app.py

```

The app will prompt you to enter a photo album **ID**.
``` bash
python app.py
Enter the album id to view. >
```

Enter an album id and press ```return```. The result will look something like the following. 

```text
[ 151 ]   possimus dolor minima provident ipsam
[ 152 ]   et accusantium enim pariatur eum nihil fugit
[ 153 ]   eum laborum in sunt ea
[ 154 ]   dolorum ipsam odit
...
```
To exit the application use the keyboard shortcut ``` command```  +  ```z```

### Unit Tests
To run the unit test use the following command ```$ python test_app_unittest.py ```