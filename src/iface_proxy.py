import controller, solid_animation, time
from multiprocessing import Process

control = controller.Controller()

spin = Process(target=lambda x:x.spin(), args=(control,))
spin.start()

solid = solid_animation.SolidAnimation(time.time() + 0.5,
                                       time.time() + 5,
                                       0.2, 0.8, 0xff0000)
control.add_animation(solid)

time.sleep(10)
spin.join()
