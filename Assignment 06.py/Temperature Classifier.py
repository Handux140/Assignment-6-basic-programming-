def classify_temperature(temperature):
    if temperature < 5:
        return "Freezing"
    elif temperature < 10:
        return "Very Cold"
    elif temperature < 20:
        return "Cold"
    elif temperature < 30:
        return "Moderate"
    elif temperature < 40:
        return "Hot"
    else:
         return "very hot"
def main():
        temperature = float(input("Enter the temperature: "))
        classification = classify_temperature(temperature)
        print("Temperature Classification:", classification)

if __name__ == "__main__":
    main()