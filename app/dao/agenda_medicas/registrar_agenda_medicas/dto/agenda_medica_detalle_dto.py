class AgendaMedicaDetalleDto:
    
    def __init__(self, id_agenda_medica: int):
        self.__id_agenda_medica= id_agenda_medica

    #getters y setters de id_pedido_compra
    @property
    def id_agenda_medica(self) -> int:
        return self.__id_agenda_medica

    @id_agenda_medica.setter
    def id_agenda_medica(self, valor: int):
        #if not isinstance(valor, int) or valor <= 0:
        #    raise ValueError("El atributo id_pedido_compra debe ser un entero positivo")
        self.__id_agenda_medica = valor