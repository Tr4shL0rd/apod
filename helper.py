import requests
import dbus

def apikeyFound(apiKey) -> bool:
    if apiKey == None:
        return False
    else:
        return True

def verifyApiKey(apiKey):
    url = f"https://api.nasa.gov/planetary/apod?api_key={apiKey}"
    status = requests.get(url)
    if b'{\n  "error": {\n    "code": "API_KEY_INVALID",' in status.content:
        return False
    return True

def setwallpaper(filepath, plugin = 'org.kde.image'):
    jscript = """
    var allDesktops = desktops();
    print (allDesktops);
    for (i=0;i<allDesktops.length;i++) {
        d = allDesktops[i];
        d.wallpaperPlugin = "%s";
        d.currentConfigGroup = Array("Wallpaper", "%s", "General");
        d.writeConfig("Image", "file://%s")
    }
    """
    bus = dbus.SessionBus()
    plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')
    plasma.evaluateScript(jscript % (plugin, plugin, filepath))
