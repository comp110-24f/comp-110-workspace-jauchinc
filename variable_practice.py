def get_weather_report() -> str:
    """Tells me how to deal with the weather"""
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize that weather.")
    return weather


if __name__ == "__main__":  # this runs the function automatically without a call
    get_weather_report()
