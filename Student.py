from enum import Enum

# Enums for Room Type, Payment Status, and Gender
class RoomType(Enum):
    SINGLE = "Single Room"
    DOUBLE = "Double Room"
    QUEEN = "Queen Room"
    KING = "King Room"
    SUITE = "Suite"

class PaymentStatus(Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"

# Guest class
class Guest:
    def __init__(self, first_name: str, last_name: str, email: str, phone: str, gender: Gender):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone = phone
        self._gender = gender

    # Getter and Setter Methods
    def get_first_name(self) -> str:
        return self._first_name

    def set_first_name(self, first_name: str):
        self._first_name = first_name

    def get_last_name(self) -> str:
        return self._last_name

    def set_last_name(self, last_name: str):
        self._last_name = last_name

    def get_email(self) -> str:
        return self._email

    def set_email(self, email: str):
        self._email = email

    def get_phone(self) -> str:
        return self._phone

    def set_phone(self, phone: str):
        self._phone = phone

    def get_gender(self) -> Gender:
        return self._gender

    def set_gender(self, gender: Gender):
        self._gender = gender

# Reservation class
class Reservation:
    def __init__(self, reservation_id: int, guest: Guest, check_in: str, check_out: str, room_type: RoomType, number_of_rooms: int):
        self._reservation_id = reservation_id
        self._guest = guest
        self._check_in = check_in
        self._check_out = check_out
        self._room_type = room_type
        self._number_of_rooms = number_of_rooms

    # Getter and Setter Methods
    def get_reservation_id(self) -> int:
        return self._reservation_id

    def set_reservation_id(self, reservation_id: int):
        self._reservation_id = reservation_id

    def get_guest(self) -> Guest:
        return self._guest

    def set_guest(self, guest: Guest):
        self._guest = guest

    def get_check_in(self) -> str:
        return self._check_in

    def set_check_in(self, check_in: str):
        self._check_in = check_in

    def get_check_out(self) -> str:
        return self._check_out

    def set_check_out(self, check_out: str):
        self._check_out = check_out

    def get_room_type(self) -> RoomType:
        return self._room_type

    def set_room_type(self, room_type: RoomType):
        self._room_type = room_type

    def get_number_of_rooms(self) -> int:
        return self._number_of_rooms

    def set_number_of_rooms(self, number_of_rooms: int):
        self._number_of_rooms = number_of_rooms

# Payment class
class Payment:
    def __init__(self, payment_id: int, reservation: Reservation, amount: float, payment_date: str, status: PaymentStatus):
        self._payment_id = payment_id
        self._reservation = reservation
        self._amount = amount
        self._payment_date = payment_date
        self._status = status

    # Getter and Setter Methods
    def get_payment_id(self) -> int:
        return self._payment_id

    def set_payment_id(self, payment_id: int):
        self._payment_id = payment_id

    def get_reservation(self) -> Reservation:
        return self._reservation

    def set_reservation(self, reservation: Reservation):
        self._reservation = reservation

    def get_amount(self) -> float:
        return self._amount

    def set_amount(self, amount: float):
        self._amount = amount

    def get_payment_date(self) -> str:
        return self._payment_date

    def set_payment_date(self, payment_date: str):
        self._payment_date = payment_date

    def get_status(self) -> PaymentStatus:
        return self._status

    def set_status(self, status: PaymentStatus):
        self._status = status

# Staff class
class Staff:
    def __init__(self, staff_id: int, first_name: str, last_name: str, role: str, email: str):
        self._staff_id = staff_id
        self._first_name = first_name
        self._last_name = last_name
        self._role = role
        self._email = email

    # Getter and Setter Methods
    def get_staff_id(self) -> int:
        return self._staff_id

    def set_staff_id(self, staff_id: int):
        self._staff_id = staff_id

    def get_first_name(self) -> str:
        return self._first_name

    def set_first_name(self, first_name: str):
        self._first_name = first_name

    def get_last_name(self) -> str:
        return self._last_name

    def set_last_name(self, last_name: str):
        self._last_name = last_name

    def get_role(self) -> str:
        return self._role

    def set_role(self, role: str):
        self._role = role

    def get_email(self) -> str:
        return self._email

    def set_email(self, email: str):
        self._email = email

# Refund class
class Refund:
    def __init__(self, refund_id: int, payment: Payment, amount_refunded: float, refund_date: str):
        self._refund_id = refund_id
        self._payment = payment
        self._amount_refunded = amount_refunded
        self._refund_date = refund_date

    # Getter and Setter Methods
    def get_refund_id(self) -> int:
        return self._refund_id

    def set_refund_id(self, refund_id: int):
        self._refund_id = refund_id

    def get_payment(self) -> Payment:
        return self._payment

    def set_payment(self, payment: Payment):
        self._payment = payment

    def get_amount_refunded(self) -> float:
        return self._amount_refunded

    def set_amount_refunded(self, amount_refunded: float):
        self._amount_refunded = amount_refunded

    def get_refund_date(self) -> str:
        return self._refund_date

    def set_refund_date(self, refund_date: str):
        self._refund_date = refund_date

# Creating Objects

# Creating a guest
guest = Guest("Ted", "Vera", "ledvera@mac.com", "505-661-1110", Gender.MALE)

# Creating a reservation
reservation = Reservation(52523687, guest, "Sun, Aug 22, 2010 - 03.00 PM", "Tue, Aug 24, 2010 - 12:00 PM", RoomType.QUEEN, 1)

# Creating a payment
payment = Payment(15541050358, reservation, 201.48, "2024-09-30", PaymentStatus.COMPLETED)

# Creating staff
staff = Staff(1, "Sara", "Ali", "Receptionist", "receptionist@example.com")

# Creating a refund
refund = Refund(1, payment, 0.0, "N/A")  # No refund in this scenario

# Displaying Information
print(f"Guest: {guest.get_first_name()} {guest.get_last_name()}, Email: {guest.get_email()}, Phone: {guest.get_phone()}")
print(f"Reservation ID: {reservation.get_reservation_id()}, Check-in: {reservation.get_check_in()}, Check-out: {reservation.get_check_out()}, Room Type: {reservation.get_room_type().value}")
print(f"Payment ID: {payment.get_payment_id()}, Amount: ${payment.get_amount()}, Status: {payment.get_status().value}")
print(f"Staff: {staff.get_first_name()} {staff.get_last_name()}, Role: {staff.get_role()}")
print(f"Refund ID: {refund.get_refund_id()}, Amount Refunded: ${refund.get_amount_refunded()}, Refund Date: {refund.get_refund_date()}")
