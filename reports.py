def import_data(filename='booking.txt'):
    """
    Import data from a file to a list. The columns are marked as follows:
    hotel;arrival_date;booked_nights;adults;children;babies;meal;country;reservation_status;reservation_status_date
    Expected returned data format:
        [["Resort Hotel", "01/22/2017", 4, 2, 0, 0, "YES", "PL", "Check-Out", "09/20/2022"],
        ["City Hotel", "01/22/2017", 2, 2, 0, 0, "NO", "FR", "Cancelled", "09/20/2022"],
        ...]

    :param str filename: optional, name of the file to be imported

    :returns: list of lists representing accomodation booking data
    :rtype: list
    """
    accomodation_booking_data =[]
    with open (filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            booking_data = line.split(";")
            accomodation_booking_data.append(booking_data)
    return accomodation_booking_data 

# filename = "booking.txt"
# print(import_data(filename='booking.txt'))




def export_data(bookings, filename='booking.txt', mode='a'):
    """
    Export data from a list to file. If called with mode 'w' it should overwrite
    data in file. If called with mode 'a' it should append data at the end.

    :param list booking: booking data
    :param str filename: optional, name of file to export data to
    :param str mode: optional, file open mode with the same meaning as\
    file open modes used in Python. Possible values: only 'w' or 'a'

    :raises ValueError: if mode other than 'w' or 'a' was given. Error message:
        'Wrong write mode'
    """
    if mode not in ("w", "a"):
        raise ValueError('Wrong write mode')

    with open (filename, mode) as file:
        for booking in bookings:
            line = ",".join(booking)
            line.write(line + "\n")




def get_rows_by_booking_status(rows, status):
    """
    Get booking rows by status

    :param list: booking data
    :param str status: status to filter by e.g. Canceled, Checked-out

    :raises ValueError: if given status is not present in the list. Error message: 'Status is not present in list'
    :returns: all rows of given status
    :rtype: list
    """
    booking_by_status = []
    for booking in rows:
        if booking[8] == status:
            booking_by_status.append(booking)
    if booking_by_status == []:
        raise ValueError('Status is not present in list')
    return booking_by_status



def get_rows_by_date(rows, date_in, date_out):
    """
    Get rows filtred by specific date

    :param list rows: rows data, date in, date out
    :returns: list of booking in date range betwee date_in and date_out
    :rtype: list
    """
    rows_by_date =[]
    date_in_value_l = date_in.split("/")
    date_in_value_s = int(date_in_value_l[2+date_in_value_l[0]+date_in_value_l])
    date_out_value_l = date_out.split("/")
    date_out_value_s = int(date_out_value_l[2]+date_out_value_l[0]+date_out_value_l[1])

    for row in rows:
        date_nights_l = row[1].split("/")
        date_nights_s = int(date_nights_l[2]+date_nights_l[0]+date_nights_l[1])

        if date_in_value_s < date_nights_s < date_out_value_s:
            rows_by_date.append(row)
    return rows_by_date




def children_number_in_date(rows, date, hotel):
    """
    Thos method should return amount of children in selected date and specific hotel

    :param list rows: booking data, date, hotel name
    :returns: number of chidren
    :rtype: int
    """
    number_of_children = 0
    for row in rows:
        if row[1] == date and row[0] == hotel:
            number_of_children = number_of_children + int(row[4])
    return number_of_children


def display_reservation(rows, date):
    """
    Method return table representation of reservation in format:

    hotel | check in   | check out  | adults | children | babies | status
    Ibis  | 20/09/2022 | 25/09/2022 | 2      | 0        | 0      | checked-in


    Please get check out date based on arrival_date and booked nights
    """
    for row in rows:
        line = "|".join(row)
        line.write(line + "\n")
