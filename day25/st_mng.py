import time
import random

class InvalideMarksError(Exception):
    "Raised when the marks are not in between 0 to 100"
    pass

class InsufficientBalanceError(Exception):
    "Raised when balance is less than exam fee"
    pass

def get_valid_marks(subject_name:str)->float:

   while True:
    try:
      marks = float(input(f"Enter a marks of {subject_name} in between 0/100"))

      if marks <0 or marks > 100:
         raise InvalideMarksError("Marks should be positive and greater than 0 less then 100")

      return marks

    except ValueError as e:
      print(f"Error: {e}")

    except InvalideMarksError as e:
      print(f"Error: {e}")

def simulate_bank_api(amount:float)-> str:
    """Simulate bank Api payment processing, 50% chance of success, 50% chance of failure"""
    if random.choice([True,False]):
        raise ConnectionError("Bank Api is not available/ bank Gateway Timeout / Network Interrupted")


    return f"payment of rupees {amount:.2f} processed successfully"

def process_payment_with_retry(amount:float,max_attempts:int=3)->str:
    for attempt in range(1, max_attempts + 1):
        try:
            result = simulate_bank_api(amount)
            return result
        except ConnectionError as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt < max_attempts:
                wait = 2 ** (attempt - 1)
                print(f"Retrying in {wait} seconds...")
                time.sleep(wait)
            else:
                raise ConnectionError(
                    "Max attempts reached, payment failed"
                )



def main():

    print("=" * 50)
    print("Welcome to the Student Marks and Payment System")
    print("=" * 50)

    student_bank_balance = 1000.00
    per_subject_exam_fee = 200

    try:

        # Get marks
        mark_physics = get_valid_marks("Physics")
        mark_chemistry = get_valid_marks("Chemistry")
        mark_math = get_valid_marks("Maths")

        # Calculate result
        total_marks = mark_physics + mark_chemistry + mark_math
        percentage = (total_marks / 300) * 100

        print(f"\nTotal Marks: {total_marks}/300")
        print(f"Percentage: {percentage:.2f}%")

        # Check result
        if percentage < 50 or mark_chemistry < 40 or mark_physics < 40 or mark_math < 40:
            print("Sorry, you are failed in the exam.")
            print("You need to pay the exam fee again.")
        else:
            print("Congratulations! You passed the exam.")

        # Calculate fee
        total_fee = per_subject_exam_fee * 3

        # Check bank balance
        if student_bank_balance < total_fee:
            raise InsufficientBalanceError(
                f"Insufficient balance. You need to pay "
                f"{total_fee:.2f} rupees."
            )

        # Process payment
        receipt = process_payment_with_retry(total_fee)

        # Deduct balance
        student_bank_balance -= total_fee

        print(receipt)
        print(f"Remaining balance: {student_bank_balance:.2f}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main() 





    

