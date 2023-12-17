import pyglet

# Replace 'your_gif_file.gif' with the path to your GIF file
gif_path = 'base_small.gif'

# Create a window
window = pyglet.window.Window()
window.set_exclusive_mouse(True)

# Load the GIF
animation = pyglet.image.load_animation(gif_path)
sprite = pyglet.sprite.Sprite(animation)

# Set the window size to match the GIF
window.width = 180
window.height = 180

@window.event
def on_draw():
    window.clear()
    window.set_caption = "Delamain"
    sprite.draw()

# Start the application
pyglet.app.run()