import arcade

arcade.open_window(1000, 800, "More Shapes")
arcade.set_background_color(arcade.color.BLACK)

arcade.start_render()
arcade.draw_lrtb_rectangle_filled(50, 150, 200, 50, arcade.color.BITTER_LEMON)
arcade.draw_lrtb_rectangle_outline(160, 360, 150, 50, arcade.color.BITTER_LEMON, 5)
arcade.draw_xywh_rectangle_outline(10, 10, 380, 250, arcade.color.EARTH_YELLOW, 5)
arcade.draw_xywh_rectangle_filled(405, 10, 150, 100, arcade.color.BOTTLE_GREEN)
arcade.draw_circle_filled(100, 600, 50, arcade.color.MAGENTA)
arcade.draw_circle_outline(100, 600, 75, arcade.color.GOLD, 6)
arcade.draw_triangle_outline(300, 400, 700, 700, 600, 400, arcade.color.AIR_SUPERIORITY_BLUE, 6)
arcade.draw_triangle_filled(300, 600, 100, 500, 200, 300, arcade.color.BUFF)

arcade.finish_render()

arcade.run()
