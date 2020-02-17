# simple_bee

## Summary

This is a toy Django project about robot bees that involves 
1. A backend to receive data from individual bees and store it in a database.
2. A frontend to show real-time individual bee data.

## Setup

The development environment is Python 3.7.4, SQLite 3.29.0 and Django 3.0.3. Other environment is not tested.

To run a local server, run the following command after cloning and navigating to the directory:

`python manage.py runserver`

Open a browser and go to http://127.0.0.1:8000/simple_bee/, you should see:

![index page](https://github.com/yilin-lu/simple_bee/blob/master/readme/index.jpg =250x)

Click on the power icon on the bottom of the page. A page will be opened on a new tab. **Please keep this page open or the random data will cease to be fired.**
More than one random data page might cause undefined behavior.
![random data page]()

Then you are all set. You can click around to explore the rest of the site.

## UI

Most of the icon should be self-explanatory. However, here is a reference:

* Power: Start random data firing.
* Plus: Register a new bee robot.
* Bee: Visit the bee robot of that id number.
* Home: Go back to the index page.

## Bee_robot json
```javascript
{
    "id": 4,
    "nectar": 80,
    "honey": 9,
    "fuel": 75,
    "damage": 51,
    "status": 2,
    "speed": 0.0,
    "latitude": 4.0,
    "longitude": 3.0,
    "elevation": -3.0,
    "is_active": true
}
```

## Supported API
Let root=http://127.0.0.1:8000/simple_bee/ 
| HTTP Request        | URL           |  Designed Behavior  |
| ------------- |-------------| -----|
| GET      | root/**int:bee_robot_id**/get/ | return Bee_robot json of the id |
| PUT      | root/**int:bee_robot_id**/put/ | demand a json identical to Bee_robot json except the id field; make the change to the database |
| DELETE     | root/**int:bee_robot_id**/delete/ | delete the record of the target Bee_robot from the database |
| POST | root/**int:bee_robot_id**/decommission/  | change the target Bee_robot's is_active field |
| POST | root/register/  | register a new Bee_robot(must operate on the frontend interface; params format is unknown.) |

## Known Limitation

* Automatic partial refresh is **only** available on the Detail page of individual Bee_robot. The other pages are with working HTTP request but not display.
* Most HTTP Requests do not send back designed confirmation. They send back html.
* **csrf is turned OFF!**
* Mutiple random data page will lead to unpredicted behavior.
* Deleting a Bee_robot will **not** free the used id.
* Fuel is auto-filled after running out.
* A Bee_robot can only be deleted if get destoryed. No repair is possible without directly PUT a new value.
* Honey and nectar update messages "+n Honey/Nectar" are delayed.
* Register page and random data page are not decorated.

## Other screenshots
![detail page]()
![register page]()
