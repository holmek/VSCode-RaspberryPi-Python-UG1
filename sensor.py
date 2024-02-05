import asyncio
from gpiozero import Buzzer
from gpiozero import MotionSensor

# Dette er mine pins på rpi5, som er gpio 16 og 12
sensor_pin = 16
buzzer_pin = 12

# Dette er mine objekter, som er pir, hvilket er motionsensoeren og buzzeren.
pir = MotionSensor(sensor_pin, queue_len=1, sample_rate=10, threshold=0.5, partial=False, pin_factory=None)
buzzer = Buzzer(buzzer_pin)

# Dette er min funktion som opfanger bevægelse og aktiverer buzzer, samt skriver en besked
async def motion_sensor():
    while True:
        if pir.motion_detected:
            print("Bevægelse opfanget i nærheden")
            buzzer.on()
            print("Buzzeren bliver aktiveret")
            buzzer.off()
        await asyncio.sleep(10)

# Dette er min hovedfunktion hvor motion_detection bliver udløst
async def main():
    try:
        task = asyncio.create_task(motion_sensor())
        await asyncio.gather(task)
    except KeyboardInterrupt:
        print("Programmet lukker")

# Dette gør at main kører når jeg starter script
if __name__ == "__main__":
    asyncio.run(main())
