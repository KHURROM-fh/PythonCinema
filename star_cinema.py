class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall_Object):
        self.hall_list.append(hall_Object)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        super().__init__()

    def entry_show(self, id, movie_name, time):
        title = (id, movie_name, time)
        self.show_list.append(title)
        rows = self.rows
        cols = self.cols
        seat = [[False for col in range(cols)] for row in range(rows)]
        self.seats[id] = seat

    def book_seats(self, show_id, row_col):
        if show_id in self.show_list[0]:
            if not self.seats[show_id][row_col[0]][row_col[1]]:
                print("Available for booking")
                self.seats[show_id][row_col[0]][row_col[1]] = True
            else:
                print("Not available")
        else:
            print("Invalid")
            return

    def view_show_list(self):
        for show in self.show_list:
            print(
                f"show id = {show[0]}, Movie name = {show[1]}, time = {show[2]}")

    def view_available_seats(self, show_id):
        if show_id in self.seats:
            available_seats = sum(sum(not seat for seat in row)
                                  for row in self.seats[show_id])
            print(f"Available seats {show_id}: {available_seats}")
        else:
            print(f"Invalid")
            return


try:
    h = Hall(4, 3, 2)
    h.entry_show("01", "Blade Runner 2049", "7PM")

    while True:
        print("1. Running Show")
        print("2. Available seats")
        print("3. Book tickets")
        print("4. Quit")
        a = int(input())
        if a == 1:
            h.view_show_list()
        elif a == 2:
            show_id = input("Enter ID: ")
            h.view_available_seats(show_id)
        elif a == 3:
            seats = int(input("How many seats are you want: "))
            for i in range(seats):
                show_id = input("Enter ID: ")
                row_col = tuple(
                    map(int, input("row and column: ").split(',')))
                h.book_seats(show_id, row_col)
        elif a == 4:
            break
except:
    print(" Please Check your Code Please! ")


















# class Star_Cinema:
#     hall_list = []

#     @classmethod
#     def entry_hall(cls, hall):
#         cls.hall_list.append(hall)


# class Hall:
#     def __init__(self, rows, cols, hall_no):
#         self._seats = {}
#         self._show_list = []
#         self._rows = rows
#         self._cols = cols
#         self._hall_no = hall_no
#         Star_Cinema.entry_hall(self)

#     def entry_show(self, id, movie_name, time):
#         show_info = (id, movie_name, time)
#         self._show_list.append(show_info)
#         self._seats[id] = [[False for _ in range(self._cols)] for _ in range(self._rows)]

#     def book_seats(self, id, seats_to_book):
#         if id not in self._seats:
#             print("Invalid show ID")
#             return

#         seats = self._seats[id]
#         for seat in seats_to_book:
#             row, col = seat
#             if 1 <= row <= self._rows and 1 <= col <= self._cols:
#                 if seats[row - 1][col - 1]:
#                     print(f"Seat ({row}, {col}) is already booked")
#                 else:
#                     seats[row - 1][col - 1] = True
#                     print(f"Seat ({row}, {col}) booked successfully")
#             else:
#                 print(f"Seat ({row}, {col}) is invalid")

#     def view_show_list(self):
#         print("Shows running:")
#         for show in self._show_list:
#             print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

#     def view_available_seats(self, id):
#         if id not in self._seats:
#             print("Invalid show ID")
#             return

#         print("Available seats:")
#         for i in range(self._rows):
#             for j in range(self._cols):
#                 if not self._seats[id][i][j]:
#                     print(f"({i+1}, {j+1})", end=' ')
#             print()  # Move to the next row

# # Example usage
# hall1 = Hall(5, 5, 1)
# hall1.entry_show(1, "Avengers", "3:00 PM")
# hall1.entry_show(2, "Joker", "6:00 PM")
# hall1.book_seats(1, [(1, 1), (2, 2), (3, 3)])
# hall1.book_seats(2, [(1, 1), (2, 2), (3, 3)])
# hall1.view_show_list()
# hall1.view_available_seats(1)
# hall1.view_available_seats(2)
