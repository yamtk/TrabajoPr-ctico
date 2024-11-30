#Punto 1:

# class rectángulo:

#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura

#     def calcular_area (self):
#         return self.base * self.altura
    
# rectangulo = rectángulo(5, 10)
# area = rectangulo.calcular_area()

# print(f"El área de rectangulo es {area}")






#Punto 2:

# class Mate:
#     def __init__(self, n):
#         self.cebadas = n
#         self.cebadas_restantes = n
#         self.estado = "vacio"

#     def cebar(self):
#         if self.estado == "leno":
#             print("¡Cuidado! ¡Te quemaste!")
#         else:
#             self.estado = "lleno"
    
#     def beber(self):
#         if self.estado == "vacio":
#             print("¡El mate está vacio!")
#         else:
#             self.estado = "vacio"
#             if self.cebadas_restantes > 0:
#                 self.cebadas_restantes -= 1
#             else:
#                 print("¡El mate está lavado")
# mate = Mate(3)

# mate.cebar
# mate.cebar
# print(f"Cebadas restantes: {mate.cebadas_restantes}")

# mate.beber()

# mate.cebar()
# mate.beber()
# mate.cebar()
# mate.beber()
# print(f"Cebadas restantes: {mate.cebadas_restantes}")







#Punto 3:

# class Corcho:
#     def __init__(self, bodega):
#         self.bodega = bodega

# class Botella:
#     def __init__(self, corcho):

#         self.corcho = corcho 

#     def tiene_corcho(self):
#         return self.corcho != "Sin corcho"

# class Sacacorchos:
#     def __init__(self):
#         self.corcho = "Vacío"
        
#     def tiene_corcho(self):
#         return self.corcho != "Vacío"

#     def destapar(self, botella):
#         if self.tiene_corcho():
#             print("El sacacorchos ya contiene un corcho. Limpialo primero")
#         elif not botella.tiene_corcho():
#             print("La botella está destapada.")
#         else:
#             self.corcho = botella.corcho 
#             botella.corcho = "Sin corcho"  
#             print(f"¡Botella destapada exitosamente! Corcho de la bodega: {self.corcho.bodega}")

#     def limpiar(self):
#         if not self.tiene_corcho():
#             print("El sacacorchos está limpio.")
#         else:
#             print(f"Se ha limpiado el corcho de la bodega: {self.corcho.bodega}")
#             self.corcho = "Vacío"

# corcho = Corcho("Bodega Los Andes")  
# botella = Botella(corcho)  
# sacacorchos = Sacacorchos() 

# sacacorchos.destapar(botella)
# sacacorchos.destapar(botella)

# sacacorchos.limpiar()
# sacacorchos.limpiar()







#Punto 4

# class Restaurante:
#     def __init__(self, restaurante_nombre, tipo_comida):
#         self.restaurante_nombre = restaurante_nombre
#         self.tipo_comida = tipo_comida

#     def describir_restaurante(self):
#         print(f"Restaurante: {self.restaurante_nombre}")
#         print(f"Tipo de comida: {self.tipo_comida}")

#     def abrir_restaurante(self):
#         print(f"El restaurante {self.restaurante_nombre} ahora está abierto.")


# class Heladeria(Restaurante):
#     def __init__(self, restaurante_nombre, tipo_comida, sabores):
#         super().__init__(restaurante_nombre, tipo_comida)
#         self.sabores = sabores

#     def mostrar_sabores(self):
#         print(f"Sabores disponibles en {self.restaurante_nombre}:")
#         for sabor in self.sabores:
#             print(f"- {sabor}")



# mi_heladeria = Heladeria("La Casa del Helado", "Helados artesanales", ["Vainilla", "Chocolate", "Fresa", "Menta"])
# mi_heladeria.describir_restaurante()  
# mi_heladeria.abrir_restaurante()      
# mi_heladeria.mostrar_sabores()        







#Punto 5:

# class Personaje:
#     def __init__(self, vida, posicion, velocidad):
#         self.vida = vida
#         self.posicion = posicion 
#         self.velocidad = velocidad

#     def recibir_ataque(self, daño):
#         self.vida -= daño
#         if self.vida <= 0:
#             print("¡El personaje ha muerto!")

#     def mover(self, direccion):
#         self.posicion[0] += direccion[0] * self.velocidad
#         self.posicion[1] += direccion[1] * self.velocidad
#         print(f"El personaje se movió a la posición {self.posicion}")


# class Soldado(Personaje):
#     def __init__(self, vida, posicion, velocidad, ataque):
#         super().__init__(vida, posicion, velocidad)
#         self.ataque = ataque

#     def atacar(self, objetivo):
#         print(f"El soldado ataca al objetivo con {self.ataque} de daño.")
#         objetivo.recibir_ataque(self.ataque)


# class Campesino(Personaje):
#     def __init__(self, vida, posicion, velocidad, cosecha):
#         super().__init__(vida, posicion, velocidad)
#         self.cosecha = cosecha

#     def cosechar(self):
#         print(f"El campesino cosechó {self.cosecha} unidades.")
#         return self.cosecha


# soldado = Soldado(vida=100, posicion=[0, 0], velocidad=2, ataque=15)
# campesino = Campesino(vida=50, posicion=[5, 5], velocidad=1, cosecha=20)


# soldado.mover([1, 1])  
# soldado.atacar(campesino)
# campesino.cosechar()
# campesino.mover([-1, 0])  







#Punto 6

# class Usuario:
#     def __init__(self, nombre, apellido, edad, email, ciudad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.email = email
#         self.ciudad = ciudad

#     def describir_usuario(self):
#         print(f"Información del usuario:")
#         print(f"- Nombre: {self.nombre} {self.apellido}")
#         print(f"- Edad: {self.edad}")
#         print(f"- Email: {self.email}")
#         print(f"- Ciudad: {self.ciudad}")

#     def saludar_usuario(self):
#         print(f"Hola, {self.nombre} {self.apellido}. Bienvenido de nuevo.\n")



# usuario1 = Usuario("Carlos", "Gómez", 30, "carlos.gomez@gmail.com", "Buenos Aires")
# usuario2 = Usuario("María", "López", 25, "maria.lopez@gmail.com", "Salta")
# usuario3 = Usuario("Ana", "Martínez", 35, "ana.martinez@gmail.com", "Córdoba")

# usuarios = [usuario1, usuario2, usuario3]

# for usuario in usuarios:
#     usuario.describir_usuario()
#     usuario.saludar_usuario()







#Punto 7:

# class Usuario:
#     def __init__(self, nombre, apellido, edad, email, ciudad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.email = email
#         self.ciudad = ciudad

#     def describir_usuario(self):
#         print(f"Información del usuario:")
#         print(f"- Nombre: {self.nombre} {self.apellido}")
#         print(f"- Edad: {self.edad}")
#         print(f"- Email: {self.email}")
#         print(f"- Ciudad: {self.ciudad}")

#     def saludar_usuario(self):
#         print(f"Hola, {self.nombre} {self.apellido}! Bienvenido de nuevo.\n")


# class Admin(Usuario):
#     def __init__(self, nombre, apellido, edad, email, ciudad, privilegios):
#         super().__init__(nombre, apellido, edad, email, ciudad)
#         self.privilegios = privilegios

#     def mostrar_privilegios(self):
#         print(f"Privilegios de {self.nombre} {self.apellido}:")
#         for privilegio in self.privilegios:
#             print(f"- {privilegio}")

# admin = Admin(
#     nombre="Laura",
#     apellido="Fernández",
#     edad=40,
#     email="laura.fernandez@gmail.com",
#     ciudad="Salta capital",
#     privilegios=["puede postear en el foro", "puede borrar un post", "puede banear usuarios"])

# admin.describir_usuario()  
# admin.mostrar_privilegios() 





#Punto 8:

# class Usuario:
#     def __init__(self, nombre, apellido, edad, email, ciudad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.email = email
#         self.ciudad = ciudad

#     def describir_usuario(self):
#         print(f"Información del usuario:")
#         print(f"- Nombre: {self.nombre} {self.apellido}")
#         print(f"- Edad: {self.edad}")
#         print(f"- Email: {self.email}")
#         print(f"- Ciudad: {self.ciudad}")

#     def saludar_usuario(self):
#         print(f"Hola, {self.nombre} {self.apellido}! Bienvenido de nuevo.\n")


# class Privilegios:
#     def __init__(self, privilegios):
#         self.privilegios = privilegios

#     def mostrar_privilegios(self):
#         print("Privilegios:")
#         for privilegio in self.privilegios:
#             print(f"- {privilegio}")


# class Admin(Usuario):
#     def __init__(self, nombre, apellido, edad, email, ciudad, privilegios):
#         super().__init__(nombre, apellido, edad, email, ciudad)
#         self.privilegios = Privilegios(privilegios)


# admin = Admin(
#     nombre="Laura",
#     apellido="Fernández",
#     edad=40,
#     email="laura.fernandez@gmail.com",
#     ciudad="Salta Capital",
#     privilegios=["puede postear en el foro", "puede borrar un post", "puede banear usuarios"]
# )


# admin.describir_usuario() 
# admin.privilegios.mostrar_privilegios()  






#Punto 9:

# from restaurante import Restaurante

# mi_restaurante = Restaurante("La Pizzería", "Italiana")
# mi_restaurante.describir_restaurante() 
# mi_restaurante.abrir_restaurante()      


# #Punto 10:

# from heladería import Heladeria

# mi_heladeria = Heladeria("Helados del Mundo", "Helados",
# ["Chocolate", "Vainilla", "Fresa", "Mango"])


# mi_heladeria.describir_restaurante()  
# mi_heladeria.abrir_restaurante()     
# mi_heladeria.mostrar_sabores()        
