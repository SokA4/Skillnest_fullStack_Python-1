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
        self.saldo_pendiente = 0

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
       pass
