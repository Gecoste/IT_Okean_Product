import flet
from flet import *
from appmenu import jumbotron
from cardsection import sectioncard
from tabsmenu import tabs_menu
def main(page:Page):
	page.padding = 0
	page.spacing = 0 
	page.add(
		# APPMENU
		jumbotron,
		# SECTION CARD MENU
		sectioncard,

		# FOR TABS SECTION
	Container(
	border_radius = border_radius.only(top_left=30,top_right=30),
	# for GET FULL WIDTH
	width=page.window_width,
	bgcolor="white",
	# THIS CONTENT
	content = tabs_menu

		)

		)


flet.app(target=main,assets_dir="assets")
