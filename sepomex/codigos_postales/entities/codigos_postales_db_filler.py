from base.entities.db_filler_interface import DBFillerInterface
from codigos_postales.models.estado import Estado, EstadoFactory
from codigos_postales.models.municipio import Municipio, MunicipioFactory
from codigos_postales.models.asentamiento import Asentamiento, AsentamientoFactory
from codigos_postales.models.codigo_postal import CodigoPostal, CodigoPostalFactory

import sys
import csv
from pathlib import Path

class CodigosPostalesDBFiller(DBFillerInterface):

    def __init__(self):
        super().__init__()

    def __codigos_postales(self):
        # MODIFICAR LAS SIGUIENTES LINEAS DEPENDIENDO DEL NOMBRE DEL ARCHIVO QUE CONTIENE LA INFORMACIÓN Y LA RUTA RELATIVA
        FILEPATH = 'raw/CPdescargatxt/CPdescarga.txt'
        script_dir = Path.cwd()

        ABSPATH =  (script_dir / FILEPATH).resolve()

        print('El path absoluto que estoy considerando para el archivo es: ')
        print(ABSPATH)
        print('\n')

        # 
        instancias_anteriores = False
        # nombres de los campos en header
        REQUIRED_FIELDS = (
            'd_codigo',
            'd_asenta',
            'd_tipo_asenta',
            'D_mnpio',
            'd_estado',
            'c_estado',
            'c_tipo_asenta',
            'c_mnpio',
            'id_asenta_cpcons'
        )
        
        # variables donde se guardara las instancias generadas
        all_data_estados = []
        all_data_municipios = []
        all_data_asentamientos = []
        all_data_codigos_postales = []

        factories = {
            'Estado': EstadoFactory(),
            'Municipio': MunicipioFactory(),
            'Asentamiento': AsentamientoFactory(),
            'CodigoPostal': CodigoPostalFactory(),
        }

        # contendran las instancias para ejecutar el bulk_create
        estados_instances = []
        municipios_instances = []
        asentamientos_instances = []
        codigos_postales_instances = []

        # usaremos estos sets para revisar eficientemente si ya hemos instanciado anteriormente dicho elemento
        estados_set = set({})
        municipios_set = set({})
        asentamientos_set = set({})

        # 
        errors = []

        if Estado.objects.all().count() + Municipio.objects.all().count() + Asentamiento.objects.all().count() + CodigoPostal.objects.all().count()  > 0:
            continuar = input("Ya existen instancias anteriores, si continuas, el contenido anterior de la base será eliminado por completo ¿Deseas continuar?(Si,No):\n")
            if continuar != "Si":
                print('finalizando script...')
                print('\n')
                return
            else:
                instancias_anteriores = True
        with open(ABSPATH, 'r', encoding="latin1") as f:
            reader = csv.reader(f, delimiter='|')
            for i, row in enumerate(reader):
                if i == 0:
                    header = row
                    column_indexes = {}
                    for field in REQUIRED_FIELDS:
                        try:
                            # solo debe haber una coincidencia, por lo que asignamos directamente el cero-ésimo valor
                            column_indexes[field] = [i for i in range(len(header)) if header[i] == field][0]
                        except Exception as e:
                            print(e)
                            print(f'El problema parece ser que el campo {field} no se encuentra en el header del archivo plano')
                            print('\n')
                            return
                else:
                    # se agregará una instancia de un nuevo estado si y solo si no había sido instanciado antes.
                    if not (int(row[column_indexes['c_estado']]) in estados_set):
                        estado = {
                            'c_estado': int(row[column_indexes['c_estado']]),
                            'd_estado': str(row[column_indexes['d_estado']])
                        }
                        estados_set.add(estado['c_estado'])
                        all_data_estados.append(estado)

                    if not (int(row[column_indexes['c_mnpio']]) in municipios_set):
                        municipio = {
                            'c_mnpio': int(row[column_indexes['c_mnpio']]),
                            'd_mnpio': str(row[column_indexes['D_mnpio']]), # AGUAS!! En este campo rompen notación, por lo que nos apegamos a la notación de sepomex (la D es mayúscula)
                            'c_estado': int(row[column_indexes['c_estado']])
                        }
                        municipios_set.add(municipio['c_mnpio'])
                        all_data_municipios.append(municipio)

                    if not (int(row[column_indexes['id_asenta_cpcons']]) in asentamientos_set):
                        asentamiento = {
                            'id_asenta_cpcons': int(row[column_indexes['id_asenta_cpcons']]),
                            'd_asenta': str(row[column_indexes['d_asenta']]),
                            'd_tipo_asenta': str(row[column_indexes['d_tipo_asenta']]),
                            'c_tipo_asenta': int(row[column_indexes['c_tipo_asenta']]),
                            'c_mnpio': int(row[column_indexes['c_mnpio']])
                        }
                        asentamientos_set.add(asentamiento['id_asenta_cpcons'])
                        all_data_asentamientos.append(asentamiento)

                    codigo_postal = {
                        'd_codigo': str(row[column_indexes['d_codigo']]),
                        'id_asenta_cpcons': int(row[column_indexes['id_asenta_cpcons']])
                    }
                    all_data_codigos_postales.append(codigo_postal)

        print("La información fue extraída de forma correcta...")
        print('\n')

        if instancias_anteriores:
            borrar_bases_confirmación = input('¡Cuidado! Si continuas, el contenido anterior de la base será eliminado por completo y es posible que no pueda ser recuperado. Escribe "Continuar, entiendo las consecuencias" y presiona [Enter] para continuar con la carga de información:\n')
            if borrar_bases_confirmación != "Continuar, entiendo las consecuencias":
                print('Tomate un cafecito, revisa que todo esté bien y vuelve a intentarlo más tarde.')
                print('\n')
                return
            else:
                print('Inicializando base de datos...')
                for factory in factories.values():
                    factory.model_class.objects.all().delete()
                print('Inicialización de las base concluida...')
                print('\n')

        # finalmente, instanciamos los elementos de la base de datos
        # ¡¡CUIDADO!! EL ORDEN ES IMPORTANTE DADO QUE EXISTE DEPENDENCIA. EL ORDEN CORRECTO DEBE SER ESTADOS, MUNICIPIOS, ASENTAMIENTOS Y FINALMENTE, CODIGOS POSTALES.
        print('Cargando información de los estados...')
        for estado in all_data_estados:
            try:
                estados_instances.append(
                    factories['Estado'].new_instance(
                        **estado
                    )
                )
            except Exception as e:
                errors.append({estado.get('c_estado'): e})
        Estado.objects.bulk_create(estados_instances)
        print('Se cargó información de los estados...')
        print('\n')

        print('Cargando información de los municipios...')
        for municipio in all_data_municipios:
            try:
                municipios_instances.append(
                    factories['Municipio'].new_instance(
                        **municipio
                    )
                )
            except Exception as e:
                errors.append({municipio.get('c_municipio'): e})
        Municipio.objects.bulk_create(municipios_instances)
        print('Se cargó información de los municipios...')
        print('\n')

        print('Cargando información de los asentamientos...')
        for asentamiento in all_data_asentamientos:
            try:
                asentamientos_instances.append(
                    factories['Asentamiento'].new_instance(
                        **asentamiento
                    )
                )
            except Exception as e:
                errors.append({asentamiento.get('id_asenta_cpcons'): e})
        Asentamiento.objects.bulk_create(asentamientos_instances)
        print('Se cargó información de los asentamientos...')
        print('\n')

        print('Cargando información de los codigos postales...')
        for codigo in all_data_codigos_postales:
            try:
                codigos_postales_instances.append(
                    factories['CodigoPostal'].new_instance(
                        **codigo
                    )
                )
            except Exception as e:
                errors.append({codigo.get('d_codigo'): e})
        CodigoPostal.objects.bulk_create(codigos_postales_instances)
        print('Se cargó información de los códigos postales...')
        print('\n')

        # en caso que se quiera imprimir a la consola posteriormente
        original_stdout = sys.stdout
        with open('filldatabase_errors.log', 'w') as errorFile:
            sys.stdout = errorFile
            print(errors)

    def fill_database(self):
        self.__codigos_postales()
