from ev3dev2.motor import LargeMotor
import time

duties = [100, 80, 60, 40, 20, -20, -40, -60, -80, -100]
motor = LargeMotor('outA')

with open("data.csv", "w") as file:
    for duty in duties:
        start_time = time.time()
        start_position = motor.position
        motor.run_direct(duty_cycle_sp=duty)
        while True:
            time_from_start = time.time() - start_time
            position_from_start = motor.position - start_position
            file.write("{},{},{}\n".format(time_from_start, position_from_start, motor.speed))
            if time_from_start > 2:
                break
        file.write("end\n")
        motor.run_direct(duty_cycle_sp=0)
        time.sleep(1)
    motor.run_direct(duty_cycle_sp=0)
