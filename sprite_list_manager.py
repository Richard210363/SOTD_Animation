


class SpriteListManager():
    """description of class"""
    def __init__(self, listname):
        pass


def loadImagesToList(listname):
    if os.path.isfile(fileName):
        image = pygame.image.load(fileName)
        image = image.convert_alpha()
        # Return the image
        return image
    else:
        raise Exception("Error loading image: " + fileName + " - Check filename and path?")
