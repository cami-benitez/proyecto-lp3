from typing import List
from datetime import date
from app.dao.agenda_medicas.registrar_agenda_medicas.dto.agenda_medica_detalle_dto import AgendaMedicaDetalleDto
from app.dao.referenciales.estado_agenda_medica.estado_agenda_medica_dto import EstadoAgendamedica
class AgendaMedicaDto:
    
    def __init__(self, id_agenda_medica: int, id_medico: int, id_especialidad: int, \
                 estado: EstadoAgendamedica, sala_atencion: str, turno: str, dia: date, detalle_agenda: List[AgendaMedicaDetalleDto]):
        self.__id_agenda_medica = id_agenda_medica
        self.__id_medico = id_medico
        self.__id_especialidad = id_especialidad
        self.__sala_atencion = sala_atencion
        self.__estado = estado
        self.__turno = turno
        self.__dia = dia
        self.__detalle_agenda = detalle_agenda

    @property
    def id_agenda_medica(self) -> int:
        return self.__id_agenda_medica

    @id_agenda_medica.setter
    def id_agenda_medica(self, valor: int):
        self.__id_agenda_medica = valor

    @property
    def id_medico(self) -> int:
        return self.__id_medico

    @id_medico.setter
    def id_medico(self, valor: int):
        if not valor:
            raise ValueError("El atributo id_medico no puede estar vacio")
        self.__id_medico = valor

    @property
    def id_especialidad(self) -> int:
        return self.__id_especialidad

    @id_especialidad.setter
    def id_especialidad(self, valor: int):
        if not valor:
            raise ValueError("El atributo id_especialidad no puede estar vacio")
        self.__id_especialidad = valor

    @property
    def sala_atencion(self) -> str:
        return self.__sala_atencion

    @sala_atencion.setter
    def sala_atencion(self, valor: str):
        if not valor:
            raise ValueError("El atributo sala_atencion no puede estar vacío")
        self.__sala_atencion = valor

    @property
    def estado(self) -> EstadoAgendamedica:
        return self.__estado

    @estado.setter
    def estado(self, valor: EstadoAgendamedica):
        if not isinstance(valor, EstadoAgendamedica):
            raise ValueError("El atributo estado debe ser de tipo 'EstadoAgendaMedica'")
        self.__estado = valor


    @property
    def turno(self) -> str:
        return self.__turno

    @turno.setter
    def turno(self, valor: str):
        if not valor:
            raise ValueError("El atributo turno no puede estar vacío")
        self.__turno = valor

    @property
    def dia(self) -> date:
        return self.__dia

    @dia.setter
    def dia(self, valor: date):
        if not isinstance(valor, date):
            raise ValueError("El atributo dia debe ser de tipo 'date'")
        self.__dia = valor

    @property
    def detalle_agenda(self) -> List[AgendaMedicaDetalleDto]:
        return self.__detalle_agenda

    @detalle_agenda.setter
    def detalle_agenda(self, detalle_agenda: List[AgendaMedicaDetalleDto]):
        if not isinstance(detalle_agenda, list):
            raise ValueError("detalle_agenda debe ser una lista de objetos AgendaMedicaDetalleDto")

        # Verificar que todos los elementos en la lista sean del tipo correcto
        for item in detalle_agenda:
            if not isinstance(item, AgendaMedicaDetalleDto):
                raise ValueError("Todos los elementos de detalle_agenda deben ser instancias de AgendaMedicaDetalleDto")

        self.__detalle_agenda = detalle_agenda
