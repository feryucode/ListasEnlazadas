#uso ejemplificado de listas enlazadas en una taqueria
#gestor de pedidos en una taqueria no es lo mismo una arden de tacos que un kilo de pastor por lo que se da prioridad a ciertas cosas
#se usa una Lista Doblemente Enlazada para mover comandas de estado (En Espera $\rightarrow$ En Comal $\rightarrow$ Listo) o cancelar pedidos en tiempo real
class Comanda:
    def __init__(self, id_orden: int, cliente: str, detalles: str):
        self.id_orden = id_orden
        self.cliente = cliente
        self.detalles = detalles
        self.prev = None
        self.sig = None


class ColaTaqueria:
    def __init__(self):
        self.cabeza = None  
        self.cola = None  
        self.mapa_comandas = (
            {}
        )  

    def nuevo_pedido(self, id_orden: int, cliente: str, detalles: str):
        nueva = Comanda(id_orden, cliente, detalles)
        self.mapa_comandas[id_orden] = nueva

        if not self.cabeza:
            self.cabeza = nueva
            self.cola = nueva
        else:
            self.cola.sig = nueva
            nueva.prev = self.cola
            self.cola = nueva

        print(f"[NUEVA COMANDA #{id_orden}] {cliente}: {detalles}")

    def despacho_prioritario(self, id_orden: int):
        if id_orden not in self.mapa_comandas:
            print(f"La orden #{id_orden} no existe o ya se entregó.")
            return

        nodo = self.mapa_comandas.pop(id_orden)

        if nodo == self.cabeza and nodo == self.cola:
            self.cabeza = None
            self.cola = None
        elif nodo == self.cabeza:
            self.cabeza = nodo.sig
            self.cabeza.prev = None
        elif nodo == self.cola:
            self.cola = nodo.prev
            self.cola.sig = None
        else:
            nodo.prev.sig = nodo.sig
            nodo.sig.prev = nodo.prev

        print(
            f"[DESPACHADO #{nodo.id_orden}] {nodo.cliente} recibió: {nodo.detalles}"
        )

    def mostrar_pantalla_cocina(self):
        actual = self.cabeza
        print("\n--- PANTALLA DE COCINA (COMANDAS PENDIENTES) ---")
        if not actual:
            print("(No hay pedidos pendientes)")
        while actual:
            print(f"  [#{actual.id_orden} | {actual.cliente}: {actual.detalles}]")
            actual = actual.sig
        print("------------------------------------------------\n")


if __name__ == "__main__":
    taqueria = ColaTaqueria()
    taqueria.nuevo_pedido(101, "Carlos", "3 Pastores con todo")
    taqueria.nuevo_pedido(102, "Ana", "2 Suaderos sin cebolla")
    taqueria.nuevo_pedido(103, "Luis", "1 Campechano y 1 Gringa")

    taqueria.mostrar_pantalla_cocina()

    taqueria.despacho_prioritario(101)

    taqueria.despacho_prioritario(103)
    taqueria.mostrar_pantalla_cocina()