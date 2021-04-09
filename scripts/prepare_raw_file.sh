#!bin/bash

# variables
REL_PATH="raw/CPdescargatxt/CPdescarga.txt"
separator='|'

# validación que el archivo se encuentré en el path correcto.
echo "Iniciando script de preparación de archivo plano de datos, se buscará el archivo en el siguiente path relativo: $REL_PATH"

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

if [ $num_spaces -lt 9 ]
  then
    echo 'El archivo no cuenta con todos los campos requeridos o el header (primera línea) no corresponde a la descripción de los campos, referirse a README.md para más información.\n'
    sleep 2
    exit 1
fi

fields=$(echo $header | sed 's/|/ /g')
busqueda="id_asenta_cpcons"

# despues de la siguiente ejecución obtenemos la columna remplazar
index=1
for field in $fields
  do
    if [[ "$field" = "$busqueda" ]]
      then
        break
      else
        index=$(($index+1))
    fi
  done

# TODO: el numero de columnas esta hardcodeado, cambiar
head -n -1 $REL_PATH | awk -v var="$index" -F $separator 'BEGIN{FS="|";OFS="|"}$var=NR{print $1,$2,$3,$4,$5,$6,$8,$9,$10,$11,$12,$13,$14,$15 }' > no-header.txt

cat no-header.txt >> new_file.txt
rm no-header.txt

# echo "ahora sed"
cp $REL_PATH raw/CPdescargatxt/CPdescarga_restoration_file.txt
sed '0,/1/ s/1/id_asenta_cpcons/' new_file.txt > $REL_PATH
# TODO: Ver porque se agrega una línea adicional, esto lo corrige temporalmente
head -n -1 $REL_PATH > tmp_file.txt
cat tmp_file.txt > $REL_PATH
rm new_file.txt tmp_file.txt

echo "Archivo modificado, contiene $num_lines. La columna id_asenta_cpcons se modificó para contener el número de línea. Puedes proceder..."
exit 0