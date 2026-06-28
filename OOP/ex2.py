from book import Book

library = [
    Book("1984", "G. Orwell"),
    Book("Moskow 2024", "V. Voinovich"),
    Book("Atlant raspravil plechi", "A. Rand")
]

for b in library:
    print (f"{b.name} - {b.author}")