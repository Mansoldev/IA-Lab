from enum import Enum
from pydantic import BaseModel, Field, ValidationError

# 1. Usamos Enum para limitar los valores posibles a una lista concreta (como en C#)
class EstadoPedido(str, Enum):
    PENDIENTE = "pendiente"
    ENVIADO = "enviado"
    CANCELADO = "cancelado"

# 2. Usamos Pydantic BaseModel en lugar de diccionarios o clases sueltas
class PedidoDto(BaseModel):
    id_pedido: int = Field(..., gt=0) # Debe ser mayor que 0
    cliente: str
    estado: EstadoPedido             # Solo acepta los valores del Enum de arriba
    total: float

    # Método de clase tipado y seguro
    def aplicar_descuento(self, porcentaje: float) -> float:
        if not (0.0 <= porcentaje <= 1.0):
            raise ValueError("El porcentaje debe estar entre 0.0 y 1.0")
        
        # El IDE y MyPy te protegen aquí: si escribes 'self.tota' (mal escrito), 
        # el editor te marcará el error en rojo inmediatamente.
        self.total = self.total * (1.0 - porcentaje)
        return self.total

# --- Ejemplo de uso seguro ---
try:
    # Si intentaras pasar un estado como "enviad" (con errata), Pydantic fallaría al instante.
    mi_pedido = PedidoDto(
        id_pedido=101,
        cliente="Ana García",
        estado=EstadoPedido.ENVIADO, 
        total=150.50
    )

    # Acceso por punto seguro y autocompletado por el IDE
    print(f"Cliente: {mi_pedido.cliente}")
    
    nuevo_total = mi_pedido.aplicar_descuento(0.10)
    print(f"Nuevo total: {nuevo_total}")

except ValidationError as e:
    print(f"Error de validación en los datos: {e}")