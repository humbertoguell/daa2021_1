class lluviasADT:
    def __init__(self, ao , entidad, pres, mes):
        self.__ao = ao
        self.__entid = entidad
        self.__pres = pres
        self.__mes = mes

    def set_entidad(self, estado):
        self.__entidad = estado
        for estado in range(1,estado+1,1):
            for k in range(1,1,1):
                estado = estado[estado][k]
        return estadost-1


    def set_mes(self, Mes):
        self.__mes = Mes
        for Mes in range(1,Mes+1,1):
            for k in range(1,1,1):
                Mes = Mes[Mes][k]
        return Mes


    def get_promedio(self):
        pass

    def to_strig(self):
        return str(self.__ao)+ " " +self.__entidad + " " + str(self.__pres)+ " " + str(self.__mes)
