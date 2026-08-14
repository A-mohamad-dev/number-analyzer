def main():
    while True:
        numbers = get_numbers()

        if not numbers:
            print("No valid numbers entered.")
        else:
            statistics = calculate_statistics(numbers)
            display_results(numbers, statistics)
  
        again = input("\nDo you want to analyze more numbers? (y/n): ").strip().lower()
        
        print()
    
        if again != "y":
            print("Goodbye!")
            print()
            break
    
def get_numbers():
    numbers_list = []
    user_input = input("Enter numbers separated with spaces: ")
    print()
    
    for item in user_input.split():
      try:
          numbers_list.append(int(item))
      except ValueError:
          print(f"{item} is not a valid number")

    print()
    return numbers_list

def analyze_number(number):
    if number == 0: 
        sign = "zero"
    elif number > 0: 
        sign = "positive"
    else:
        sign = "negative"
    
    parity =  "even" if number % 2 == 0 else "odd"
    
    return parity, sign

def calculate_statistics(numbers):
    positive = 0
    negative = 0
    zero = 0
    even = 0
    odd = 0

    for number in numbers:
        parity, sign = analyze_number(number)
    
        if parity == "even":
            even += 1
        else:
            odd += 1
    
        if sign == "zero":
            zero += 1
        elif sign == "positive":
            positive += 1
        else:
            negative += 1
  
    total = sum(numbers)
    if numbers:
        average = total/len(numbers)
    else:
        average = None
    return {
        "even": even,
        "odd" : odd,
        "zero" : zero,
        "positive" : positive,
        "negative" : negative,
        "sum" : total,
        "average" : average,
        }

def display_results(numbers, statistics):
    print("\n========== Number Analyzer ==========\n")
    
    for number in numbers:
        parity, sign = analyze_number(number)
        print(f"{number:>5} is {parity} and {sign}")
    
    print("\n---------- Statistics ----------\n")
    
    print(f"Even:     {statistics['even']}")
    print(f"Odd:      {statistics['odd']}")
    print(f"Zero:     {statistics['zero']}")
    print(f"Positive: {statistics['positive']}")
    print(f"Negative: {statistics['negative']}")
    print(f"Sum:      {statistics['sum']}")
    print(f"Average:  {statistics['average']:.2f}")

if __name__ == "__main__":
    main()