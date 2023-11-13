from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem, ThreeLineListItem
from kivy.uix.scrollview import ScrollView


class listApp(MDApp):
    
    def build(self):
        screen = Screen()
        
        scroll = ScrollView()
        
        list_view = MDList()
        
        # add MD list to scrollview
        scroll.add_widget(list_view)
        
        for i in range(20):
            items = ThreeLineListItem(text = 'Item ' + str(i), secondary_text = 'Hello World',
                                    tertiary_text = 'Third text')
            # add one list item to MDList
            list_view.add_widget(items)
        
        # add MdList to our screen
        screen.add_widget(scroll)
        return screen
    
listApp().run()