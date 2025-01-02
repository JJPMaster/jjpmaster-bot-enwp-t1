import pywikibot
from pywikibot.comms.eventstreams import site_rc_listener

site = pywikibot.Site('en', 'wikipedia')
page = pywikibot.Page(site, 'User:JJPMaster/Editnotice requests')
cat = pywikibot.Category(site, 'Wikipedia template-protected edit requests')

rc = site_rc_listener(site)
for change in rc:
    if (change["namespace"] == 11): 
        print(change)
        my_list = list(cat.members())
        for i in range(len(my_list)): 
            my_list[i] = my_list[i].title()

        editnotices = list(filter(lambda i: i.startswith("Template talk:Editnotices/"), my_list))
        annotated_list = ''.join(f'* [[{j}]]\n' for j in editnotices) if len(editnotices) > 0 else '\n* \'\'None\'\''
        print(editnotices)
        page.text = "Current editnotice edit requests:\n" + annotated_list
        page.save(f"Bot: Updating editnotice request list ({len(editnotices)} requests)")
