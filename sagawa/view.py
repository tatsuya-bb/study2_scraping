import eel
import desktop
import search

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def sagawa_search(file_name):
    search.sagawa_search(file_name)

desktop.start(app_name,end_point,size)
