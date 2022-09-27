import arcade
#use this to open the window, width 800, Height, 600
my_window = arcade.open_window(600, 800, "Our First Window Demo")
arcade.set_background_color(arcade.color.BABY_BLUE)

arcade.start_render()
#everything else goes here
for xloc in range(100, 900, 80):
    arcade.draw_line(xloc, 50, xloc, 900, arcade.color.AFRICAN_VIOLET, 10)
    yloc = xloc
    arcade.draw_line(70, yloc, 900, yloc, arcade.color.BRIGHT_UBE, 10)

arcade.finish_render()


arcade.run()
