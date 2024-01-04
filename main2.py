from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import ScreenManager, Screen
import tmdbsimple as tmdb
import random
import helpers3



tmdb.API_KEY = '2d868ee7566f31aea09f09c92ec65d1c'


class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MovieGenerator(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(helpers3.KV)
        self.dialog = None
        self.decade_popup = None
        self.movie_lst = []
        self.user_lst = []
        self.without_genre_user_lst = []
        self.user_selected_rating_lst = ''
        self.user_selected_decade_lst_gte = ''
        self.user_selected_decade_lst_lte = ''
        self.user_selected_num_voters_lst_gte = ''
        self.user_selected_num_voters_lst_lte = ''
        self.x = 0
        self.y = 0
        self.naughty_list = []
        self.bad_list = []
        self.good_movies = []
        self.good_movie_list = []
        self.good_movie_on_list = None
        self.bad_movie_on_list = None
        self.user_selected_decade_text = None

        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "A200"

        genre = tmdb.Genres()
        genre_lst = []
        for genre in genre.movie_list()['genres']:
            genre_lst.append(genre['name'])

        # user selected with-genre parameter

        menu_items_genre = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.add_genre(x),
            } for i in genre_lst
        ]
        self.genre = MDDropdownMenu(
            caller=self.screen,
            items=menu_items_genre,
            width_mult=4,
        )
        # user selected without-genre parameter

        menu_items_without_genre = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.add_without_genre(x),
            } for i in genre_lst
        ]
        self.without_genre = MDDropdownMenu(
            caller=self.screen,
            items=menu_items_without_genre,
            width_mult=4,
            position="center",
        )

        # user selected rating parameter

        rating_list = [9,8.75,8.5,8.25,8,7.75,7.5,7.25,7,6.75,6.5,6.25,6]

        menu_items_rating = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.add_rating(x),
            } for i in rating_list
        ]
        self.rating = MDDropdownMenu(
            caller=self.screen,
            items=menu_items_rating,
            width_mult=4,
        )

        # user selected decade parameter

        decade_list = [1960, 1970, 1980, 1990, 2000, 2010, 2020]

        menu_items_decade = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.add_decade(x),
            } for i in decade_list
        ]
        self.decade = MDDropdownMenu(
            caller=self.screen,
            items=menu_items_decade,
            width_mult=4,
        )

        # user selected num_voters parameter

        num_voters_list = [50,300,1000,5000]

        menu_items_num_voters = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.add_num_voters(x),
            } for i in num_voters_list
        ]
        self.num_voters = MDDropdownMenu(
            caller=self.screen,
            items=menu_items_num_voters,
            width_mult=4,
        )

        self.load_data()
        self.load_good_data()

    def build(self):
        return self.screen

    def load_naughty_list(self):
        bad_list_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.open_bad_item(x),
            } for i in self.naughty_list
        ]
        self.bad_list = MDDropdownMenu(
            caller=self.screen,
            items=bad_list_items,
            width_mult=4,
        )

    def open_bad_item(self, x):
        self.bad_movie_on_list = x
        new_x = x.replace("[", "")
        new_xx = new_x.replace("]", "")
        list_x = new_xx.split("'")
        joint_title = f'{list_x[1]}, {list_x[3]}'
        self.dialog = None
        if not self.dialog:
            self.dialog = MDDialog(
                title= joint_title,
                text= list_x[5],
                buttons=[
                    MDFlatButton(
                        text="Delete Movie",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press=self.remove_bad_item,
                        on_release=self.dismiss_dialog),

                    MDFlatButton(
                        text="Back",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.dismiss_dialog),
                    ],
                )
        self.dialog.open()

    def remove_bad_item(self, x):
        self.delete_data(self.bad_movie_on_list)
        self.load_naughty_list()
        self.bad_movie_on_list = None

    def load_good_list(self):
        good_list_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.open_good_item(x),
            } for i in self.good_movies
        ]
        self.good_movie_list = MDDropdownMenu(
            caller=self.screen,
            items=good_list_items,
            width_mult=4,
        )

    def open_good_item(self, x):
        self.good_movie_on_list = x
        new_x = x.replace("[", "")
        new_xx = new_x.replace("]", "")
        list_x = new_xx.split("'")
        joint_title = f'{list_x[1]}, {list_x[3]}'
        self.dialog = None
        if not self.dialog:
            self.dialog = MDDialog(
                title= joint_title,
                text= list_x[5],
                buttons=[
                    MDFlatButton(
                        text="Delete Movie",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press=self.dismiss_dialog,
                        on_release=self.remove_good_item),

                    MDFlatButton(
                        text="Back",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.dismiss_dialog),
                    ],
                )
        self.dialog.open()

    def remove_good_item(self, obj):
        self.delete_good_data(self.good_movie_on_list)
        self.load_good_list()
        self.good_movie_on_list = None

    def add_genre(self, x):
        if len(self.user_lst) >= 2:
            self.dialog = None
            if not self.dialog:
                self.dialog = MDDialog(
                    title="ENOUGH!",
                    text="You are maxed out on genres!, press the ready button to discover new movie",
                    buttons=[
                        MDFlatButton(
                            text="Back",
                            theme_text_color="Custom",
                            text_color=self.theme_cls.primary_color,
                            on_release=self.dismiss_dialog),
                    ],
                )
            self.dialog.open()
        else:
            self.user_lst.append(x)

    def add_without_genre(self, x):
        if len(self.without_genre_user_lst) >= 2:
            self.dialog = None
            if not self.dialog:
                self.dialog = MDDialog(
                    title="ENOUGH!",
                    text="You are maxed out on without - genres!, press the ready button to discover new movie",
                    buttons=[
                        MDFlatButton(
                            text="Back",
                            theme_text_color="Custom",
                            text_color=self.theme_cls.primary_color,
                            on_release=self.dismiss_dialog),
                    ],
                )
            self.dialog.open()
        else:
            self.without_genre_user_lst.append(x)

    def add_rating(self, x):
        self.user_selected_rating_lst = str(x)

    def add_decade(self, x):
        self.user_selected_decade_lst_gte = x
        y = int(x)
        y = y + 10
        self.user_selected_decade_lst_lte = str(y)

    def add_num_voters(self, x):
        self.user_selected_num_voters_lst_gte = x
        x = int(x)
        y = 0
        if x == 50:
            y = int(x)
            y = y+250
        elif x == 300:
            y = int(x)
            y = y + 700
        elif x == 1000:
            y = int(x)
            y = y + 4000
        elif x == 5000:
            y = int(x)
            y = y + 10000000
        self.user_selected_num_voters_lst_lte = str(y)

    def find_genre(self):
        #find genre_id of user clicked genre
        self.movie_lst = []
        genre = tmdb.Genres()
        genre_id = []
        without_genre_id = []
        for thing in genre.movie_list()['genres']:
            if thing['name'] in set(self.user_lst):
                genre_id.append(thing['id'])
            else:
                continue

        genre_id_string = map(str, genre_id)
        delimiter = ','
        genre_id_string = delimiter.join(genre_id_string)

        for thing in genre.movie_list()['genres']:
            if thing['name'] in set(self.without_genre_user_lst):
                without_genre_id.append(thing['id'])
            else:
                continue

        without_genre_id_string = map(str, without_genre_id)
        delimiter = ','
        without_genre_id_string = delimiter.join(without_genre_id_string)

        #making the movie list

        discovery = tmdb.Discover()
        print(genre_id_string)
        print(without_genre_id_string)
        print(self.user_selected_num_voters_lst_gte)
        print(self.user_selected_num_voters_lst_lte)
        print(self.user_selected_rating_lst)
        print(self.user_selected_decade_lst_gte)
        print(self.user_selected_decade_lst_lte)
        x = 0
        while True:
            x += 1
            page = discovery.movie(page=x, with_genres=f'{genre_id_string}',
                                       without_genres=f'{without_genre_id_string}',
                                       sort_by='vote_average.desc', vote_average_gte=f'{self.user_selected_rating_lst}',
                                       vote_count_gte=f'{self.user_selected_num_voters_lst_gte}',
                                       vote_count_lte=f'{self.user_selected_num_voters_lst_lte}',
                                       release_date_gte=f'{self.user_selected_decade_lst_gte}',
                                       release_date_lte=f'{self.user_selected_decade_lst_lte}',
                                       with_original_language='en')['results']

            if len(page) == 0:
                break
            else:
                for movie in page:
                    list_list = []
                    title = movie['original_title']
                    list_list.append(title)
                    rating = movie['vote_average']
                    list_list.append(rating)
                    overview = movie['overview']
                    list_list.append(overview)
                    self.movie_lst.append(list_list)
            if len(self.movie_lst) > 500:
                break
            else:
                continue

        print(len(self.movie_lst))

        random.shuffle(self.movie_lst)
        if len(self.movie_lst) < 1:
            self.dialog = None
            if not self.dialog:
                self.dialog = MDDialog(
                    title="ENOUGH!",
                    text="Make new selections, no movies were discovered.",
                    buttons=[
                        MDFlatButton(
                            text="Clear Search Preferences, and go back",
                            theme_text_color="Custom",
                            text_color=self.theme_cls.primary_color,
                            on_press = self.clear_genres,
                            on_release=self.dismiss_dialog)
                    ],
                )
            self.dialog.open()
        else:
            new_lst = []
            for movie in self.movie_lst:
                another_list = []
                for item in movie:
                    num = str(item)
                    another_list.append(num)
                new_lst.append(another_list)

            self.movie_lst = new_lst

            x = 0
            for movie in self.movie_lst:

                for item in movie:
                    if item in set(self.naughty_list):
                        self.movie_lst[x].remove(item)
                        x += 1
                    elif item in set(self.good_movies):
                        self.movie_lst[x].remove(item)
                        x += 1
                    else:
                        x += 1
                        continue

            self.movie_browse()

    def movie_browse(self):
        self.dialog = None
        if not self.dialog:
            next_movie_title = self.movie_lst[self.x][self.y]
            next_movie_rating = self.movie_lst[self.x][self.y+1]
            joint_title = f'{next_movie_title}, {next_movie_rating}'
            next_movie_description = self.movie_lst[self.x][self.y+2]
            self.dialog = MDDialog(
                title= joint_title,
                text= next_movie_description,
                buttons=[
                    MDFlatButton(
                        text="ADD TO GOOD LIST",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press=self.add_good_movies_list,
                        on_release=self.change_movie),

                    MDFlatButton(
                        text="Clear Search Preferences",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.clear_genres),

                    MDFlatButton(
                        text="NEXT",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release= self.change_movie),

                    MDFlatButton(
                        text="ADD TO NAUGHTY LIST",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press=self.add_naughty_list,
                        on_release=self.change_movie
                        ),
                    ],
                )
        self.dialog.open()

    def clear_genres(self, obj):
        self.user_lst = []
        self.without_genre_user_lst = []
        self.user_selected_rating_lst = ''
        self.user_selected_decade_lst_gte = ''
        self.user_selected_decade_lst_lte = ''
        self.user_selected_num_voters_lst_gte = ''
        self.user_selected_num_voters_lst_lte = ''
        self.dialog.dismiss()

    def clear_genres2(self):
        self.user_lst = []
        self.without_genre_user_lst = []
        self.user_selected_rating_lst = ''
        self.user_selected_decade_lst_gte = ''
        self.user_selected_decade_lst_lte = ''
        self.user_selected_num_voters_lst_gte = ''
        self.user_selected_num_voters_lst_lte = ''


    def dismiss_dialog(self,obj):
        self.dialog.dismiss()

    def change_movie(self, obj):
        self.x += 1
        self.dialog.dismiss()

        if self.x < (len(self.movie_lst) - 1):
            self.dialog = None
            if not self.dialog:
                next_movie_title = self.movie_lst[self.x][self.y]
                next_movie_rating = self.movie_lst[self.x][self.y + 1]
                joint_title = f'{next_movie_title}, {next_movie_rating}'
                next_movie_description = self.movie_lst[self.x][self.y + 2]
                self.dialog = MDDialog(
                    title=joint_title,
                    text=next_movie_description,
                    buttons=[
                        MDFlatButton(
                            text="ADD TO GOOD LIST",
                            theme_text_color="Custom",
                            text_color=self.theme_cls.primary_color,
                            on_press=self.add_good_movies_list,
                            on_release=self.change_movie),

                        MDFlatButton(
                            text="Clear Genres",
                            theme_text_color="Custom",
                            text_color=self.theme_cls.primary_color,
                            on_release=self.clear_genres),

                        MDFlatButton(
                            text="NEXT",
                            theme_text_color="Custom",
                            text_color=self.theme_cls.primary_color,
                            on_release=self.change_movie),

                        MDFlatButton(
                            text="ADD TO BAD LIST",
                            theme_text_color="Custom",
                            text_color=self.theme_cls.primary_color,
                            on_press=self.add_naughty_list,
                            on_release=self.change_movie),

                    ],
                )
            self.dialog.open()
        else:
            self.movie_lst = []
            self.clear_genres2()


    def add_good_movies_list(self, obj):
        self.good_movies.append(self.movie_lst[self.x])
        self.save_good_data()
        self.load_good_list()

    def save_good_data(self):
        data = self.good_movies
        filename = "my_good_movies"
        file = open(filename, "w")
        for movie in data:
            file.write(f'{movie}\n')
        file.close()

    def load_good_data(self):

        try:
            with open('my_good_movies', 'r') as file:
                content = file.read()
                n_content = content.split('\n')
                n_content = [x for x in n_content if x]
                self.good_movies = n_content
                self.load_good_list()
        except (Exception,):
            self.load_good_list()

    def delete_good_data(self, movie):
        with open("my_good_movies", "r") as f:
            # read data line by line
            data = f.readlines()
            # open file in write mode
        with open("my_good_movies", "w") as f:

            for line in data:

                # condition for data to be deleted
                if line.strip("\n") != movie:
                    f.write(line)
        self.load_good_data()

    def add_naughty_list(self, obj):
        self.naughty_list.append(self.movie_lst[self.x])
        self.save_data()
        self.load_naughty_list()

    def save_data(self):
        data = self.naughty_list
        filename = "my_bad_movies"
        file = open(filename, "w")
        for movie in data:
            file.write(f'{movie}\n')
        file.close()

    def load_data(self):

        try:
            with open('my_bad_movies', 'r') as file:
                content = file.read()
                n_content = content.split('\n')
                n_content = [x for x in n_content if x]
                self.naughty_list = n_content
                self.load_naughty_list()
        except:
            self.load_naughty_list()


    def delete_data(self, movie):
        with open("my_bad_movies", "r") as f:
            # read data line by line
            data = f.readlines()
            # open file in write mode
        with open("my_bad_movies", "w") as f:

            for line in data:

                # condition for data to be deleted
                if line.strip("\n") != movie:
                    f.write(line)
        self.load_data()




MovieGenerator().run()