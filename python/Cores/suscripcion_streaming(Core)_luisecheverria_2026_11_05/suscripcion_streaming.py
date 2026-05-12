"""
Define la clase SuscripcionStreaming, que debe incluir:

Atributos:
usuario (nombre del usuario asociado a la suscripción)
tipo_suscripcion (Gratis, Estándar, Premium)
costo_mensual (según el tipo de suscripción)
saldo_pendiente (monto acumulado que debe pagar el usuario)
Métodos:
realizar_pago(self, monto) reduce el saldo pendiente según el monto pagado.
cambiar_suscripcion(self, nuevo_tipo) cambia el tipo de suscripción y ajusta el costo mensual.
ver_contenido_exclusivo(self) permite el acceso a contenido según el tipo de suscripción. La suscripción “Gratis” no tiene acceso a contenido exclusivo.
mostrar_info_suscripcion(self) muestra el estado actual de la suscripción del usuario."""



class SuscripcionStreaming:
    costos_suscripcion = {"Gratis": 0,"Estándar": 5.99,"Premium": 10.99}

    def __init__(self, usuario, tipo_suscripcion="Gratis"):
        self.usuario = usuario
        self.tipo_suscripcion = tipo_suscripcion
        self.costo_mensual = self.costos_suscripcion(tipo_suscripcion)
        self.saldo_pendiente = self.costo_mensual

    def realizar_pago(self, monto):
        """Reduce el saldo pendiente según el monto pagado."""
        self.saldo_pendiente -= monto
        print(f"Pago realizado: ${monto:.2f}. Saldo pendiente: ${self.saldo_pendiente:.2f}.")

    def cambiar_suscripcion(self, nuevo_tipo):
        """Cambia el tipo de suscripción y actualiza el costo mensual."""
        if nuevo_tipo in self.costos_suscripcion:
            self.tipo_suscripcion = nuevo_tipo
            self.costo_mensual = self.costos_suscripcion[nuevo_tipo]
            self.saldo_pendiente = self.costos_suscripcion[nuevo_tipo]
            print(f"{self.usuario} ha cambiado a {nuevo_tipo}.")
        else:
            print(f"Error: '{nuevo_tipo}' no es un tipo de suscripción válido.")

    def ver_contenido_exclusivo(self):
        """Permite ver contenido exclusivo según el tipo de suscripción."""
        if self.tipo_suscripcion == "Gratis":
            print("Acceso denegado. Suscríbete para ver contenido exclusivo.")

        elif self.tipo_suscripcion == "Estándar":
            print("Acceso a contenido exclusivo limitado.")

        elif self.tipo_suscripcion == "Premium":
            print("Acceso completo a contenido exclusivo.")
       

    def mostrar_info_suscripcion(self):
        """Muestra la información de la suscripción del usuario."""
        print(
            f"Usuario: {self.usuario}, "
            f"Tipo de Suscripción: {self.tipo_suscripcion}, "
            f"Costo Mensual: {self.costo_mensual}, "
            f"Saldo Pendiente: {self.saldo_pendiente}")
        

Dany = SuscripcionStreaming("Dany", "Estándar")
Luis = SuscripcionStreaming("Luis", "Premium")
Constanza = SuscripcionStreaming("Constanza", "Gratis")

"""Crea 3 usuarios con diferentes tipos de suscripción.
Haz que el primer usuario intente ver contenido exclusivo, mejore su suscripción y pague su saldo.
Haz que el segundo usuario vea contenido exclusivo, cambie su suscripción a Premium y pague dos veces.
Haz que el tercer usuario intente pagar una cantidad menor a su saldo pendiente y vea contenido exclusivo."""

print("\n--- Usuario 1: Dany intenta ver contenido exclusivo, mejorar su suscripción y pagar su saldo ---")
Dany.ver_contenido_exclusivo()
Dany.cambiar_suscripcion("Estándar")
Dany.realizar_pago(5.99)

print("\n--- Usuario 2: Luis ve contenido exclusivo, cambia su suscripción a Premium y paga dos veces ---")
Luis.ver_contenido_exclusivo()
Luis.cambiar_suscripcion("Premium")
Luis.realizar_pago(10.99)
Luis.realizar_pago(6.98)

print("\n--- Usuario 3: Constanza intenta pagar una cantidad menor a su saldo pendiente y ve contenido exclusivo ---")
Constanza.realizar_pago(0.50)
Constanza.ver_contenido_exclusivo()

print("\n--- Información de suscripción de cada usuario ---")
Dany.mostrar_info_suscripcion()
Luis.mostrar_info_suscripcion()
Constanza.mostrar_info_suscripcion()