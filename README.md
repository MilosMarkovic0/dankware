# dankware
 Python module with various features!
 
## Multithreading
```py
from dankware import multithread
import time

a = 0
def example():
    global a
    a += 1
    print(a)
    time.sleep(5)
        
multithread(example, 10)
```
> <img width="404" alt="image" src="https://user-images.githubusercontent.com/52797753/153721721-0541e26b-f0b2-4c87-8c61-778a817cf80e.png">

<p>&nbsp;</p>    

---  

# Banners

```py
banner = '''

     888                   888                                             
     888                   888           s i r . d a n k ' s               
     888                   888                                             
 .d88888  8888b.  88888b.  888  888 888  888  888  8888b.  888d888 .d88b.  
d88" 888     "88b 888 "88b 888 .88P 888  888  888     "88b 888P"  d8P  Y8b 
888  888 .d888888 888  888 888888K  888  888  888 .d888888 888    88888888 
Y88b 888 888  888 888  888 888 "88b Y88b 888 d88P 888  888 888    Y8b.     
 "Y88888 "Y888888 888  888 888  888  "Y8888888P"  "Y888888 888     "Y8888  

'''
```

## Colourize Banner (random)
```py
from dankware import clr_banner
print(clr_banner(banner))
```
> <img width="429" alt="image" src="https://user-images.githubusercontent.com/52797753/153722086-2f372bfa-4872-46a0-81f8-cdf7c2344fd6.png">

## Align Banner (console center)
```py
from dankware import align_banner
print(align_banner(banner))
```
> <img width="617" alt="image" src="https://user-images.githubusercontent.com/52797753/153722230-1f3b6103-6d8a-4537-9828-1718a6bd3367.png">

## Align Coloured Banner
```py
from dankware import align_banner, clr_banner
print(align_banner(banner, clr_banner(banner)))
```
> <img width="638" alt="image" src="https://user-images.githubusercontent.com/52797753/153722373-9925dd25-83bb-4d1c-83eb-bfaae1802088.png">

<p>&nbsp;</p>    

---  

# Gradient Reworked [ Originally By @venaxyt ]

```py
from dankware import fade
banner = '''

                              888 d8b                   888    
       v e n a x y t ' s      888 Y8P                   888    
                              888                       888    
 .d88b.  888d888 8888b.   .d88888 888  .d88b.  88888b.  888888 
d88P"88b 888P"      "88b d88" 888 888 d8P  Y8b 888 "88b 888    
888  888 888    .d888888 888  888 888 88888888 888  888 888    
Y88b 888 888    888  888 Y88b 888 888 Y8b.     888  888 Y88b.  
 "Y88888 888    "Y888888  "Y88888 888  "Y8888  888  888  "Y888 
     888                                                       
Y8b d88P                                                       
 "Y88P"                                                        


'''
```

## Black
```py
print(fade(banner, "black"))
```
> <img width="370" alt="image" src="https://user-images.githubusercontent.com/52797753/153722811-b257611e-9111-4a0e-92fb-7dbe503ce6db.png">
```py
print(fade(banner, "black", "V"))
```
> <img width="363" alt="image" src="https://user-images.githubusercontent.com/52797753/153723205-a91eb1c6-07bc-4bc6-9fa6-52231e50a25c.png">

## Red
```py
print(fade(banner, "red"))
```
> <img width="372" alt="image" src="https://user-images.githubusercontent.com/52797753/153722946-3221bfd8-ff9d-4c9d-8b70-0c2736ec4e30.png">
```py
print(fade(banner, "red", "V"))
```
> <img width="367" alt="image" src="https://user-images.githubusercontent.com/52797753/153723473-bdb75ea7-2df2-4f70-adb5-cf5caa57200a.png">

## Green
```py
print(fade(banner, "green"))
```
> <img width="369" alt="image" src="https://user-images.githubusercontent.com/52797753/153723050-c30bd3f1-989a-4141-b40a-2869a2dadef6.png">
```py
print(fade(banner, "green", "V"))
```
> <img width="367" alt="image" src="https://user-images.githubusercontent.com/52797753/153723481-2e5c21b2-0f12-4d99-ab8d-a3e5c40e4c16.png">

## Cyan
```py
from dankware import fade
print(fade(banner, "cyan"))
```
> <img width="369" alt="image" src="https://user-images.githubusercontent.com/52797753/153723059-b4808365-6006-4726-b427-b6848e0fc0e5.png">
```py
print(fade(banner, "cyan", "V"))
```
> <img width="363" alt="image" src="https://user-images.githubusercontent.com/52797753/153723496-8d03c5d3-601e-499d-80cd-51c3648957bf.png">

## Blue
```py
print(fade(banner, "blue"))
```
> <img width="360" alt="image" src="https://user-images.githubusercontent.com/52797753/153723092-0a32d8e6-680e-4df3-bdf1-089663f25f45.png">
```py
print(fade(banner, "blue", "V"))
```
> <img width="363" alt="image" src="https://user-images.githubusercontent.com/52797753/153723509-41732010-b7d5-4867-95f9-690d47322536.png">

## Purple
```py
print(fade(banner, "purple"))
```
> <img width="367" alt="image" src="https://user-images.githubusercontent.com/52797753/153723148-2c94c459-1441-4752-a11f-a547754da7bc.png">
```py
print(fade(banner, "purple", "V"))
```
> <img width="357" alt="image" src="https://user-images.githubusercontent.com/52797753/153723519-00aa980e-4a04-4d8d-a319-5691c1f8e517.png">

## Pink
```py
print(fade(banner, "pink", "V"))
```
> <img width="363" alt="image" src="https://user-images.githubusercontent.com/52797753/153723540-b324dfe1-5ae2-4b66-ad3a-546a589558c8.png">

## Random
```py
print(fade(banner, "random", "V"))
```
> <img width="362" alt="image" src="https://user-images.githubusercontent.com/52797753/153723545-0ea34ea7-1844-4ace-8948-3e71e28c0a30.png">