# ehc/main.py
import os
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()


class ChargingCostRequest(BaseModel):
    """
    Represents a request for charging cost calculation.

    Attributes:
        battery_capacity (float): The capacity of the battery in kilowatt-hours.
        on_peak_cost_per_kwh (float): The cost per kilowatt-hour during on-peak hours.
        off_peak_cost_per_kwh (float): The cost per kilowatt-hour during off-peak hours.
        charging_speed (ChargingSpeed): The speed of charging, either "level1" or "level2".
    """
    battery_capacity: float
    on_peak_cost_per_kwh: float
    off_peak_cost_per_kwh: float

    class ChargingSpeed(str, Enum):
        LEVEL1 = "level1"
        LEVEL2 = "level2"

    charging_speed: ChargingSpeed


@app.post("/calculate")
async def calculate_charging_cost(request: ChargingCostRequest):
    """
    Calculate the cost of charging a vehicle based on the battery capacity, and electricity costs.

    Args:
        request (ChargingCostRequest): The request object containing the charging parameters.

    Returns:
        dict: A dictionary containing the calculated costs and a summary of the charging cost.

    Raises:
        dict: An error dictionary if an invalid charging speed is selected.
    """
    battery_capacity = request.battery_capacity
    on_peak_cost_per_kwh = request.on_peak_cost_per_kwh
    off_peak_cost_per_kwh = request.off_peak_cost_per_kwh
    charging_speed = request.charging_speed

    # Convert cents to dollars
    on_peak_cost_per_kwh = on_peak_cost_per_kwh / 100
    off_peak_cost_per_kwh = off_peak_cost_per_kwh / 100

    # Determine charging time based on speed
    if charging_speed == "level1":
        charging_time_hours = 50  # Level 1 takes 40-50 hours to charge from empty
        charging_description = "Level 1 (120V outlet, 40-50 hours from empty)"
    elif charging_speed == "level2":
        charging_time_hours = 10  # Level 2 takes 4-10 hours to charge from empty
        charging_description = "Level 2 (220V outlet, 4-10 hours from empty)"
    else:
        return {"error": "Invalid charging speed selected. Choose 'level1' or 'level2'."}

    # Calculate total costs
    on_peak_cost = battery_capacity * on_peak_cost_per_kwh
    off_peak_cost = battery_capacity * off_peak_cost_per_kwh

    # Calculate cost per hour
    on_peak_cost_per_hour = on_peak_cost / charging_time_hours
    off_peak_cost_per_hour = off_peak_cost / charging_time_hours

    # Create summary
    summary = (
        f"Charging your vehicle using {charging_description} will cost:\n"
        f"- ${on_peak_cost:.2f} during on-peak hours (${on_peak_cost_per_hour:.2f} per hour)\n"
        f"- ${off_peak_cost:.2f} during off-peak hours (${off_peak_cost_per_hour:.2f} per hour)\n"
        "You should schedule your charging between off-peak hours for the cheapest costs."
    )

    return {
        "on_peak_cost": round(on_peak_cost, 2),
        "off_peak_cost": round(off_peak_cost, 2),
        "on_peak_cost_per_hour": round(on_peak_cost_per_hour, 2),
        "off_peak_cost_per_hour": round(off_peak_cost_per_hour, 2),
        "summary": summary
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
