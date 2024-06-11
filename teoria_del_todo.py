import network
import socket
from time import sleep
import machine
from machine import Pin
import utime


ssid = 'wea'
password = '12345678'

Motor_A_Adelante = Pin(16, Pin.OUT)
Motor_A_Atras = Pin(17, Pin.OUT)
Motor_B_Adelante = Pin(18, Pin.OUT)
Motor_B_Atras = Pin(19, Pin.OUT)

def mover(numero, duty):
    servo_pwm = machine.PWM(machine.Pin(numero))
    servo_pwm.freq(50)
    servo_pwm.duty_u16(duty)

def adelante():
    Motor_A_Adelante.value(1)
    Motor_B_Adelante.value(1)
    Motor_A_Atras.value(0)
    Motor_B_Atras.value(0)
    
def atras():
    Motor_A_Adelante.value(0)
    Motor_B_Adelante.value(0)
    Motor_A_Atras.value(1)
    Motor_B_Atras.value(1)

def detener():
    Motor_A_Adelante.value(0)
    Motor_B_Adelante.value(0)
    Motor_A_Atras.value(0)
    Motor_B_Atras.value(0)

def izquierda():
    Motor_A_Adelante.value(1)
    Motor_B_Adelante.value(0)
    Motor_A_Atras.value(0)
    Motor_B_Atras.value(1)

def derecha():
    Motor_A_Adelante.value(0)
    Motor_B_Adelante.value(1)
    Motor_A_Atras.value(1)
    Motor_B_Atras.value(0)


detener()
    
def conectar():
    red = network.WLAN(network.STA_IF)
    red.active(True)
    red.connect(ssid, password)
    while red.isconnected() == False:
        print('Conectando ...')
        sleep(1)
    ip = red.ifconfig()[0]
    print(f'Conectado con IP: {ip}')
    return ip
    
def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def pagina_web():
    html = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                            <style>
                              #container {
                                position: relative;
                                margin: 0px;
                                width: 1000px;
                                height: 1100px;
                                left: 200px;
                                top: 200px;
                                perspective: 800px;
                                border: 0px solid black;
                              }
                              #brazo {
                                top: 300px;
                                left: 300px;
                                width: 25px;
                                height: 400px;
                                background-color: transparent;
                                border-radius: 0px;
                                position: relative;
                                transform: rotateZ(30deg)
                              }
                              #brazo::before {
                                content: "";
                                position: absolute;
                                width: 100%;
                                height: 50%;
                                border-radius: 40px 30px 30px 40px;
                                background-color: #5B618C;
                                border: 2px solid black;
                              }
                              
                              .brazo2 {
                                width: 400px;
                                height: 25px;
                                position: relative;
                                top: 0px;
                                left: -175px;
                                border-radius: 3px;
                                background-color: transparent;
                                transform: rotateZ(180deg)
                              }

                              .brazo2::after {
                                content: "";
                                position: absolute;
                                width: 50%;
                                height: 100%;
                                bottom: 0px;
                                right: 0px;
                                border-radius: 40px 30px 30px 40px;
                                background-color: #5B618C;
                                border: 2px solid black;
                              }
                              
                              .brazo3 {
                                width: 350px;
                                height: 20px;
                                position: absolute;
                                top: 10px;
                                left: 210px;
                                border-radius: 3px;
                                background-color: transparent;
                                transform: rotateZ(-40deg)
                              }

                              .brazo3::after {
                                content: "";
                                position: absolute;
                                width: 50%;
                                height: 100%;
                                bottom: 0px;
                                right: 0px;
                                border-radius: 40px 30px 30px 40px;
                                background-color: #5B618C;
                                border: 2px solid black;
                              }
                              
                              #brazo4 {
                                position: absolute;
                                width: 50px;
                                height: 9px;
                                top: 18px;
                                left: 340px;
                                z-index: -5;
                                border-radius: 40px 30px 30px 40px;
                                background-color: #5B618C;
                                border: 2px solid black;
                              }
                              
                              #brazo5 {
                                position: absolute;
                                width: 50px;
                                height: 9px;
                                top: 8px;
                                left: 380px;
                                z-index: -10;
                                border-radius: 40px 30px 30px 40px;
                                background-color: #5B618C;
                                border: 2px solid black;
                              }
                              
                              #motor1 {
                                top: 475px;
                                left: 300px;
                                width: 30px;
                                height: 18px;
                                background-color: #3C4EE2;
                                border-radius: 0px 0px 0px 0px;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid blue;  
                              }
                              
                              #motor2 {
                                background-color: #3C4EE2;
                                position: absolute;
                                border: 2px solid blue;
                                width: 30px;
                                height: 18px;
                                top: 1px;
                                left: 210px;
                                z-index: 10;
                              }
                              
                              #motor3 {
                                background-color: #3C4EE2;
                                position: absolute;
                                border: 2px solid blue;
                                width: 30px;
                                height: 18px;
                                top: 1px;
                                left: 350px;
                                z-index: 10;
                              }
                              
                              #motor4 {
                                background-color: #3C4EE2;
                                position: absolute;
                                border: 2px solid blue;
                                width: 30px;
                                height: 18px;
                                top: 23px;
                                left: 340px;
                                z-index: -10;
                              }
                              
                              #motor5 {
                                top: 540px;
                                left: 300px;
                                width: 30px;
                                height: 18px;
                                background-color: #3C4EE2;
                                border-radius: 0px 0px 0px 0px;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid blue;
                                z-index: -5;
                              }
                              
                              #motor6 {
                                top: 610px;
                                left: 360px;
                                width: 120px;
                                height: 40px;
                                background-color: #FFFB00;
                                border-radius: 10px 10px 10px 10px;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid black;
                              }


                               #tornillo1 {
                                width: 10px;
                                height: 10px;
                                position: absolute;
                                top: 500px;
                                left: 310px;
                                border-radius: 100%;
                                background-color: #BABCCB;
                                z-index: 10;
                                border: 1px solid black;
                              }
                              
                              #tornillo2 {
                                width: 10px;
                                height: 10px;
                                position: absolute;
                                top: 460px;
                                left: 310px;
                                border-radius: 100%;
                                background-color: #BABCCB;
                                z-index: 10;
                                border: 1px solid black;
                              }
                              
                              
                              #tornillo3 {
                                width: 10px;
                                height: 10px;
                                position: absolute;
                                top: 100px;
                                left: 8px;
                                border-radius: 100%;
                                background-color: #BABCCB;
                                z-index: 10;
                                border: 1px solid black;
                              }
                              
                              #tornillo4 {
                                width: 10px;
                                height: 10px;
                                position: absolute;
                                top: 50px;
                                left: 8px;
                                border-radius: 100%;
                                background-color: #BABCCB;
                                z-index: 10;
                                border: 1px solid black;
                              }

                              #tornillo5 {
                                width: 10px;
                                height: 10px;
                                position: absolute;
                                top: 5px;
                                left: 270px;
                                border-radius: 100%;
                                background-color: #BABCCB;
                                z-index: 10;
                                border: 1px solid black;
                              }
                              
                              #tornillo6 {
                                width: 10px;
                                height: 10px;
                                position: absolute;
                                top: 5px;
                                left: 310px;
                                border-radius: 100%;
                                background-color: #BABCCB;
                                z-index: 10;
                                border: 1px solid black;
                              }
                              

                              
                              #tornillo7 {
                                width: 10px;
                                height: 10px;
                                position: absolute;
                                top: 3px;
                                left: 310px;
                                border-radius: 100%;
                                background-color: #BABCCB;
                                z-index: 10;
                                border: 1px solid black;
                              }
                              
                              #tornillo8 {
                                width: 10px;
                                height: 10px;
                                position: absolute;
                                top: 3px;
                                left: 240px;
                                border-radius: 100%;
                                background-color: #BABCCB;
                                z-index: 10;
                                border: 1px solid black;
                              }
                              
                              #tornillo9 {
                                top: 535px;
                                left: 250px;
                                width: 8px;
                                height: 50px;
                                background-color: #BABCCB;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: -10;
                              }
                              
                              #tornillo10 {
                                top: 535px;
                                left: 360px;
                                width: 8px;
                                height: 50px;
                                background-color: #BABCCB;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: -10;
                              }
                              
                              #soporte {
                                top: 450px;
                                left: 260px;
                                width: 100px;
                                height: 80px;
                                background-color: #5B618C;
                                border-radius: 30px 30px 0px 0px;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid black;
                              }
                              
                              #soporte1 {
                                background-color: #F3523C;
                                position: absolute;
                                border: 2px #CF2710;
                                width: 25px;
                                height: 45px;
                                top: 60px;
                                left: 35px;
                                border-radius: 0px 15px 15px 0px;
                                z-index: -10;
                              }
                              
                              #soporte2 {
                                background-color: #F3523C;
                                position: absolute;
                                border: 2px #CF2710;
                                width: 25px;
                                height: 45px;
                                top: 18px;
                                left: 280px;
                                border-radius: 0px 15px 15px 0px;
                                z-index: -10;
                                transform: rotateZ(90deg)
                              }
                              
                              
                              #soporte3 {
                                top: 525px;
                                left: 230px;
                                width: 150px;
                                height: 15px;
                                background-color: #5B618C;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid black;
                              }
                              
                              
                              #soporte4 {
                                top: 578px;
                                left: 230px;
                                width: 150px;
                                height: 15px;
                                background-color: #5B618C;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid black;
                              }
                              
                              #soporte5 {
                                top: 593px;
                                left: 200px;
                                width: 550px;
                                height: 15px;
                                background-color: #5B618C;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid black;
                              }
                              
                              #soporte6 {
                                top: 570px;
                                left: 400px;
                                width: 320px;
                                height: 20px;
                                background-color: white;
                                border-radius: 5px 5px 5px 5px;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid black;
                              }
                              
                              #soporte7 {
                                top: 548px;
                                left: 420px;
                                width: 120px;
                                height: 20px;
                                background-color: white;
                                border-radius: 5px 5px 5px 5px;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid black;
                              }
                              
                              #rasberry {
                                top: 538px;
                                left: 470px;
                                width: 60px;
                                height: 10px;
                                background-color: #45AF00;
                                border-radius: 2px 2px 2px 2px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                              }
                              
                              #puenteh {
                                top: 559px;
                                left: 640px;
                                width: 80px;
                                height: 8px;
                                background-color: #DF2B15;
                                border-radius: 5px 5px 5px 5px;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid black;
                              }
                              
                              #llanta1 {
                                top: 570px;
                                left: 300px;
                                width: 100px;
                                height: 100px;
                                background-color: ;
                                border-radius: 100%;
                                position: absolute;
                                perspective: 100px;
                                border: 20px solid black;
                              }
                               
                              #llanta2 {
                                top: 590px;
                                left: 320px;
                                width: 60px;
                                height: 60px;
                                background-color: #F3D425;
                                border-radius: 100%;
                                position: absolute;
                                perspective: 100px;
                                border: 20px solid yellow;
                              }
                              
                              #cable1{
                                width: 22px;
                                height: 200px;
                                top: 0px;
                                left: 15px;
                                background-color: #EAB045;
                                position: absolute;
                                border-radius: 15px 15px 15px 15px;
                                z-index: -5;
                              }
                              
                              #cable2{
                                width: 200px;
                                height: 22px;
                                top: 8px;
                                left: 200px;
                                background-color: #EAB045;
                                position: absolute;
                                border-radius: 15px 15px 15px 15px;
                                z-index: -5;
                              }
                              
                              #cable3{
                                width: 180px;
                                height: 22px;
                                top: 5px;
                                left: 170px;
                                background-color: #EAB045;
                                position: absolute;
                                border-radius: 15px 15px 15px 15px;
                                z-index: -5;
                              }
                              
                              #soporteb{
                                top: 450px;
                                left: 1360px;
                                width: 250px;
                                height: 80px;
                                background-color: #5B61BC;
                                border-radius: 0px 0px 0px 0px;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid black;
                                z-index: -15;
                              }
                              
                              #soporteb2 {
                                top: -80px;
                                left: -70px;
                                width: 390px;
                                height: 80px;
                                background-color: #5B61BC;
                                border-radius: 100px 100px 0px 0px;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid black;
                                z-index: -10;
                              }
                              
                              #soporteb3 {
                                top: 0px;
                                left: -3px;
                                width: 253px;
                                height: 400px;
                                background-color: #5B61BC;
                                border-radius: 0px 0px 0px 0px;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid black;
                                z-index: -10;
                              }
                              
                              #soporteb4 {
                                top: 100px;
                                left: 25px;
                                width: 200px;
                                height: 290px;
                                background-color: #FFFFFF;
                                border-radius: 0px 0px 0px 0px;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid black;
                                z-index: -5;
                              }
                              
                              #soporteb5 {
                                top: 130px;
                                left: 80px;
                                width: 100px;
                                height: 150px;
                                background-color: #FFFFFF;
                                border-radius: 0px 0px 0px 0px;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid black;
                                z-index: -5;
                              }
                              
                              #soporteb6 {
                                top: -75px;
                                left: 45px;
                                width: 160px;
                                height: 160px;
                                background-color: #5B61BC;
                                border-radius: 100%;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid black;
                                z-index: -5;
                              }
                              
                              #soporteb7 {
                                top: 40px;
                                left: 40px;
                                width: 15px;
                                height: 70px;
                                background-color: #5B61BC;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: 10;
                              }
                              
                              #soporteb8 {
                                top: 40px;
                                left: 105px;
                                width: 15px;
                                height: 70px;
                                background-color: #5B61BC;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: 10;
                              }
                              
                              #soporteb9 {
                                top: -80px;
                                left: 57px;
                                width: 15px;
                                height: 160px;
                                background-color: #5B61BC;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: 5;
                              }
                              
                              #soporteb10 {
                                top:-80px;
                                left: 87px;
                                width: 15px;
                                height: 160px;
                                background-color: #5B61BC;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: 10;
                              }

                              #soporteb11 {
                                top: -200px;
                                left: 40px;
                                width: 15px;
                                height: 160px;
                                background-color: #5B61BC;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: 5;
                              }
                              
                              #soporteb12 {
                                top: -200px;
                                left: 105px;
                                width: 15px;
                                height: 160px;
                                background-color: #5B61BC;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: 5;
                              }

                              #soporteb13 {
                                top: -280px;
                                left: 25px;
                                width: 15px;
                                height: 100px;
                                background-color: #5B61BC;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: 5;
                              }
                              
                              #soporteb14 {
                                top: -280px;
                                left: 120px;
                                width: 15px;
                                height: 100px;
                                background-color: #5B61BC;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: 5;
                              }
                              
                              #soporteb15 {
                                top: -380px;
                                left: 40px;
                                width: 80px;
                                height: 150px;
                                background-color: #5B61BC;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: 5;
                              }
                              
                              #soporteb16 {
                                top: -380px;
                                left: 40px;
                                width: 15px;
                                height: 15px;
                                background-color: #5B61BC;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: 4;
                              }
                              
                              #soporteb17 {
                                top: -380px;
                                left: 105px;
                                width: 15px;
                                height: 15px;
                                background-color: #5B61BC;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: 4;
                              }
                              
                              #soporteb18 {
                                top: -60px;
                                left: 0px;
                                width: 15px;
                                height: 70px;
                                background-color: #5B61BC;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: 5;
                              }

                              #soporteb19 {
                                top: -60px;
                                left: 0px;
                                width: 15px;
                                height: 70px;
                                background-color: #5B61BC;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: 5;
                              }
                              
                              #soporteb20 {
                                top: -80px;
                                left: -10px;
                                width: 60px;
                                height: 15px;
                                background-color: #5B61BC;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: 0;
                                transform: rotateZ(-45deg)
                              }
                              
                              #soporteb21 {
                                top: -80px;
                                left: -35px;
                                width: 60px;
                                height: 15px;
                                background-color: #5B61BC;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: 0;
                                transform: rotateZ(-135deg)
                              }
                              
                              #motorb1 {
                                top: 55px;
                                left: 10px;
                                width: 28px;
                                height: 40px;
                                background-color: #3C4EE2;
                                border-radius: 0px 0px 0px 0px;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid blue;
                                z-index: 5;
                              }
                              
                              #motorb2 {
                                top: 55px;
                                left: 120px;
                                width: 28px;
                                height: 40px;
                                background-color: #3C4EE2;
                                border-radius: 0px 0px 0px 0px;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid blue;
                                z-index: 5;
                              }
                              
                              #motorb3 {
                                top: -95px;
                                left: 10px;
                                width: 28px;
                                height: 40px;
                                background-color: #3C4EE2;
                                border-radius: 0px 0px 0px 0px;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid blue;
                                z-index: 5;
                              }
                              
                              #motorb4 {
                                top: -200px;
                                left: 56px;
                                width: 28px;
                                height: 40px;
                                background-color: #3C4EE2;
                                border-radius: 0px 0px 0px 0px;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid blue;
                                z-index: 5;
                              }
                              
                              #motorb5 {
                                top: -360px;
                                left: 65px;
                                width: 28px;
                                height: 40px;
                                background-color: #3C4EE2;
                                border-radius: 0px 0px 0px 0px;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid blue;
                                z-index: 5;
                              }

                              
                              #rasb {
                                top: 200px;
                                left: 105px;
                                width: 50px;
                                height: 80px;
                                background-color: #2ABF2C;
                                border-radius: 2px 2px 2px 2px;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid black;
                                z-index: 0;
                              }
                              
                              #puentehb {
                                top: 310px;
                                left: 95px;
                                width: 70px;
                                height: 80px;
                                background-color: #F14848;
                                border-radius: 2px 2px 2px 2px;
                                position: absolute;
                                perspective: 100px;
                                border: 2px solid black;
                                z-index: 0;
                              }
                              
                               #tornillob1 {
                                top: -380px;
                                left: 40px;
                                width: 15px;
                                height: 15px;
                                background-color: #BABCCB;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: 10;
                              }
                              
                              #tornillob2 {
                                top: -380px;
                                left: 105px;
                                width: 15px;
                                height: 15px;
                                background-color: #BABCCB;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: 10;
                              }
                              
                               #tornillob3 {
                                top: -320px;
                                left: 40px;
                                width: 15px;
                                height: 15px;
                                background-color: #BABCCB;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: 10;
                              }
                              
                              #tornillob4 {
                                top: -320px;
                                left: 105px;
                                width: 15px;
                                height: 15px;
                                background-color: #BABCCB;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: 10;
                              }
                              
                              #llantab1 {
                                top: 50px;
                                left: 255px;
                                width: 80px;
                                height: 150px;
                                background-color: #000000;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: 5;
                              }
                              
                              #llantab2 {
                                top: 50px;
                                left: -90px;
                                width: 80px;
                                height: 150px;
                                background-color: #000000;
                                border-radius: 15px 15px 15px 15px;
                                position: absolute;
                                perspective: 100px;
                                border: 1px solid black;
                                z-index: 5;
                              }  
                              
                              #llantab3 {
                                top: 50px;
                                left: 330px;
                                width: 8px;
                                height: 150px;
                                background-color: #FFFB00;
                                border-radius: 0px 5px 5px 0px;
                                position: absolute;
                                perspective: 100px;
                                z-index: 6;
                              }
                              
                              #llantab4 {
                                top: 50px;
                                left: -90px;
                                width: 8px;
                                height: 150px;
                                background-color: #FFFB00;
                                border-radius: 5px 0px 0px 5px;
                                position: absolute;
                                perspective: 100px;
                                z-index: 6;
                              } 
                            </style>
                            <script>
                                let yPosition = 450;
                                let moving = false;
                                let movingb = false;
                                let rotationZ = 0;
                                let movingc = false;
                                let movingd = false;
                                let angbrazo3  = -45;
                                
                                function moveSoportebY() {
                                    if (moving) {
                                        const soporteb = document.getElementById('soporteb');
                                        yPosition -= 2;  // Incrementar la posición Y
                                        soporteb.style.top = `${yPosition}px`;
                                        requestAnimationFrame(moveSoportebY);
                                    }
                                }
                                function moveSoportebYb() {
                                    if (movingb) {
                                        const soporteb = document.getElementById('soporteb');
                                        yPosition += 2; 
                                        soporteb.style.top = `${yPosition}px`;
                                        requestAnimationFrame(moveSoportebYb); 
                                    }
                                }
                                function startMove() {
                                    moving = true;
                                    moveSoportebY();
                                }
                                function startMoveb() {
                                    movingb = true;
                                    moveSoportebYb();
                                }
                                function rotateSoportebZ() {
                                    if (movingc) {
                                        const soporteb = document.getElementById('soporteb');
                                        rotationZ += 1;
                                        soporteb.style.transform = `rotateZ(${rotationZ}deg)`;
                                        requestAnimationFrame(rotateSoportebZ);
                                    }
                                }
                                function rotateSoportebZb() {
                                    if (movingd) {
                                        const soporteb = document.getElementById('soporteb');
                                        rotationZ -= 1;
                                        soporteb.style.transform = `rotateZ(${rotationZ}deg)`;
                                        requestAnimationFrame(rotateSoportebZb);
                                    }
                                }
                                function startRotate() {
                                    movingc = true;
                                    rotateSoportebZ();
                                }
                                function startRotateb() {
                                    movingd = true;
                                    rotateSoportebZb();
                                }
                                function stopRotate() {
                                    moving = false;
                                    movingb = false;
                                    movingc = false;
                                    movingd = false;
                                }
                                
                                function movermotor1a(ang) {
                                    rotationZ = ang;
                                    const soporteb16 = document.getElementById('soporteb16');
                                    soporteb16.style.transform = `rotateZ(${rotationZ}deg)`;
                                }
                                function movermotor1b(ang) {
                                    rotationZ = ang;
                                    const soporteb17 = document.getElementById('soporteb17');
                                    soporteb17.style.transform = `rotateZ(${rotationZ}deg)`;
                                }
                                
                                function movermotor2(ang) {
                                    rotationZ = ang;
                                    const brazo3 = document.getElementById('brazo3');
                                    brazo3.style.transform = `rotateZ(${rotationZ}deg)`;
                                }
                                
                                function movermotor3(ang) {
                                    rotationZ = ang;
                                    const brazo2 = document.getElementById('brazo2');
                                    brazo2.style.transform = `rotateZ(${rotationZ}deg)`;
                                }
                                
                                function movermotor4(ang) {
                                    rotationZ = ang;
                                    const brazo = document.getElementById('brazo');
                                    brazo.style.transform = `rotateZ(${rotationZ}deg)`;
                                }
                                
                                function movermotor5(ang) {
                                    rotationZ = ang;
                                    const soporteb6 = document.getElementById('soporteb6');
                                    soporteb6.style.transform = `rotateZ(${rotationZ}deg)`;
                                }
                            </script>
                </head>

                <body>
                <h1>Grua:</h1>
                <!-- grafica -->
                                <div id="container">
                                    <div id="brazo" >
                                        <div id="tornillo3"></div>
                                        <div id="tornillo4"></div>
                                        <div id="cable1"></div>
                                        <div id="soporte1"></div>
                                            <div class="brazo2" id="brazo2">
                                                <div class="brazo3" id="brazo3">
                                                    <div id="tornillo7"></div>
                                                    <div id="tornillo8"></div>
                                                    <div id="cable3"></div>
                                                    <div id="motor4"></div>
                                                    <div id="brazo4"></div>
                                                    <div id="brazo5"></div>
                                                </div>
                                                <div id="tornillo5"></div>
                                                <div id="soporte2"></div>
                                                <div id="cable2"></div>
                                                <div id="motor2"></div>
                                                <div id="motor3"></div>
                                                <div id="tornillo6"></div>
                                            </div>
                                   </div>
                                   <div id="soporte" ></div>
                                   <div id="soporte3"></div>
                                   <div id="tornillo2"></div>
                                   <div id="tornillo1"></div>
                                   <div id="tornillo10"></div>
                                   <div id="tornillo9"></div>
                                   <div id="motor1"></div>
                                   <div id="motor5"></div>
                                   <div id="motor6"></div>
                                   <div id="soporte4"></div>
                                   <div id="soporte5"></div>
                                   <div id="soporte6"></div>
                                   <div id="soporte7"></div>
                                   <div id="rasberry"></div>
                                   <div id="puenteh"></div>
                                   <div id="llanta1"></div>
                                   <div id="llanta2"></div>
                                   <div id="soporteb">
                                       <div id="soporteb2"></div>
                                       <div id="soporteb3"></div>
                                       <div id="soporteb4"></div>
                                       <div id="soporteb5"></div>
                                       <div id="rasb"></div>
                                       <div id="puentehb"></div>
                                       <div id="soporteb6">
                                           <div id="soporteb7"></div>
                                           <div id="soporteb8"></div>
                                           <div id="soporteb9"></div>
                                           <div id="soporteb10"></div>
                                           <div id="soporteb11"></div>
                                           <div id="soporteb12"></div>
                                           <div id="soporteb13"></div>
                                           <div id="soporteb14"></div>
                                           <div id="soporteb15"></div>
                                           <div id="soporteb16">
                                               <div id="soporteb18"></div>
                                               <div id="soporteb20"></div>
                                           </div>
                                           <div id="soporteb17">
                                               <div id="soporteb19"></div>
                                               <div id="soporteb21"></div>
                                           </div>
                                           <div id="motorb1"></div>
                                           <div id="motorb2"></div>
                                           <div id="motorb3"></div>
                                           <div id="motorb4"></div>
                                           <div id="motorb5"></div>
                                           <div id="tornillob1"></div>
                                           <div id="tornillob2"></div>
                                           <div id="tornillob3"></div>
                                           <div id="tornillob4"></div>
                                       </div>
                                       <div id="llantab1"></div>
                                       <div id="llantab2"></div>
                                       <div id="llantab3"></div>
                                       <div id="llantab4"></div>
                                 </div>
                  
                                            <!--botones-->
                        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
                        <hr>
                        <h1>Controles:</h1>
                        <center>
                        <form action="./adelante" onsubmit="startMove();">
                        <input type="submit" value="Adelante"style="background-color: #04AA6D;border-radius: 15px;height:120px;width:120px;border: none;color: white;padding: 16px 24px;margin: 4px 2px"  />
                        </form>
                        <table><tr><td>
                        <form action="./izquierda" onsubmit="startRotateb();">
                        <input type="submit"value="Izquierda"style="background-color: #04AA6D;border-radius: 15px;height:120px; width:120px;border: none; color: white;padding: 16px 24px;margin: 4px 2px"/>
                        </form></td>
                        <td><form action="./detener" onsubmit="stopRotate()">
                        <input type="submit" value="Detener" style="background-color: #FF0000; border-radius: 50px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px" />
                        </form></td>
                        <td><form action="./derecha" onsubmit="startRotate();">
                        <input type="submit" value="Derecha" style="background-color: #04AA6D; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px"/>
                        </form></td>
                        </tr></table>
                        <form action="./atras" onsubmit="startMoveb();">
                        <input type="submit" value="Atras" style="background-color: #04AA6D; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px"/>
                        </form>
                        
                        <table><tr><td><form action="./motor1_0" onsubmit="movermotor1a(0);movermotor1b(0);">
                        <input type="submit"value="0%"style="background-color: #00FFF3;border-radius: 15px;height:120px; width:120px;border: none; color: white;padding: 16px 24px;margin: 4px 2px"/>
                        </form></td>
                        <td><form action="./motor1_50" onsubmit="movermotor1a(-45);movermotor1b(45);">
                        <input type="submit" value="50%" style="background-color: #00FFF3; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px"/>
                        </form></td>
                        <td><form action="./motor1_100" onsubmit="movermotor1a(-90);movermotor1b(90);">
                        <input type="submit" value="100%" style="background-color: #00FFF3; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px" />
                        </form></td>
                        </tr></table>
                        
                        <table><tr><td>
                        <form action="./motor2_0" onsubmit="movermotor2(-80);">
                        <input type="submit"value="0%"style="background-color: #0008FF;border-radius: 15px;height:120px; width:120px;border: none; color: white;padding: 16px 24px;margin: 4px 2px"/>
                        </form></td>
                        <td>
                        <form action="./motor2_50" onsubmit="movermotor2(0);">
                        <input type="submit" value="50%" style="background-color: #0008FF; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px"/>
                        </form></td>
                        <td>
                        <form action="./motor2_100" onsubmit="movermotor2(80);">
                        <input type="submit" value="100%" style="background-color: #0008FF; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px" />
                        </form></td>
                        </tr></table>
                        
                        <table><tr><td><form action="./motor3_0" onsubmit="movermotor3(180);">
                        <input type="submit"value="0%"style="background-color: #5500FF;border-radius: 15px;height:120px; width:120px;border: none; color: white;padding: 16px 24px;margin: 4px 2px"/>
                        </form></td>
                        <td><form action="./motor3_50" onsubmit="movermotor3(230);">
                        <input type="submit" value="50%" style="background-color: #5500FF; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px"/>
                        </form></td>
                        <td><form action="./motor3_100" onsubmit="movermotor3(270);">
                        <input type="submit" value="100%" style="background-color: #5500FF; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px" />
                        </form></td>
                        </tr></table>
                        
                        <table><tr><td><form action="./motor4_0" onsubmit="movermotor4(-30);">
                        <input type="submit"value="0%"style="background-color: #AA00FF;border-radius: 15px;height:120px; width:120px;border: none; color: white;padding: 16px 24px;margin: 4px 2px"/>
                        </form></td>
                        <td><form action="./motor4_50" onsubmit="movermotor4(30);">
                        <input type="submit" value="50%" style="background-color: #AA00FF; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px"/>
                        </form></td>
                        <td><form action="./motor4_100" onsubmit="movermotor4(90);">
                        <input type="submit" value="100%" style="background-color: #AA00FF; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px" />
                        </form></td>
                        </tr></table>
                        
                        <table><tr><td><form action="./motor5_0;" onsubmit="movermotor5(-90);">
                        <input type="submit"value="0%"style="background-color: #FF00DC;border-radius: 15px;height:120px; width:120px;border: none; color: white;padding: 16px 24px;margin: 4px 2px"/>
                        </form></td>
                        <td><form action="./motor5_50" onsubmit="movermotor5(0);">
                        <input type="submit" value="50%" style="background-color: #FF00DC; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px"/>
                        </form></td>
                        <td><form action="./motor5_100" onsubmit="movermotor5(90);">
                        <input type="submit" value="100%" style="background-color: #FF00DC; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px" />
                        </form></td>
                        </tr></table>
                        
              </div>
                                
            </body>

            </html>
            """
    return str(html)

def serve(connection):
    while True:
        cliente = connection.accept()[0]
        peticion = cliente.recv(1024)
        peticion = str(peticion)
        try:
            peticion = peticion.split()[1]
        except IndexError:
            pass
        if peticion == '/adelante?':
            adelante()
        elif peticion =='/izquierda?':
            izquierda()
        elif peticion =='/detener?':
            detener()
        elif peticion =='/derecha?':
            derecha()
        elif peticion =='/atras?':
            atras()
        elif peticion =='/motor1_0?':
            mover(1,1000)
        elif peticion =='/motor1_50?':
            mover(1,1500)
        elif peticion =='/motor1_100?':
            mover(1,2000)
        elif peticion =='/motor2_0?':
            mover(2,900)
        elif peticion =='/motor2_50?':
            mover(2,4450)
        elif peticion =='/motor2_100?':
            mover(2,8000)
        elif peticion =='/motor3_0?':
            mover(3,1000)
        elif peticion =='/motor3_50?':
            mover(3,4000)
        elif peticion =='/motor3_100?':
            mover(3,7000)
        elif peticion =='/motor4_0?':
            mover(4,7000)
            mover(5,1000)
        elif peticion =='/motor4_50?':
            mover(4,4000)
            mover(5,4000)
        elif peticion =='/motor4_100?':
            mover(4,1000)
            mover(5,7000)
        elif peticion =='/motor5_0?':
            mover(6,1000)
        elif peticion =='/motor5_50?':
            mover(6,4500)
        elif peticion =='/motor5_100?':
            mover(6,8000)
        html = pagina_web()
        cliente.send(html)
        cliente.close()

try:
    ip = conectar()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()
