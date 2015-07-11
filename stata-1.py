#!/usr/bin/python
import lxml.html as html
from pandas import DataFrame

main_domain_stat = 'http://worldofwarships.ru/community/accounts/'

nick = ('61510-T_Shtirlits','163480-')

print (nick);
player_url=main_domain_stat+nick[1]+'/#!general_pvp'
print (player_url)
page = html.parse(player_url)

e = page.getroot().\
        find_class('avg_xp').\
        pop()
print (e)
#t = e.getchildren().pop()

#events_tabl = DataFrame([{'EVENT':i[0].text, 'LINK':i[2]} for i in t.iterlinks()][5:])

#event_date = DataFrame([{'EVENT': evt.getchildren()[0].text_content(), 'DATE':evt.getchildren()[1].text_content()} for evt in t][2:])

#sum_event_link = events_tabl.set_index('EVENT').join(event_date.set_index('EVENT')).reset_index()

#sum_event_link.to_csv('..\list_ufc_events.csv',';',index=False)



