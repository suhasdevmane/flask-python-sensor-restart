import asyncio
import os

from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager

# EMAIL = os.environ.get("suhasdevmanecardiffuni@gmail.com")
# PASSWORD = os.environ.get("Suhas@551993")

EMAIL="suhasdevmanecardiffuni@gmail.com"
PASSWORD="Suhas@551993"


async def main():
    print(f"Email: {EMAIL}, Password: {PASSWORD}")  # Add this line
    # Setup the HTTP client API from user-password
    # When choosing the API_BASE_URL env var, choose from one of the above based on your location.
    # Asia-Pacific: "iotx-ap.meross.com"
    # Europe: "iotx-eu.meross.com"
    # US: "iotx-us.meross.com"
    http_api_client = await MerossHttpClient.async_from_user_password(api_base_url='https://iotx-eu.meross.com',
                                                                      email=EMAIL, 
                                                                      password=PASSWORD)

    # Setup and start the device manager
    manager = MerossManager(http_client=http_api_client)
    await manager.async_init()

    # Retrieve all the MSS310 devices that are registered on this account
    await manager.async_device_discovery()
    plugs = manager.find_devices(device_type="mss310")

    if len(plugs) < 1:
        print("No MSS310 plugs found...")
    else:
        # Choose the device based on its name
        chosen_device_name = "Bedroom_heater"    #or "Bedroom_heater"
        chosen_device = None
        for plug in plugs:
            if plug.name == chosen_device_name:
                chosen_device = plug
                break

        if chosen_device is None:
            print(f"Device with name '{chosen_device_name}' not found.")
        else:
            # The first time we play with a device, we must update its status
            await chosen_device.async_update()
            # We can now start playing with that        
            print(f"Turing off {chosen_device.name}")
            await chosen_device.async_turn_off(channel=0)
            print("Waiting a bit before turning it on")
            await asyncio.sleep(5)
            print(f"Turning on {chosen_device.name}...")
            await chosen_device.async_turn_on(channel=0)

    # Close the manager and logout from http_api
    manager.close()
    await http_api_client.async_logout()


if __name__ == '__main__':
    # Windows and python 3.8 requires to set up a specific event_loop_policy.
    #  On Linux and MacOSX this is not necessary.
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.stop()
