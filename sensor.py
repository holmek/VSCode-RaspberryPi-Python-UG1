# Jeg importerer modulerne fra gpiozero/asyncio
from gpiozero import MotionSensor, Buzzer
import asyncio

# Dette er mine pins på rpi5, som er gpio 16 og 12
sensor_pin = 16
buzzer_pin = 12

# Dette er mine objekter, som er pir, hvilket er motionsensoeren og buzzeren.
pir = MotionSensor(sensor_pin, queue_len=5, sample_rate=5, threshold=0.3, partial=False, pin_factory=None)
buzzer = Buzzer(buzzer_pin)

# Dette er min funktion som opfanger bevægelse og aktiverer buzzer, samt skriver en besked
async def motion_detection():
    while True:
        if pir.motion_detected:
            print("Bevægelse opfanget i nærheden. Buzzeren bliver aktiveret")
            buzzer.beep(on_time=0.5, off_time=0.5, n=1, background=True)
        await asyncio.sleep(1)

# Dette er min hovedfunktion hvor motion_detection bliver udløst
async def main():
    try:
        await motion_detection()
    except KeyboardInterrupt:
        print("Programmet lukker")

# Dette gør at main kører når jeg starter script
if __name__ == "__main__":
    asyncio.run(main())
    
