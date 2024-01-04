
KV = '''
WindowManager:
    FirstWindow:
    SecondWindow:

<FirstWindow>:
    canvas:
        Color:
            rgba: 0,.5,1,.1
        Rectangle:
            size: self.size
            pos: self.pos
    name: "first"
    
    
    MDScreen:
        MDTopAppBar:
            markup: True
            title: "[b]Movie[/b] [font=times]Generator[/font]"
            pos_hint: {"top" : 1}
            icon: "instagram"

        MDRectangleFlatButton:
            id: next
            text: "'Lists'"
            pos_hint: {"center_x": .8, "center_y": .45}
            on_release: app.root.current = "second"
            
        MDRectangleFlatButton:
            id: next
            text: "'Clear Search Preferences'"
            pos_hint: {"center_x": .8, "center_y": .35}
            on_release: app.clear_genres2()

        MDLabel:
            markup: True
            text: "[font=times]1. Select up to 2 Genres MAX you want your movie to include. (recommended to choose 1)[/font]"
            icon: "instagram"
            font_size: 20
            size_hint_y: None
            pos_hint: {"center_x": .55, "center_y": .8}
            padding_y: 15
        
        MDLabel:
            markup: True
            id: welcome_label
            text: "[font=times]2. Select up to 2 Genres you want your movie NOT to include. (recommended to choose 1)[/font]"
            font_size: 20
            size_hint_y: None
            pos_hint: {"center_x": .55, "center_y": .75}
            padding_y: 15
            
        MDLabel:
            markup: True
            id: welcome_label
            text: "[font=times]3. Select the rating, number of rating voters, and decade.[/font]"
            font_size: 20
            size_hint_y: None
            pos_hint: {"center_x": .55, "center_y": .7}
            padding_y: 15
        
        MDLabel:
            markup: True
            id: welcome_label
            text: "[font=times]3. Click [b]READY[/b] to generate a random movie.[/font]"
            font_size: 20
            size_hint_y: None
            pos_hint: {"center_x": .55, "center_y": .65}
            padding_y: 15
            
        MDLabel:
            markup: True
            id: welcome_label
            text: "[font=times]4. Add movie to either [b]GOOD[/b] or [b]BAD list[/b] or click next to generate new movie.[/font]"
            font_size: 20
            size_hint_y: None
            pos_hint: {"center_x": .55, "center_y": .6}
            padding_y: 15
            
        MDLabel:
            markup: True
            id: welcome_label
            text: "[font=times]5. Click [b]List's[/b] to go to your good and bad lists. These movies will not be randomly generated.[/font]"
            font_size: 20
            size_hint_y: None
            pos_hint: {"center_x": .55, "center_y": .55}
            padding_y: 15
            
        MDRaisedButton:
            id: genre
            text: "Genre"
            pos_hint: {"center_x": .5, "center_y": .45}
            on_release: app.genre.open()
            
        MDRaisedButton:
            id: genre
            text: "Without Genre"
            pos_hint: {"center_x": .5, "center_y": .38}
            on_release: app.without_genre.open()
            
        MDRaisedButton:
            id: genre
            text: "Rating"
            pos_hint: {"center_x": .5, "center_y": .31}
            on_release: app.rating.open()
        
        MDRaisedButton:
            id: genre
            text: "Decade"
            pos_hint: {"center_x": .5, "center_y": .24}
            on_release: app.decade.open()
        
        
        MDRaisedButton:
            id: genre
            text: "Num Voters"
            pos_hint: {"center_x": .5, "center_y": .17}
            on_release: app.num_voters.open()
        
        MDRectangleFlatButton:
            text:"READY"
            pos_hint: {'center_x': 0.5,'center_y': 0.075}
            on_release: app.find_genre()



<SecondWindow>:

    canvas:
        Color:
            rgba: 0,.5,1,.2
        Rectangle:
            size: self.size
            pos: self.pos
    
    name: "second"

    MDScreen:
        
        MDTopAppBar:
            markup: True
            title: "[b]List[/b] [font=times]Page[/font]"
            pos_hint: {"top" : 1}
            icon: "instagram"
        
        MDRaisedButton:
            id: back
            text: "Click to go Back"
            pos_hint: {"center_x": .2, "center_y": .5}
            on_release: 
                root.manager.transition.direction = "left"
                root.manager.current = "first"
                
        
        MDLabel:
            markup: True
            id: welcome_label
            text: "[font=times]1. Click on either button to see your good and bad lists.[/font]"
            font_size: 20
            size_hint_y: None
            pos_hint: {"center_x": .55, "center_y": .8}
            padding_y: 15
        
        MDLabel:
            markup: True
            id: welcome_label
            text: "[font=times]2. Click on movie to remove it from list.[/font]"
            font_size: 20
            size_hint_y: None
            pos_hint: {"center_x": .55, "center_y": .75}
            padding_y: 15
        
        MDRaisedButton:
            id: genre
            text: "Bad List"
            pos_hint: {"center_x": .5, "center_y": .4}
            on_release: app.bad_list.open()
        
        MDRaisedButton:
            id: genre
            text: "Good List"
            pos_hint: {"center_x": .5, "center_y": .6}
            on_release: app.good_movie_list.open()
'''
