from card import Card

side_positions = [(0.1, 0.2), (0.1, 0.4), (0.1, 0.6)]
central_positions = [0.1]
card = Card("white", "test-data/hearts.png", "test-data/hearts.png", side_positions, central_positions, "VII", (0.05, 0.1))
card.create_image(300, 500).save("test.png")
