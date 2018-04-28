import sys, controller_model, interface_proxy
from threading import Thread

control = controller_model.Controller()
t1 = Thread(target=interface_proxy.Interface, args=(sys.argv[1],int(sys.argv[2]), control))
t1.start()
t2 = Thread(target=control.spin)
t2.start()
