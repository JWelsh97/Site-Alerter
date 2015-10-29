import requests
import sys
import yaml
from pushbullet import PushBullet

def sitestatus(url):
    """
    Determines why the site
    cannot be accessed, places
    data in tuple
    """
    try:
        r = requests.get(url)
    except requests.ConnectionError:
        return ("Error", "Webserver is offline.")
    except requests.Timeout:
        return ("Error", "Server is offline.")
    except Exception as e:
        return ("Failure", str(e))


def read_config():
    """
    Reads the YAML config file
    """
    f = open("config.yaml", "r")
    conf = f.read()
    f.close()
    return yaml.load(conf)


conf = read_config()
sitestatus = sitestatus(conf["site"])
print sitestatus
pb = PushBullet(conf["access_token"])
if sys.argv > 1:
    for arg in sys.argv:
        if sys.arg == "--list":
            for device in pb.get_devices():
                print device

