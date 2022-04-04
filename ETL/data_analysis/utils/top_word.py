from collections import Counter

def top_word(lista):

    count_lista=Counter(lista)
    top_words = count_lista.most_common()
    #first, second, *_, last = count_lista.most_common()
    if len(top_words)<3:
        top_words = [0,0,0]
    return top_words

""" a=['celulares', 'pistas', 'conducían', 'william', 'v', 'principal', 'sospechoso', 'número', 'teléfono', 'tenía', 'víctima', 'joven', 'había', 'realizado', 'contactos', 'desde', 'zona', 'sur', 'ciudad', 'paz', 'hubo', 'llamadas', 'uso', 'mensajes', 'texto', 'tráfico', 'datos', 'recolección', 'veintena', 'videos', 'concentraron', 'cámaras', 'cercanas', '800', 'metros', 'alrededor', 'registrada', 'nombre', 'madre', 'acusado', 'ana', 'mc', 'conoció', 'conductor', 'vehículo', 'era', 'jashiro', 'oliver', 'hayakawa', 'condarco', 'habitación', 'acusado', 'encontraron', 'todas', 'pruebas', 'delincuente', 'utilizó', 'teléfono', 'víctima', 'cámaras', 'vigilancia', 'teléfonos', 'celulares', 'pistas', 'conducían', 'william', 'v', 'principal', 'sospechoso', 'número', 'teléfono', 'tenía', 'víctima', 'joven', 'había', 'realizado', 'contactos', 'desde', 'zona', 'sur', 'ciudad', 'paz', 'hubo', 'llamadas', 'uso', 'mensajes', 'texto', 'tráfico', 'datos', 
'recolección', 'veintena', 'videos', 'concentraron', 'cámaras', 'cercanas', '800', 'metros', 'alrededor', 'registrada', 'nombre', 'madre', 'acusado', 'ana', 'mc', 'conoció', 'conductor', 'vehículo', 'era', 'jashiro', 'oliver', 'hayakawa', 'condarco', 'habitación', 'acusado', 'encontraron', 'todas', 'pruebas', 'delincuente', 'utilizó', 'teléfono', 'víctima']
b=top_word(a)
print(b) """