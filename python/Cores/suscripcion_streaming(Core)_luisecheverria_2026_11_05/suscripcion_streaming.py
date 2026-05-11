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
        reducir_monto = min(monto, self.saldo_pendiente)
        self.saldo_pendiente -= reducir_monto

    def cambiar_suscripcion(self, nuevo_tipo):
        """Cambia el tipo de suscripción y actualiza el costo mensual."""
        if nuevo_tipo in self.costos_suscripcion:
            self.tipo_suscripcion = nuevo_tipo
            self.saldo_pendiente = self.costos_suscripcion[nuevo_tipo]

    def ver_contenido_exclusivo(self):
        """Permite ver contenido exclusivo según el tipo de suscripción."""

        if self.tipo_suscripcion == "Gratis":
            return "No tienes acceso a contenido exclusivo."

        elif self.tipo_suscripcion == "Estándar":
            return "Acceso a contenido exclusivo estándar."

        elif self.tipo_suscripcion == "Premium":
            return "Acceso a todo el contenido exclusivo."
       

    def mostrar_info_suscripcion(self):
        """Muestra la información de la suscripción del usuario."""
        return (
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

print(Dany.ver_contenido_exclusivo())
Dany.cambiar_suscripcion("Premium")
print(Dany.mostrar_info_suscripcion())
Dany.realizar_pago(10.99)

print(Luis.ver_contenido_exclusivo())
Luis.cambiar_suscripcion("Premium")
print(Luis.mostrar_info_suscripcion())
Luis.realizar_pago(10.99)

print(Constanza.mostrar_info_suscripcion())
Constanza.realizar_pago(0.99)