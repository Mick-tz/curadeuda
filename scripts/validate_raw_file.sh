#!bin/bash

# variables
REL_PATH="raw/CPdescargatxt/CPdescarga.txt"
separator='|'

# validación que el archivo se encuentré en el path correcto.
echo "Iniciando script de validación de archivo plano de datos, se buscará el archivo en el siguiente path relativo: $REL_PATH"

# por usabilidad se añaden sleeps de 1 segundo
sleep 1
ls ${REL_PATH} > /dev/null
if [ $? -eq 0 ]
  then
    echo 'archivo encontrado...\n'
  else
    echo 'No se encontró el archivo de datos, asegurate de haber ejecutado el script desde la raíz del proyecto, en caso contrario, favor de referirse al README.md para más información.\n'
    exit 1
fi

sleep 1
# validación separador de valores
echo "Se usará $separator como separador de valores. Referirse al README.md para más información.\n"

sleep 1

header=$(head -n 1 $REL_PATH)
# echo $header
num_spaces=$(echo $header | awk -F $separator '{print NF}')

if [ $num_spaces -lt 7 ]
  then
    echo 'El archivo no cuenta con todos los campos requeridos o el header (primera línea) no corresponde a la descripción de los campos, referirse a README.md para más información.\n'
    sleep 2
    exit 1
fi

for campo in d_codigo c_estado d_estado d_asenta d_tipo_asenta D_mnpio c_mnpio
  do
    echo $header | grep "|$campo|" > /dev/null
    if [ $? -ne 0 ]
      then
        # si no se encontro el campo rodeado de dos "pipes" se busca en el primer y último campo
        first_field=$(echo $header | awk -F $separator '{print $1}')
        last_field=$(echo $header | awk -F $separator '{print $(NF)}')
        if [ $first_field != $campo ] && [ $last_field != $campo ]
          then
            echo "El campo $campo no se encontró en el header, favor de validar...\n"
            exit 1
        fi
    fi
done

sleep 1
echo "Se encontraron todos los campos, validando calidad del archivo...\n"

# se obtiene el numero de líneas
num_lines=$(wc -l $REL_PATH | awk -F " " '{print $1}')
num_fields=$(awk -F $separator '{print NF}' $REL_PATH | uniq)
campos_por_linea=$(echo $num_fields | awk -F " " '{print NF}')
if [ "$campos_por_linea" != "1" ]
  then
    echo "Existe un renglón con un número incorrecto de columnas, favor de validar el archivo."
    exit 1
fi
echo "Archivo validado correctamente, contiene $num_lines. Cada renglón cuenta con $num_fields campos. Puedes proceder..."
exit 0