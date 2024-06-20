# Electric Vehicle Home Charging Calculator [EHC]

This is a cost calculator for charging electric vehicles at home.

I recently purchased my first electric vehicle, a Mazda CX-90 PHEV (plug-in hybrid), and I couldn't find a suitable EV cost calculator to determine the cost of charging at home in the US. So I decided to create one.

You see, the cost of charging an electric vehicle at home is not as simple as it seems. It depends on the following factors:
- The cost of electricity in your area
- The efficiency of your electric vehicle
- The capacity of your electric vehicle's battery
- The charging speed of your electric vehicle
- The charging speed of your home charger
- The time of day you charge your electric vehicle
- The day of the week you charge your electric vehicle
- The month of the year you charge your electric vehicle
- The weather conditions when you charge your electric vehicle
- The temperature when you charge your electric vehicle

Right now we only take into account the cost of electricity in your area, on and off peak rates, the charging speed of your home charger setup and the size of your electric vehicle battery. I plan to add more factors in the future. If you have any suggestions, please let me know by creating an issue or a pull request.

## How to use the calculator
You can access the calculator by visiting the hosted swagger doc [here](https://ehc.onrender.com/docs) (on a free instance so it may take a couple of seconds to boot up) or by running the following command in your terminal:

```bash
poetry run ehc/main.py
```

And then visiting [http://localhost:8000/docs](http://localhost:8000/docs) in your browser.

## How to calculate the cost of charging an electric vehicle at home
To calculate the cost of charging an electric vehicle at home, you need to know the following information:
- The cost of electricity in your area
- The on-peak cost per kilowatt-hour
- The off-peak cost per kilowatt-hour
- The capacity of the battery in kilowatt-hours
- The charging speed of your charging setup

You can find the cost of electricity in your area by visiting your utility company's website or by calling them. You can find the on-peak and off-peak rates by looking at your utility bill or by visiting your utility company's website.

The capacity of the battery in kilowatt-hours is usually listed in the owner's manual of your electric vehicle. The charging speed of your charging setup is usually listed in the owner's manual of your home charger.

Once you have this information, you can use the calculator to determine the cost of charging your electric vehicle at home by hitting the "Try it out" button on the "calculate" endpoint section within the swagger docs and entering the required information listed above (real front end coming soon).
