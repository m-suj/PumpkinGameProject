import arcade


class Scene:
    """Simple layered scene class"""

    def __init__(self, scene_elements: list[str]):
        self.scene_sprites = [arcade.Sprite(filename) for filename in scene_elements]
        prev_height = 0
        for element in self.scene_sprites:
            prev_height += element.height/2
            element.center_x, element.center_y = element.width/2, prev_height
            prev_height += element.height/2


    def draw(self):
        for element in self.scene_sprites:
            element.draw(pixelated=True)