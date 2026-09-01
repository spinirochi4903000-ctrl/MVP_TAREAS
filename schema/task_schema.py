from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum


class PriorityTaskEnum(str, Enum):
    alta = "alta"
    media = "media"
    baja = "baja"


class EstateTaskEnum(str, Enum):
    pendiente = "pendiente"
    en_proceso = "en_proceso"
    terminada = "terminada"


class TaskSchema(BaseModel):
    id_tarea: Optional[int] = None
    id_tipo_tarea: int
    fecha_hora: datetime
    descripcion: str
    fecha_vencimiento: Optional[datetime] = None
    prioridad: PriorityTaskEnum = PriorityTaskEnum.media
    estado: EstateTaskEnum = EstateTaskEnum.pendiente


class TaskUpdateSchema(BaseModel):
    id_tipo_tarea: Optional[int] = None
    fecha_hora: Optional[datetime] = None
    descripcion: Optional[str] = None
    fecha_vencimiento: Optional[datetime] = None
    prioridad: Optional[PriorityTaskEnum] = None
    estado: Optional[EstateTaskEnum] = None
