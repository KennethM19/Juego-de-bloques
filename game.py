from elements.Director import Director

if __name__ == '__main__':
    director = Director("Juego ladrillos")
    director.add_scene("LevelOne")
    director.add_scene("EndGame")
    director.execute("LevelOne")
